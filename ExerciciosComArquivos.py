#ExerciciosComArquivos

# arq = open("A.txt")
# arq = read()
# arq = write("1,2")
# arq = close()

# while condition:
#     pass
#
# for condition:
#
# if condition:


# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256


###########################################################3

# with open("A.txt","w") as arq:
#     arq.write("200.135.80.9,192.168.1.1,8.35.67.74,257.32.4.5,85.345.1.2,1.2.3.4,9.8.234.5,192.168.0.256")
#
#
# with open("A.txt") as arq:
#     print(arq.read())



###################################################################

# with open("A.txt","w") as arq:
#     arq.write("200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256")
#
#
# with open("A.txt") as arq:
#     print(arq.read())

#######################################################################


# with open("A.txt","w") as arq:
#     arq.write("200.135.80.9,192.168.1.1,8.35.67.74,257.32.4.5,85.345.1.2,1.2.3.4,9.8.234.5,192.168.0.256")
#
#
# with open("A.txt") as arq:
#     ler = arq.read()
#     lista_ip = ler.split(",")
#     for ip in lista_ip:
#         q = open("B.txt","a")
#         q.write(ip+"\n")
#         q.close()
#
#     print(ler)

##############################################################

# with open("A.txt","w") as arq:
#         arq.write("200.135.80.9,192.168.1.1,8.35.67.74,257.32.4.5,85.345.1.2,1.2.3.4,9.8.234.5,192.168.0.256")
#
#
# with open("A.txt") as arq:
#         ler = arq.read()
#         lista_ip = ler.split(",")
#         for ip in lista_ip:
#             q = open("B.txt","a")
#             q.write(ip+'\n')
#             q.close()
#
#             l_ip = ip.split(".")
#             if int(l_ip[0])% 2 == 0:
#                 p = open("par.txt","a")
#                 p.write(ip + "\n")
#                 p.close()
#             else:
#                 p = open("impar.txt","a")
#                 p.write(ip + "\n")
#                 p.close()
#
#         print(ler)

#############################################################

#l l = [0,1,2,3,4,5]


# import random
# l = list(range(0,10))
# str_p = "file_"
# for _ in l:
#     num = random.choice(l)
#     r = open(f"{str_p}{num}","a")
#     r.write(f"{random.random()},\n")
#     r.close()
#
#     print(num)


######################################################################

# import glob
# str_p = "file_"
# #print(glob.glob("*"))
# print(glob.glob(f'{str_p}*'))

########################################################################

# import glob
# str_p = "file_"
# print(glob.glob("*"))
# print(glob.glob(f'{str_p}*'))
# l_arq = glob.glob(f'{str_p}*')
#
# for arq in l_arq:
#     print(arq)
#     q = open(arq)
#     print(q.read())
#     q.close()


##################################################################################3


# import random
# l = list(range(0,10))
# str_p = "file_"
# for _ in l:
#     num = random.choice(l)
#     r = open(f"{str_p}{num}","a")
#     r.write(f"{random.random()},\n")
#     r.close()
#
#     print(num)



############################################################


# import glob
# str_p = "file_"
# print(glob.glob("*"))
# print(glob.glob(f'{str_p}*'))
# l_arq = glob.glob(f'{str_p}*')
#
# for arq in l_arq:
#     print(arq)
#     q = open(arq)
#     ler = q.read()
# #    print(ler)
#     lista = ler.strip("\n")
#     lista = lista.split(",")
#     for l in lista:
#         l = l.strip("\n")
#         if l:
#             num = float(l)
#
#             print(num)
#     # print(lista)
#     q.close()

    #######################################################################


    #Achar maximo, minimo

# import glob
# str_p = "file_"
# print(glob.glob("*"))
# print(glob.glob(f'{str_p}*'))
# l_arq = glob.glob(f'{str_p}*')
#
# num_min = 2
# file_min = 2
# num_max = 0
# file_max = 0
#
# for arq in l_arq:
#     print(arq)
#     q = open(arq)
#     ler = q.read()
#     q.close()
# #    print(ler)
#     lista = ler.strip("\n")
#     lista = lista.split(",")
#     for l in lista:
#         l = l.strip("\n")
#         if l:
#             num = float(l)
#
#             print(num)
#             if num < num_min:
#                 num_min = num
#                 file_min = arq
#
# min = open("min.txt","w")
# min.write(f'{file_min}\t{num_min}')
# min.close()

##################################################################


import glob
str_p = "file_"
print(glob.glob("*"))
print(glob.glob(f'{str_p}*'))
l_arq = glob.glob(f'{str_p}*')

num_min = 2
file_min = 2
num_max = 0
file_max = 0

for arq in l_arq:
    print(arq)
    q = open(arq)
    ler = q.read()
    q.close()
#    print(ler)
    lista = ler.strip("\n")
    lista = lista.split(",")
    for l in lista:
        l = l.strip("\n")
        if l:
            num = float(l)

            print(num)
            if num < num_min:
                num_min = num
                file_min = arq
            if num > num_max:
                num_max = num
                file_max = arq


min = open("min.txt","w")
min.write(f'{file_min}\t{num_max}')
min = open("max.txt","w")
min.write(f'{file_max}\t{num_max}')
min.close()
