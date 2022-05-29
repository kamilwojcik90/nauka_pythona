# najprostrzy sposob definiowania obiektu
# pass jest to miejsce dla funkcjonalnosci, ktora bedzie dodana pozniej
# pass moze byc uzyte w ciele metody ktore nioc nie robi

# self reprezentuje instacje klasy, dzieki uzyciu self mozemy miec dostep do wlasciwosci i metod klasy w pythonie
class Paletka:
    def __init__(self, kolor):
    #pass

# tworzymy obiekt na podstawie klasy
def testklasy():
    paletka_a = Paletka()
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
    # print("Obiekt typu " + {type(paletka_a)} + " zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_a))
