from SDES_base import encrypt

def encod_text(text, cle)-> list:
    """ Cette fonction va encoder un texte avec le chiffrement SDES """
    liste_cod = []
    for elem in text:
        if type(elem)==str:
            bloc_8_bits = ord(elem)
            liste_cod.append(encrypt(cle, bloc_8_bits))
        else:
            liste_cod.append(encrypt(cle, elem))

    return liste_cod





def double_encod(text,cle,cle2):
    """Cette fonction va encoder 2 fois le text (double SDES)"""
    return encod_text(encod_text(text, cle),cle2)




cle1 = 0b1110001110
cle2 = 0b0101010101
texte_clair = "Hello"
texte_chiffre = double_encod(texte_clair, cle1,cle2)

print("Texte Clair:", texte_clair)
print("Texte Chiffré:", texte_chiffre)



