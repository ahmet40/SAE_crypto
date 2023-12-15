from scapy.all import *
import os
import sys
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
sys.path.append(os.path.join(ROOT,'code/'))
from Aes_cipher import aes_decrypt

def ouvrir_fichier(fichier:str):
    """
        Ouvre le fichier trace_sae.cap
    """
    trace= rdpcap(fichier)
    ligne_udp=[]
    for ligne in trace:
        if "UDP" in ligne:          #les message passent par l'UDP c'est donc ce qu'on veut
            iv=ligne[Raw].load[:16] #c'est ce qui nous permet de savoir l'iv
            la_ligne=ligne[Raw].load
            ligne_udp.append((iv,la_ligne[16:]))
    return ligne_udp

def decrypt_ligne_udp(ligne_udp:list,key:int):
    """
        Decrypte les lignes UDP
    """
    message=[]
    for ligne in ligne_udp:
        message.append(aes_decrypt(ligne[1],key,ligne[0]))
    return message




key=0b1110011101101101001100010011111110010010101110011001000001001100  #la clé de chiffrement trouver sur l'image rossignol2.bmp
key_256 = 0b1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100

# Convertir la clé en une séquence d'octets de 32 octets (256 bits)
key_256_bytes = key_256.to_bytes(32, byteorder='big')

# Utiliser key_256_bytes comme clé pour le déchiffrement


script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "trace_sae.cap")
decrypted_messages=decrypt_ligne_udp(ouvrir_fichier(file_path), key_256_bytes)
print(decrypted_messages)
