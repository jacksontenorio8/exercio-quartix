"""@jacksontenorio8
O restaurante “Tudo de Bom” cobra R$ 32,00 pelo quilo de refeição. Escreva um algoritmo que 
leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
"""
k = float(input('Digite o peso: '))
p = k * 32
print('O valor a ser pago é R${}'.format(p))