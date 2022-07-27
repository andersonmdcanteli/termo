"""Tests if the remove_accents is working as expected

---> Class Test_remove_accents: verifica se esta sendo remivdo
    - ç
    - ^
    - `
    - ´
    - ~
    - ¨



--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/test_palavra_check_letra_repetida.py
    or
    python -m unittest -b tests/test_palavra_check_letra_repetida.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from functions.functions import palavra_check_letra_repetida
os.system("cls")

class Test_palavra_check_letra_repetida(unittest.TestCase):

    def test_sem_letra_repetida(self):
        result = palavra_check_letra_repetida("abcde")
        self.assertEqual(result, "", msg="output não é vazio para palavra sem letra repetida")

        result = palavra_check_letra_repetida("cetro")
        self.assertEqual(result, "", msg="output não é vazio para palavra sem letra repetida")

        result = palavra_check_letra_repetida("AMORE")
        self.assertEqual(result, "", msg="output não é vazio para palavra sem letra repetida")


    def test_com_letra_repetida(self):
        result = palavra_check_letra_repetida("amora")
        if "AMORA" in result:
            result = True
        self.assertTrue(result, msg="não foi identificada a letra repetida")

        result = palavra_check_letra_repetida("araao")
        if "ARAAO" in result:
            result = True
        self.assertTrue(result, msg="não foi identificada a letra repetida")



if __name__ == "__main__":
    unittest.main()
