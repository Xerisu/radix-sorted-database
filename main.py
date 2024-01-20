#import datetime

class Użytkownicy:
    def __init__(self):
        self.uzytkownicy = []
    # napisała Katarzyna Kowalska
    # funkcja sprawdza tylko poprawność na poziomie intów, sprawdzenie czy przyjmujemy inty trzeba zrobić gdzie indziej
    def dodaj_uzytkownika(self, rok, miesiac, dzien, godzina, minuta, sekunda):
            if rok > 2024:
                 #todo: zrobić to z całą datą nie tylko rokiem
                 print("Użytkownik nie może się urodzić w przyszłości")
                 return
            if miesiac > 12 or miesiac < 0:
                print("Niepoprawny miesiąc")
            if dzien > 31 or dzien < 0:
                 print("Niepoprawny dzień!")
            if godzina > 60 or godzina < 0:
                 print("Niepoprawna godzina!")
            if minuta > 60 or minuta < 0:
                 print("Niepoprawna minuta!")
            if sekunda > 60 or sekunda < 0:
                 print("Niepoprawna sekunda!")
            self.uzytkownicy.append( {
            "rok" : rok,
            "miesiac" : miesiac,
            "dzien" : dzien,
            "godzina" : godzina,
            "minuta" : minuta,
            "sekunda" : sekunda    
                })
    
    def posortuj_po_dacie_radix_sort(self):
        return

# napisała Katarzyna Kowalska
# tab_to_sort : tablica którą będziemy sortować, nie obchodzi nas jej zawartość
# key : tablica cyfr zawierających liczby od 0 do 9 po których będziemy sortować
def counting_sort(tab_to_sort : list, key : list) -> None:

    count_array = []
    for i in range(10):
        count_array.append(0)

    for elem in key:
        count_array[elem] += 1
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    sorted_tab = []
    for i in range(len(key)):
        sorted_tab.append(0)

    for i in range(len(key)-1, -1, -1):
        count_array[key[i]] -= 1
        index = count_array[key[i]]
        sorted_tab[index] = tab_to_sort[i] 
    return sorted_tab
         
         
         



# testy, do wywalenia lub zakomentowania potem

uzytkownicy = Użytkownicy()
uzytkownicy.dodaj_uzytkownika(2002, 12, 12, 12, 12, 12)
uzytkownicy.dodaj_uzytkownika(2002, 12, 12, 12, 50, 12)

tab10 = [1, 5, 3, 2, 5, 1, 5, 0, 1]
tab1 = [2, 3, 1, 7, 1, 3, 5, 4, 1]
tabMain = [12, 53, 31, 27, 51, 13, 55, 4, 11]

tabMain = counting_sort(tabMain, tab1)
tab10 = counting_sort(tab10, tab1)
tabMain = counting_sort(tabMain, tab10)

print(tabMain)