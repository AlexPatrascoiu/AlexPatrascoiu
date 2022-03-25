from tabulate import tabulate

# 1Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
#
#
# class cerc:                                       #am creat clasa cerc
#     raza = 0                                      #aici se vor defini atributele
#     aria=0
#     circumferinta=0
#     culoare= None
#
#     def __init__(self,raza,culoare):              #creez contstructor
#         self.raza = raza                          #creez atributele declarate mai sus
#         self.culoare = culoare
#
#
#
#     def arie_cerc(self,raza):                     #creez o functie unde se va calcula aria
#         aria = 3.14*(raza)**2
#         return aria
#
# clr=input('Introduceti culoarea:')
# cerc_obiect=cerc(3,clr)
# arie=cerc_obiect.arie_cerc(3)                     #apelez functie si ii dau valoarea 3 la raza.
# print(arie)                                       #afisez aria
# print(cerc_obiect.culoare)
# print(cerc_obiect.arie_cerc(5))





#
# 2 Calculeaza aria dreptunghiului
#
# class Dreptunghi:
#     lungime = 0
#     latime = 0
#     Culoare = None
#
#
#     def __init__(self,lungime,latime,culoare):                         #am creat un constructor cu toata atributele cerute in problema.
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#
#     def arie_dreptunghi(self,lungime,latime):                         #am creat o functie ce va calcula si afisa aria.
#         aria=lungime*latime
#         print(f'Aria este: {aria}')
#
#     def culoare_dreptunghi(self,Culoare):                             #am creat o functie pentru culoare, deoarece aceasta va fi afisata separat.
#             print(f'Culoarea este: {Culoare}')
#
#
# drepunghi_obj=Dreptunghi(12, 15, 'Alb')                                #am creat un obiect la care am atribuit niste valori efective,
# drepunghi_obj.arie_dreptunghi(12,5)
# drepunghi_obj.culoare_dreptunghi('Verde')




# 3
#
# class Angajat:
#     nume= None
#     prenume= None
#     salariu=0

#     def __init__(self,nume,prenume,salariu):
#         self.nume=nume
#         self.prenume=prenume
#         self.salariu=salariu
#
#     def nume_complet(self,nume,prenume):
#         nume_complet= nume + prenume
#         return nume_complet
#
#     def salariu_lunar(self,salariu):
#
#         print(f'Salariul lunar este:{salariu}')
#
#     def salariu_anual(self,salariu):
#         salariuanual=salariu*12
#         return salariuanual
#
# angajat_obj=Angajat('Alex', 'Dorin', 5000)
# angajat_obj.salariu_lunar(2000)
# venit=angajat_obj.salariu_anual(3000)
# print(angajat_obj.nume,angajat_obj.prenume,angajat_obj.salariu)
# print(venit)
# angajat_obj.salariu=1000
# print(angajat_obj.salariu)
# angajat_obj.prenume='Alin'
# print(angajat_obj.prenume)

4

# from datetime import date                                             #am importat functia date
# today = date.today()                                                  # se va afisa data de astazi.
#
# class Factura:                                                        #am creat clasa "factura"
#     numar=0
#     nume_produs=None                                                  #am definit niste atribute
#     cantitate=0
#     pret_buc=0
#     seria='G12345'
#
#     def __init__(self,numar,nume_produs,cantitate,pret_buc):          #am definit un constructor cu toate atributele mai putina seria.
#         self.numar=numar
#         self.nume_produs=nume_produs
#         self.cantitate=cantitate
#         self.pret_buc=pret_buc
#
#
#     def schimba_cantitatea(self,cantitate):
#         self.cantitate=cantitate
#         return self.cantitate
#
#     def schimba_pretul(self, pret):
#         self.pret_buc=pret
#         return self.pret_buc
#
#     def schimba_nume_produs(self, nume):
#         self.nume_produs=nume
#         return self.nume_produs
#
#     def genereaza_factura(self):
#         total=self.pret_buc*self.cantitate
#         print(f'Am generat factura la: {self.nume_produs} in cantitate de {self.cantitate} la un pret unitar de {self.pret_buc} avand un total de {total}')
#
#
#
#
#
# factura_obj=Factura(1,'Factura Gaz',6,300)                    #am creat un obiect la care am atribuit valori efective clasei "factura"
# factura_obj.schimba_pretul(460)
# cantitate_finala=factura_obj.schimba_cantitatea(2)
# factura_obj.genereaza_factura()
# print(cantitate_finala)
# print(factura_obj.cantitate)
# print('Data de astazi este: ', today)                             #am afisat data de astazi.


# 5

class Cont:
    iban=0
    titular_cont=None
    sold=0

    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold


    def cont_iban(self,iban):
        print(f'mai are in contul {iban}')

    def titular(self,titular_cont):
        print(f'Titularul {titular_cont}')

    def sold_cont(self,sold):
        print(f'suma {sold} Lei')

    def debitare_cont(self,suma_debitare):
        self.sold=self.sold-suma_debitare
        return self.sold

    def creditare_cont(self,suma_creditata):
        self.sold=self.sold+suma_creditata
        return self.sold

cont_bancar=Cont(3560124256789015, 'Popescu Marin', 4020)
# print(cont_bancar.debitare_cont(32))
# print(cont_bancar.creditare_cont(18))
print(f'Titularul {cont_bancar.titular_cont} are in contul {cont_bancar.iban} suma de {cont_bancar.sold} Lei')
