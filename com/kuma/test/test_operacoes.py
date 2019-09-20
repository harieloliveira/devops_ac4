from unittest import TestCase
from com.kuma.operacoes import operacoes

class TestOperacoes(TestCase):
    def setUp(self):
        self.operacoes = operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1,5]),6, "Should be 6")
    
    def test_palavra(self):
        self.assertEqual(self.operacoes.total_letras('Hariel'),6, "Should be 6")