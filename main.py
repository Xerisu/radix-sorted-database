# import datetime
import csv

class Użytkownicy:
    def __init__(self):
        self.uzytkownicy = []

    # napisała Katarzyna Kowalska
    def dodaj_uzytkownika(self, rok, miesiac, dzien, godzina, minuta, sekunda):
        self.uzytkownicy.append({
            "rok": rok,
            "miesiac": miesiac,
            "dzien": dzien,
            "godzina": godzina,
            "minuta": minuta,
            "sekunda": sekunda
        })

    #napisał Tymoteusz Hryć
    def posortuj_po_dacie_radix_sort(self):
        # Sort by seconds
        self.uzytkownicy = self.radix_sort("sekunda")
        # Sort by minutes
        self.uzytkownicy = self.radix_sort("minuta")
        # Sort by hours
        self.uzytkownicy = self.radix_sort("godzina")
        # Sort by days
        self.uzytkownicy = self.radix_sort("dzien")
        # Sort by months
        self.uzytkownicy = self.radix_sort("miesiac")
        # Sort by years
        self.uzytkownicy = self.radix_sort("rok")

    #napisał Tymoteusz Hryć
    def radix_sort(self, key):


        # Pobierz maksymalną wartość w danej kolumnie
        max_value = max(self.uzytkownicy, key=lambda x: x[key])[key]

        # Zainicjuj koszyki
        buckets = [[] for _ in range(10)]

        # Wykonaj sortowanie dla każdej cyfry w danej kolumnie
        exp = 1
        while max_value // exp > 0:
            # Rozdziel elementy do odpowiednich koszyków
            for user in self.uzytkownicy:
                buckets[(user[key] // exp) % 10].append(user)

            # Sklej koszyki
            self.uzytkownicy = [user for bucket in buckets for user in bucket]

            # Wyczyść koszyki
            buckets = [[] for _ in range(10)]

            # Przesuń się do kolejnej cyfry
            exp *= 10

        return self.uzytkownicy

    # wykonała Kasia Kowalska
    def print_uzytkownicy(self):
        for uzytkownik in self.uzytkownicy:
            miesiac = uzytkownik["miesiac"]
            if miesiac < 10:
                miesiac = "0" + str(miesiac)
            godzina = uzytkownik["godzina"]
            if godzina < 10:
                godzina = "0" + str(godzina)
            dzien = uzytkownik["dzien"]
            if dzien < 10:
                dzien = "0" + str(dzien)
            minuta = uzytkownik["minuta"]
            if minuta < 10:
                minuta = "0" + str(minuta)
            sekunda = uzytkownik["sekunda"]
            if sekunda < 10:
                sekunda = "0" + str(sekunda)            
            print(f"{uzytkownik["rok"]}-{miesiac}-{dzien} {godzina}:{minuta}:{sekunda}")



# napisała Kasia Kowalska            
# inicjalizowanie uzytkownikow i dodawanie rzeczy z pliku
baza = Użytkownicy()
with open('baza.txt', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        baza.dodaj_uzytkownika(int(row['rok']), int(row['miesiac']), int(row['dzien']), int(row['godzina']), int(row['minuta']), int(row['sekunda']))
    print("Dodano istniejących użytkowników z pliku do programu")
while(True):
    print("Aby dodać nowego użytkownika do bazy, wpisz \"dodaj\", aby wyświetlić posortowanych użytkowników, wpisz \"posortuj\", aby zakonczyć działanie programu, wpisz \"zakoncz\"")
    slowo = input()

    if slowo== 'dodaj':
        print("Podaj datę urodzenia użytkownika, z dokładnością do sekundy:")
        try:
            rok = int(input("Podaj rok:"))
        except:
            print("Niepoprawny format!")
            continue
        if rok > 2024:
            print("Użytkownik nie może urodzić się w przyszłości")
            continue
        if rok < 1900:
            print("Użytkownik nie może być aż tak stary")
            continue

        try:
            miesiac = int(input("Podaj miesiąc:"))
        except:
            print("Niepoprawny format!")
            continue
        if miesiac > 12 or miesiac < 1:
            print("Niepoprawny miesiąc!")
            continue

        try:
            dzien = int(input("Podaj dzień:"))
        except:
            print("Niepoprawny format!")
            continue
        if dzien > 31 or dzien < 1:
            print("Niepoprawny dzień!")
            continue

        try:
            godzina = int(input("Podaj godzinę:"))
        except:
            print("Niepoprawny format!")
            continue
        if godzina > 23 or godzina < 1:
            print("Niepoprawna godzina!")
            continue

        try:
            minuta = int(input("Podaj minutę:"))
        except:
            print("Niepoprawny format!")
            continue
        if minuta > 59 or minuta < 1:
            print("Niepoprawna minuta!")
            continue

        try:
            sekunda = int(input("Podaj sekundę:"))
        except:
            print("Niepoprawny format!")
            continue
        if sekunda > 59 or sekunda < 1:
            print("Niepoprawna sekunda!")
            continue
        
        baza.dodaj_uzytkownika(rok,miesiac,dzien,godzina,minuta,sekunda)
        with open('baza.txt', mode='a') as csvfile:
            csvfile.write(f"{rok},{miesiac},{dzien},{godzina},{minuta},{sekunda}\n")    
        print("Pomyślnie dodano nowego użytkownika!")


    elif slowo == 'posortuj':
        print("Sortowanie użytkowników...")
        baza.posortuj_po_dacie_radix_sort()
        print("Posortowani użytkownicy:")
        baza.print_uzytkownicy()
    elif slowo == 'zakoncz':
        print("Dziękujemy za skorzystanie z naszego programu. Miłego dnia!")
        exit()
    else:
        print("Nieznana komenda!")



