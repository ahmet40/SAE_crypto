# Partie 1:

## Question 1
- Dans le cas du chiffrement RSA nous pouvons dire que le déchiffrement est quasiment impossible si la clé est correctement implémenter. En effet dans un chiffrement RSA bien implémenter la clé utiliser est de 2048 à 3072 bits, de plus sachant il y a deux clé (ce qui augmente considérablement les chances de ne pas pouvoir déchiffrer) nous pouvons mettre ce nombre au carré et cela fait un nombre de possibilité quasiment impossible à trouver.
Dans le cas ou les clés de chiffrement sont petits ou mal utilisé nous avons plus de posibbilité de trouver le message chiffrer.


## Question 2
- L'algorithme SDES utilise une clé de 10 bits. De plus, il y a deux bits qui sont réserver lors du chiffrement nous pouvons donc dire que le nombre de possibilité est de 2 puissance 8 qui est égales à 256. L'algorithme SDES est donc peu sécurisé, car nous pouvons le déchiffrer en seulement 256 essaie. De plus, d'autres type d'algorithmes de chiffrement symétrique vu en cours sont peu sécurisés comme le chiffrement César qui peut être déchiffré en 26 essaie.

## Question 3
- Lorsque nous allons chiffrer un texte en utilisant l'algorithme SDES nous allons avoirs 256 possibiltée. Dans le cas ou nous utilisons le double SDES qui correspond a rechiffrer le message déjà chiffrer une première fois, cela permet d'être un tout petit peu plus sécuris car le fait deux chiffrer une seconde fois le message revient a faire 256*256=65 536 possibilité qui peut prendre un peut de temps mais qui sera déchiffrer au bout de 1 ou 2 heures grand maximum.



# Partie 2

# Question 1:
L'alghorithme AES prend une clé de taille 256 bits qui est beaucoup plus grand que l'alghorithme SDES qui lui utilise une clé de 10 bits et dans lequels il y a 2 bits qui ne change pas et qui fait que la clé est de taille 8 bits. Nous devons donc faire tourner nos clé sur une boucle beaucoup plus grandes et donc qui prend plus de temps.


## Résumer des images
Pour trouver la clé caché dans l'image rossignole 2, nous avonc commencer par crée une fonction qui prend en paramètre une image et qui va parcourir les differents pixels par ligne et par colonne de l'image. Nous allions donc obtenir une chaine 1 et de 0 suivant la couleur blanche ou la couleur noir. Lorsque nous avions executer cette fonction sur l'image rossignol 1 nous avions obtenus une variéter de 1 et de 0 et lorsque nous l'avions executer sur l'image rossignole 2, nous nous sommes rendue compte que seul la première ligne de 64 bits contenait des 1 et des 0 et que tout le restes était des 0. Nous avions donc su et remarquer que c'était la clé que l'on chercher. Nous avons donc garder cette clé de 64 bits pour la partie 3.

# Partie 3

Dans cette partie, ils nous a été demandés de décrypter des messages envoyés. Pour ce faire, nous avions accès à la trace réseaux, nous savions que les messages étaient envoyés par des requêtes UDP et que l'indice de vecteur (iv) était sur 16 bits. Avec toutes ces informations, nous avons construit une première fonction (ouvrir_fichier(fichier)) permettant d'ouvrir la trace réseaux, de la lire ligne par ligne de récupérer les lignes UDP tout en extrayant l'iv. Nous avons donc en retour une liste de couples de ligne UDP qui contiennent à l'indice 0 l'iv et à l'indice 1 le message crypté qui a était envoyer. Maintenant, que nous avions nos messages, nous avons créé une seconde fonction (decrypt_ligne_udp(ligne_udp,key)). Dans cette fonction le paramètre key correspond à une clé de 256 bits que l'on a extrait de l'image rossignole 2 (la clé qui a été extraite était sur 64 bits, mais nous l'avons dupliqué 4 fois pour l'avoir en 256 bits.) que l'on a trouver dans la partie 2. Cette fonction va lire chaque couple de la liste et va appeler la méthode aes_decrypt() avec comme paramètre le message, la clé, et l'iv. En retour de cette fonction, nous allons avoir une liste de messages décryptés.

Nous avons donc un premier message qui est : La crypto c'est trop bien!

Et un message de retour qui est : Je suis complètement d'accord!

vous pouvez aussi voir les messages lors de l'execution du main

# Partie 4

## Question 1

Le fait d'utiliser toujours la même clé pour chiffrer les messages cause des soucis de sécuriter. En effet une clé avec utilisation répéter est plus vulnérable au déchiffrement par brute force ou l'utilisateur essayera toutes les combinaisons logique possible. Il y a aussi un manque de confidentialité à long terme car dans le cas ou, un utilisateur déchiffre un message alors tous les messages chiffrer avec cette clé serait découvertes. De plus l'un des objectifs de la cryptographie est de sécurisé  et de protéger les information si il y l'utilisation constante d'une clé sela réduit l'efficacité de la cryptographie.

# Question 2

Nous pouvons dire que le protocole plutotBonneConfidentialité ressemble au protocole réseaux SSL/TLS. En effet, nous pouvons remarquez qu'entre ces deux protocole il y a beaucoup de ressemblance par exemple :
- chiffrement asymétrique : le protocole SSL utilise un chiffrement asymétrique tel que RSA pour s'échanger les clés de session tout comme le protocole plutotBonneConfidentialité.
- chiffrement symétrique : le protocole plutotBonneConfidentialité utilise un chiffrement symétrique pour la communication et le protocole SSL utilise le chiffrement AES pour la Communication qui est un chiffrement symétrique.
- Objectif : les deux protocoles ont le même objectif. En effet le protocole plutotBonneConfidentialité est utilisé pour chiffrer des messages entre les deux amoureux et le protocole SSL est utiliser pour chiffrer les messages.

Pour le protocole plutotBonneConfidentialité la partie qui certifie l'authenticité des clés est absente.

Voilà comment se passe cette certification dans un protocole tel que SSL :
- Une autorité de certification émet des certificats électroniques qui contiennent la clé publique d'une entité et signé par la clé privée de l'autorité de certification.

- une fois que la communication est sécurisée, les parties concernées par la communication vérifie le certificats présente par l'autre partie.
(Si l'une des deux parties ne possède pas la clé publique, elle peut utiliser une chaîne de certificat pour remonter jusqu'au certificat).

# Question 3
Il peut être utilisé pour des transactions financières en ligne. Un exemple serait pour le paiement par carte bancaire. En effet pour une telle transaction, il est nécessaire de garantir une confidentialité optimale pour ne pas que les numéros de carte soit volés facilement et pour empêcher des attaques durant la transaction.

Un autre cas serait lors de la transmission d'informations médicales, professionnels ou même politiques. En effet, cela augmenterait la sécurité des informations et garantirait que les documents envoyés restent sécurisés et ne sont pas facilement accessibles et compréhensibles, surtout en période de conflits géopolitiques ou face à des personnes potentiellement nuisibles telles que des entreprises ou des individus.


# Question 4

- L'application Whatsapp utilise le chiffrement bout en bout pour les conversations, cela permet de sécuriser la conversation et d'assurer que seul le destinataire et l'expéditeur peuvent lire, voir et comprendre les messages envoyés. Cette application utilise le protocole de chiffrement de Signal. Ce protocole utilise des protocoles de chiffrements asymétriques pour l'échange de clés et des chiffrements symétrique telles qu'AES pour sécuriser la communication.

- L'application Signal utilise aussi le chiffrement bout en bout pour les conversations tout comme WhatsApp cela permet de sécuriser la conversation et de permettre que seul le destinataire et l'expéditeur peuvent lire les messages.
Comme son nom Signal va utiliser le protocole de chiffrement signal (l'explication de ce protocole est fournie dans la partie de WhatsApp).

- L'application Telegram utilise aussi le chiffrement bout en bout. Les discussions vont être protégées durant la transmission.
Cette application n'utilise pas le protocole Signal. Elle utilise le protocole de chiffrement MTProto. Ce protocole est très critiqué, car c'est un protocole fait par Telegram, mais Telegram affirme que le niveau de sécurité est élevé. Ce protocole utilise aussi un chiffrement asymétrique et symétrique.

# Question 5

- Argument en faveur : cela permettrait à l'autorité d'empêcher des communications qui peuvent être criminelles ou menaçantes pour la société. Cela peut aussi permettre de mettre l'accent sur le fait de protéger les enfants contre l'exploitation. Elle pourrait aussi permettre de gérer des activités illicites telles que la vente de drogue, d'arme ou autre.

En résumé, le fait que l'autorité ait accès à ces communications permettrait une plus grande sécurité.

- Argument contre : cela permettrait à l'autorité de tout connaître sur les conversations et donc cela atteindrai le droit à la vie privé et permettrai un accès non autorisé à des informations personnelles. Certaines personnes peuvent aussi craindre que ces lois puissent être utilisées de manière abusive pour surveiller les citoyens. De plus, le fait d'imposer le déchiffrement des conversations peut créer des failles de sécurité, qui engendrerait des attaques régulières.

En résumé, cela donnerait à l'autorité et aux attaquants un accès aux informations privé des citoyens.