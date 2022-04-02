from abc import ABC, abstractmethod
#ABSTRACTION

class FormaGeometrica(ABC):
    PI = 3.14                               #am creat un field pi


    @abstractmethod
    def aria(self):                         #Contine o metoda abstracta aria
        raise NotImplementedError


                                            #Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
    def descrie(self):
        print("Cel mai probabil am colturi")


#INHERITANCE

class Patrat(FormaGeometrica):
    __latura = 0


    def __init__(self,latura):
        self.__latura=latura


    @property                           #am creat un property ca sa pot avea acces la getter, setter si deleter
    def latura(self):
        return self.__latura

    @latura.getter                      #am definit un getter
    def latura(self):
        return self.__latura

    @latura.setter                      #am definit un setter
    def latura(self, latura_noua):
        self.__latura = latura_noua

    @latura.deleter                     #am definit un deleter
    def latura(self):
        self.__latura = None


    def aria(self):
        return self.__latura**2


class Cerc(FormaGeometrica):
    __raza = 0


    def __init__(self, raza):
        self.__raza = raza


    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza_noua):
        self.__raza = raza_noua

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        return self.PI*self.__raza**2

    def descrie(self):
        return 'Eu nu am colturi'

cerc=Cerc(3)                                      #am definit un obiect cerc
print(cerc.PI)
cerc.aria()
print(cerc.aria())
print(cerc.descrie())
print(cerc.raza)
cerc.raza=6.2
print(cerc.raza)
del cerc.raza
print(cerc.raza)

patrat=Patrat(2)                            #am definit un obiect patrat
print(patrat.aria())
print(patrat.descrie())
print(patrat.latura)
patrat.latura = 4
print(patrat.latura)
del patrat.latura
print(patrat.latura)


