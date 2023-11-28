import unittest
from robot import *

class basicInfoTest(unittest.TestCase):

    def setUp(self):
        _, self.robot = start()
    
    def testing_01_location(self):
        questions = ["onde a academia iron men está localizada?",
                "onde a iron men está localizada?",
                "onde está localizada a academia iron men?",
                "onde está localizada a iron men?",
                "onde fica a academia iron men?",
                "onde fica a iron men?",
                "onde a academia iron men fica?",
                "onde a iron men fica?",
                "onde vocês funcionam?",
                "onde a academia iron men funciona?",
                "onde a iron men funciona?",
                "qual é a localização da academia iron men?",
                "qual é a localização da iron men?",
                "qual é o endereço da academia iron men?",
                "qual é o endereço da iron men?"]
        
        for question in questions:
            print(f"Testando pergunta: {question}")

            replies = self.robot.get_response(question)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("a iron men está localizada", replies.text.lower())
    
    def testing_02_opening_hours(self):
        questions = ["qual é o horário de funcionamento da academia iron men?",
                "qual é o horário de funcionamento da iron men?",
                "que horas vocês funcionam?",
                "que horas a academia iron men funciona?",
                "que horas a iron men funciona?",
                "que horas vocês ficam aberto?"]
        
        for question in questions:
            print(f"Testando pergunta: {question}")

            replies = self.robot.get_response(question)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("a iron men funciona", replies.text.lower())
    
    def testing_03_registration_fee(self):
        questions = ["há alguma taxa de inscrição?",
                "há alguma taxa de matrícula?",
                "existe alguma taxa de inscrição?",
                "existe alguma taxa de matrícula?",
                "é necessário pagar alguma taxa de inscrição?",
                "preciso pagar algum valor para me matricular?",
                "preciso pagar algum valor para me inscrever?",
                "tem taxa de inscrição?"]
        
        for question in questions:
            print(f"Testando pergunta: {question}")

            replies = self.robot.get_response(question)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("para se matricular na iron men", replies.text.lower())
    
    def testing_04_trial_classes(self):
        questions = ["a academia iron men oferece aulas experimentais?",
                "a iron men oferece aulas experimentais?",
                "a iron men tem aulas experimentais?",
                "a iron men tem aulas de cortesia?",
                "a iron men oferece aulas de teste?",
                "a iron men disponibiliza aulas de teste?"]
        
        for question in questions:
            print(f"Testando pergunta: {question}")

            replies = self.robot.get_response(question)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("o público interessado em conhecer a iron men", replies.text.lower())
    
    def testing_05_equipments(self):
        questions = ["que tipos de equipamentos a iron men possui?",
                "que tipos de equipamentos a academia iron men possui?",
                "a iron men possui quais tipos de equipamentos?",
                "a academia iron men possui quais tipos de equipamentos?",
                "quais são os equipamentos disponíveis na iron men?",
                "quais tipos de máquinas a iron men oferece?"]
        
        for question in questions:
            print(f"Testando pergunta: {question}")

            replies = self.robot.get_response(question)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("a iron men possui uma infraestrutura completa", replies.text.lower())

    def testing_06_payment(self):
        questions = ["quais são os preços dos planos?",
                "quais os valores dos planos disponíveis?",
                "quais planos a iron men oferece?",
                "quais planos a academia iron men oferece?",
                "a iron men oferece quais planos?",
                "a academia iron men oferece quais planos?",
                "quais os preços dos planos?"]
        
        for question in questions:
            print(f"Testando pergunta: {question}")

            replies = self.robot.get_response(question)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("a iron men oferece os seguintes planos", replies.text.lower())

    def testing_07_modalities(self):
        questions = ["a iron men oferece aulas de dança?",
                "a iron men oferece aulas de yoga?",
                "a iron men oferece aulas de pilates?",
                "a iron men oferece aulas de artes maciais?",
                "a iron men oferece aulas de jiu-jitsu?",
                "a iron men oferece aulas de boxe?",
                "a iron men oferece aulas de judô?",
                "a iron men oferece aulas de karatê?",
                "a iron men oferece outras modalidades além da musculação?",
                "a academia oferece aulas de dança?",
                "a academia oferece aulas de yoga?",
                "a academia oferece aulas de pilates?",
                "a academia oferece aulas de artes marciais?",
                "a academia oferece aulas de jiu-jitsu?",
                "a academia oferece aulas de boxe?",
                "a academia oferece aulas de judô?",
                "a academia oferece aulas de karatê?",
                "a academia oferece outras modalidades além da musculação?",
                "além da musculação, a academia tem aulas de dança, artes marciais, pilates, yoga ou outras atividades?"]
        
        for question in questions:
            print(f"Testando pergunta: {question}")

            replies = self.robot.get_response(question)
            self.assertGreaterEqual(replies.confidence, MINIMUM_TRUST)
            self.assertIn("além da musculação, a iron men oferece", replies.text.lower())
