#Zadanie 1
def informatyka(n):
    print("Informatyka " * n)

informatyka(10)
informatyka(1+4)


#Zadanie 2
def pole_kwadratu(a):
    return a**2

def pole_prostokąta(a, b):
    return (a*b)

print(pole_kwadratu(16))
print(pole_prostokąta(14, 19))

#Zadanie 3
def pole_powierzchni_calkowitej(d, h):
    return pole_kwadratu(d) *2 + pole_prostokąta(d, h) * 4
print(pole_powierzchni_calkowitej(5, 10))

#Zadanie 4
def srednia_wazona(oceny, wagi, ilosc):
    suma_ocen = 0
    suma_wag = 0
    for i in range(ilosc):
        suma_ocen += oceny[i] * wagi[i]
        suma_wag += wagi[i]

    return suma_ocen/suma_wag

print(srednia_wazona([5,6,4.25,6,6,4],[4, 2,4,2,2,4], 6))

#Zadanie 5
def NWD(pierwsza, druga):
    mniejszy = min([pierwsza, druga])
    for i in range(mniejszy):
        a = mniejszy-i
        if pierwsza % a == 0 and druga % a == 0:
            return (a)

print(NWD(16,88))
#