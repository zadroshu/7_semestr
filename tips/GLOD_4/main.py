import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import math
import random as r
from tkinter import *
import tkinter as tk
from tkinter import ttk  # нужно для отображения объектов

'''
Модель Эллиота (обобщенная модель Гилберта)
Последовательность ошибок {Ei} - определяется функцией распределения P(l)
В схеме восстановления предполагаются, что есть хорошие и плохие состояния каналов
В "хорошем"  состоянии вероятность  искажения символов кода Е = 0, а в "плохом" Е>0
В лабораторной работе генерация помеховой обстановка в канале просходит по следующей схеме:
1. Определяется дистанция до очередной помехи по функции распределения F(d)
2. Определяется длительность помехи по функции распределения F(b)
3. Амплитуда помехи определяется по формуле F(a)
4. Полярность помехи - вероятностью Pn(+) положительного напряжения помехи
Если напряжение помехи Uп больше порогового уровня сигнала Uпор, то она внесет искажения
(если имеет разную полярность с сигналом) 
Елси на интервале D ошибок нет, то число неискаженныъ бит NB и длительность интервала
до ошибки L увеличивается на величину D. Затем проверяется условие A<Up - внесет ли помеха искажение?
если ампилтуда помехи меньше уровня порогового напряжения UP, то к величинам
NB и L прибавляется длительность помехи и осуществляется переход к STATIB, в которой величина счетчиека C2(1) увеличивается на единицу
Счетчик накапливает частоту событий, состяощих в том, что на всей длине помехи не было ошибок.
Если  A> Uп, то происходит моделирования процессов налодения помехи на полезный сигнал 
'''

# Кол-во бит
N = 1000 * 150
# длина кода
code_length = 10
# число искаженных символов
reg = 2
# sigma
sigma = 3
# ???
lamb = 1
# напряжение
U = 0.5

# E=0 E>1
e = np.round(np.random.normal(0.4, 0.1, N+1), 0)
c = np.random.choice([1, 0], N+1, p=[0.4, 0.6])
c_mod = np.empty(N+1)
interference = np.zeros(N+1)
# ошибка
error_interval = []
errors_ins_interference = []

num_good_bits = 0
num_bad_bits = 0

num_good_msgs = 0
num_bad_msgs = 0

errors_ins_msg = []
# вероятность ошибки
P_er = []
# Вероятность стирания при стирании
P_sd = []
# Вероятность стирания при декодировании
P_nd = []


def view_records(args, tree):
    # [tree.delete(i) for i in tree.get_children()]
    tree.insert('', 'end', values=args)  # выводит значения из базы данных в приложение с конца


def definition_of_interference(x, y, d, b, a, N):
    while x < y + int(d[0]) and x < N:
        interference[x] = 0
        x += 1
    y = x
    while y < x + int(b[0]) and y < N:
        interference[y] = a
        y += 1
    x = y
    return x, y


def intervals_error(N):
    k = 0
    for x in range(N):
        if e[x] == 0:
            k += 1
        else:
            if k > 0:
                error_interval.append(k)
            k = 0


def interference_errors(N):
    n = 0
    for x in range(N):
        if (interference[x] != 0):
            if (e[x] == 1):
                n += 1
        else:
            if n > 0:
                errors_ins_interference.append(n)
            n = 0


def count_bad_bits(N):
    num_bad_bits = 0
    for x in range(N):
        if (e[x] > 0) and (interference[x] > U or interference[x] < -U):
            if interference[x] > U and c[x] < 1:
                c_mod[x] = abs(c[x] - 1)
                num_bad_bits += 1
                continue
            elif interference[x] < U and c[x] > 1:
                c_mod[x] = abs(c[x] - 1)
                num_bad_bits += 1
                continue
        else:
            c_mod[x] = c[x]
    for x in range(N):
        if c_mod[x] != 0 and c_mod[x] != 1:
            c_mod[x] = 0
    return num_bad_bits


def count_good_bits(N):
    num_good_msgs = 0
    for x in range(0, N, code_length):
        if np.array_equal(c[x:x + code_length], c_mod[x:x + code_length]):
            num_good_msgs += 1
        else:
            m = 0
            for k in range(x, x + code_length - 1):
                if c[k] != c_mod[k]:
                    m += 1
            errors_ins_msg.append(m)
    return num_good_msgs


def main(u_porog, tree):
    ###Перебор пороговых значений
    for U in u_porog.split():
        # Два опыта на каждое значение
        for t in range(1, 3):
            num_good_bits = 0
            num_bad_bits = 0
            num_good_msgs = 0
            num_bad_msgs = 0
            x = 0
            y = 0
            # проход по каждому биту сообщений
            while x < N:
                # дистанция до помехи
                d = np.round(np.random.exponential(lamb, 1), 2)
                # длительность помехи
                b = np.round(np.random.exponential(lamb, 1), 2)
                # полярность напряжения помехи 50%/50%
                p = np.random.choice([1, -1], 1, p=[0.5, 0.5])
                # амплитуда помехи
                a = p * np.random.exponential(lamb, 1)

                x, y = definition_of_interference(x, y, d, b, a, N)

            intervals_error(N)
            interference_errors(N)

            num_bad_bits = count_bad_bits(N)
            num_good_bits = N - num_bad_bits

            num_good_msgs = count_good_bits(N)
            num_bad_msgs = int((N / code_length) - num_good_msgs)

            P_er.append(round(num_bad_bits / (num_bad_bits + num_good_bits), 3))
            # вероятность попадания g ошибок на фиксированных позициях кода длины n (1 формула)
            P_er_t = round((P_er[-1] ** (reg)) * (1 - P_er[-1]) ** (code_length - reg), 3)
            # вероятность возникновения g ошибок на длине кода n (2 формула)
            P_g_n = round(math.factorial(code_length) / (math.factorial(code_length - reg) * math.factorial(reg)) * (
                        P_er[-1] ** (reg)) * (1 - P_er[-1]) ** (code_length - reg), 3)
            err_mean = 0
            # среднее число ошибок на длине n (3 формула)
            for g in range(1, code_length):
                err_mean += g * (
                            math.factorial(code_length) / (math.factorial(code_length - g) * math.factorial(reg)) * (
                                P_er[-1] ** (g)) * (1 - P_er[-1]) ** (code_length - g))
            err_mean = round(err_mean, 3)
            # Pср (5 формула)
            P_sd.append(round(code_length * P_er[-1], 3))
            # Режим обнаружения r ошибок (6 формула)
            P_nd.append(round(
                math.factorial(code_length) / (math.factorial(code_length - reg + 1) * math.factorial(reg + 1)) * (
                            P_er[-1] ** (reg + 1)), 7))

            args = (
            U, t, N, num_good_bits, num_bad_bits, num_bad_msgs, num_good_msgs, P_er[-1], P_er_t, P_g_n, err_mean,
            P_sd[-1], P_nd[-1])
            view_records(args, tree)

    fig = plt.figure(figsize=(15, 9))
    ax1 = plt.subplot2grid((5, 1), (0, 0), rowspan=2, colspan=1)
    line = plt.bar(range(N % 121), interference[:len(interference) % 121], align='center', width=1, fill=False,
                   edgecolor='b', linewidth=2)
    line2 = plt.plot(range(N % 121), np.full(N % 121, int(U)), color="red")
    line3 = plt.plot(range(N % 121), np.full(N % 121, -int(U)), color="red")
    ax1.plot()
    # ax2 = fig.add_subplot(3,1,2)
    ax2 = plt.subplot2grid((5, 1), (2, 0), rowspan=1, colspan=1)
    line4 = plt.bar(range(N % 121), e[:len(e) % 121], align='center', width=1, fill=False, edgecolor='k', linewidth=2)
    ax2.plot()
    # ax3 = fig.add_subplot(3,1,3)
    ax3 = plt.subplot2grid((5, 1), (3, 0), rowspan=1, colspan=1)
    line5 = plt.bar(range(N % 121), c[:len(c) % 121], align='center', width=1, fill=False, edgecolor='b', linewidth=2)
    ax3.plot()
    ax4 = plt.subplot2grid((5, 1), (4, 0), rowspan=1, colspan=1)
    line6 = plt.bar(range(N % 121), c_mod[:len(c_mod) % 121], align='center', width=1, fill=False, edgecolor='g',
                    linewidth=2)
    ax4.plot()
    plt.show()
    fig = plt.figure(figsize=(9, 7))
    n, bins, patches = plt.hist(error_interval, 7, density=1, facecolor='blue', alpha=0.9, width=2)
    sns.distplot(error_interval, hist=False, color='k')
    plt.show()
    fig = plt.figure(figsize=(9, 7))
    n, bins, patches = plt.hist(errors_ins_interference, 7, density=1, facecolor='blue', alpha=0.9, width=0.2)
    plt.show()
    fig = plt.figure(figsize=(9, 7))
    n, bins, patches = plt.hist(errors_ins_msg, 7, density=1, facecolor='blue', alpha=0.9, width=0.2)
    plt.show()
    U = [1, 1, 1.5, 1.5, 2, 2, 2.5, 2.5, 3, 3, 3.5, 3.5, 4, 4]

    fig = plt.figure(figsize=(9, 7))
    plt.plot(U, P_er[0::2], '-mo')
    plt.plot(U, P_er[1::2], '-mo')
    plt.show()
    fig = plt.figure(figsize=(9, 7))
    plt.plot(U, P_sd[0::2], '-mo')
    plt.plot(U, P_sd[1::2], '-mo')
    plt.show()
    fig = plt.figure(figsize=(9, 7))
    plt.plot(U, P_nd[0::2], '-mo')
    plt.plot(U, P_nd[1::2], '-mo')
    plt.show()


if __name__ == "__main__":
    window = Tk()
    window.title("Модель Эллиота")
    window.geometry('1050x450+300+200')
    window.resizable(False, False)

    tree = ttk.Treeview(columns=(
    'Uпор', '№ опыта', 'Кол. Бит', 'Неиск. Бит', 'Иск. Бит', 'Иск. Сообщ', 'Неиск. Сооб', 'P(ош)', 'P(ош. фикс)',
    'P(ош. Не фикс)', 'Сред. Ош', 'P(сд)', 'P(нд)'), height=15,
                        show='headings')  # создание таблицы show='headings'-чтобы не было 0 значения кортежа

    # характеристики колонок
    tree.column('Uпор', width=70, anchor=tk.CENTER)
    tree.column('№ опыта', width=70, anchor=tk.CENTER)
    tree.column('Кол. Бит', width=90, anchor=tk.CENTER)
    tree.column('Неиск. Бит', width=70, anchor=tk.CENTER)
    tree.column('Иск. Бит', width=70, anchor=tk.CENTER)
    tree.column('Иск. Сообщ', width=90, anchor=tk.CENTER)
    tree.column('Неиск. Сооб', width=90, anchor=tk.CENTER)
    tree.column('P(ош)', width=70, anchor=tk.CENTER)
    tree.column('P(ош. фикс)', width=90, anchor=tk.CENTER)
    tree.column('P(ош. Не фикс)', width=100, anchor=tk.CENTER)
    tree.column('Сред. Ош', width=70, anchor=tk.CENTER)
    tree.column('P(сд)', width=80, anchor=tk.CENTER)
    tree.column('P(нд)', width=80, anchor=tk.CENTER)

    # Наименование колонок
    tree.heading('Uпор', text='Uпор')
    tree.heading('№ опыта', text='№ опыта')
    tree.heading('Кол. Бит', text='Кол. Бит')
    tree.heading('Неиск. Бит', text='Неиск. Бит')
    tree.heading('Иск. Бит', text='Иск. Бит')
    tree.heading('Иск. Сообщ', text='Иск. Сообщ')
    tree.heading('Неиск. Сооб', text='Неиск. Сооб')
    tree.heading('P(ош)', text='P(ош)')
    tree.heading('P(ош. фикс)', text='P(ош. фикс)')
    tree.heading('P(ош. Не фикс)', text='P(ош. Не фикс)')
    tree.heading('Сред. Ош', text='Сред. Ош')
    tree.heading('P(сд)', text='P(сд)')
    tree.heading('P(нд)', text='P(нд)')
    tree.pack()

    btn_cancel = ttk.Button(text='Закрыть', command=window.destroy)
    btn_cancel.place(x=700, y=370, width=100, height=50)

    label_description = tk.Label(text='Введите Uпор через пробел:')
    label_description.place(x=30, y=385)

    entry_u = ttk.Entry(width=30)
    entry_u.place(x=200, y=385)

    btn_start = ttk.Button(text='Начать', command=lambda: main(entry_u.get(), tree))
    btn_start.place(x=420, y=370, width=100, height=50)
    window.mainloop()


