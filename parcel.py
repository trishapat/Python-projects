# brak sprawdzania paczki z najmniejszą ilością pustych kilogramów
# listy nie zostały użyte

ilosc_paczek = int(input("Proszę podaj ilość paczek, które chcesz wysłać: "))
ilosc_paczek_wyslanych = 1
suma_kilogramow_wyslanej_paczki = 0
suma_kilogramow_wyslanych = 0

for numer_paczki in range(ilosc_paczek):
    waga_paczki = float(input(f"Podaj wagę paczki {numer_paczki + 1}: "))
    if waga_paczki > 10 or waga_paczki < 1:
        print("Paczka nie znajduje się w przedziale od 1 do 10 kg")
        break
    suma_kilogramow_wyslanych += waga_paczki
    if suma_kilogramow_wyslanej_paczki + waga_paczki <= 20:
        suma_kilogramow_wyslanej_paczki += waga_paczki
    else:
        ilosc_paczek_wyslanych += 1
        suma_kilogramow_wyslanej_paczki = 0
        suma_kilogramow_wyslanej_paczki += waga_paczki

suma_pustych_kg = ilosc_paczek_wyslanych * 20 - suma_kilogramow_wyslanych

if ilosc_paczek_wyslanych == 1:
    if suma_kilogramow_wyslanych == 0:
        ilosc_paczek_wyslanych = 0

if ilosc_paczek_wyslanych != 0:
    print(f"Liczba wysłanych paczek to: {ilosc_paczek_wyslanych}: ")
    print(f"Suma kilogramów wysłanych wynosi: {suma_kilogramow_wyslanych}")
    print(f"Suma pustych kilogramów to: {suma_pustych_kg}")
else:
    print("Spróbuj ponownie")
