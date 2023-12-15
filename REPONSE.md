# Partie 2

# Question 1:
    L'alghorithme AES prend une clé de taille 256 bits qui est beaucoup plus grand que l'alghorithme SDES qui lui utilise une clé de 10 bits et dans lequels il y a 2 bits qui ne change pas et qui fait que la clé est de taille 8 bits. Nous devons donc faire tourner nos clé sur une boucle beaucoup plus grandes et donc qui prend plus de temps.

# Question 2 :
### 2.1 /
    AES est généralement plus rapide que SDES en raison de sa complexité structurelle, de ses blocs de données plus grands et de la possibilité d'utiliser des clés plus longues. 
    En éxécutant le fichier arsene_lupin :
        AES Time: 0.0006282329559326172
        SDES Time: 0.08947396278381348

![Comparaison AES et SDES](doc/compare_AES_SDES.png)

### 2.2 /
    Si nous devions réaliser une attaque par force brute sur AES, testant toutes les possibilités, cela nécessiterait d'explorer les 2^256 combinaisons de clés. Nous avons décidé de tester le processus de déchiffrement avec une clé sur un texte d'environ 800 caractères, ce qui a pris environ 3.933906555175781e-05 secondes.

    Maintenant, pour obtenir une estimation du temps total nécessaire, multiplions le nombre total de possibilités par le temps obtenu :
    2^256 × 3.933906555175781e−05

    Soit 3,464257806*10^66 année





# Question 3 :