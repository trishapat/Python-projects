ilosc_paczek = int(input("Proszę podaj ilość paczek, które chcesz wysłać: "))
ilosc_paczek_wyslanych = 1
suma_kilogramow_wyslanej_paczki = 0
paczka_najmniej_kilogramow = 0
suma_kilogramow_wyslanych = 0
numer_paczki_najwiecej_pustych_kg = 1

for numer_paczki in range(ilosc_paczek):
    waga_paczki = float(input(f"Podaj wagę paczki {numer_paczki + 1}: "))
    if waga_paczki > 10 or waga_paczki < 1:
        print("Paczka nie znajduje się w przedziale od 1 do 10 kg")
        break
    suma_kilogramow_wyslanych += waga_paczki
    if suma_kilogramow_wyslanej_paczki + waga_paczki <= 20:
        suma_kilogramow_wyslanej_paczki += waga_paczki
        paczka_najmniej_kilogramow += waga_paczki
    else:
        ilosc_paczek_wyslanych += 1
        suma_kilogramow_wyslanej_paczki = 0
        suma_kilogramow_wyslanej_paczki += waga_paczki
        if suma_kilogramow_wyslanej_paczki < paczka_najmniej_kilogramow:
            paczka_najmniej_kilogramow += waga_paczki
            numer_paczki_najwiecej_pustych_kg += 1

suma_pustych_kilogramow = ilosc_paczek_wyslanych * 20 - suma_kilogramow_wyslanych

if ilosc_paczek_wyslanych == 1:
    if suma_kilogramow_wyslanych == 0:
        ilosc_paczek_wyslanych = 0

if ilosc_paczek_wyslanych != 0:
    print(f"Liczba wysłanych paczek to: {ilosc_paczek_wyslanych}: ")
    print(f"Suma kilogramów wysłanych wynosi: {suma_kilogramow_wyslanych}")
    print(f"Suma pustych kilogramów to: {suma_pustych_kilogramow}")
    print(f"Paczka z największą ilością pustych kilogramów to paczka numer: "
          f"{numer_paczki_najwiecej_pustych_kg}")
else:
    print("Spróbuj ponownie")
