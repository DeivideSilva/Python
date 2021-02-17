import os
os.system('cls')

""" n=int(input('Digite um numero: '))
for c in range(0,11):
 print(n,"x",c,"=",c*n) """

 #Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
""" for c in range(2,51,2):
    print(c)  """

#Crie um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,indo de 10 até 0,com uma pausa de 1 segundo entre eles.
""" from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print("Bum!! Bum!! Poow!! Poow!!") """

#Exercicio Criar uma programa que exiba a quantidade de * com base no número digitado.
""" n = int(input("Informe um numero: "))
asteristico = ''
for cont in range(n):
    asteristico += '*'
    print(asteristico) """

""" c= 1
while c < 10:
    print(c)
    c+=1
print('FIM') """

""" n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("FIM") """
""" 
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print("Você digitou {} números pares e {} números impares!".format(par,impar))

 """

 #Faça um programa que leia o sexo de uma pessoa,mas só aceite os valores 'M ou 'F'.
 #Caso esteja errado,peça a digitação novamente até ter um valor correto.

""" sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input("Informe um sexo:(M) ou (F) ").upper()
    if sexo != 'M' and sexo != 'F':
       print("Opção incorreta tente novamente!!!")

print("Você é do sexo {}".format(sexo))
 """

 #Crie um programa que leia dois valores e mostre um menu na tela:
 #[1] somar
 #[2]multiplicar
 #[3]maior
 #[4]novos numeros
 #[5]sair do programa
 #Seu programa deverá realizar a operação solicitada em cada caso.

""" v1= int(input("Informe um numero: "))
v2= int(input("Informe outro numero: "))

op = 0
while op != 5:
  op = int(input("Escolha uma opção: \n1-para somar \n2-para multiplicar\n3-Para numeros maiores\n4-Para novos numeros\n5-Para sair\n"))

  print("Você escolheu a opção:",op)
  
  if op == 1:
      print("A soma é ",v1 + v2,"\n")
  if op == 2:
      print("A multiplicação é: ",v1 * v2,"\n")
  if op == 3:
      if v1 > v2:
        print("O maior numero é: ",v1,"\n" )
      else:
        print("O maior numero é ",v2,"\n")
  if op == 4:
      int(input("Informe um numero: "))
      int(input("Informe outro numero: "))
print("Saindo do programa.....") """

""" Crie um programa que leia varios numeros inteiros pelo teclado.O programa só vai parar quando o usuário digitar o valor 999,que é 
a condição de parada.No final,mostre quantos números foram digitados
e qual foi a soma entre eles,(desconsiderando a flag).
"""
""" cont = 0
soma = 0
while 'true':
    n = int(input("Digite um número: (999 para parar)"))
    if n == 999:
        break
    cont +=1
    soma += n
print(f"A quantidade de números é {cont} e a soma é {soma}") """

#lanche = ("Hambúrguer","Suco","Pizza",#"Pudim","Batata frita","Torta")
#for c in lanche:
  #  print(f"Eu vou comer {c}")
#print("Comi muito!!!")

#for c in range(0,len(lanche)):
  #  print(f"Eu vou comer {lanche[c]}")

#for pos,c in enumerate(lanche):
    #print(f"Eu vou comer {c} na posição #{pos}")

#print(sorted(lanche)) #Coloca em ordem
#a = (1,3,6,8,9)
#b = (10,20,3,6,8,11)
#c = a + b
#print(c.count(8)) # Mostra quantas vezes o numeros aparece.
""" v = ("Zero","Um","Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez")
while 'true':
    n = int(input("Digite um número entre (0 e 20):"))
    if n < 0 or n > 20:
        print("Erro!!Tente novamente")
    for c in enumerate(v):
        if c[0] == n:
         print(f"Você digitou{c}") """
  
#num = (2,4,0,12) # Tupla é imutavel
#print(num)
       
#num = [2,4,0,12] # Lista
#num.append(100) # Serve para adicionar na lista
#num.sort() # Coloca em ordem
#num.insert(1,2) # Serve para inserir especificando a posição.
#num.sort(reverse=True) # Coloca ao contrario a oredem da lista.
#num.pop() # Remove o ultimo elemento da lista.
#num.pop(1) # Remove o indice especificado 
#num.remove(2) # Remove o elemento mesmo que possua outros elementos iguais.
""" if 3 in num:
    num.remove(3)
else:
    print(f"O número não existe na lista")
print(num)
print(f"A lista possui {len(num)} elementos") 

"""

""" valores = list()
valores.append(10)
valores.append(30)
valores.append(100)

for c,v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
print("Cheguei ao final da lista....") 

"""

""" valores = list()
for cont in range(0,5):
    valores.append(int(input("Digite um número: ")))
print(f"Você digitou {valores}") """

""" a = [2,8,9,10,23]
b = a[:] # Só adiciona na lista b
b[2] = 55 # Adiciona em ambas as listas
print(a)
print(b) 

"""

# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final,mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

""" valores = list()
maior = menor = 0
for cont in range(0,5):
    valores.append(int(input(f"Informe um valor na posição {cont}: ")))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print("-=" *30)
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i,v in enumerate(valores):
    if v == maior:
        print(f"{i}...",end="")
        print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i,v in enumerate(valores):
    if v == menor:
        print(f"{i}...",end="")
print() 

"""

""" 
galera = [["Julia",10],["Princesa",9],["Joaquim",37],["Paula",22]]
for pessoas in galera:
    print(f"{pessoas[0]} tem {pessoas[1]} anos de idade.") 
"""
""" galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1

print(f'Temos {totalmaior} maior(es) e {totalmenor} menor(es) de idade.') """

""" pessoas = {"nome": "Deivide", "sexo":"M","idade":36}
print(f'O nome {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.items()) """

###################### Dicionarios ######################

#pessoas = {"nome": "Deivide", "sexo":"M","idade":36}
#del pessoas['sexo']
""" pessoas['peso'] = 90.0
for k,v in pessoas.items():
    print(f'{k} = {v}') """

""" brasil = []
estado1 = {'uf':'São Paulo','sigla':'SP'}
estado2 = {'uf':'Rio de janeiro','sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf']) """

###################### Funções ######################

""" def mostralinha():
    print('-'*30)
mostralinha()
mostralinha() """

""" def mensagem(msg):
    print(msg)
mensagem('Isto é uma função!!!') """

""" def soma(n1,n2):
    s = n1 + n2
    print('-'*30)
    print(f'A soma é: {s}')
    print('-'*30)

soma(50,50) """

""" def contador(*num):
    print(num)

contador(1,6,8,9,7)
contador(10,20,65,45,78,96)
contador(1,2,3) """

""" def dobravalores(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [12,6,5,2,3,4]
dobravalores(valores)
print(valores) """

""" def soma(* n): # desempacotamento
    s = 0
    for num in n:
        s += num
    print(f'Somando os valores {n} temos {s}')

soma(25.60,30)
soma(100,200,500,80) """
  
# definir a função
# calcular a area do terreno
""" def area(l,c):
    result = l * c
    print(f'A área do terreno {l}x{c} é de {result}m²')


v1= float(input('Informe a largura do terreno: '))
v2 = float(input('Informe o comprimento do terreno: '))
area(v1,v2)
 """
#def contador(i,f,p):
   
""" Faz uma contagem e mostra na tela.
    param i: inicio da contagem
    param f: fim da contagem
    param p: passo da contagem     
"""
  #  c = 1
   # while c <= f:
       # print(f'{c} ',end='')
       # c += p
    #print('FIM!')


#contador(0,100,10) 

#help(contador)

""" def soma(v1=0,v2=0,v3=0):
    return v1 + v2 + v3
   

x= soma(5,2,8)
print(f'A soma entre os três valores é {x}') """
#import uteis
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#n = int(input("Digite um número: "))
#fat = uteis.fatorial(n)
#print(f'O fatorial do numero {n} é {fat}')
#print(f'O dobro do numero {n} é {uteis.dobro(n)}')
#print(f'O triplo do numero {n} é {uteis.triplo(n)}')
#print(f'Os resultados são {f1}, {f2} e {f3}')


###################### Tratamento de Erros ######################

try:
    a = int(input('Informe um número: '))
    b = int(input('Informe outro número: '))
    c = a / b
except:
    print('Houve um erro :(')
else:  
  print(f'O resultado da divisão é {c}')



