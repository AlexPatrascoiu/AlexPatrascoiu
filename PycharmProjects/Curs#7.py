from abc import ABC, abstractmethod

class Angajat(ABC):
    @abstractmethod
    def pontaj(self):
        raise NotImplementedError

    @abstractmethod
    def testAlcool(self):
        raise NotImplementedError

class AngajatSRI(Angajat):
    __numeProiectAlpha = 'Cod Secret Vulturul'

    def pontaj(self):
        frecventaPontareLuna = 1
        return frecventaPontareLuna

    def testAlcool(self):
        frecventaTestAlcool = 8
        return frecventaTestAlcool

    def ascultaTelefoane(self):
        tipTepefoane = 'Smartphone'
        return tipTepefoane

    @property
    def numeProiectAlpha(self):
        return self.__numeProiectAlpha

    @numeProiectAlpha.getter
    def numeProiectAlpha(self):
        print(f'Numele proiectului este: {self.__numeProiectAlpha}')
        return self.__numeProiectAlpha


    @numeProiectAlpha.setter
    def numeProiectAlpha(self, nume_nou):
        if(nume_nou not in ('asculta', 'citeste','Colecteaza')):
            self.__numeProiectAlpha = nume_nou
        else:
            print('numele nu este sigur')
            raise NameError('Numele nu este sigur')

    @numeProiectAlpha.deleter
    def numeProiectAlpha(self):
        self.__numeProiectAlpha = None



angajatSRI1 = AngajatSRI()
angajatSRI1.pontaj()
print(angajatSRI1.ascultaTelefoane())



# def addnr1(x,y,*args):
#     print(x,y,*args)
#     return sum(args)
#
# suma = addnr1(1,2,3,4)
# print(suma)


# super class
class Student:
    # protected data members
    _name = None

    # constructor
    def __init__(self, name):
        self._name = name


# derived class
class  ChildStudent(Student):
    _classAttribute = "test"
    # constructor
    def __init__(self, name):
        Student.__init__(self, name)

    # public member function
    def displayDetails(self):
        # accessing protected data members of parent class
        print("Name: ", self._name)