import sqlite3
from pathlib import Path
from termcolor import colored
from app.lib.interface import Interface
from app.lib.validators import Validators
from app.utils.edit_pessoas_cadastradas import Edit, Remove

# caminho base do projeto (app/)
BASE_DIR = Path(__file__).resolve().parent.parent

# caminho do banco
DB_PATH = BASE_DIR / 'database' / 'pessoas_cadastradas.db'


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


class Pessoas_cadastradas:
    def __init__(self):
        i = Interface(' <<< PESSOAS CADASTRADAS >>> ', '')
        print(f' {" <<< PESSOAS CADASTRADAS >>> ":-^80} ')

    def mostrar_pessoas(self):
        banco = get_connection()
        cursor = banco.cursor()

        cursor.execute("SELECT id, nome FROM pessoas ORDER BY nome")
        pessoas = cursor.fetchall()

        if not pessoas:
            print(colored('No momento, não há ninguém cadastrado no banco de dados.', 'red'))
            banco.close()
            input(colored('\nPressione ENTER para voltar ao menu...', 'yellow'))
            return

        for pessoa in pessoas:
            print(colored(f'{pessoa[0]} | {pessoa[1]}', 'green'))

        banco.close()
        self.options()


    def options(self):
        while True:
            i = Interface('', '')
            print(i.line())

            try:
                ID = int(
                    input(
                        'Digite o ID da pessoa para ver os dados completos '
                        '(0 para voltar ao menu inicial): '
                    )
                )

                if ID == 0:
                    return

                banco = get_connection()
                cursor = banco.cursor()

                cursor.execute(
                    "SELECT id, nome, idade, email, telefone, cpf FROM pessoas WHERE id = ?",
                    (ID,)
                )
                person = cursor.fetchone()
                banco.close()

                if not person:
                    print(colored('Pessoa não encontrada.', 'red'))
                    continue   # ← volta a pedir o ID

                # ---- DAQUI PRA BAIXO SÓ RODA SE A PESSOA EXISTIR ----

                print(i.line())
                print(colored(f"{f'Dados de {person[1]}':^{i.tamanho_fonte}}", 'cyan'))

                print(
                    f'ID: {person[0]}\n'
                    f'Nome completo: {person[1]}\n'
                    f'Idade: {person[2]}\n'
                    f'Email: {person[3]}\n'
                    f'Telefone: {person[4]}\n'
                    f'CPF: {person[5]}'
                )

                print(f"{' <<< OPÇÕES DISPONÍVEIS >>> ':-^{i.tamanho_fonte}}")

                avaliable_options = [
                    'Ver os dados de outra pessoa',
                    'Editar dados',
                    'Deletar dados',
                    'Voltar ao menu inicial'
                ]

                for idx, item in enumerate(avaliable_options, start=1):
                    print(f'\033[33m{idx} - \033[36m{item}\033[m')

                print(i.line())
                option = int(i.read_option(avaliable_options))

                if option == 1:
                    continue

                elif option == 2:
                    Edit(ID).edit()
                    return

                elif option == 3:
                    Remove(ID).remove()
                    return

                elif option == 4:
                    return

            except ValueError:
                print(colored('Opção inválida, tente novamente.', 'red'))

            except Exception as erro:
                print(colored('Algo deu errado, voltando ao menu inicial.', 'red'))
                print(erro)
                return
