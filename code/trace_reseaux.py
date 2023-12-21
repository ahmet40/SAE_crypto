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
