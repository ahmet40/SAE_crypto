from SDES_base import encrypt,decrypt

def encod_text(text, cle)-> list:
    """ Cette fonction va encoder un texte avec le chiffrement SDES 
        Args:
            Param :
                text : le texte a encoder
                cle : la clé de chiffrement
            Returns :
                liste_cod : liste des blocs de 8 bits codés
    """
    liste_cod = []
    for elem in text:
        if type(elem)==str:
            bloc_8_bits = ord(elem)
            liste_cod.append(encrypt(cle, bloc_8_bits))
        else:
            liste_cod.append(encrypt(cle, elem))
    return liste_cod


def double_encod(text,cle,cle2):
    """Cette fonction va encoder 2 fois le text (double SDES)
        Args:
            Param :
                text : le texte a encoder
                cle : la clé de chiffrement
                cle2 : la clé de chiffrement
            Returns :
                liste_cod : liste des blocs de 8 bits codés
    """
    return encod_text(encod_text(text, cle),cle2)

def decod_text(text, cle)-> list:
    """ Cette fonction va decoder un texte avec le chiffrement SDES
        Args:
            Param :
                text : le texte a decoder
                cle : la clé de chiffrement
            Returns :
                liste_cod : liste des blocs de 8 bits décodés
    """
    liste_cod = []
    for elem in text:
        if type(elem)==str:
            bloc_8_bits = ord(elem)
            liste_cod.append(decrypt(cle, bloc_8_bits))
        else:
            liste_cod.append(decrypt(cle, elem))
    return liste_cod

def decod_text2(text, cle)-> str:
    """ Cette fonction va decoder un texte avec le chiffrement SDES et va les mettre en lettre
        Args:
            Param :
                text : le texte a decoder
                cle : la clé de chiffrement
            Returns :
                liste_cod : liste des blocs de 8 bits décodés
    """
    liste_cod = ""
    for elem in text:
        if type(elem)==str:
            bloc_8_bits = ord(elem)
            liste_cod+=chr(decrypt(cle, bloc_8_bits))
        else:
            liste_cod+=chr(decrypt(cle, elem))
    return liste_cod
