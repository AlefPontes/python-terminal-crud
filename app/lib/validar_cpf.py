import re

class VerifyCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def isCpfValid(self):
        """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

        # Checa se o tipo é
        if not isinstance(self.cpf,str):
            return False

        # Remove alguns caracteres indesejados
        self.cpf = re.sub("[^0-9]",'',self.cpf)
        
        # Verificação inicial do cpf
        if self.cpf=='00000000000' or self.cpf=='11111111111' or self.cpf=='22222222222' or self.cpf=='33333333333' or self.cpf=='44444444444' or self.cpf=='55555555555' or self.cpf=='66666666666' or self.cpf=='77777777777' or self.cpf=='88888888888' or self.cpf=='99999999999':
            return False

        # Checa se a String tem 11 caracteres
        if len(self.cpf) != 11:
            return False

        sum = 0
        weight = 10

        """ Calculating the first cpf check digit. """
        for n in range(9):
            sum = sum + int(self.cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 -  sum % 11

        if verifyingDigit > 9 :
            firstVerifyingDigit = 0
        else:
            firstVerifyingDigit = verifyingDigit

        """ Calculating the second check digit of cpf. """
        sum = 0
        weight = 11
        for n in range(10):
            sum = sum + int(self.cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 -  sum % 11

        if verifyingDigit > 9 :
            secondVerifyingDigit = 0
        else:
            secondVerifyingDigit = verifyingDigit

        if self.cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
            return True
        return False

