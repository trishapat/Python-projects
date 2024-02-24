ilosc_paczek = int(input("Proszę podaj ilość paczek, które chcesz wysłać: "))
ilosc_paczek_wyslanych = 0
waga_wyslanej_paczki = 0

paczki_wyslane_wagi = []

for numer_paczki in range(ilosc_paczek):
    waga_paczki = float(input(f"Podaj wagę paczki {numer_paczki + 1}: "))

    if waga_paczki > 10 or waga_paczki < 1:
        print("Paczka nie znajduje się w przedziale od 1 do 10 kg")
        break

    if waga_wyslanej_paczki + waga_paczki > 20:
        ilosc_paczek_wyslanych += 1
        paczki_wyslane_wagi.append(waga_wyslanej_paczki)
        waga_wyslanej_paczki = 0
    waga_wyslanej_paczki += waga_paczki


if waga_wyslanej_paczki != 0:
    ilosc_paczek_wyslanych += 1
    paczki_wyslane_wagi.append(waga_wyslanej_paczki)

    paczka_najwiecej_pustych_kg = min(paczki_wyslane_wagi)

if paczki_wyslane_wagi:
    print(f"Liczba wysłanych paczek to: {ilosc_paczek_wyslanych}: ")
    print(f"Suma kilogramów wysłanych wynosi: {sum(paczki_wyslane_wagi)}")
    print(f"Suma pustych kilogramów to: "
          f"{ilosc_paczek_wyslanych * 20 - sum(paczki_wyslane_wagi)} kg")
    print(f"Paczka z największą ilością pustych kilogramów to paczka numer: "
          f"{paczki_wyslane_wagi.index(paczka_najwiecej_pustych_kg) + 1}")
else:
    print("Spróbuj ponownie")
