#
# Autores:
# Michel 
#
# Data: 01/10/2022
##

# range(start, stop, step) 

for i in range(10):
    print(i) # Imprime 0 a 9
    
for i in range(10):
  print(i, end='') # Imprime 0 a 9

for i in range(9, -1, -1):
    print(i) # Imprime 9 a 0

# Interação em uma lista
cores = ["vermelho", "verde", "azul", "amarelo"]
print(cores)
for i in cores:
  print(i)
# Imprime vermelho verde azul amarelo


# Quebre o loop em "azul"
cores = ["vermelho", "verde", "azul", "amarelo"]
for i in cores:
    if i == "azul":
        break
    print(i)
# Imprime verde vermelho

# pule azul"
cores = ["vermelho", "verde", "azul", "amarelo"]
for i in cores:
    if i == "azul":
        continue
    print(i)
# Imprime vermelho verde amarelo

