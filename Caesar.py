alphabet= ['a','b','c','d','e','f','h','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction= input("Type 'encode' to encode or 'decode' to decode: \n").lower()

text = input("Type your message: \n").lower()
shift = int(input("Type the shift: \n"))


def encode(origine_txt,shif_nuber):
    caesar_cipher= ''
    for letter in origine_txt:
        position_shift= alphabet.index(letter) + shif_nuber
        position_shift %= len(alphabet)

        caesar_cipher += alphabet[position_shift]
    print(f"ici c'est le resultat de l'encodage: {caesar_cipher}")

def decode(origine_txt,shif_nuber):
    caesar_cipher= ""
    for letter in origine_txt:
        chiffre_position= alphabet.index(letter) - shif_nuber
        chiffre_position %= len(alphabet)
        caesar_cipher += alphabet[chiffre_position]
    print(f"Le resultat du decodage: {caesar_cipher}")

def caesar(origine_txt,shif_nuber,encode_decode):
    if encode_decode == 'decode':
        decode(origine_txt,shif_nuber)
    elif encode_decode == 'encode':
        encode(origine_txt,shif_nuber)
    else:
        print("erreur veuillez entrer le Type 'encode' to encode or 'decode' to decode\n")
        exit()


if __name__=='__main__':
    caesar(origine_txt=text,shif_nuber=shift,encode_decode=direction)

