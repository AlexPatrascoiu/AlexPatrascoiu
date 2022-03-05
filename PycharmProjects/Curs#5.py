#for este un tip de iteratie care se foloseste pentru a trece secvential prin lista sia identifica elementele pe baza de index

#for each este un tip de iteratie care se foloseste pentru a trece secvential prin lista si a identifica elementele pe baza de continut

# for each este util atunci cand vrem sa parcurgem toata lista si sa afisam ceva din ea.
print('-------------------for--------------------')

for i in range(len(masini)):
    print(f'masina mea preferata este {masini[i]}')

'''
modalitatea de executie a instructiunii de mai sus:

len(masini)=8
i = 0 -> 0 < 8? DA ->  masina mea preferata este masini[0] (Audi)
'''





print('---------------for each----------------')







for masina in masini:
    print(f'masina mea preferata este: {masina}')





print('--------------------WHILE---------------------')






index_masina = 0
while index_masina<len(masini):
    print(f'masina mea preferata este {masini[index_masina]}')
    index_masina+=1


print('------------------for else--------------')


for masina in masini:
    if masina=='Mercedes':
        print(f'Am gasit masina dorita de dvs, {masina}')
        break
    else:
        print(f'Am gasit masina {masina}, mai cautam')


for masina in masini:
    if masina=='Trabant' or masina== 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')





