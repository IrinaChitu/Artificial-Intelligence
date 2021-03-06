""" definirea problemei """
import configuratii as cf

class Nod:

    NR_LINII = 20
    NR_COLOANE = 20


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

    def __init__(self, pozitii, scop):

        self.nod_start = Nod(list(pozitii), float('inf'))
        self.reprez_scop = list(scop)


    def scop(self, nod):
        return nod.info == self.reprez_scop


    def get_x_y(self, ind):
        j_elem = ind // 20
        i_elem = ind % 20
        return i_elem, j_elem


    # TODO completat euristica
    # Reprez_nod este configuratia curenta a labirintului.
    # Prin self avem acces la reprez_scop.
    # O varianta de euristica e aceea de a calcula distanta intre locatia cifrei 1 in reprez_nod si locatia cifrei 1 in reprez_scop.
    def calculeaza_h(self, reprez_nod):
        # ...
        poz_cifra_1_in_reprez_nod = reprez_nod.index(1)
        poz_cifra_1_in_reprez_scop = self.reprez_scop.index(1)

        i_nod, j_nod = self.get_x_y(poz_cifra_1_in_reprez_nod)
        i_scop, j_scop = self.get_x_y(poz_cifra_1_in_reprez_scop)

        return abs(i_nod - i_scop) + abs(j_nod - j_scop)


    def interschimba(self, ind1, ind2, l):  # l = lista in care se realizeaza interschimbarea
        lnou = list(l)
        lnou[ind1], lnou[ind2] = lnou[ind2], lnou[ind1]
        return lnou


    # TODO Calcul succeesori
    # Nod este o configuratie curenta de labirint.
    # Pornind de la locatia in care se afla cifra 1, se poate stabili toate mutarile posibile
    # (sus, jos, stanga, dreapta) si vor fi adaugate in l_succesori.
    def calculeaza_succesori(self, nod):
        # ...
        # poz_cifra_1_in_reprez_nod = self.nod.index(1)
        # i, j = self.get_x_y(poz_cifra_1_in_reprez_nod)
        poz_cifra_1_in_nod = nod.info.index(1)
        i = poz_cifra_1_in_nod // 20
        j = poz_cifra_1_in_nod % 20
        l_succesori = []
        if i >= 1:
            poz_cifra_1_in_urma_mutarii = poz_cifra_1_in_nod - 20
            if nod.info[poz_cifra_1_in_urma_mutarii] != 2:
                lista_noua = self.interschimba(poz_cifra_1_in_nod, poz_cifra_1_in_urma_mutarii, nod.info.copy())
                h_fiu = self.calculeaza_h(lista_noua)
                l_succesori.append((Nod(lista_noua, h_fiu), 1))

        if i <= 18:
            poz_cifra_1_in_urma_mutarii = poz_cifra_1_in_nod + 20
            if nod.info[poz_cifra_1_in_urma_mutarii] != 2:
                lista_noua = self.interschimba(poz_cifra_1_in_nod, poz_cifra_1_in_urma_mutarii, nod.info.copy())
                h_fiu = self.calculeaza_h(lista_noua)
                l_succesori.append((Nod(lista_noua, h_fiu), 1))
        if j >= 1:
            poz_cifra_1_in_urma_mutarii = poz_cifra_1_in_nod - 1
            if nod.info[poz_cifra_1_in_urma_mutarii] != 2:
                lista_noua = self.interschimba(poz_cifra_1_in_nod, poz_cifra_1_in_urma_mutarii, nod.info.copy())
                h_fiu = self.calculeaza_h(lista_noua)
                l_succesori.append((Nod(lista_noua, h_fiu), 1))
        if j <= 18:
            poz_cifra_1_in_urma_mutarii = poz_cifra_1_in_nod + 1
            if nod.info[poz_cifra_1_in_urma_mutarii] != 2:
                lista_noua = self.interschimba(poz_cifra_1_in_nod, poz_cifra_1_in_urma_mutarii, nod.info.copy())
                h_fiu = self.calculeaza_h(lista_noua)
                l_succesori.append((Nod(lista_noua, h_fiu), 1))
        return l_succesori


""" Sfarsit definire problema """

""" Clase folosite in algoritmul A* """

class NodCautare:
    def __init__(self, nod_graf, succesori=[], parinte=None, g=0, f=None):
        self.nod_graf = nod_graf
        self.succesori = succesori
        self.parinte = parinte
        self.g = g
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore(self):
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        nod_c = self
        while nod_c.parinte is not None:
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parinte
        return False

    def __str__(self):
        return str(self.nod_graf)


""" Algoritmul A* """

def debug_str_l_noduri(l):
    sir = ""
    for x in l:
        sir += str(x) + "\n"

    return sir

def get_lista_solutii(l):
    drum = []
    for x in l:
         drum.append(x.nod_graf.info)
    return drum

def in_lista(l, nod):
    for x in l:
        if x.nod_graf.info == nod.info:
            return x
    return None



def a_star(graf):
    rad_arbore = NodCautare(nod_graf=graf.nod_start)
    print(graf.nod_start.info)
    print(graf.nod_start)

    open_list = [rad_arbore]
    closed = []
    while len(open_list) > 0:
        nod_curent = open_list.pop(0)
        closed.append(nod_curent)
        if graf.scop(nod_curent.nod_graf):
            break
        l_succesori = graf.calculeaza_succesori(nod_curent.nod_graf)
        for (nod, cost) in l_succesori:
            if (not nod_curent.contine_in_drum(nod)):
                x = in_lista(closed, nod)
                g_succesor = nod_curent.g + cost
                f = g_succesor + nod.h
                if x is not None:
                    if (f < nod_curent.f):
                        x.parinte = nod_curent
                        x.g = g_succesor
                        x.f = f
                else:
                    x = in_lista(open_list, nod)
                    if x is not None:
                        if (x.g > g_succesor):
                            x.parinte = nod_curent
                            x.g = g_succesor
                            x.f = f
                    else:  # cand nu e nici in closed nici in open
                        nod_cautare = NodCautare(nod_graf=nod, parinte=nod_curent, g=g_succesor)
                        open_list.append(nod_cautare)
        open_list.sort(key=lambda x: (x.f, x.g))

    f = open('demo_file.txt', 'a')
    f.write(debug_str_l_noduri(nod_curent.drum_arbore()))
    return get_lista_solutii(nod_curent.drum_arbore())


def main(pozitii, scop):
    problema = Graf(pozitii, scop)
    return a_star(problema)


def asd():
    return main(cf.start, cf.scop)
