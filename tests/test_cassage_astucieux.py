import unittest
import sys
import os

ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
sys.path.append(os.path.join(ROOT,'code/'))
from SDES import encod_text,double_encod
from cassage_text import cassage_astucieux,cassage_brutale

ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
sys.path.append(os.path.join(ROOT,'doc/'))


class TestCassageFunctions(unittest.TestCase):

    def test_cassage_astucieux(self):
        """
            Cette methode va nous permettre de tester le cassage astucieux sur un message simple
        """
        texte_clair = "Hello"
        texte_chiffre = double_encod(texte_clair, 100,10)
        self.assertEqual(cassage_astucieux(texte_clair,texte_chiffre), (100,10))

    def test_arsene_lupin(self):
        """
            Cette methode va nous permettre de tester le cassage astucieux sur un extrait du livre arsene lupin
        """
        fichier_texte = os.path.join(ROOT, 'doc/arsene_lupin_extrait.txt')
        with open(fichier_texte, 'r', encoding='utf-8') as file:
            texte_clair=file.read()
            lignes = texte_clair.splitlines()[2:]
            texte_clair_modifie = '\n'.join(lignes)

        texte_chiffre = double_encod(texte_clair_modifie, 255,255)
        les_cles=cassage_astucieux(texte_clair_modifie,texte_chiffre)
        print(les_cles)
        self.assertEqual(les_cles, (255,255))


if __name__ == '__main__':
    unittest.main()
