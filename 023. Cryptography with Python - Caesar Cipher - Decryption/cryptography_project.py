from decryption_cryptography import  decryption_function

print("Decryption!")
text_d = input("Input Text: ")
shifter_d = int(input("Input Shift number: "))

print(decryption_function(text_d, shifter_d))
