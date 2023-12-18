import time
from datetime import datetime
import sys
import os
import random
from SDES import double_encod,encod_text
from cassage_text import cassage_astucieux,cassage_brutale
from decryptage_image import get_rgb_at_position
from PIL import Image
from trace_reseaux import *

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'doc/'))

while True:
    print("\033[92m================================\033[0m")
    print("    1 : tester le cassage astucieux avec 2 clé aléatoire")
    print("    2 : tester le cassage brutale \033[91mCela prend du temps !\033[0m")
    print("    3 : trouver et afficher la clé des images rossignol")
    print("    4 : trouver les message caché de la trace réseaux")
    print("    5 : tester le double encod sur un message simple avec des clés aléatoires")
    print("    6 : quitter")
    print("\033[92m================================\033[0m")
    liste_possibilite = ["1", "2", "3", "4", "5","6"]
    valeur = input("veuillez-choisir une action : ")
    if valeur in liste_possibilite:
        if valeur == "1":
            print("le message est le contenu du fichier arsene_lupin_extrait.txt")
            fichier_texte = os.path.join(ROOT, 'doc/arsene_lupin_extrait.txt')

            with open(fichier_texte, 'r', encoding='utf-8') as file:
                texte_clair = file.read()
                lignes = texte_clair.splitlines()[2:]
                texte_clair_modifie = '\n'.join(lignes)
            cle1, cle2 = random.randint(1, 255), random.randint(1, 255)
            
            texte_chiffre = double_encod(texte_clair_modifie, cle1, cle2)
            print(f"voici la valeur des de cle: {cle1},{cle2}")
            start_time = time.time()
            les_cles = cassage_astucieux(texte_clair_modifie, texte_chiffre)
            if les_cles:
                end_time = time.time()
                elapsed_time = end_time - start_time
                formatted_time = str(datetime.utcfromtimestamp(elapsed_time).strftime('%H:%M:%S.%f')[:-3])
                print(formatted_time, f"temps après cassage et voici les clés, cle1={les_cles[0]} , cle2={les_cles[1]}")
        
        elif valeur =="2":
            print("le message est le contenu du fichier arsene_lupin_extrait.txt")
            fichier_texte = os.path.join(ROOT, 'doc/arsene_lupin_extrait.txt')
            with open(fichier_texte, 'r', encoding='utf-8') as file:
                texte_clair=file.read()
                lignes = texte_clair.splitlines()[2:]
                texte_clair_modifie = '\n'.join(lignes)

            cle1, cle2 = random.randint(1, 5), random.randint(1, 255)
            print(f"voici la valeur des de cle: {cle1},{cle2}. La valeur de la clé 1 est compris entre 1 et 5 sinon le cassage brutal prend beaucoup de trop temps")
            texte_chiffre = double_encod(texte_clair_modifie, cle1,cle2)
            
            start_time = time.time()
            les_cles = cassage_brutale(texte_clair_modifie, texte_chiffre)
            if les_cles:
                end_time = time.time()
                elapsed_time = end_time - start_time
                formatted_time = str(datetime.utcfromtimestamp(elapsed_time).strftime('%H:%M:%S.%f')[:-3])
                print(formatted_time, f"temps après cassage et voici les clés, cle1={les_cles[0]} , cle2={les_cles[1]}")
        
        
        elif valeur=="3":
            ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
            sys.path.append(os.path.join(ROOT,'doc/'))
            image = os.path.join(ROOT, 'doc/rossignol1.bmp')
            image2 = os.path.join(ROOT, 'doc/rossignol2.bmp')
            print("\033[91mCette action peut prendre quelques secondes !!\033[0m")
            
            print("\033[91m===========\033[0m")  
            print("\033[93mVoici un extrait de 256 bits de l'image rosignol 1 : \033[0m", get_rgb_at_position(Image.open(image))[:256])
            print("\033[94m------------\033[0m")
            
            print("\033[93mVoici un extrait de 256 bits de l'image rosignol 2 : \033[0m", get_rgb_at_position(Image.open(image2))[:256])
            print("\033[91m===========\033[0m")
            
            print("\033[93mVoici un extrait de 64 bits de l'image rosignol 1 : \033[0m", get_rgb_at_position(Image.open(image))[:64])
            print("\033[94m------------\033[0m")
            
            print("\033[93mVoici un extrait de 64 bits de l'image rosignol 2 : \033[0m", get_rgb_at_position(Image.open(image2))[:64])
            print("\033[91m===========\033[0m")
            print("Nous pouvons donc bien voir que la clé a été codée sur 64 bits car à partir de 64 bits nous avons plus que des 0 dans l'image")

        elif valeur=="4":
            key_256 = 0b1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100
            # Convertir la clé en une séquence d'octets de 32 octets (256 bits)
            key_256_bytes = key_256.to_bytes(32, byteorder='big')
            # Utiliser key_256_bytes comme clé pour le déchiffrement
            script_directory = os.path.dirname(os.path.abspath(__file__))
            print(script_directory,"hahah")
            file_path = os.path.join(script_directory+"/../doc", "trace_sae.cap")
            decrypted_messages=decrypt_ligne_udp(ouvrir_fichier(file_path), key_256_bytes)
            if decrypted_messages:
                for i in range(len(decrypted_messages)):
                    print(f"Voici le message numéro {i+1} et voici ce qu'il contient : {decrypted_messages[i]}")
        
        elif valeur =="5":        
            cle = 0b0001001110
            texte_clair = input("Veuillez entrer un texte à chiffrer en simple encod: ")
            print(f"Voici le texte clair : {texte_clair}, et voici la clé qui va la chiffrer : {cle}")
            texte_chiffre = encod_text(texte_clair, cle)
            l=[]
            for lettre in texte_chiffre:
                l.append(chr(lettre))
            print(f"Voici une verion lisible d'un premier encode : {l}")
            print("\033[93m-------------------------------------------------------------------------------------------------\033[0m")
            cle2 = 0b000111111
            texte_clair = input("Veuillez entrer un texte à chiffrer : ")
            print(f"Voici le texte clair : {texte_clair}, et voici les clé qui vont la chiffrer : {cle}, {cle2}")
            double_chiffre = double_encod(texte_clair, cle, cle2)
            j=[]
            for lettre in double_chiffre:
                j.append(chr(lettre))
            print(f"Voici une verion lisible d'un premier encode : {j}")
            
        elif valeur == "6":
            print("Au revoir")
            break
    else:
        print("\033[91mveuillez entrer des valeurs possibles !\033[0m")
