"""@jacksontenorio8
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro 
entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.
"""
a = int(input('Digite um número: '))
for i in range(11):
    x = a * i
    print(f'{a} x {i} = {x}')

