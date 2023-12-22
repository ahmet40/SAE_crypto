import sys
import os
import time
import matplotlib.pyplot as plt

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
sys.path.append(os.path.join(ROOT, 'doc/'))

from SDES import double_encod
from cassage_text import cassage_brutale, cassage_astucieux

fichier_texte = os.path.join(ROOT, 'doc/arsene_lupin_extrait.txt')

with open(fichier_texte, 'r', encoding='utf-8') as file:
    texte_clair = file.read()
    lignes = texte_clair.splitlines()[2:]
    texte_clair_modifie = '\n'.join(lignes)

# Listes pour stocker les résultats
temps_brutale = []
temps_astucieux = []
tailles_messages = []

for i in range(10, 60, 10):
    # Chiffre le texte en utilisant double_encod
    texte_chiffre = double_encod(texte_clair_modifie[:i], 10, 10)

    # Effectue le cassage brutale et mesurer le temps
    start_time = time.time()
    result_brutale = cassage_brutale(texte_clair_modifie[:i], texte_chiffre)
    end_time = time.time()
    temps_brutale.append(end_time - start_time)
    
    # Effectue le cassage astucieux et mesurer le temps
    start_time = time.time()
    result_astucieux = cassage_astucieux(texte_clair_modifie[:i], texte_chiffre)
    end_time = time.time()
    temps_astucieux.append(end_time - start_time)
    
    # Ajoute la taille du message à la liste
    tailles_messages.append(i)

    # Assertion d'exemple du cas de test
    assert result_brutale == (10, 10)

# Trace les résultats
plt.plot(tailles_messages, temps_brutale, label='Cassage Brutale')
plt.plot(tailles_messages, temps_astucieux, label='Cassage Astucieux')
plt.xlabel('Taille du Message')
plt.ylabel('Temps (secondes)')
plt.title('Comparaison de Cassage Brutale et Cassage Astucieux')
plt.legend()
plt.show()
