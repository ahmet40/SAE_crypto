from SDES import double_encod
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

