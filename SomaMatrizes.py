M = [[float(input("numero: ")) for i in range(2)] for j in range(2)]
B = [[float(input("numero: ")) for i in range(2)] for j in range(2)]



R = [[0 for i in range(2)] for j in range(2)]

for i in range(2):
    for j in range(2):
        R[i][j] = M[i][j] + B[i][j]

print(R)


##########################################################


R = [[[x + y for x,y in zip(m,b)] for m in M] for b in B]

print(R)


