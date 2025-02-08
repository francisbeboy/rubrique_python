
alphabet= ['a','b','c','d','e','f','h','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction= input("Type 'encode' to encode or 'decode' to decode: \n").lower()

text = input("Type your message: \n").lower()
shift = int(input("Type the shift: \n"))


def encode(origine_txt,shif_nuber):
    caesar_cipher= ''

    for letter in origine_txt:
        if letter not in alphabet:
            caesar_cipher += letter
        else:

            position_shift= alphabet.index(letter) + shif_nuber
            position_shift %= len(alphabet)
            caesar_cipher += alphabet[position_shift]
    print(f"ici c'est le resultat de l'encodage: {caesar_cipher}")

def decode(origine_txt,shif_nuber):
    caesar_cipher= ""
    for letter in origine_txt:
        if letter not in alphabet:
            caesar_cipher += letter
        else:

            chiffre_position= alphabet.index(letter) - shif_nuber
            chiffre_position %= len(alphabet)
            caesar_cipher += alphabet[chiffre_position]
    print(f"Le resultat du decodage: {caesar_cipher}")

def caesar(origine_txt,shif_nuber,encode_decode):
    if encode_decode == 'decode':
        print(f"Voici votre {encode_decode} des lettres:")
        decode(origine_txt,shif_nuber)
    elif encode_decode == 'encode':
        print(f"Voici votre {encode_decode} des lettres:")
        encode(origine_txt,shif_nuber)

