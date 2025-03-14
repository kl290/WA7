import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aufgabe.eingabe_zahl import eingabe_zahl

import unittest
from unittest.mock import patch


class TestEingabeZahl(unittest.TestCase):

    @patch('builtins.input', return_value = '7.5')
    def test_bei_ungueltiger_int(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = 1, max_val = 10, return_type = int)
        self.assertIsNone(result)

    @patch('builtins.input', return_value = '7.5')
    def test_bei_gueltiger_float(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = 1, max_val = 10, return_type = float)
        self.assertEqual(result, 7.5)

    @patch('builtins.input', return_value = '5')
    def test_gueltige_eingabe_bereich(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = 1, max_val = 10, return_type = int)
        self.assertEqual(result, 5)

    @patch('builtins.input', return_value = '-2')
    def test_eingabe_unter_minimalwert(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = -1, max_val = 10, return_type = int)
        self.assertIsNone(result)

    @patch('builtins.input', return_value = '20')
    def test_eingabe_ueber_maximalwert(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = 1, max_val = 15, return_type = int)
        self.assertIsNone(result)

    @patch('builtins.input', return_value = 'abc')
    def test_ungueltige_eingabe_text(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", return_type = int)
        self.assertIsNone(result)

    @patch('builtins.input', return_value = ['array'])
    def test_ungueltige_eingabe_array(self, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", return_type = float)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
