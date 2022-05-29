#importujemy modul i nadajemy mu alias
from mytoolkit import matematyczny as mat
from mytoolkit import pomocniczy as pom
# Wywolanie funkcji metod z mytoolkit/matematyczny alias mat

print(mat.dodaj(4, 14))
print(mat.odejmij(14,9))

# Wywolanie funkcji z mytoolkit/pomocniczy alias pomocniczy
pom.czesc()
