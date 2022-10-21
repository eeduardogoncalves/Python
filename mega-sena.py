import random

possibilidades = list(range(1, 61))
loreria = []

for x in range(6):
    numero = random.choice(possibilidades)
    loreria.append(numero)
    possibilidades.remove(numero)
print(sorted(loreria))

