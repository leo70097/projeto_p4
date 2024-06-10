import unittest
from Models.HardwareTicket import HardwareTicket
from Models.ticket import Ticket
from datetime import datetime

class TestHardwareTicket(unittest.TestCase):
    def setUp(self):
        pass

    def test_hardware_ticket_construction(self):
        # Teste para garantir que o construtor da classe HardwareTicket funciona corretamente
        hardware_ticket = HardwareTicket(datetime.now(), 123, "porAtender","tipo", "equipamento", "avaria", datetime.now(), "descricaoReparacao", "pecas", "estado")
        self.assertEqual(hardware_ticket.data_hora, datetime.now())
        self.assertEqual(hardware_ticket.codigo_colaborador, 123)
        self.assertEqual(hardware_ticket.estado_ticket, "porAtender")
        self.assertEqual(hardware_ticket.tipo_ticket, "Hardware")
        self.assertEqual(hardware_ticket.equipamento, "equipamento")
        self.assertEqual(hardware_ticket.avaria, "avaria")
        self.assertEqual(hardware_ticket.dataAtendimento, datetime.now())
        self.assertEqual(hardware_ticket.descricaoReparacao, "descricaoReparacao")
        self.assertEqual(hardware_ticket.pecas, "pecas")
        self.assertEqual(hardware_ticket.estado, "estado")

    def test_metodo_de_teste_2(self):
        # Outro exemplo de teste
        self.assertTrue(10 > 5)

if __name__ == '__main__':
    unittest.main()