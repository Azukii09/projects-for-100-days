#define decrypt function
def decryption_function(text, key):
    #define character
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #define var for output encryption
    new_text = list(text.upper())
    a = list()
    #make shifter and index for char
    sifter = key % 26
    index_char = list()
    #logic for get char input index in alphabet var
    for char in new_text:
        if char in alphabet:
            index_char.append(alphabet.index(char))
        else:
            index_char.append(char)
    #logic for shifting char base on sifter index
    for i in index_char:
        if isinstance(i, int) and i-sifter < 0:
            a.append(alphabet[(26-(sifter-i))])
        elif isinstance(i, int) and i-sifter > 0:
            a.append(alphabet[i-sifter])
        else:
            a.append(i)
    #return encrypted password
    return "".join(a)