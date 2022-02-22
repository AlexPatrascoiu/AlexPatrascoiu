# # 1. Declare a new variable that will store the text "Welcome to programming"
#
# var = 'Welcome to programming'
# print(var)
# print(type(var))
#
# #2  Extract the first three characters of the text using string slicing and print it (should display Wel)
#
# print(var[0:3])
#
# #3 Print on the screen the text in reverse
#
# print(var[::-1])
#
# #4 Print on the screen the text by skipping every other character
#
# print(var[::2])
#
# #5 Print on the screen how many times the letter e and o appear on the screen:"The letter e appears 2 times and the letter o also appears 3 times". Use the formatting option
#
# letter_e = var.count('e')
# letter_o = var.count('o')
#
# print(f'e apare de {letter_e} ori , o apare de {letter_o} ori ')
#
# #6  Print the sentence on the screen in capitals
#
# print(var.upper())
#
# #7 Inside the string replace the letter m with the letter p
#
# print(var.replace('m','p'))
#
# #9 Inside the string replace the word "Welcome" with the word "Bienvenue"
#
# print(var.replace('Welcome' , 'Bienvenue'))
#
# #10 Print on the screen the last letter in the text
#
# print(var[21:22:])
#
# #11  Define a new variable and initialise it with the value of 0
#
# new_var = 0
# print(new_var)
#
#
# #12 Using assignment operations apply the sum, difference, multiplication and division between the variable that you declared and the number 7
#
# x = int(input('introduceti un numar: '))
# y = 7
#
# print(f'suma este: ', x + y)
# print(f'diferenta este: ', x - y)
# print(f'produsul este: ', x*y)
# print(f'impartirea este: ', x/y)
#
# #13 Using the arithmetical operations perform the operations of modulo and power between the variable that you declared and the number 2
#
# print(f'diferenta impartirii este:', x%2)
# print(f'ridicarea la putere este: ', x**2)
#
# #14 Using the comparison operations check the value of the variable that you defined against the number 5
#
# print(f'valoarea introdusa este mai mare: ', x > 5)
# print(f'valoarea introdusa este mai mica:', x < 5)
# print(f'valoarea introdusa este egala:', x == 5)
#
# #15 Using the variable that you defined perform complex comparison operations using the logical operators and/or/not
#
# print(x<y and x<5)
# print(x>y or x>5)
# print(x == y and x>5 or x<5)

# '''16 Write a program that will do the following:
# - Define a new variable called waking hour
# - Will evaluate the value of the variable against the number 7
# - If the hours is seven, then it will print on the screen: "Wring wring, it's time to wake up"
# - Otherwise it will print on the screen: "Lay down your head and I'll sing you a lullaby
# '''
#
# waking_hour = int(input('introduceti ora de trezire: '))
#
# if waking_hour == 7 :
#     print("Wring wring, it's time to wake up")
# elif waking_hour <7 :
#     print('\n Lay down your head and I\'ll sing you a lullaby'
#           '\n Back to the years of loo-li lai-lay'
#           '\n And I\'ll sing you to sleep and I\'ll sing you tomorrow'
#           '\n Bless you with love for the road that you go')
# else:
#     print('you\'re late for work')

#17  Create a list containing 10 elements

# lista = ['mere','mici','bere','dulciuri','baterie','apa plata','sac','cafea','lapte','paine']


#18 Print all the elements of the list on the screen

# print(lista)

#19 Count the number of items stored in the list

# print(len(lista))
#
# #20  Reverse the list
#
# print(lista[::-1])

#21 Add an element to the list

# lista.append('Suc')
# print(lista)

#22  Define a second list and attach its elements to the first one
#
# lista_noua = ['cumparaturi','picnic','mic dejun']
# lista.extend(lista_noua)
# print(lista)

#23 Define two sets containing a set of unique elements an calculate the common elements between them and then the difference between them
#
# set_1 = {'40','Wifi','RAM','motorina','percutie'}
# set_2 = {'33','rochie','ochelari','motorina','retea','Wifi','autonomie'}
#
# set_common = set_1.intersection(set_2)
# set_exclude = set_1.difference(set_2)
# print(set_common)
# print(set_exclude)



#24 Check if one set is a subset or superset of another set. If found, delete all elements from that set
#
# if set_2.issubset(set_1) :
#     print('Elementele din al 2 lea set se regasesc si in primul')
# else :
#     print('elementele din al 2lea set nu se regasesc in primul set')



#25 Print the value of key 'history' from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# print(sampleDict['class']['student']['marks']['history'])

#26 Delete a list of keys from a dictionary Given:  Keys to remove  = ["name", "salary"]

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# sample_dict.pop('name')
# sample_dict.pop('salary')
# print(sample_dict)

#27  Check if value 200 exists in the following dictionary.

# sampledict = {'a': 100, 'b': 200, 'c': 300}
#
# contains = 200 in sampledict.values()
# print(contains)

#28  Change Brad's salary to 8500 in the following dictionary.

# sample_Dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
#
# sample_Dict['emp3'] = ' salary: 8500 '
#
# print(sample_Dict)