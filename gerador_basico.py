# Gerador de CPF
import random

for _ in range(1):
    cpf = ''

    for i in range(9):
        cpf += str(random.randint(0, 9))

    fator_calculo_1 = 10
    resultado_1 = 0
    digito_1 = 0

    for item in cpf:
        resultado_1 += (int(item) * fator_calculo_1)
        fator_calculo_1 -= 1
        
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = 0 if digito_1 > 9 else digito_1

    cpf += str(digito_1)

    fator_calculo_2 = 11
    resultado_2 = 0
    digito_2 = 0

    for item in cpf:
        resultado_2 += (int(item) * fator_calculo_2)
        fator_calculo_2 -= 1

    digito_2 = (resultado_2 * 10) % 11
    digito_2 = 0 if digito_2 > 9 else digito_2

    cpf += str(digito_2)

    print(f'CPF gerado: {cpf}')