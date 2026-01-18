from datetime import date
from termcolor import colored
from app.lib.validar_cpf import *
import re

ano_atual = date.today().year

class Validators:
    def __init__(self):
        self.dados = dict()

    def verificar_dados(self):
        self.verify_name()
        self.verify_old()
        self.verify_email()
        self.verify_number()
        self.verify_cpf()
        return self.dados

    def verify_name(self):
        while True:
            nome = input('Nome completo: ')

            if nome.replace(" ", "").isalpha():
                self.dados['nome'] = str(nome).strip().title()
                return self.dados['nome']

            else:
                print(colored('Digite um nome apenas com letras, caracteres especiais e números não são aceitos.', 'red'))
                

    def verify_old(self):
        while True:
            nascimento = input('Ano de nascimento: ')
            try:
                int(nascimento)
                nascimento = int(nascimento)
                idade = ano_atual - nascimento
                if idade < 18:
                    print(colored('Você não pode cadastrar uma pessoa menor de idade no sistema.', 'red'))
                else:
                    self.dados['idade'] = idade
                    return self.dados['idade']
            except:
                print(colored('Digite um ano de nascimento válido', 'red'))

    def verify_email(self):
        while True:
            email = str(input('Endereço de e-mail: ')).strip()
            pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(pattern, email):
                self.dados['email'] = email
                return self.dados['email']
            else:
                print(colored('O endereço de e-mail que você digitou não existe, tente novamente.', 'red'))
        
    def verify_number(self):
        while True:
            telefone = (str(input('Digite o número de telefone (Com ou sem pontuação) '))).replace('(', '').replace(')', '').replace('-', '').strip()
            if len(telefone) != 11:
                print(colored('Número de telefone inválido, isso pode ser por você ter digitado sem o DDD ou pelo formato estar incorreto.', 'red'))
            else:
                self.dados['telefone'] = telefone
                return self.dados['telefone']

    def verify_cpf(self):
        while True:
            cpf = (str(input('CPF (Com ou sem pontuação): '))).replace('.', '').replace('-', '').strip()
            c = VerifyCPF(cpf)
            if c.isCpfValid() == True:
                self.dados['cpf'] = str(cpf)
                return self.dados['cpf']
            
            else:
                print(colored('Número de CPF inválido, tente novamente!', 'red'))
