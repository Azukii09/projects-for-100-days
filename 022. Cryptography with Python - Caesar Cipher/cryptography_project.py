from encryption.encryption_cryptography import encrypt_function

print("Encryption!")
text = input("Input Text: ")
shifter = int(input("Input Shift number: "))

print(encrypt_function(text, shifter))

