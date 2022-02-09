# user_role = input('inser the user role.it can be admin, guest, editor,')
#
# if not(user_role=='admin') :
#     print('Role is not admin. Sorry, you cannot edit the file')
#

#liste

# list1 = ["abc", 34 , True, 'male', float]
#
# print(list1)
# print(list1[0])
# print(len(list1))

#dict

# thisdict = {
#     'brand': "volvo"
#     'model': "c60"
#     'year' : 2011}
#
# print(thisdict)
# print(thidict['brand'])
# print(len(thisdict))
#
# #set
#
# culori = {'alb', 'rosu', 'galben'}
# print(culori)
# print(len(culori))
#
# #tuple
# thistuple = ('mere', 'banane', 'cirese')
# print(thistuple)
print('------------------------------------------------------------------')

#liste

nume = 'Mihai'
len(nume)
nume_list = ['M','i','h','a','i'] #am definit o lista cu 5 elemente
print(nume_list[0])     #am accesat primul element din lista; am afisat pe ecran.
print(len(nume_list))
print(nume_list[0:2])   #se poate aplica slice pe liste? DA;

                      #limita superioara a intervalului nu se ia in considerare.
# print(nume_list)
# remove = nume_list.remove('a')   #vrem sa scoatem litera a din lista.
# print(nume_list)

# pop = nume_list.pop()         #scoate ultima valoare din lista
# print(nume_list)
# print(remove)
# print(pop)
'''
diferenta intre pop si remove:

-remove sterge 1 singur caracter intre (),pop sterge 1 singur caracter in functie de index.
-remove nu returneaza nimic;    pop returneaza o valoare.
'''

#cum sa suprascriem valoarea de la o anumita pozitie

# nume_list[1] = 'o'
# print(nume_list)

#cum adaugam un element intr-o anumita pozitie.

# nume_list.insert(2,'R')
# print(nume_list)
# nume_list.append('T')
# print(nume_list)
#
# lista_in_lista = [
#     [1,2,3] , [4,5,6] , ['a','b','c']
# ]
#
# print(lista_in_lista[0][1],lista_in_lista[2][2],lista_in_lista[2][1])

#set

vocale = {'A','E','I','O','U'}
# print(type(nume_list))
# print(type(vocale))
# #print(vocale[0])              #am accesat elementul din pozitia 0.
# vocale.add('a')

#
# litera = input('va rog introduceti o litera: ').upper()
# if litera in vocale :
#     print('litera este o vocala')

#tuplu; este imutabil (ce este definit nu se mai poate schimba), permite valori si este ordonata.

camere_hotel = (1,2,3,4,5,5)
print(camere_hotel[0])
print(camere_hotel.count(5))    #functia count afiseaza de cate ori apare elementu din tuplu
print(camere_hotel.index(3))    #functia index returneaza pozitia elementului din tuplu
print(len(camere_hotel))        #afiseaza numarul de elemente din tuplu.

#dictionar este o structura care stocheaza informatii in formatul cheie:valoare.

capitale = {
    'Romania':'Bucuresti' ,
    'Italia':'Roma' ,
    'Ukraina':'Kiev'

}
print(capitale['Romania'])       #accesarea informatiilor din dictionar in functie de cheie
print(capitale.get('Romania'))   #idem

#cum sa actualizam o informatie.

capitale['Romania'] = 'Cluj'    #inlocuim o valoare din dictionar pe baza de cheie
print(capitale['Romania'])

#adaugam o informatie noua

capitale['Rusia'] = 'Moscova'
print(capitale['Rusia'])
print(len(capitale))

#cum putem sterge o informatie existenta.

def calculeazasuma(a, b):
    sum = a + b
    return sum


capitale.pop('Rusia')
print(capitale)
print(calculeazasuma(5, 6))



