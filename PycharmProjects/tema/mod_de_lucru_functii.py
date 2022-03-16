def suma2nr(nr1, nr2):
    # logica de python
    # adunam cele 2 numere si le salvam intr-o variabila
    suma = nr1 + nr2
    # vreau sa returnez rezultatul, adica suma
    return suma

# write once! use n times!
def suma2nrv2(nr1, nr2):
    return nr1 + nr2
    # tot ce punem dupa return va expune functia

# apelam functii
rezultat = suma2nr(3, 4)
print(rezultat)

def numar_par(numer):
    if numer % 2 == 0:
        return True
    else:
        return False

print(f'Pt par:{numar_par(4)}' , f'Pt impar:{numar_par(3)}')

'''
To calculate the length of a string in Python, 
you can use the built-in len() method. 
It takes a string as a parameter and returns an integer as the length of that string. 
For example len("educative") will return 9 because there are 9 characters in "educative".
'''


# nr de caractere din nume
# ce nume sa ii dau la f? ce face ea?
# ce parametrii am nevoie si ce nume sa le dau? ce reprezinta fiecare?
def name_char_counter(name, surname, mid_name):
    # vreau sa aflu numarul total de char
    # aflu lungimea fiecarui string in parte
    # apoi adun aceste lungimi
    # expun cu return acest rezultat
    total = len(name) + len(surname) + len(mid_name)
    return total

name = 'Andy'
surname = 'S'
mid_name = ''

print(name_char_counter(name, surname, mid_name))
print(name_char_counter('Alexandru', 'Patrascoiu', 'Dorin'))

'''
Q: how to find the total number of elements in a list in python
A: The most straightforward way to get the number of elements in a list is to use the Python built-in function len() . 
As the name function suggests, len() returns the length of the list, regardless of the types of elements in it
'''

# vreau o f care sa primeasca o lista de numere ca si param
# vreau sa imi returneze media aritmetica a tuturor numerelor din lista
def media_aritm_rounded(lista_numere):
    # 1. cum se calculeaza media artimetica?
    # se aduna numerele si se impart la countul lor
    # 2. deci trebuie sa ajung la fiecare in parte
    # cum parcurg o lista de numere? si sa le iau rand pe rand
    # 3. cum le adun?
    # 4. cum aflu nr total de numere din lista
    # efectuez total imparti la count
    # 5. expun rezultatul cu return
    suma = 0
    for numar in lista_numere:  # am reusit sa iterez prin lista
        suma = suma + numar
    total_nr = len(lista_numere)
    media_aritm = suma / total_nr
    return round(media_aritm)



lista_mea = [3, 4, 3]
print(media_aritm_rounded(lista_mea))