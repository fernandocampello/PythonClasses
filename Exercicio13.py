import math



PI = math.pi

h = float(input("h: "))


PesoHomem = (72.7*h) - 58

PesoMulher = (62.1*h) - 44.7

'''print(f"Peso do Homem:{PesoHomem} Peso da Mulher:{PesoMulher}")'''

print("Peso do Homem",PesoHomem)
print("Peso da Mulher",PesoMulher)


print("Peso do Homem: %0.2f" %PesoHomem)
print("Peso da Mulher %0.2f" %PesoMulher)


print("Peso do Homem: %9.2f" %PesoHomem)
print("Peso da Mulher %9.2f" %PesoMulher)


print("Peso do Homem: %0.4f" %PesoHomem)
print("Peso da Mulher %0.4f" %PesoMulher)

print("Peso do Homem: %12.4f" %PesoHomem)
print("Peso da Mulher %12.4f" %PesoMulher)
