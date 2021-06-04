distancia = float(input('Digite a distancia da viagem: '))
r = distancia * 0.50
t = distancia * 0.45
if distancia <= 200:
    print(f'A passagem fica R${r:.2f}')
else:
    print(f'Por causa da promocao , a passagem fica R${t:.2f}')
