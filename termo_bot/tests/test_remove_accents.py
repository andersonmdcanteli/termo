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
    python -m unittest -v tests/test_remove_accents.py
    or
    python -m unittest -b tests/test_remove_accents.py

--------------------------------------------------------------------------------
"""

import os
import unittest
from functions.functions import remove_accents
os.system("cls")

class Test_remove_characters(unittest.TestCase):

    def test_cedilha(self):
        result = remove_accents("ç")
        self.assertEqual(result, "c", msg="does not removed ç")

        result = remove_accents("balança")
        self.assertEqual(result, "balanca", msg="does not removed ç")

    def test_cirncuflexo(self):
        result = remove_accents("ô")
        self.assertEqual(result, "o", msg="does not removed ^")

        result = remove_accents("avô")
        self.assertEqual(result, "avo", msg="does not removed ^")

    def test_agudo(self):
        result = remove_accents("ó")
        self.assertEqual(result, "o", msg="does not removed ´")

        result = remove_accents("avó")
        self.assertEqual(result, "avo", msg="does not removed ´")

    def test_grave(self):
        result = remove_accents("ò")
        self.assertEqual(result, "o", msg="does not removed ´")

        result = remove_accents("avò")
        self.assertEqual(result, "avo", msg="does not removed `")

    def test_til(self):
        result = remove_accents("ã")
        self.assertEqual(result, "a", msg="does not removed ~")

        result = remove_accents("não")
        self.assertEqual(result, "nao", msg="does not removed ~")

    def test_trema(self):
        result = remove_accents("ü")
        self.assertEqual(result, "u", msg="does not removed ¨")

        result = remove_accents("pingüim")
        self.assertEqual(result, "pinguim", msg="does not removed ¨")



if __name__ == "__main__":
    unittest.main()
