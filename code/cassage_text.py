from SDES import double_encod, decod_text, encod_text
from CONSTANTE import MAX_BYTE_SDES

def cassage_brutale(message_clair: str, message_chiffre: list) -> tuple:
    """
    Cette méthode va nous permettre de trouver les deux clés qui ont permis de passer
    du message clair au message crypté.
    Args:
        message_clair (string): le message clair.
        message_chiffre (list): une liste d'entiers représentant les lettres du message chiffré.
    Returns:
        couple (tuple): la clé 1 et la clé 2.
    """
    cle1 = ""
    cle2 = ""
    for k1 in range(MAX_BYTE_SDES):
        for k2 in range(MAX_BYTE_SDES):
            if double_encod(message_clair, k1, k2) == message_chiffre:
                cle1 = k1
                cle2 = k2
                return (cle1, cle2)
    return None

def cassage_astucieux(message_clair: str, message_chiffre: list) -> tuple:
    """
    Cette méthode va nous permettre de trouver les deux clés qui ont permis de passer
    du message clair au message crypté en utilisant une méthode astucieuse et plus rapide.
    Args:
        message_clair (string): le message clair.
        message_chiffre (list): une liste d'entiers représentant les lettres du message chiffré.
    Returns:
        couple (tuple): la clé 1 et la clé 2.
    """
    cle1=dict()
    
    message_coupe_claire= message_clair[:10]
    message_coupe_chiffre= message_chiffre[:10]

    for k1 in range(MAX_BYTE_SDES):
        cle1[tuple(encod_text(message_coupe_claire, k1))] = k1
    for k2 in range(MAX_BYTE_SDES):
        m_c = tuple(decod_text(message_coupe_chiffre, k2))
        if m_c in cle1:
            return (cle1[m_c], k2)

    return None
