def decryption_function(text, key):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    new_text = list(text.upper())
    a = list()
    sifter = key % 26
    index_char = list()
    for char in new_text:
        if char in alphabet:
            index_char.append(alphabet.index(char))
        else:
            index_char.append(char)
    for i in index_char:
        if isinstance(i, int) and i-sifter < 0:
            a.append(alphabet[(26-(sifter-i))])
        elif isinstance(i, int) and i-sifter > 0:
            a.append(alphabet[i-sifter])
        else:
            a.append(i)
    return "".join(a)