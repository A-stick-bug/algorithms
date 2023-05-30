from itertools import zip_longest

def split_len(s, key):
    split_s = []
    for i in range(0, len(s), key):
        split_s.append(s[i:i + key])
        i += key
    #
    # last_length = len(split_s[-1])
    # if last_length < key:
    #     split_s[-1] += (key - last_length) * " "
    return split_s


def encrypt(s, key):
    s = split_len(s, key)
    encrypted = list(zip_longest(*s, fillvalue=" "))
    encrypted = list(map(lambda x: "".join(x), encrypted))
    return "".join(encrypted).strip()


word = "Hello World This is a message and it is encrypted with transposition cipher. Here are some filler words to increase text length and make it easier for automatic decrypting tools to decrypt."
key = 2
encrypted = encrypt(word, key)

print(encrypted)
