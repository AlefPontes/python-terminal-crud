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
    # garante que a pasta do banco exista
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    criar_tabela(conn)
    return conn


def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT,
            telefone TEXT,
            cpf TEXT UNIQUE
        )
    """)
    conn.commit()


class Cadastrar_pessoa:
    def __init__(self):
        i = Interface(' <<< CADASTRAR NOVAS PESSOAS >>> ', '')
        i.cabeçalho()

    def cadastrar(self):
        banco = get_connection()
        cursor = banco.cursor()

        while True:
            while True:
                try:
                    v = Validators()
                    pessoa = v.verificar_dados()

                    cursor.execute(
                        """
                        INSERT INTO pessoas (nome, idade, email, telefone, cpf)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (
                            pessoa['nome'],
                            pessoa['idade'],
                            pessoa['email'],
                            pessoa['telefone'],
                            pessoa['cpf']
                        )
                    )

                    banco.commit()
                    break

                except sqlite3.IntegrityError:
                    print(colored('CPF já cadastrado.', 'red'))

                except Exception as erro:
                    print(colored('Algo deu errado, tente novamente.', 'red'))
                    print(erro)

            print(colored('Pessoa cadastrada com sucesso!', 'green'))

            while True:
                opcao = input(
                    colored('Deseja cadastrar uma nova pessoa? [S/N] ', 'cyan')
                ).strip().upper()

                if opcao.startswith('S'):
                    break
                elif opcao.startswith('N'):
                    banco.close()
                    return
                else:
                    print(colored('Opção inválida, tente novamente.', 'red'))
