#Classe  wiki python  lista de exerc'icios
class Bola:  # é só um esquema

    def __init__(self,cor,raio):
        self.cor = cor
        self.raio = raio

    def mostrar_cor(self):
        print(self.cor)

    def mostrar_raio(self):
        print(self.raio)


###############################################

bola  = Bola('verde',10)
print(bola.cor)
print(bola.raio)
tenis = Bola('azul',3)
print(tenis.cor)
print(tenis.raio)


bola.mostrar_cor()
tenis.mostrar_cor()
bola.mostrar_raio()
tenis.mostrar_raio()

tenis.material = 'polimero'
bola.material = 'palha'
print(tenis.material)
print(bola.material)

class BolaGolf(Bola):
    material = 'palha'

golf = BolaGolf('branco',1)
print(golf.material)
golf.mostrar_cor()
golf.mostrar_raio()


class BolaSquah(Bola):
    def __init__(self,cor,raio,material):
        Bola.__init__(self,cor,raio)
        self.material = material

    def exibir_material(self):
        print(self.material)

squash = BolaSquah('verde',17,'lona')
squash.exibir_material()
squash.mostrar_cor()
squash.mostrar_raio()

#################################################################33

class Bola:
    def __init__ (self,cor):
        self.cor = cor
    def trocar_cor(self,outra_cor):
        self.cor = outra_cor

bol = Bola('verde')
bol.trocar_cor('vermelho')
print(bol.cor)

###############################################333

class Quadrado:
    def __init__ (self,lado):
        self.lado = lado
    def mudar_lado(self,outro_lado):
        self.lado = outro_lado
    def calcular_area(self):
        area = self.lado**2
        print(area)

quad = Quadrado(19)
print(quad.lado)
quad.mudar_lado(1729)
print(quad.lado)
quad.calcular_area()

##########################################################3

# Classe Retangulo: Crie uma classe que modele um retangulo:
#
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.


class Retangulo:
    def __init__ (self,base,altura):
        self.base = base
        self.altura = altura
    def alterar_base_altura(self,outra_base,outra_altura):
        self.base = outra_base
        self.altura = outra_altura
    def calcular_area(self):
        area = self.base*self.altura
        return(area)

retan = Retangulo(16,23)
print(retan.base)
print(retan.altura)
retan.alterar_base_altura(14.8,21)
#retan.alterar_altura(21)
print(retan.base)
print(retan.altura)
retan.calcular_area()
print(retan.calcular_area())
