

###############################################################


# \t  tab
# \n new line

# ler = open("arquivo.dat")
# # esc = open("arquivo.dat", "w")
#
# print(ler.read())
# print("---")
#
# # ler.close()
#
# ler.seek(0)
#
# print(ler.read())
#
# ler.close()

#################################################################

# nome_arq = "arquivo.dat"
#
# arq_add = open("arquivo.dat", "a")
#
# arq_add.write("6\tet\t22\n")
# arq_add.close()
#
#
# ler = open(nome_arq)
# # esc = open("arquivo.dat", "w")
#
# print(ler.read())
# print("---")
#
#
#
# leitura = ler.read()
#
# print(leitura)
# print(leitura)
#
#
# ler.close()





######################################################################

# nome_arq = "arquivo.dat"
#
# arq_add = open("arquivo.dat", "a")
# id, nome, idade = (
#     input('id: '),
#     input('nome: '),
#     input('idade: ')
# )
#
#
# arq_add.write(f"{id}\t{nome}\t{idade}\n")
# arq_add.close()
#
#
# ler = open(nome_arq)
# # esc = open("arquivo.dat", "w")
#
# print(ler.read())
# print("---")
#
#
#
# leitura = ler.read()
#
# print(leitura)
# print(leitura)
#
#
# ler.close()

################################################################


# manipulando = open("arquivo.dat")
#
# leitura = manipulando.readlines()
#
# for linha in leitura:
#     print(linha, end='')
#
#
# manipulando.close()

# arq.write("1\tiury\t27\n")
# arq.write("2\tguilherme\t35\n")
# arq.write("3\tmarcos\t63\n")
# arq.write("4\tiury\t49\n")
# arq.write("5\tfernando\t71\n")
#
# arq.close()

####################################################################

# manipulando = open("arquivo.dat")
#
# leitura = manipulando.readlines()
#
# for linha in leitura:
#     linha = linha.split('\t')
#     print(linha)
#
#
# manipulando.close()


#########################################################################


# manipulando = open("arquivo.dat")
#
# leitura = manipulando.readlines()
#
#
# n = len(leitura)
# total_idade = 0
#
# for linha in leitura:
#     linha = linha.strip('\n')
#     linha = linha.split('\t')
#
#     id = int(linha[0])
#     nome = linha[1]
#     idade = int(linha[2])
#
#
#
#     total_idade = total_idade + idade
#
#     print(f"id: {id}; nome: {nome}; idade: {idade}")
#
# print(total_idade)
#
# media = total_idade/n
#
# print(f"soma das idades: {total_idade}")
# print(f"média das idades: {total_idade/n}")
# ssq = 0
#
# idademin = 10**3
# idademax = 0
# nomeidademin = ""
# nomeidademax = ""
#
# for linha in leitura:
#     linha = linha.strip('\n')
#     linha = linha.split('\t')
#
#     id = int(linha[0])
#     nome = linha[1]
#     idade = int(linha[2])
#
#
#     ssq = ssq + (idade - media)**2
#
#     if idademin > idade:
#         idademin = idade
#         nomeidademin = nome
#
#     if idademax < idade:
#         idademax = idade
#         nomeidademax = nome
#
# std = (ssq/(n-1))**0.5
#
# print(f"desvio padrão das idades: {std}")
#
# print(f"idade mínima: {idademin}")
# print(f"idade mínima: {idademax}")
#
# manipulando.close()


######################################################################33

manipulando = open("arquivo.dat")

leitura = manipulando.readlines()


n = len(leitura)
total_idade = 0

for linha in leitura:
    linha = linha.strip('\n')
    linha = linha.split('\t')

    id = int(linha[0])
    nome = linha[1]
    idade = int(linha[2])



    total_idade = total_idade + idade

    print(f"id: {id}; nome: {nome}; idade: {idade}")

print(total_idade)

media = total_idade/n

print(f"soma das idades: {total_idade}")
print(f"média das idades: {total_idade/n}")
ssq = 0

idademin = 10**3
idademax = 0
nomeidademin = ""
nomeidademax = ""

for linha in leitura:
    linha = linha.strip('\n')
    linha = linha.split('\t')

    id = int(linha[0])
    nome = linha[1]
    idade = int(linha[2])


    ssq = ssq + (idade - media)**2

    if idademin > idade:
        idademin = idade
        nomeidademin = nome

    if idademax < idade:
        idademax = idade
        nomeidademax = nome

std = (ssq/(n-1))**0.5

print(f"desvio padrão das idades: {std}")

print(f"idade mínima: {idademin}")
print(f"idade mínima: {idademax}")

manipulando.close()


######################################################################
