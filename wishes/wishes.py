'''Stwórz program, który generuje spersonalizowaną kartkę urodzinową. Program będzie prosił użytkownika o konkretne informacje, a następnie generował kartkę urodzinową na podstawie jego odpowiedzi. Wiek osoby powinien być obliczany na podstawie roku urodzenia podanego przez użytkownika.

1. Napisz program, który prosi użytkownika o podanie następujących informacji:

 - Imię odbiorcy
 - Rok urodzenia
 - Spersonalizowaną wiadomość
 - Imię nadawcy

2. Program powinien następnie obliczyć wiek odbiorcy na podstawie obecnego roku i roku urodzenia podanego przez użytkownika.

3. Wygeneruj spersonalizowaną kartkę urodzinową z następującą wiadomością:

[Imię odbiorcy], wszystkiego najlepszego z okazji [Wiek] urodzin!

[Spersonalizowana Wiadomość]

[Imię Nadawcy]

Wskazówki:

- Upewnij się, że program jest łatwy w obsłudze
- Podczas obliczania wieku odbiorcy, pamiętaj, aby konwertować dane wprowadzone przez użytkownika na odpowiedni typ zmiennej.
- Możesz zodyfikować szablon według własnego uznania. Upewnij się, że wyświetlasz wszystkie niezbędne zmienne.'''

rok_urodzenia = int(input("Podaj rok urodzenia solenizanta/solenizantki:"))
imie_solenizant = input("Podaj imię solenizanta/solenizantki:")
imie_nadawca = input("Podaj swoje imię:")
wiadomosc = input("Podaj wiadomość, którą ma otrzymać solenizant/solenizantka:")
wiek = int(2024 - rok_urodzenia)
print(f"{imie_solenizant}, wszystkiego najlepszego z okazji {wiek} urodzin! ")
print("")
print(wiadomosc)
print("")
print(imie_nadawca)