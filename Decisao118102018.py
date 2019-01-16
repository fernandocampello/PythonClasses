# def list_2_ex_1():
#     """
#     Faça um Programa que peça dois números e imprima o maior deles.
#     """
#     a = input()
#     b = input()
#     #if int(a) < int(b):
#     if float(a) < float(b):
#         print(b)
#     else:
#         print(a)
# list_2_ex_1()


# def list_2_ex_2():
#     """
#     Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#     """
#     a = input()
#     if int(a) > 0:
#         print("Positivo")
#     else:
#         print("Negativo")
# list_2_ex_2()


# def test():
#     import doctest
#     doctest.testmod(verbose=True)
#
# def list_2_ex_2(a):
#     """
#     Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#     >>> list_2_ex_2(1)
#     Positivo
#     >>> list_2_ex_2(-2.5)
#     Negativo
#     >>> list_2_ex_2(0)
#     Nulo
#     """
#
#     if float(a) > 0:
#         print("Positivo")
#     elif float(a) <0:
#         print("Negativo")
#     if float(a) == 0:
#         print("Nulo")
#
# test()
#
# val = input("Digite um valor:")
# list_2_ex_2(val)

######################################################

# coding: utf-8

def test():
    import doctest
    doctest.testmod(verbose=True)




def list_2_ex_3(Sexo):
    u"""
    Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
    F - Feminino, M - Masculino, Sexo Inválido.
    >>> list_2_ex_3('F')
    Feminino
    >>> list_2_ex_3('M')
    Masculino
    >>> list_2_ex_3('G')
    Sexo Inválido
    """
    if not (Sexo in ['F','f','m','M']):
        print("Sexo Inválido")
    elif Sexo in ['F','f']:
        print("Feminino")
    else:
        print("Masculino")

test()

F = input("Digite o seu sexo:")
print(list_2_ex_3('F'))
print(help(list_2_ex_3))
