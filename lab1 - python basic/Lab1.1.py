#comentarii
# - pe o linie
""" comentarii pe
mai multe lini"""
''' comentarii pe mai 
multe linii si astfel'''

#variabile
print('variabile')
v_1 = 7;
print(v_1)
print(type(v_1))
v_1 += 4
print(v_1)
print(v_1/2)
print(v_1//2)   # parte intreaga
v_1 **= 2       # ridicare la patrat
print(v_1)

print()

#liste - pot contine elemente de mai multe tipuri
print('[ lista ]')
l_1 = [1, 10, 5, 15]    # indexeaxa de la 0
afiseaza = '%d %s' % (l_1[2], 'este al 3lea element din lista')
print(afiseaza)
print(str(l_1[2]) + ' este al treilea element')

l_1.append(100)
print(l_1)
l_1.append([200, 300])
print(l_1)
l_1 += [20]
print(l_1)

l_1.pop()               # sterge ultimul element
l_1.pop()               # pop-ul returneaza elementul sters
print(l_1)
print(l_1.pop(0))       # poate primi indexul elementului pe care vrem sa il stergem | returneaza elementul de pe pozitia resp
print(l_1)

l_1.extend([200, 300])  # concateneaza listele, adauga elementele date
print(l_1)
l_1.insert(1, 1000)     # adauga val la indexul specificat: (index, valoare)
print(l_1)

print(l_1[2:5:1])       # nume_lista[start : stop+1 : pasul cu care afiseaza]  (start inclusiv | stop exclusiv | stop )
print(l_1[-1])          # afiseaza ultimul element <=> print(l_1[len(l_1)-1])
print(l_1[-2])          # penultimul element
print(l_1[-1: :-1])     # afiseaza invers <=> print(l_1[: :-1])
print(l_1[:5])          # afiseaza de la 0 la 4
print(l_1[1:])          # afiseaza de la poz 1 pana la final
print(l_1[::])          # afiseaza toata lista <=> print(l_1)
print(l_1[:9])          # daca depaseste lungimea listei => afiseaza tot

#instructiunea for
print('afiseaza lista')
for val in l_1:
    print(val)                  # print pune automat new line

print('afiseaza in range')
for idx in range(len(l_1)):     # daca range are un singur parametru => de la 0 la valoarea parametrului (exclusiv)
    print(l_1[idx])

print('range')
range(3, 10, 2)                 # lim inf, lim sup, pas      || lim inf inclusiv, lim sup exclusiv
for i in range(2, 10, 2):
    print(i, end=' ')
print()

print()

#List Comprehension
print("List Comprehension")
print(l_1)
l_2 = [val*2 for val in l_1]    # l_2 este l_1 dublat
print(l_2)
l_3 = [val_1*val_2 for val_1 in l_1 for val_2 in l_2 if val_2 > 7]
print(l_3)
# echivalent cu
l_4 =[]
for val_1 in l_1:
    for val_2 in l_2:
        if val_2 > 7:
            l_4.append(val_1*val_2)
print(l_4)

print()

print("{ dictionare }")
#dictionare - chei si valori
d_1 = {
    'culori':['rosu', 'verde'],
    'mancare':['paste', 'mar'],
    'numere':[10, 20]
}
print(d_1['mancare'])
print(d_1["mancare"][1])

for key in d_1:
    for val in d_1[key]:
        print(val, end=' ')   # ca sa nu mai dea newline
    print()                     # print('\n') - inca un enter

print()
print('sets')
#seturi - folosite pt cand vrem sa eliminam duplicate dintr-o lista
s_1 = {1, 2, 3, 4, 5, 3}        #elimina duplicate
print(s_1)
lista = [2, 5, 2, 3, 1]
lista_1 = list( set(lista) )
print(lista_1)
print('experiment')
print(lista)
lista = set(lista)
print(lista)
lista = list(lista)
print(lista)

print()
#functii
def f1(l):                     # mereu def inaintea unei functii
    s = 0
    for val in l:
        s += val
    return s                    # suma elementelor din lista l

v = f1(lista_1)
print(v)

print(f1([1, 2, 3]))

#clase in pdf


#Exercitii
# 1.
y_pred = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]     #etichete prezise
y_true = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]     #etichete reale

# a)
def accuracy_score(y_pred, y_true):
    eq = 0                                  # equal
    for idx in range(len(y_pred)):
        if y_pred[idx] == y_true[idx]:
            eq += 1
    return eq/len(y_pred)
print(accuracy_score(y_pred, y_true))

# b)
# tp = true positive
# fp = false positive
# fn = false negative
def precision_recall_score(y_true, y_pred):
    tp = 0
    fp = 0
    fn = 0
    for idx in range(len(y_pred)):
        if y_pred[idx] == y_true[idx] and y_pred[idx] == 1:
            tp += 1
        if y_pred[idx] == 1 and y_true[idx] == 0:
            fp += 1
        if y_pred[idx] == 0 and y_true[idx] == 1:
            fn += 1
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return precision, recall

print(precision_recall_score(y_true, y_pred))

# # c)
# def  ​mse(y_true, y_pred):              #mean square error
#     mse = 0
#     for idx in range(len(y_pred)):
#         mse += (y_pred[idx] - y_true[idx])**2

#ctrl + click pe functie => te trimite la definitie
