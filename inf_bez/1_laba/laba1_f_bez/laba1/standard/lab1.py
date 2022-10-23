import string

alphabet = string.ascii_lowercase
shift=3

def crypt(text):
    rez=""
    for c in text:
        if c != " ":
            i=alphabet.find(c)
            i= (i+shift+len(alphabet)) % len(alphabet)
            rez=rez+alphabet[i]
        else:
             rez=rez+" "
    return rez


def decrypt(text):
    rez=""
    for c in text:
        if c != " ":
            i=alphabet.find(c)
            i= (i-shift+len(alphabet)) % len(alphabet)
            rez=rez+alphabet[i]
        else:
             rez=rez+" "
    return rez


# in_str = "helo world"
# out_str=crypt(in_str)
# print(out_str)
# print(decrypt(out_str))
