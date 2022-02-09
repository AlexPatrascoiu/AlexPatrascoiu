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
print(nume_list)
remove = nume_list.remove('a')   #vrem sa scoatem litera a din lista.
print(nume_list)

pop = nume_list.pop(2)         #scoate ultima valoare din lista
print(nume_list)
print(remove)
print(pop)
'''
diferenta intre pop si remove:

-remove sterge 1 singur caracter intre (),pop sterge 1 singur caracter in functie de index.
-remove nu returneaza nimic;    pop returneaza o valoare.
'''







