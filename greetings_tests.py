import unittest
from robot import *

class greetingsTest(unittest.TestCase):

    def setUp(self):
        _, self.robot = start()

    def testing_01_welcome(self):
        greetings = ["oi", "olá", "e aí", "eae", "tudo bem?", "td bem?", "oi, tudo bem?", "olá, tudo bem?", "oi, td bem?", "olá, td bem?", "e aí, beleza?", "eae, beleza?"]

        for greeting in greetings:
            print(f"Testando saudação: {greeting}")

            replies = self.robot.get_response(greeting)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("olá, sou o ironbot", replies.text.lower())
    
    def testing_02_time_greetings(self):
        greetings = ["bom dia", "boa tarde", "boa noite", "oi, bom dia", "olá, bom dia", "e aí, bom dia", "eae, bom dia", "oi, boa tarde", "olá, boa tarde", "e aí, boa tarde", "eae, boa tarde", "oi, boa noite", "olá, boa noite", "e aí, boa noite", "eae, boa noite"]

        for greeting in greetings:
            print(f"Testando saudação: {greeting}")

            replies = self.robot.get_response(greeting)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("sou o ironbot", replies.text.lower())

