import unittest
from unittest.mock import patch
from io import StringIO

from src.utils import executar_quiz
from src.questoes import perguntas


class TestQuiz(unittest.TestCase):

    @patch("builtins.input", side_effect=["2", "2", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_quiz_todas_corretas(self, mock_stdout, mock_input):
        executar_quiz(perguntas)
        output = mock_stdout.getvalue()
        self.assertIn("Você fez 3 ponto(s) de 3.", output)

    @patch("builtins.input", side_effect=["1", "1", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_quiz_algumas_erradas(self, mock_stdout, mock_input):
        executar_quiz(perguntas)
        output = mock_stdout.getvalue()
        self.assertIn("Você fez 1 ponto(s) de 3.", output)

    @patch("builtins.input", side_effect=["3", "1", "3"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_quiz_todas_erradas(self, mock_stdout, mock_input):
        executar_quiz(perguntas)
        output = mock_stdout.getvalue()
        self.assertIn("Você fez 0 ponto(s) de 3.", output)

    @patch("builtins.input", side_effect=["2", "2", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_mensagens_corretas(self, mock_stdout, mock_input):
        executar_quiz(perguntas)
        output = mock_stdout.getvalue()
        self.assertIn("Correto!", output)
        self.assertNotIn("Errado!", output)

    @patch("builtins.input", side_effect=["3", "1", "3"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_mensagens_erradas(self, mock_stdout, mock_input):
        executar_quiz(perguntas)
        output = mock_stdout.getvalue()
        self.assertIn("Errado!", output)
        self.assertNotIn("Correto!", output)


if __name__ == "__main__":
    unittest.main()
