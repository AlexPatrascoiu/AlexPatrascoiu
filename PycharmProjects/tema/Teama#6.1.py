#1Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

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






#2 Calculeaza aria dreptunghiului

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
#



#3

# class Angajat:
#     nume= None
#     prenume= None
#     salariu=0
#
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

#4
#
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
#     def numar_factura(self,numar):
#
#        print(f'Numarul facturii este: {numar}')
#
#     def numeProdus(self,nume_produs):
#         print(f'Numele este: {nume_produs}')
#
#     def cantitate_produs(self,cantitate):
#
#         print(f'Cantitatea este: {cantitate}')
#
#     def pret(self,pret_buc):
#         print(f'Pretul este: {pret_buc} RON')
#
#     def serie(self,seria):
#         print(f'Seria este: {seria}')
#
#
# factura_obj=Factura(1,'Factura Gaz',2,420)                    #am creat un obiect la care am atribuit valori efective clasei "factura"
# factura_obj.numar_factura(2)
# factura_obj.numeProdus('Factura Curent')
# factura_obj.cantitate_produs(2)
# factura_obj.pret(430)
# factura_obj.serie('G12345')
#
# print('Data de astazi este: ', today)                             #am afisat data de astazi.


#5
#
# class Cont:
#     iban=0
#     titular_cont=None
#     sold=0
#
#     def __init__(self,iban,titular_cont,sold):
#         self.iban=iban
#         self.titular_cont=titular_cont
#         self.sold=sold
#
#
#     def cont_iban(self,iban):
#         print(f'mai are in contul {iban}')
#
#     def titular(self,titular_cont):
#         print(f'Titularul{titular_cont}')
#
#     def sold_cont(self,sold):
#         print(f'suma {sold} Lei')
#
# cont_bancar=Cont(3560124256789015, 'Popescu Marin', 4020)
# cont_bancar.titular('Mircea Florentin')
# cont_bancar.cont_iban(3560124256789015)
# cont_bancar.sold_cont(3760)

