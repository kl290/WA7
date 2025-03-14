import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aufgabe.eingabe_zahl import eingabe_zahl

import unittest
from unittest.mock import patch


class TestEingabeZahl(unittest.TestCase):

    @patch('builtins.input', side_effect = ['7.5', '5'])
    @patch('builtins.print')
    def test_bei_ungueltiger_int(self, mock_print, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", return_type = int)
        mock_print.assert_called_once_with(f"Ungültige Eingabe '7.5'. Bitte eine gültige Zahl eingeben!")
        self.assertEqual(result, 5)

    @patch('builtins.input', return_value = '7.5')
    @patch('builtins.print')
    def test_bei_gueltiger_float(self, mock_print, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", return_type = float)
        mock_print.assert_not_called()
        self.assertEqual(result, 7.5)

    @patch('builtins.input', return_value = '5')
    @patch('builtins.print')
    def test_gueltige_eingabe_bereich(self, mock_print, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = 1, max_val = 10, return_type = int)
        mock_print.assert_not_called()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect = ['-2', '5'])
    @patch('builtins.print')
    def test_eingabe_unter_minimalwert(self, mock_print, mock_input, min_val = -1):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = -1, max_val = 10, return_type = int)
        mock_print.assert_called_once_with(f"Die Zahl muss mindestens {min_val} sein!")
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect = ['20', '10'])
    @patch('builtins.print')
    def test_eingabe_ueber_maximalwert(self, mock_print, mock_input, max_val = 15):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ", min_val = 1, max_val = 15, return_type = int)
        mock_print.assert_any_call(f"Die Zahl darf höchstens {max_val} sein!")
        self.assertEqual(result, 10)

    @patch('builtins.input', side_effect = [[], '5'])
    @patch('builtins.print')
    def test_ausgabe_fehlermeldung_bei_ungueltiger_eingabe_array(self, mock_print, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ")
        mock_print.called_once_with("Ungültige Eingabe '[]'. Bitte eine gültige Zahl eingeben!")
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['abc', '7.5'])
    @patch('builtins.print')
    def test_ausgabe_fehlermeldung_bei_ungueltiger_eingabe(self, mock_print, mock_input):
        result = eingabe_zahl("Geben Sie eine Zahl ein: ")
        mock_print.assert_called_once_with("Ungültige Eingabe 'abc'. Bitte eine gültige Zahl eingeben!")
        self.assertEqual(result, 7.5)



if __name__ == '__main__':
    unittest.main()
