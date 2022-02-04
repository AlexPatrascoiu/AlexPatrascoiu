#1

# o variabila este o cutiuta in care tinem lucruri de valoare sau valori.
# este un spatiu de memorie alocat calculatorului in care se atribuie o anumita constanta.(valoare)


#2 declar si initializez o variabila din fiecare tip.

#string

# Nume = 'Alex'
#
# #int
#
# Ora = 10
#
# #float
#
# pi = 3.1415

# #boolean
# True = Student
# False = QA_engineer

#3 am afisat si verificat tipul de variabila
# print(Nume)
# print(type(Nume))
# print(Ora)
# print(type(Ora))
# print(pi)
# print(type(pi))

#4 am rotunjit un numar

# print(round(pi))

#5 Printez 4 propozitii NU STIU A 4 A VARIANTA
# a = "Am fost acolo si mi-a placut"
# b = 2022
# c = 4.5
# student = True
# print(a)
# print(f'suntem in anul', b)
# print(f'bere cu' , c , '%' , ' alcool')
# print(f'sunt student? {student}')

#6 Citeste de la tastatura numele

# Nume = input('Introduceti numele: ')
# Prenume = input('Introduceti prenumele: ')
#
# print(len(Nume + Prenume))
#
# #7 Aria drepunghiului
#
# x = int(input('latura mica este: '))
# y = int(input('latura mare este: '))
#
# print('aria este: ' ,x*y)

#8 Afiseaza stringul fara ultimele caractere

my_string = 'Coral is either the stupidest animal or the smartest rock'
# x=int(input('introduceti un numar: '))
# #x=int(x) - se poate si asa fara int inainte de input
# print(my_String[:-x])

#9 creaza un string nou folosing primele 5 + ultimele 5 caractere

# string1 = my_String[:5]        #am selectat doar primul cuvant
# string2 = my_String[53:]       #am selectat ultimul cuvant
# print(string1 , string2)       #afisez ambele cuvinte intr-un singur print

#10 Afisati de cate ori apare cuvantul "the"

# index = my_String.count('the')
# print(index)


#11 inlocuieste 'the' cu 'THE' peste tot

# print(my_String.replace('the','THE'))

#12 afiseaza indexul de start al cuvantului rock, folosing asta + slicing afiseaza tot stringul pana la capat.

# index_start=my_String.index('rock') #am definit string-ul de la care se ia primul index
#
# print(len(my_String))
# print(index_start)
# print(my_String[0:53])
#
#
# #13  verifica daca primul si ultimul caracter sunt la fel (assert) + case sensitive.
# my_string = str(input('Introduceti o propozitie')) #am creat o valoare ce se introduce de la tastatura si este fortata sa devina string
#
# assert my_string[0].lower() == my_string[len(my_string)-1].lower() #am creat un assert intre primul index din variabila mea fortata sa fie cu litere mici si l-am comparat cu ultimu index
#
# print('Corect')  #am afisat

#14 afiseaza doar numerele pare; afisaza numerele impare (slicing + pas)

# string = '0123456789' #am definit un string cu cifre

# par = string[::2]   #am delimitat doar cifrele pare prin slicing
# impar = string[1::2]   #am delimitat doar cifrele impare prin slicing

# print('Numere pare: ',par)
# print('Numere impare: ',impar)


#15 folosind assert se verifica daca stringul contine doar numere.



# print(string.isdigit())        #functie ce verifica stringul sa fie doar numere
#
#
# assert string.isdigit() == True
#
#
# print('Contine doar numere')
#



#16 citeste de la tastatura un string de dimensiune impara; afiseaza caracterul din mijloc


# k = input('introdu un cuvant: ')  #am definit un input de string
# m = k[len(k)//2]                   # am definit o formula ce inseamna jumatatea oricarui string
# print(m)                            #am afisat jumatatea stringului


#17Folosind assert, verificati daca un string este palindrom

#
# z = input('Introduceti un cuvant: ')  #am definit variabila
#
# palindrom = z[::-1]                   #am definit palindromul prin metoda slice
#
# assert z == palindrom                 #am declarat assert-ului ca palindromul definit mai sus este identic cu ce se introduce la tastatura
#
# print('cuvantul intrdodus este palindrom')     #am verificat si afisat ca este palindrom




#18folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')si salveaza fiecare cuvant intr-o variabila

# a,b = input('Scrie 2 cuvinte:').split()
# print(f'{a}, {b}')

#19citeste un string de la tastatura (eg: alabala portocala) salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)

#create user input
# string = input("Scrie ceva: ")
# #find out the length of the variable 'string'
# print(len(string))
# #find first character from the string
# first = string[0]
# print(string[0])
# #find last character from the string
# last = string[-1]
# #string between index 0 and -1
# mid_temp = string[1:-1]
# #capitalize first_character in the whole string position 1
# middle = mid_temp.replace(first, first.upper())
# #capitalize 1st character in the string apart from index 0 and -1
# final = first + middle + last
# print(final)


# #20 citeste user si parola de la tastatura

# user = input('introduceti User Name: ') #se introduce de la tastatura un username
# parola = input('introduceti parola: ')   #se introduce de la tastatura o parola
# parola_ascunsa = '*' * len(parola)     #ascund parola cu symbolul *


# print(parola_ascunsa , len(parola) , 'caractere') #printez parola introdusa si lungimea sa