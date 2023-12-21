import os
import sys
try:
    from Crypto.Random import get_random_bytes
except ImportError:
    print("Le module Crypto n'est pas installé.")
    sys.exit(1)

from Aes_cipher import aes_decrypt, aes_encrypt
from SDES import encod_text, decod_text2
import time
import matplotlib.pyplot as plt

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'doc/'))

# Génération de clé AES et SDES
aes_key = get_random_bytes(32)
sdes_key = 255

# Lecture du contenu du fichier
fichier_texte = os.path.join(ROOT, 'doc/arsene_lupin_extrait.txt')
with open(fichier_texte, 'r', encoding='utf-8') as file:
    texte_clair = file.read()
    lignes = texte_clair.splitlines()[2:]
    texte_clair_modifie = '\n'.join(lignes)

# Listes pour stocker les tailles du message et les temps d'exécution
message_sizes = []
aes_times = []
sdes_times = []

# Commencer avec un message de 100 caractères
current_message_size = 100

# Boucle sur différentes tailles de messages
for _ in range(5):
    # Générer un message avec la taille actuelle
    modified_text = texte_clair_modifie[:current_message_size]

    message_sizes.append(current_message_size)

    # Mesure du temps d'encryptage et de décryptage pour AES
    start_time = time.time()
    aes_ciphertext, aes_iv = aes_encrypt(modified_text, aes_key)
    aes_decrypted_message = aes_decrypt(aes_ciphertext, aes_key, aes_iv)
    aes_execution_time = time.time() - start_time
    aes_times.append(aes_execution_time)

    # Mesure du temps d'encryptage et de décryptage pour SDES
    start_time = time.time()
    sdes_ciphertext = encod_text(modified_text, sdes_key)
    sdes_decoded_message = decod_text2(sdes_ciphertext, sdes_key)
    sdes_execution_time = time.time() - start_time
    sdes_times.append(sdes_execution_time)

    # Vérification de la cohérence des résultats
    assert aes_decrypted_message == modified_text
    assert sdes_decoded_message == modified_text

    # Augmenter la taille du message pour la prochaine itération
    current_message_size += 100

# Tracer le graphe
plt.plot(message_sizes, aes_times, label='AES')
plt.plot(message_sizes, sdes_times, label='SDES')
plt.xlabel('Taille du Message')
plt.ylabel('Temps d\'exécution (s)')
plt.legend()
plt.show()
