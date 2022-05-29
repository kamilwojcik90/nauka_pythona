# najprostrzy sposob definiowania obiektu
# pass jest to miejsce dla funkcjonalnosci, ktora bedzie dodana pozniej
# pass moze byc uzyte w ciele metody ktore nioc nie robi
class Paletka:
    pass

# tworzymy obiekt na podstawie klasy
paletka_a = Paletka()
print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
# print("Obiekt typu " + {type(paletka_a)} + " zawiera od razu pewne właściwości i metody:")
print(dir(paletka_a))
