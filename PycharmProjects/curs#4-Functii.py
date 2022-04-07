'''
RECAP

'''

#
# lista = [1,2,3,4]
# lista.reverse()
# print(lista)


#3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
#Gasiti 2 variante sa le uniti intr-o singura lista.
#Afisati lista ordonata astfel [0,1,2,3,4,5,6]


# 4.Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista


# Folositi o functie care sa stearga lista de la ex3

# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren'
# Afisati 'mai aveti z schimbari'
#
# Testati codul cu diferite valori

# SCHIMBARI_MAXIME = 3
# schimbari_efectuate = 0
# schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
# echipa = {'j1','j2','j3','j4','j5'}
# jucator_in = 'j6'
# jucator_out = 'j1'
# if jucator_out in echipa and schimbari_efectuate <SCHIMBARI_MAXIME:
#     if jucator_in in echipa:
#         print("Nu putem face schimbarea deoarece jucatorul introdus este deja in teren")
#     else:
#         echipa.remove(jucator_out)
#         echipa.add(jucator_in)
#         schimbari_ramase -= 1
#         print(f"A intrat {jucator_in} si a iesit {jucator_out}. Mai aveti {schimbari_ramase} schimbari disponibile")
#         print(f"Actuala echipa este {echipa}")
# else:
#     if schimbari_ramase<=0:
#         print("Nu mai ai schimbari disponibile")
#     print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_in} nu este in teren")



# for i in range(999):
#     if i == 9 :
#         break
#     print(i)


print('---------------------------while--------------------------------')
i = 0
while i <= 3:
    print(f'valoarea curenta a contorului este {i}')
    i = i+1
    print(f'Valoarea contorului dupa incrementare este {i}')
else:
    print('Testul a luat sfarsit')                              #se va executa instructiunea 1 singura data dupa ce conditia de evaluare nu mai este indeplinita.

print('---------------------------for--------------------------------')

for i in range(1, 102):
    print(f'acesta este dalmatianul cu numarul {i}')                    #se printeaza de la 1 la 101 dalmatieni

for i in range(0, 101, 2):                                              #se printeaza in ordine crescatoare
    print(f'Urmatorul numar par este {i}')

for i in range(100, 0, -2):                                             #se printeaza in ordine descrescatoare V1
     print(f'Urmatorul numar par este {i}')

for i in reversed(range(0, 101, 2)):                                    #se printeaza in ordine descrescatoare V2
    print(f'Urmatorul numar par este {i}')

#
culori =['albastru','alb','verde','alb','rosu']
for culoare in culori :
    print(f'culoarea curenta este {culoare}')                             #se parcurge toata lista pe rand


for i in range(len(culori)):
    if culori[i] == 'alb':
        culori[i] = 'mov'
    print(f'lista curenta este {culori}')
print(f'lista finala este {culori}')

for culoare in culori :
    if culoare == 'mov':
        index = culori.index('mov')
        culori[index] = 'magenta'
        print(f'culoarea curenta este {culori[index]}')


print('---------------------------break--------------------------------')

for i in range(len(culori)):
    if culori[i] == 'magenta':
        culori[i] = 'purple'
        print(f'lista curenta este {culori}')
        break                                                # se opreste dupa ce gaseste prima culoare magenta din lista
print(f'lista finala este {culori}')


print('---------------------------continue--------------------------------')

for i in range(len(culori)):
    if culori[i] == 'magenta':
        culori[i] = 'purple'
        print(f'lista curenta este {culori}')
        continue
print(f'lista finala este {culori}')
note_premiante = []
note = [10,4,6,8,6]

for note in note:
    if note <=4:
        print(f'studentul curent a picat si a luat nota {note}')
        continue
    note_premiante.append(note)
print(f'lista note premiante este: {note_premiante}')


