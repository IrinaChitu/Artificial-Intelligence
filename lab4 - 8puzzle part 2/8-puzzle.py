""" definirea problemei """
''' am facut joculetul asta cu ei in laborator si se juca dand coordonate de la tastatura'''


class Nod:
    NR_LINII = 3
    NR_COLOANE = 3

    def __init__(self, info, h):
        self.info = info
        self.h = 0

    def __repr__(self):
        sir = "\n"
        for i in range(0, Nod.NR_LINII):
            for j in range(0, self.__class__.NR_COLOANE):
                sir += str(self.info[i * self.__class__.NR_COLOANE + j]) + " "
            sir += "\n"
        return sir


class Graf:
    def __init__(self, start, scop):
        self.nod_start = Nod(start, float('inf'))
        self.reprez_scop = scop
        self.afis_scop = Nod([1, 2, 3, 4, 5, 6, 7, 8, 0], float('inf'))

    def scop(self, nod):
        return nod.info == self.reprez_scop

    def interschimba(self, ind1, ind2, l):
        lnou = list(l)
        lnou[ind1], lnou[ind2] = lnou[ind2], lnou[ind1]
        return lnou



# ---------------------------------------
start = [2, 4, 3, 8, 7, 5, 1, 0, 6]
scop = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# ...
'''
ind1 - prima placuta
ind2 - a doua placuta
interschimba - intersch placutele de la inidicii de mai sus
'''

# ob = Graf(start, scop)
# while (not ob.scop(ob.nod_start)):
#     print('start: ')
#     print(ob.nod_start)
#     ind1 = int(input('ind1: '))
#     ind2 = int(input('ind2: '))
#     ob.nod_start.info = ob.interschimba(ind1, ind2, ob.nod_start.info)

