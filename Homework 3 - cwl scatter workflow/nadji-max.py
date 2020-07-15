import sys

class Potrosnja:
    broj = ""
    novac = 0.0

    def __init__(self,broj,novac):
        self.broj = broj
        self.novac = novac
    
    def dodajNovac(self, novac):
        self.novac += novac


niz = []

def nadjiBroj(niz, broj):
    for i in range(len(niz)):
        if (niz[i].broj == broj):
            return i
    
    return -1

for i in range(1,len(sys.argv)):
    f = open(sys.argv[i], "r")
    
    for line in f:
        tokens = line.split(",")
        broj = tokens[0]
        novac = float(tokens[1])

        indeks = nadjiBroj(niz, broj)

        if (indeks == -1):
            niz.append(Potrosnja(broj, novac))
        else:
            niz[indeks].dodajNovac(novac)

maxNovac = -1.0
maxBroj = ""

for element in niz:
    if (element.novac > maxNovac):
        maxNovac = element.novac
        maxBroj = element.broj


print(maxBroj+","+str(maxNovac))



  