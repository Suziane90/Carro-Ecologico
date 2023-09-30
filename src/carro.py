class Carro:

    def __init__(self, passageiros=0, combustivel=0, quilometragem=0):
        self.passageiros = passageiros  # so suporta duas pessoas
        self.combustivel = combustivel  # so suporta 100 litros
        self.quilometragem = quilometragem

    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.combustivel

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self): #Como o carro estava vazio, deve ser possivel embarcar  ////   Como o carro estava cheio (2 passageiros), nao deve ser possivel embarcar
        if self.passageiros == 0 or self.passageiros < 2:
            self.passageiros += 1
            return True
        else:
            return False

    def desembarcar(self):  #Como o carro nao estava vazio, deve ser possivel desembarcar
        if self. passageiros == 0:
            return False
        else:
            return True

    def dirigir(self, distancia): # 1 quilometro por litro  /// O carro tinha 32 litros e percorreu uma distancia de 10 km
       return None

    def abastecer(self, quantidade): # O valor de combustivel desejado excede o tamanho do tanque. Logo o tanque fica cheio
        if quantidade > self.combustivel:
            self.combustivel = 100
            return True
        else:
            return False