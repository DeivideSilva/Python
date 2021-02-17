comprimento = float(input('Digite o comprimento do caminhão: '))
largura = float(input('Digite a largura do caminhão: '))
furo1 = float(input('Digite o valor do primeiro furo: '))
furo2 = float(input('Digite o valor do segundo furo: '))

area = comprimento * largura
soma = (furo1 + furo2) / 2
metrosCubicos = area * soma

print('O valor em metros cubicos é {:.2f}m³'.format(metrosCubicos))