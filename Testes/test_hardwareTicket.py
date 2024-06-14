import unittest
from Models.HardwareTicket import HardwareTicket
from datetime import datetime

class TestHardwareTicket(unittest.TestCase):
    
    def setUp(self):
        # Configuração inicial antes de cada teste
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
        # Teste para verificar a inicialização correta dos atributos da classe HardwareTicket
        
        # Verificações usando assertEqual para garantir que cada atributo está correto
        self.assertEqual(self.ticket.id, 1)
        self.assertEqual(self.ticket.colaborador_id, 101)
        self.assertEqual(self.ticket.equipment, 'Laptop')
        self.assertEqual(self.ticket.avaria, 'Não liga')
        
        # Verificações usando assertIsNone para garantir que os atributos opcionais estão inicializados como None
        self.assertIsNone(self.ticket.descricao_reparacao)
        self.assertIsNone(self.ticket.data_hora_atendimento)
        self.assertIsNone(self.ticket.pecas)

        # Verificações adicionais do estado_ticket e tipo_ticket
        self.assertEqual(self.ticket.estado_ticket, 'porAtender') # Verifica o estado inicial do ticket
        self.assertEqual(self.ticket.tipo_ticket, 'hardware')  # Verifica o tipo de ticket inicial

        
    # Executa os testes quando o arquivo é chamado diretamente
    if __name__ == '__main__':
        unittest.main()

    # python -m unittest discover Testes

