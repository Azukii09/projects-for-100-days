#import function for encryption_cryptography
from encryption_cryptography import encrypt_function

#run program for encryption
print("Encryption!")
text = input("Input Text: ")
shifter = int(input("Input Shift number: "))

print(encrypt_function(text, shifter))

