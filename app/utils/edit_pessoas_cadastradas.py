import sqlite3
from pathlib import Path
from termcolor import colored
from app.lib.interface import Interface
from app.lib.validators import Validators

# caminho base do projeto (app/)
BASE_DIR = Path(__file__).resolve().parent.parent

# caminho do banco
DB_PATH = BASE_DIR / 'database' / 'pessoas_cadastradas.db'


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


class Remove:
    def __init__(self, ID):
        self.ID = ID

    def remove(self):
        banco = get_connection()
        cursor = banco.cursor()

        try:
            cursor.execute(
                "DELETE FROM pessoas WHERE id = ?",
                (self.ID,)
            )

            if cursor.rowcount == 0:
                print(colored('Pessoa não encontrada.', 'red'))
            else:
                banco.commit()
                print(colored('Dados deletados com sucesso!', 'green'))

        except Exception as er:
            print(colored('Perdão, algo deu errado, tente novamente.', 'red'))
            print(er)

        finally:
            banco.close()


class Edit:
    def __init__(self, ID):
        self.ID = ID

    def edit(self):
        banco = get_connection()
        cursor = banco.cursor()

        try:
            cursor.execute(
                "SELECT * FROM pessoas WHERE id = ?",
                (self.ID,)
            )
            person = cursor.fetchone()

            if not person:
                print(colored('Pessoa não encontrada.', 'red'))
                return

            i = Interface('', '')
            v = Validators()

            while True:
                print(i.line())
                print('Qual dado você quer editar?')

                avaliable_options = [
                    'Nome',
                    'Idade',
                    'Email',
                    'Telefone',
                    'CPF',
                    'Voltar ao menu inicial'
                ]

                for idx, item in enumerate(avaliable_options, start=1):
                    print(f'\033[33m{idx} - \033[36m{item}\033[m')

                option = int(i.read_option(avaliable_options))
                print(i.line())

                if option == 1:
                    new_name = v.verify_name()
                    cursor.execute(
                        "UPDATE pessoas SET nome = ? WHERE id = ?",
                        (new_name, self.ID)
                    )

                elif option == 2:
                    new_old = int(v.verify_old())
                    cursor.execute(
                        "UPDATE pessoas SET idade = ? WHERE id = ?",
                        (new_old, self.ID)
                    )

                elif option == 3:
                    new_email = v.verify_email()
                    cursor.execute(
                        "UPDATE pessoas SET email = ? WHERE id = ?",
                        (new_email, self.ID)
                    )

                elif option == 4:
                    new_telefone = v.verify_number()
                    cursor.execute(
                        "UPDATE pessoas SET telefone = ? WHERE id = ?",
                        (new_telefone, self.ID)
                    )

                elif option == 5:
                    new_cpf = v.verify_cpf()
                    cursor.execute(
                        "UPDATE pessoas SET cpf = ? WHERE id = ?",
                        (new_cpf, self.ID)
                    )

                else:
                    return

                banco.commit()
                print(colored('Dado atualizado com sucesso!', 'green'))

                while True:
                    response = input(
                        colored('Deseja alterar mais algum dado? [S/N] ', 'yellow')
                    ).strip().upper()

                    if response.startswith('S'):
                        break
                    elif response.startswith('N'):
                        return
                    else:
                        print(colored('Opção inválida, tente novamente.', 'red'))

        except Exception as er:
            print(colored('Perdão, algo deu errado, tente novamente.', 'red'))
            print(er)

        finally:
            banco.close()
