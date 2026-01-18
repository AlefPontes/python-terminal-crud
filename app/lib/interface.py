from termcolor import colored

class Interface:
    def __init__(self, cabeçalho, lista, tam=80):
        self.opções = lista
        self.tamanho_fonte = tam
        self.texto_cabeçalho = cabeçalho

    def line(self):
        return '-' * self.tamanho_fonte

    def cabeçalho(self):
        print(self.line())
        print(f'{f"{self.texto_cabeçalho}":^{self.tamanho_fonte}}')
        print(self.line())

    def read_option(self, opções):
        while True:
            leitura_opção = input(colored('Sua opção: ', 'yellow'))
            try:
                opção = int(leitura_opção)
                if opção < 1 or opção > len(opções):
                    print(colored('Opção inválida, tente novamente.', 'red'))
                else: 
                    return leitura_opção
            except (TypeError, ValueError, KeyboardInterrupt):
                print(colored('Opção inválida, tente novamente.', 'red'))

    def main_menu(self):
        self.cabeçalho()
        c = 1
        for item in self.opções:
            print(f'\033[33m{c} - \033[36m{item}\033[m')
            c += 1
        self.line()
