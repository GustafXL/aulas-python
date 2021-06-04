from time import sleep
v = int(input('Qual velocidade voce estava indo ? '))
f = (v-80)*7
sleep(3)
if v >= 80:
    print('Voce foi multado , por excesso de velocidade !')
else:
    print('OK Muito bem , Dirija com cuidado.')
print(f'O valor da multa para pagar e de R${f:.2f}')


