from SDES import double_encod,decod_text,encod_text
from CONSTANTE import MAX_BYTE_SDES
def cassage_brutale(message_clair:str,message_chiffre:list) -> tuple:
    """
        Cette methode va nous permettre de trouver les deux cle qui ont permit de passer
        du message claire au message crypte
        Args:
            param:
                message_clair(string) : le message claire
                message_chiffre(list): une liste d'entier representant les lettre du message chiffre
            return:
                couple (tuple) : la clé 1 et la clé 2 
    """
    cle1=""
    cle2=""
    for k1 in range(MAX_BYTE_SDES):
        for k2 in range(MAX_BYTE_SDES):
            if double_encod(message_clair,k1,k2)==message_chiffre:
                cle1=k1
                cle2=k2
                print(f"la valeur de la cle 1 est : {cle1} et celle de la clé2 : {cle2}")
                return (cle1,cle2)
    print("les clé n'ont pas était trouver !!")

def cassage_astucieux(message_clair:str,message_chiffre:list) -> tuple:
    """
        Cette methode va nous permettre de trouver les deux cle qui ont permit de passer
        du message claire au message crypte en utilisant une methode astucieuse et plus rapide
        Args:
            param:
                message_clair(string) : le message claire
                message_chiffre(list): une liste d'entier representant les lettre du message chiffre
            return:
                couple (tuple) : la clé 1 et la clé 2 
    """
    cle1=[]
    cle2=[]
    c1=-1
    c2=-1
    for k1 in range(MAX_BYTE_SDES):
        cle1.append(encod_text(message_clair,k1))
        cle2.append(decod_text(message_chiffre,k1))
    intersection = list(filter(lambda x: x in cle1, cle2))
    for i in range(len(cle1)):
        if cle1[i] == intersection[0]:
            c1=i
        if cle2[i] == intersection[0]:
            c2=i
    if c1!=-1 and c2!=-1:
        return (c1,c2)
    return "cassage impossible"
