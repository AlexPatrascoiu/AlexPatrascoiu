#operator de asignare
# x = 3 #asignare = stocarea unei valori la o anumita adresa de memorie
# print(x)
# x = x + 3 #creste valoarea lui x cu 3
# print(x)
# x += 3 #face acelasi lucru cu x=x+3
# print(x)
# x = x - 3
# print(x)
# x -= 3
# print(x)
#
# x = x * 3
# print(x)
# x *= 3
# print(x)
# x = x / 3
# print(x)
# x /= 3
# print(x)
# print('--------------------------------------------------------------------------------------')
#
# #operatori aritmetici
# print(10%3)  #restul impartirii
# print(2**3)  #ridicare la putere
# print(x**(1/2)) #radical din x
#
# #operatori de comparare
#
# x = 5
# y = 3
# print(x==y)  #operator de comparatie ,  daca x = y; afiseaza true/false
# x = y
# print(x==y)
# print(x!=y) #verifica daca valorile sunt diferite
# print(x<y)
# print(x<=y)
# print(x>y)
# print(x>=y)
#
# #operatori logici
#
# '''
# operatorii logici sunt AND , OR , NOT
# intotdeauna operatorul AND are prioritate in fata operatorului OR
# '''
#
print(x<2 and x<y)  #ambele conditii trebuie sa fie true pentru a avea rezultatul true.
print(x>2 and x<y)
print(x>2 and x<y or y>2)
print(x>2 and (x<y or y>2))
print('-------------------------------------------------------------------------------')
pasaport = input('Are pasaportul valid : DA/NU ')
ambii_parinti = input('Are ambii parinti? DA/NU ')
permisiune = input('Are permisiune? DA/NU/NA ' )

if pasaport == 'DA' and (ambii_parinti == 'DA' or permisiune == 'DA') :
    print('Permite calatoria')
else :
    print('Nu permite calatoria')

NOTA_DE_TRECERE = 5 #o constanta se scrie litere mari si se doreste sa nu se schimbe.
NOTA_DE_TRECERE_PURTARE = 7
nota_examen = int(input('Introdu nota la examen '))
nota_purtare = int(input('Introdu nota la purtare '))
if nota_examen >= NOTA_DE_TRECERE and nota_purtare >= NOTA_DE_TRECERE_PURTARE :
    print('Bravo ai trecut!')
    if nota_examen == 10 and nota_purtare == 10 : #acest if se executa doar daca este adevarata conditia de la primul if
        print('Felicitari esti premiat!')
else :
    print('Nu ai trecut clasa! :(')



