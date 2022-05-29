# najprostrzy sposob definiowania obiektu
# pass jest to miejsce dla funkcjonalnosci, ktora bedzie dodana pozniej
# pass moze byc uzyte w ciele metody ktore nioc nie robi

# self reprezentuje instacje klasy, dzieki uzyciu self mozemy miec dostep do wlasciwosci i metod klasy w pythonie
# Tworzenie obiektu realizujemy przez tzw. konstruktor - jest to specjalna metoda, ktora wykonywana kiedy tworzymy nasz obiekt
class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzylismy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")
    #pass
    def info(self):
        print(f"Kolor obiektu to: {self.kolor_obiektu}")

    def info_ex(self, nazwa):
        print(f"Kolor obiektu {nazwa} to {self.kolor_obiektu}")
# tworzymy obiekt na podstawie klasy
def testklasy():
    paletka_a = Paletka("czerwony")
    paletka_b = Paletka("niebieski")
    print("")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
    # print("Obiekt typu " + {type(paletka_a)} + " zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_a))

    print("")
    print(f"Obiekt typu {type(paletka_b)} zawiera od razu pewne właściwości i metody:")
    # print("Obiekt typu " + {type(paletka_a)} + " zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_b))

    print("")
    print(f"Kolor dla paletka_a: {paletka_a.kolor_obiektu}")
    print(f"Kolor dla paletka_b: {paletka_b.kolor_obiektu}")

    paletka_a.info()
    paletka_b.info()
    paletka_a.info_ex("paletka_a")
    paletka_b.info_ex("paletka_b")
