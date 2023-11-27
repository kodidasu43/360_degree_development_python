alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_encrypt_decrypt_choice=input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
text=input("Enter you text for encode or decode\n")
shift=int(input("Enter your scecret shift key\n"))

def caser(text_from_user,shift_number,userchoice):
    if userchoice=='decode':
        shift_number*=-1
    cipher_text=""
    for letter in text_from_user:
     poistion=alphabet.index(letter)
     print(poistion)
     new_position=poistion+shift_number
     print(new_position)
     cipher_text+=alphabet[new_position]
     print(cipher_text)
    print(f"The {userchoice} text is {cipher_text}")
    
caser(text_from_user=text,shift_number=shift,userchoice=user_encrypt_decrypt_choice)
    