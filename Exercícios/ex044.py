"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format(' LOJAS STARK '))
preço = float(input('Qual o valor da compra? R$ '))
print('''Escolha a forma de pagamento:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão''')
pgto = int(input('Forma de pagamento: '))
if pgto == 1:
    total = preço - (preço * 10 / 100)
elif pgto == 2:
    total = preço - (preço * 5 / 100)
elif pgto == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em 2x (sem juros) de R${:.2f}.'.format(parcela))
elif pgto == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas pasrcelas? '))
    parcelas = total / totalparc
    print('Sua compra será parcelada em {}x (com juros) de R${:.2f}'.format(totalparc, parcelas))
else:
    total = preço
    print('Opção de pagamento INVÁLIDA. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preço, total))
