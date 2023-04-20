# affine cipher

k = int(input())
s = list(input())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1, len(s) + 1):
    shift = (3 * i + k) % 26
    letter = alphabet.index(s[i-1])
    if letter - shift < 0:
        letter += 26

    s[i-1] = alphabet[letter-shift]

print("".join(s))
