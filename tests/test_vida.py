import unittest
from vida_plus.main import cadastrar, estatisticas, buscar


class TestVida(unittest.TestCase):
    def test_vazio(self):
        self.assertIsNone(estatisticas([]))

    def test_cadastro_e_busca(self):
        pacientes = []
        cadastrar(pacientes, ' João Silva ', 30, '(11) 99999-0000')
        self.assertEqual(buscar(pacientes, 'JOAO')[0]['nome'], 'João Silva')
        self.assertEqual(buscar(pacientes, 'Maria'), [])

    def test_estatistica_e_empates(self):
        pacientes = []
        for nome, idade in [('A', 20), ('B', 20), ('C', 50)]:
            cadastrar(pacientes, nome, idade, '11999990000')
        r = estatisticas(pacientes)
        self.assertEqual((r['total'], r['media']), (3, 30))
        self.assertEqual(len(r['novos']), 2)
        self.assertEqual(r['velhos'][0]['nome'], 'C')

    def test_invalidos_nao_alteram_lista(self):
        pacientes = []
        for nome, idade, tel in [('', 20, '11999990000'), ('Ana', -1, '11999990000'),
                                  ('Ana', 131, '11999990000'), ('Ana', 20, '123'),
                                  ('Ana', True, '11999990000')]:
            with self.assertRaises(ValueError):
                cadastrar(pacientes, nome, idade, tel)
        self.assertEqual(pacientes, [])

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            buscar([], ' ')


if __name__ == '__main__':
    unittest.main()

