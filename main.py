from time import sleep
from app.lib.interface import Interface
from app.utils.cadastrar_pessoas import Cadastrar_pessoa
from app.utils.mostrar_pessoas_cadastradas import Pessoas_cadastradas
from termcolor import colored
2
class Main:
    def __init__(self, options):
        self.options = options
        while True:
            i = Interface(' <<< MENU PRINCIPAL >>> ', self.options)
            i.main_menu()
            option = int(i.read_option(self.options))
            if option == 1:
                c = Cadastrar_pessoa()
                c.cadastrar()
            elif option == 2:
                m = Pessoas_cadastradas()
                m.mostrar_pessoas()
            elif option == 3:
                i.line()
                print(f"{' <<< OBRIGADO POR UTILIZAR NOSSO SISTEMA >>> ':-^80}")
                i.line()
                print(colored('Finalizando o programa...', 'red'))
                sleep(1)
                exit()

options = ['Cadastrar novas pessoas', 'Ver pessoas cadastradas', 'Sair do programa']

if __name__ == '__main__':
    Main(options)
