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

ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
sys.path.append(os.path.join(ROOT,'doc/'))
image = os.path.join(ROOT, 'doc/rossignol2.bmp')
image2 = os.path.join(ROOT, 'doc/rossignol1.bmp')


print(get_rgb_at_position(Image.open(image))[:64])
print()
print(get_rgb_at_position(Image.open(image2))[:64])
