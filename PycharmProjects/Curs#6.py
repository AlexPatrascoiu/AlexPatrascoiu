
#functii cu mai multi parametrii

# nume=input('Introduceti userul:')
# ocupatie=input('Introduceti functia:')
# ani=input('Introduceti varsta:')
#
# def say_hi(user, ani, ocupatie):
#     print(f'Hi {user},{ani},{ocupatie}')
#
# nume_input=['Alex', 'Roxy','Marian', 'Alexandra']
# for nume in nume_input:
#     say_hi(nume,ani,ocupatie)


#functie cu valori numerice

def calculeaza_impozit(valoare_salariu):

    if valoare_salariu < 4000:
        tax=0
    elif valoare_salariu >= 4000:
        tax=0.1
    elif valoare_salariu>=5000 and valoare_salariu<33500:
        tax=0.22
    else:
        tax=0.4
    salariu_impozat=valoare_salariu-valoare_salariu*tax
    impozit=valoare_salariu*tax
    return f'taxa aplicata a fost de {tax}, iar salariul dupa impozit este: {salariu_impozat}. impozitul este de {impozit}'

valoare_salariu=int(input('Introduceti salariul: '))
taxa=calculeaza_impozit(valoare_salariu)
print(calculeaza_impozit(valoare_salariu))