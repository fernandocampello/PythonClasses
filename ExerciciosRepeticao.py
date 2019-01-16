"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""


# for i in range(3):
#     nota = input("Digite uma nota: ")
#     print(nota)
#
#     nota = float(nota)
#
#     if nota >= 0 and nota <= 10:
#         continue
#     else:
#         break



# for i in range(3):
#     nota = input("Digite uma nota: ")
#
#     nota = float(nota)
#
#     if nota >= 0 and nota <= 10:
#         print(f"{i} nota:  {nota}")
#         break
#     else:
#         print(f"{i} nota errada: {nota}")
#         continue
#
# print('Fim do script')

##############################################################################

# for i in range(1,4,1):
#     nota = input("Digite uma nota: ")
#
#     nota = float(nota)
#
#     if nota >= 0 and nota <= 10:
#         print(f"{i} nota:  {nota}")
#         break
#     else:
#         print(f"{i} nota errada: {nota}")
#
#     print('Fim do loop - for')
#     continue
#
#
# print('Fim do script')

#########################################################################

# nota = -1
#
# while not (nota >= 0 and nota <= 10):
#     nota = input("Digite uma nota: ")
#     nota = float(nota)
# else:
#     print(f'nota: {nota}')
#
# print('Fim do script - while')

############################################################################3

"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50"""

######################################################

# n = 19
#
# for i in range(1,11,1):
#     print(f'{n} x {i} = {n*i}')
#
# print(f'Tabuada de {n}')



#########################################################

# n = 19
#
# i = 0
#
# while i <10:
#     i = i + 1
#     print(f'{n} x {i} = {n*i}')
#
# print(f'Tabuada de {n}')


######################################################################

"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""

################################################################

# n_par = 0
# n_impar = 0
#
# for i in range(1,11):
#     number = input('Digite um número: ')
#     number = int(number)
#     if(number % 2 == 0):
#         print('Número par')
#         n_par = n_par + 1
#     else:
#         print('Número ímpar')
#         n_impar = n_impar + 1
#
# print(f'impar: {n_impar}')
# print(f'impar: {n_impar}')

################################################################################3

"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo."""

##################################################################


# F0 = 0
# F1 = 1
# F2 = F1 + F0
# print(F0)
# print(F1)
# print(F2)
#
# F3 = F2 + F1
# F4 = F3 + F2
#
#
#
#
# n = input('Digite um número inteiro não negativo: ')
# n = int(n)
#
# for i in range(1,n):
#     F3 = F2 + F1
#     print(F3/F2)
#     F1 = F2
#     F2 = F3
#
#     print(F3)


    ##########################################################

N = int(input('Digite o número de termos da série de Fibonacci: '))

fib = [0,1,1]

for i in range(3,N):
#    fib.append(fib[i-1] + fib[i-2])
    fib += [fib[i-1] + fib[i-2]]

    print(fib[i]/fib[i-1])

for seq in fib:
    print(seq)
