import string

alphabet = string.ascii_lowercase
shift = 3


def crypt(text):
    shift = 3
    rez = ""
    for c in text:
        if c != ' ':
            i = alphabet.index(c)
            i = (i + shift + len(alphabet)) % len(alphabet)
            rez = rez + alphabet[i]
            shift = ord(alphabet[i]) - ord('a')
        else:
            rez = rez + " "
    return rez


def decrypt(text):
    shift = 3
    rez = ""
    for c in text:
        if c != ' ':
            i = alphabet.index(c)
            i = (i - shift + len(alphabet)) % len(alphabet)
            rez = rez + alphabet[i]
            shift = ord(c) - ord('a')
        else:
            rez = rez + " "
    return rez;


in_str = "hello world"
out_str = crypt(in_str)
print(out_str)
print(decrypt(out_str))
