# SAE_crypto

## Origine du projet
Ce projet est la suite de la partie 1 d'une SAE cryptographie proposée par l'IUT informatique d'Orléans. Dans ce projet, nous devions notamment créer des scripts pour chiffrer deux fois un texte en SDES (une extension du chiffrement DES). Programmer deux méthodes permettant de trouver deux clés qui ont permis de chiffrer en SDES (une première version longue et une seconde version améliorée et plus rapide). Nous devions aussi visualiser deux images pour voir les bits différents et pour nous permettre de trouver une clé de chiffrement. Après avoir trouvé la clé, nous devions lire une ligne réseaux par lesquels a était échanger des messages entre deux personnes et nous devions déchiffrer ces images avec la clé trouvée dans la partie précédente. Au-delà de la programmation, nous devions répondre à des questions.

## Membre du groupe

- MARIDAT Ethan (2A3B)
- BABA Ahmet (2A3B)

# Lancement du projet
Pour lancer le projet, il vous suffit de vous mettre à la racine du projet et de lancer le fichier 'lancement.sh'. Ce dernier va nous permettre d'installer tous les modules python nécessaires pour le bon fonctionnement du projet et lancer le fichier 'main.py' qui se trouve dans le répertoire, code et qui contient un affichage dans le terminal notamment pour tester les cassages de façon aléatoire sur un grand texte, de voir les bits que renvoient les images, de lire la trace réseaux et découvrir les messages cachés d'Alice et Bob, tester le simple et le double encode pour voir la différence.

# Tests
Pour tester le bon fonctionnement de nos méthodes au-delà du fichier main, nous avons réalisé des fichiers de tests. Vous pouvez les visualiser dans le répertoire 'testes' et les lancer un fichier en faisant la commandes python3 'NomDuFichier'. Il existe plusieurs fichiers de tests :
- Le fichier 'test_AES.py' : permet de tester notre fichier 'Aes_cipher.py'
en générant une clé, chiffrant un message et le déchiffrant.

- Le fichier 'test_cassage_brutale': permet de tester notre fonction cassage brutal qui se trouvait dans le fichier 'cassage_texte.py'. Il va notamment tester cette méthode sur un texte simple et sur le texte arsene_lupin qui se trouver dans le dossier doc (rien que le fait de la tester sur des clés simples prend beaucoup de temps).


- Le fichier 'test_cassage_astucieux.py' : permet de tester notre fonction cassage astucieux qui se trouvait dans le fichier 'cassage_texte.py'. Il va notamment tester cette méthode sur un texte simple et sur le texte arsene_lupin qui se trouver dans le dossier doc (nous pourrons voir que même sur des clés très grands cela prend très peu de temps.).

- Le fichier 'test_SDES.py' : permet de tester les fonctions encod_text, double_encod sur des textes simple.

## Comparaison

Nous avons également développé des programmes affichant des graphiques avec deux courbes afin de comparer l'efficacité en temps.

- Le fichier 'compare_brutale_atucieux' : Le programme génère des textes chiffrés de tailles croissantes, mesure le temps nécessaire pour casser le chiffrement à l'aide des méthodes brutale et astucieux, puis affiche les résultats sur un graphique pour comparer l'efficacité en fonction de la taille du texte.

- Le fichier 'compare_SDES_AES' :  Ce programme évalue les performances d'encryptage et de décryptage pour SDES et AES en utilisant des messages de tailles variables, mesurant les temps d'exécution et affichant les résultats sous forme de graphique pour comparer l'efficacité des deux algorithmes en fonction de la taille du message.

# Réponse

Pour lire les réponse aux questions vous pouvez les lires dans le fichier REONSE.md qui est à la racine du projet.

# Répartition des tâches

- MARIDAT : encod_texte,double_encod,code cassage brutale, déchiffrement des bits images rossignoles, réponse au question de la partie 2,réalisations de tests, les fichiers de comparaison

- BABA : decode_texte,code cassage astucieux, lire la trâce résaux, réponse aux questions de la partie 4,réalisations de tests, réalisation des fichier main.py, lancement.sh,requirements.txt