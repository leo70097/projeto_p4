import unittest
from Models.HardwareTicket import HardwareTicket
from datetime import datetime

class TestHardwareTicket(unittest.TestCase):
    
    def setUp(self):
        self.ticket = HardwareTicket(
            id=1,
            colaborador_id=101,
            equipment='Laptop',
            avaria='Não liga',
            descricao_reparacao=None,
            data_hora_atendimento=None,
            pecas=None
        )


    def test_initialization(self):
        self.assertEqual(self.ticket.id, 1)
        self.assertEqual(self.ticket.colaborador_id, 101)
        self.assertEqual(self.ticket.equipment, 'Laptop')
        self.assertEqual(self.ticket.avaria, 'Não liga')
        self.assertIsNone(self.ticket.descricao_reparacao)
        self.assertIsNone(self.ticket.data_hora_atendimento)
        self.assertIsNone(self.ticket.pecas)
        self.assertEqual(self.ticket.estado_ticket, 'porAtender')
        self.assertEqual(self.ticket.tipo_ticket, 'hardware')

    # python -m unittest discover Testes
        
    if __name__ == '__main__':
        unittest.main()
