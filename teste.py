import pandas as pa
#print('Hello Word')
#print('Teste')
"""
canal = "YOUTUBE"
curso = "Phyton"
print(canal + " " + curso)
"""

#if 20 > 3:
    #print('MAIOR')
#print('FIM...')


#array = ['carro','avião','navio']
#print(array[1])
#import random

"""num_1 = 20
num_2 = 50.6
num_3 = 1j
num_r = random.randrange(0,60)
x = num_r
"""

#print("Valor: " + str(x) + " Tipo " + str(type(x)))

#texto = "Estou aprendendo Python"
#texto.strip() # Retira os espaços em branco
#print(texto.lower()) # Transforma tudo para minuscula
#print(texto.upper()) # Transforma tudo para maiuscula
#print(texto.replace("Python","JavaScript")) # Troca uma palavra
#a = texto.split(" ") # Separa a string em partes
#print(a[2])

#res = "Estou" in texto
#print(res)
#print(texto[16:23])
#print("O tamanho do texto é : "+ str(len(texto)))

""" dia = 5
mes = "fevereiro"
ano = 2021
data = "{} de {} de {}"
print(data.format(dia,mes,ano))
nome = input('Informe o seu nome ')
print('Prazer em conhecer ' + nome) """
""" 
texto = 'Agora tem'

if texto:
    print('Possui texto')
else:
    print('Não possui texto!!!') """


""" carros = ["Gol","Argo","Fusca","Corsa","Palio"]
carros2 = ["147","Celta","Brasilia"]
carros3 = carros + carros2
#carros.append("Civic")
#carros.append("Corola")
#carros.remove("Argo")

print(str(len(carros3)) + " carros na lista")
print(carros3) """


""" res = 0
numero1 = input("Informe um numero: ")
numero2 = input("Informe outro numero: ")
op = input("Informe uma opração:(+ - * /) ")

if op == "+":
    res = int(numero1) + int(numero2)
elif op == "-":
    res = int(numero1) - int(numero2)
elif op == "*":
    res = int(numero1) * int(numero2)
elif op == "/":
    res = int(numero1) / int(numero2)
else:
    print("Informe uma operação valida!!!")

print("O resultado é: "+ str(res)) """

####################################################################
#import os
#os.system("cls")

""" carros = ["CRV","Parati","Monza","Ford Ka","Fiesta"]

for carro in carros:
    if(carro =="Monza"):
        break
    print(carro) """

""" cores = ["azul","amarelo","verde","roxo","branco"]
i = 0
tamanho = len(cores)
while i < tamanho:
    print(cores[i])
    i+=1
print("Fim do Loop....") """

""" carros = []
print("#### Pressione (s) para sair ####")
carro = input("Informe um carro... ")
while carro != "s":
     carros.append(carro)
     carro = input("Informe um carro... ")
for n in carros:
    print(n)

print("Finalizando.....") """

""" carros = [
    ["Modelo","HRV"],
    ["Fabricante","Honda"],
    ["Ano",2018]
]
for l,c in carros:
    print("Linha: " + l + " | " + "Coluna: " + str(c)) """

""" teste = pa.read_excel('março.xlsx')
print(teste) 

"""