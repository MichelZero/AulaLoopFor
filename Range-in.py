#
# Autores:
# Michel 
#
# Data: 01/10/2022
#
#
# Usando a função range()
# A função range() de Python facilita gerar uma série de números. Por
# exemplo, podemos usar a função range() para exibir uma sequência de
# números

# range(parada: int)
# range(parada) -> objeto de intervalo

# range(inicio: int, parada: int, paso: int=...)
# range(inicio, parada[, paso]) -> objeto de intervalo

# Retorna um objeto que produz uma sequência de inteiros desde o 
# início (inclusive) para parar (exclusivo) por etapa.
# por exemplo 
# o padrão de início é 0 e a parada é omitida! 
# intervalo (4) produz 0, 1, 2, 3.
# Esses são exatamente os índices válidos para uma lista de 4 elementos.
# Quando o passo é dado, ele especifica o incremento (ou decremento).

#########    range    ######################
valor1 = range(4)
print(valor1) # range(0, 4)
print(type(valor1)) # <class 'range'>

valor2 = range(1,4,1)
print(valor2) # range(1, 4)

valor3 = range(1,10,1)
print(valor3) # range(1, 10)

valor4 = range(-5,5,1)
print(valor4) # range(-5, 5)
print()

#########    in   #############################

print(2 in valor1) # o 2 esta na lista valor1? True
print(0 in valor2) # o 0 esta na lista valor2? False
print(10 in valor3) # o 10 esta na lista valor3? False
print(-2 in valor4) # o -2 esta na lista valor4? True
print()
oracao = "vamos para a aula?"
print("para" in oracao) # True
print('m' in oracao) # True
print('z' in oracao) # False
