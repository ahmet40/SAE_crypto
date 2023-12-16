# Partie 2

# Question 1:
    L'alghorithme AES prend une clé de taille 256 bits qui est beaucoup plus grand que l'alghorithme SDES qui lui utilise une clé de 10 bits et dans lequels il y a 2 bits qui ne change pas et qui fait que la clé est de taille 8 bits. Nous devons donc faire tourner nos clé sur une boucle beaucoup plus grandes et donc qui prend plus de temps.

# Partie 4

## Question 1
Le fait d'utiliser toujours la même clé pour chiffrer les messages cause des soucis de sécuriter. En effet une clé avec utilisation répéter est plus vulnérable au déchiffrement par brute force ou l'utilisateur va essayer toutes les combinaisons logique possible. Il y a aussi un manque de confidentialité à long terme permet dans le cas ou un utilisateur déchiffre un message alors tous les messages chiffrer sera découvert. De plus l'un des objectifs de la cryptographie est de sécurisé  et de protéger les information si il y l'utilisation constante d'une clé sela réduit l'efficacité de la cryptographie.

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
Il peut être utilisé pour des transactions financières en ligne. Un exemple serait pour le paiement par carte bancaire. En effet pour une telle transaction, il est nécessaire de garantir une confidentialité optimale pour ne pas que les numéros de carte soit volés facilement et pour empêcher des attaques durant la transaction. Un autre cas serait lors de la transmission d'informations médicales, professionnels ou même politiques. En effet, cela augmenterait la sécurité des informations et garantirait que les documents envoyés restent sécurisés et ne sont pas facilement accessibles et compréhensibles, surtout en période de conflits géopolitiques ou face à des personnes potentiellement nuisibles telles que des entreprises ou des individus.


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