import random

def gerar_centena():
    return random.randint(100, 999)

def gerar_milhar():
    return random.randint(1000, 9999)

def gerar_grupo():
    return random.randint(1, 25)

def gerar_terno_de_grupo():
    return random.sample(range(1, 26), 3)

def gerar_duque_de_grupo():
    return random.sample(range(1, 26), 2)

def gerar_duque_de_dezenas():
    return random.sample(range(10, 100), 2)

def gerar_terno_de_dezenas():
    return random.sample(range(10, 100), 3)

centena = gerar_centena()
milhar = gerar_milhar()
grupo = gerar_grupo()
terno_de_grupo = gerar_terno_de_grupo()
duque_de_grupo = gerar_duque_de_grupo()
duque_de_dezenas = gerar_duque_de_dezenas()
terno_de_dezenas = gerar_terno_de_dezenas()

print("GERADOR JOGO DO BICHO")
print()
print("Centena:", centena)
print("Milhar:", milhar)
print("Grupo:", grupo)
print("Terno de Grupo:", terno_de_grupo)
print("Duque de Grupo:", duque_de_grupo)
print("Duque de Dezenas:", duque_de_dezenas)
print("Terno de Dezenas:", terno_de_dezenas)
