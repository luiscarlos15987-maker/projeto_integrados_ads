"""Protótipo acadêmico em memória. Use apenas dados fictícios."""
import unicodedata


def normalizar(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto.casefold())
                   if unicodedata.category(c) != 'Mn')


def cadastrar(pacientes, nome, idade, telefone):
    nome = nome.strip()
    if not nome:
        raise ValueError('Informe o nome.')
    if isinstance(idade, bool) or not isinstance(idade, int) or not 0 <= idade <= 130:
        raise ValueError('Idade deve ser um inteiro entre 0 e 130.')
    digitos = ''.join(c for c in telefone if c in '0123456789')
    if len(digitos) not in (10, 11):
        raise ValueError('Telefone deve conter DDD e 10 ou 11 dígitos.')
    paciente = {'nome': nome, 'idade': idade, 'telefone': digitos}
    pacientes.append(paciente)
    return paciente


def estatisticas(pacientes):
    if not pacientes:
        return None
    minimo = min(p['idade'] for p in pacientes)
    maximo = max(p['idade'] for p in pacientes)
    return {'total': len(pacientes),
            'media': sum(p['idade'] for p in pacientes) / len(pacientes),
            'novos': [p for p in pacientes if p['idade'] == minimo],
            'velhos': [p for p in pacientes if p['idade'] == maximo]}


def buscar(pacientes, nome):
    termo = normalizar(nome.strip())
    if not termo:
        raise ValueError('Digite um nome para buscar.')
    return [p for p in pacientes if termo in normalizar(p['nome'])]


def listar(pacientes):
    if not pacientes:
        print('Nenhum paciente encontrado.')
    for indice, p in enumerate(pacientes, 1):
        print(f"{indice}. {p['nome']} | {p['idade']} anos | {p['telefone']}")


def main():
    pacientes = []
    while True:
        print('\n=== SISTEMA CLÍNICA VIDA+ ===\n1. Cadastrar paciente\n2. Ver estatísticas'
              '\n3. Buscar paciente\n4. Listar todos os pacientes\n5. Sair')
        try:
            opcao = input('Escolha uma opção: ').strip()
            if opcao == '1':
                nome = input('Nome: ')
                try:
                    idade = int(input('Idade: '))
                except ValueError:
                    print('Idade inválida. Digite um número inteiro.'); continue
                telefone = input('Telefone com DDD: ')
                cadastrar(pacientes, nome, idade, telefone)
                print('Paciente cadastrado com sucesso!')
            elif opcao == '2':
                resultado = estatisticas(pacientes)
                if resultado is None:
                    print('Nenhum paciente cadastrado.'); continue
                print(f"Total: {resultado['total']} | Idade média: {resultado['media']:.2f}")
                print('Mais novos:'); listar(resultado['novos'])
                print('Mais velhos:'); listar(resultado['velhos'])
            elif opcao == '3':
                listar(buscar(pacientes, input('Nome para busca: ')))
            elif opcao == '4':
                listar(pacientes)
            elif opcao == '5':
                print('Programa encerrado.'); break
            else:
                print('Opção inválida. Escolha de 1 a 5.')
        except ValueError as erro:
            print(erro)
        except (EOFError, KeyboardInterrupt):
            print('\nPrograma encerrado.'); break


if __name__ == '__main__':
    main()

