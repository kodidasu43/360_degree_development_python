alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_encrypt_decrypt_choice=input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
text=input("Enter you text for encode or decode\n")
shift=int(input("Enter your scecret shift key\n"))

def encrypt(plain_text,shift_number):
    encoded_text=""
    for letter in plain_text:
     poistion=alphabet.index(letter)
     print(poistion)
     new_position=poistion+shift_number
     print(new_position)
     encoded_text+=alphabet[new_position]
     print(encoded_text)
    print(f"The encoded text is {encoded_text}")
    
def decrypt(encoded_user_text,shift_number_to_decode):
    decode_text=""
    for letter in encoded_user_text:
     poistion=alphabet.index(letter)
     print(poistion)
     new_position=poistion-shift_number_to_decode
     print(new_position)
     decode_text+=alphabet[new_position]
     print(decode_text)
    print(f"The decoded text is {decode_text}")
    
if user_encrypt_decrypt_choice == 'encode':
    encrypt(plain_text=text,shift_number=shift)
elif user_encrypt_decrypt_choice == 'decode':
    decrypt(encoded_user_text=text,shift_number_to_decode=shift)
