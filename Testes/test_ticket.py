import unittest
from datetime import datetime
from Models.Ticket import Ticket

class TestTicket(unittest.TestCase):

    def setUp(self):
        # Configuração inicial, criando um objeto Ticket para usar nos testes
        self.ticket = Ticket(1, 101, 'porAtender', datetime.now(), 'hardware')

    def test_initialization(self):
        # Teste para verificar a inicialização correta dos atributos do Ticket
        self.assertEqual(self.ticket.id, 1)
        self.assertEqual(self.ticket.colaborador_id, 101)
        self.assertEqual(self.ticket.estado_ticket, 'porAtender')
        self.assertIsInstance(self.ticket.data_hora, datetime)
        self.assertEqual(self.ticket.tipo_ticket, 'hardware')

if __name__ == '__main__':
    unittest.main()