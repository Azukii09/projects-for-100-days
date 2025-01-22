#import package
from decryption_cryptography import  decryption_function

#run program
print("Decryption!")
text_d = input("Input Text: ")
shifter_d = int(input("Input Shift number: "))

# call function
print(decryption_function(text_d, shifter_d))
