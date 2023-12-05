import unittest
import sys
import os

ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
sys.path.append(os.path.join(ROOT,'code/'))
from SDES import encod_text,double_encod

class TestSDESFunctions(unittest.TestCase):

    def test_encod_text_with_string_input(self):
        cle = 0b1110001110
        texte_clair = "Hello"
        texte_chiffre = encod_text(texte_clair, cle)
        self.assertEqual(texte_chiffre, [159, 225, 82, 82, 108])

    def test_encod_text_with_list_input(self):
        cle = 0b1110001110
        liste_claire = [72, 101, 108, 108, 111]
        liste_chiffre = encod_text(liste_claire, cle)
        self.assertEqual(liste_chiffre, [159, 225, 82, 82, 108])

    def test_double_encod(self):
        cle1 = 0b1110001110
        cle2 = 0b0101010101
        texte_clair = "Hello"
        double_chiffre = double_encod(texte_clair, cle1, cle2)
        self.assertEqual(double_chiffre, [29, 188, 15, 15, 164])


if __name__ == '__main__':
    unittest.main()
