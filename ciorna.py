from abc import ABC, abstractmethod


class cerc(ABC):
    @abstractmethod
    def raza(self):
        pass

    @abstractmethod
    def pi(self):
        raise NotImplementedError


def arie():
    arie = pi * (raza) ** 2
    return arie


class Cerc(cerc):
    __descriere = "Cel mai probabil am colturi"
    arie = 0

    def __init__(self, descriere):
        __descriere = descriere

    def raza(self):
        raza = 3
        return raza

    def pi(self):
        pi = 3.14
        return pi
    print({pi})
    @property
    def aria(self):
        return arie

    @aria.getter
    def raza(self):
        print(f"Aria este {arie}")
        return arie

    @aria.setter
    def aria(self, aria):
        try:
            if aria > 0:
                print('Aria este valida')

            else:
                raise NameError("Introduceti din nou raza")
        except:
            print("Cercul nu este definit corect")

    @raza.deleter
    def cerc(self):
        self.raza(cerc) == None

    # def adauga_nume(self,nume_vechi):
    #     nume_vechi.append(self.__numeProiectAlpha)
    #     print(nume_vechi)
    @cerc.setter
    def cerc(self, value):
        self._cerc = value



print(Cerc.cerc)
