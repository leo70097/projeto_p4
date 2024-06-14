import unittest
from datetime import datetime
from Models.SoftwareTicket import SoftwareTicket

class TestSoftwareTicket(unittest.TestCase):

    def setUp(self):
        self.ticket = SoftwareTicket(1, 101, 'Software XYZ', 'Instalação de software')

    def test_initialization(self):
        self.assertEqual(self.ticket.id, 1)
        self.assertEqual(self.ticket.colaborador_id, 101)
        self.assertEqual(self.ticket.software, 'Software XYZ')
        self.assertEqual(self.ticket.descricao_necessidade, 'Instalação de software')
        self.assertIsNone(self.ticket.descricao_intervencao)
        self.assertIsNone(self.ticket.data_hora_atendimento)

if __name__ == '__main__':
    unittest.main()