# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em °C: '))
fah = ((9 * temp) / 5) + 32
print('A temperatura de {:.2f}°C equivale a {:.2f}°F.'.format(temp, fah))
