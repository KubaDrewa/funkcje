#Funkcja niezwracająca wartości
def wypisz_50_czesc():
    print('czesc ' * 50) # dp tych danych nie ma dostępu z zewnątrz funkcji
    print(50)

wypisz_50_czesc()
print("xd")
wypisz_50_czesc()

#Funkcja zwracająca wartości
def f(x):
    return 3 * x + 5

wynikf5 = f(5)
print(wynikf5)

print(f(1))


#Funkcja do obliczania funkcji ważonej

def srednia_wazona(oceny, wagi):
    suma_oceny_wagi = 0
    suma_wagi = 0
    for i in range(len(oceny)):
        suma_oceny_wagi += oceny[i] + wagi[i]
        suma_wagi += wagi[i]
    return suma_oceny_wagi / suma_wagi

print(srednia_wazona([6, 3], [2, 1]))

#Funkcja wywołuje funkcje
lista_napisow = ["123", "4563", "6722128"]
lista_dlugosci = list(map(len, lista_napisow))
print(lista_dlugosci)
lista_liczb = list(map(int, lista_napisow))
print(lista_liczb)
