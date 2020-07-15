import sys

class Potrosnja:
    broj = ""
    novac = 0.0

    def __init__(self,broj,novac):
        self.broj = broj
        self.novac = novac
    
    def dodajNovac(self, novac):
        self.novac += novac

f = open(sys.argv[1], "r")
cenaSms = float(sys.argv[2])
cenaPoziv = float(sys.argv[3])

niz = []

def nadjiBroj(niz, broj):
    for i in range(len(niz)):
        if (niz[i].broj == broj):
            return i
    
    return -1

for line in f:
    tokens = line.split(",")
    broj = tokens[0]
    tip = tokens[1]
    kolicina = float(tokens[2])
    #print(kolicina)

    indeks = nadjiBroj(niz, broj)
    cena = 1.0

    if (tip == "sms"):
        cena = cenaSms
    else:
        cena = cenaPoziv
    
    #print(cena)

    if (indeks == -1):
        niz.append(Potrosnja(broj, kolicina*cena))
    else:
        niz[indeks].dodajNovac(kolicina*cena)

for element in niz:
    print(str(element.broj)+","+str(element.novac))



  