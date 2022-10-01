#
# Autores:
# Michel 
#
# Data: 01/10/2022
##

############### fatorial 

################   1.1   #########################
numero = int(input('Digite um número inteiro positivo: '))

fat = 1
while numero > 0:
  fat = fat * numero
  numero = numero - 1
print('O fatorial desse número é ', fat)


############  1.2  #############################
#Exemplo (fatorial sem recursão):

numero = int(input('Digite um número inteiro positivo: '))

fat = 1
for i in range(1, numero + 1):
  fat = fat * i
  print(i, '->', fat)
  

################   1.3   ###########################
# se a entrada for ZERO
#entrada
num1 = int(input("informe um número :"))
temp= num1
fat = 1 
#processamento
if num1 == 0 :
  pass 
else:
  while (num1 > 0):
    fat = fat * num1 # 5*4*3*2*1
    num1 = num1 - 1

#saida  
print(f"o fatorial de {temp} é {fat}")  


############  2  ###############################
# exemplo (Fatorial com função e sem recursão)
#https://pt.wikipedia.org/wiki/Fatorial

def fatorial(valor):
  valor = valor if valor > 1 else 1
  fat = 1
  for i in range(1, valor+1):
    fat = fat * i
  return fat

# Testando...
numero = int(input('Digite um número inteiro positivo: '))
for i in range(1, numero+1):
  #print(numero)
  print(i, '->', fatorial(i))