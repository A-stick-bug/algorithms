alphabet = ";#mnCV!>l+*3%bs_6Zfh?AP@)DiqQT8Mu~}d&U,S<t:{k(2c9W=5g1/RXK$HvwxrjJeYE]`o^70FayB.pG4-IL[NzO"


def get_cipherletter(new_key, letter):
    if letter in alphabet:
        return alphabet[new_key]
    else:
        return letter


def encrypt(message):
    result = ""
    key = len(message)

    for letter in message:
        new_key = (alphabet.find(letter) + key) % len(alphabet)
        result = result + get_cipherletter(new_key, letter)

    return result


def decrypt(message):
    result = ""
    key = len(message)

    for letter in message:
        new_key = (alphabet.find(letter) - key) % len(alphabet)
        result = result + get_cipherletter(new_key, letter)

    return result
