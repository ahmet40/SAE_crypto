from PIL import Image
import os
import sys




def get_rgb_at_position(image):
    """
        Cette fonction va nous permettre de recuperer les valeurs rgb de chaque pixel de l'image
    """
    cle_chiffrement=""
    for y in range(image.size[1]):    #pour chaque ligne de l'image 
        for x in range(image.size[0]):
            cle_chiffrement += str(image.getpixel((x,y))%2)
    
    return cle_chiffrement

