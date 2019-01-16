# def test():
#     import doctest
#     doctest.testmod(verbose=True)
#
# def lista_2_ex_4(letra):
#     """
#     Faca um Programa que verifique se uma letra digitada é vogal ou consoante.
#     >>> lista_2_ex_4('a')
#     vogal
#     >>> lista_2_ex_4('b')
#     consoante
#     >>> lista_2_ex_4('5')
#     algarismo
#     """
#     if letra in ['a','e','i','o','u']:
#         print('vogal')
#     elif letra in ['0','1','3','4','5','6','7','8','9']:
#         print('algarismo')
#     else:
#         print('consoante')
#
#
#
#
# test()
# letra = input("Digite uma letra: ")
# print(lista_2_ex_4(letra))
# print(help(lista_2_ex_4))

####################################################################

#Exercício 5

# def test():
#     import doctest
#     doctest.testmod(verbose=True)
#
# def lista_2_ex_5(nota_a,nota_b):
#     """
#     Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.
#     >>> lista_2_ex_5(5.0,5.0)
#     Reprovado
#     5.0
#     >>> lista_2_ex_5(6.0,9.0)
#     Aprovado
#     7.5
#     >>> lista_2_ex_5(10.0,10.0)
#     Aprovado com Distinção
#     10.0
#     """
#     Média = (nota_a + nota_b)/2.0
#     if Média >= 7.0 and Média < 10:
#         print('Aprovado')
#     elif Média < 7.0:
#         print('Reprovado')
#     else:
#         print('Aprovado com Distinção')
#     print(Média)
# test()
# a, b = float(input('a: ')), float(input('b: '))
# while a < 0 or a > 10.0:
#     a = float(input('new a: '))
# while b < 0 or b > 10.0:
#     b = float(input('new b: '))
# print(lista_2_ex_5(a,b))


#######################################################################################

#Exercício 6

# def test():
#     import doctest
#     doctest.testmod(verbose=True)
# def lista_2_ex_6(a,b,c):
#     """
#     Faça um Programa que leia três números e mostre o maior deles.
#     >>> lista_2_ex_6(1,0,5)
#     5
#     >>> lista_2_ex_6(3,6,5)
#     6
#     >>> lista_2_ex_6(-11,0,3)
#     3
#     """
#     if a > b and a > c:
#         print(a)
#     if b > a and b > c:
#         print(b)
#     if c > a and c > b:
#         print(c)
#     # elif Média < 7.0:
#     #     print('Reprovado')
#     # else:
#     #     print('Aprovado com Distinção')
#     # print(Média)
#
#
# test()
# a, b, c = float(input('a: ')), float(input('b: ')), float(input('c: '))
# # while a < 0 or a > 10.0:
# #     a = float(input('new a: '))
# # while b < 0 or b > 10.0:
# #     b = float(input('new b: '))
# print(lista_2_ex_6(a,b,c))



########################################################

#Exercício 7

def test():
    import doctest
    doctest.testmod(verbose=True)


def lista_2_ex_7(a,b,c):
    """
    Faça um Programa que leia três números e mostre o maior e o menor deles.
    >>> lista_2_ex_7(1,0,5)
    5
    0
    >>> lista_2_ex_7(3,6,5)
    6
    >>> lista_2_ex_7(-11,0,3)
    3
    >>> lista_2_ex_7(2,1,6)
    1
    >>> lista_2_ex_7(8,9,-5)
    -5
    >>> lista_2_ex_7(23,7,4)
    4
    """

    if a > b and a > c:
        print(a)
    if b > a and b > c:
        print(b)
    if c > a and c > b:
        print(c)
    if a < b and a < c:
        print(a)
    if b < a and b < c:
        print(b)
    if c < a and c < b:
        print(c)



test()
a, b, c = float(input('a: ')), float(input('b: ')), float(input('c: '))
print(lista_2_ex_7(a,b,c))
