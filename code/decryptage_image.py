# Description: Ce fichier contient l& fonctions permettant de decrypter une image et récupérer les pixels avec leur valeur rgb de l'image
def get_rgb_at_position(image):
    """
        Cette fonction va nous permettre de recuperer les valeurs rgb de chaque pixel de l'image
        Args:
            Param :
                image : l'image a decrypter
            Returns :
                liste_rgb : liste des valeurs rgb de chaque pixel de l'image
    """
    cle_chiffrement=""
    for y in range(image.size[1]):    #pour chaque ligne de l'image 
        for x in range(image.size[0]):  #pour chaque pixel de la colonne
            cle_chiffrement += str(image.getpixel((x,y))%2) #recupere la valeur rgb du pixel
    return cle_chiffrement
