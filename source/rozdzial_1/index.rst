===========================
Wprowadzenie
===========================

:Autor:
    Oskar Wrona

Rozdział stanowi indywidualne wprowadzenie do sprawozdania z kursu baz danych,
realizowanego w semestrze letnim roku akademickiego 2025/2026.

Wprowadzenie tematyczne
=======================

Ćwiczenia i eksperymenty przedstawione w raporcie obejmują pełny cykl pracy
z relacyjną bazą danych: od poznania zagadnień związanych z jej utrzymaniem,
przez analizę wymagań i projektowanie struktury danych, aż do implementacji,
zasilenia bazy danymi oraz wykonywania zapytań. Część literaturowa przybliża
praktyczne aspekty eksploatacji PostgreSQL, między innymi dobór sprzętu,
konfigurację serwera, kontrolę i konserwację, monitorowanie, diagnostykę,
partycjonowanie, bezpieczeństwo, tworzenie kopii zapasowych oraz zagadnienia
wydajności, skalowania i replikacji.

Część projektowa została oparta na przykładzie systemu zarządzania sprzedażą
w sklepie internetowym. Analizie poddano procesy związane z obsługą klientów,
produktów, producentów, kategorii, kodów rabatowych, zamówień, płatności,
wysyłek oraz opinii. Na tej podstawie przygotowano model konceptualny, model
logiczny doprowadzony do trzeciej postaci normalnej oraz dwa modele fizyczne,
dostosowane odpowiednio do PostgreSQL i SQLite. Szczególną uwagę poświęcono
poprawnemu odwzorowaniu zależności między danymi, zachowaniu historii cen
produktów w zamówieniach oraz zastosowaniu kluczy i więzów integralności.

W dalszej części raportu przedstawiono implementację schematów w obu systemach
zarządzania bazą danych oraz wsadowe wprowadzanie danych z pliku CSV za pomocą
skryptów napisanych w języku Python. Omówiono walidację danych, sprawdzanie
istnienia rekordów powiązanych, kolejność operacji oraz obsługę transakcji
i błędów. Działanie utworzonych baz sprawdzono następnie za pomocą zapytań
wykorzystujących złączenia, agregacje, grupowanie, sortowanie i podzapytania.
Zapytania przygotowano oddzielnie dla PostgreSQL i SQLite, co umożliwiło
porównanie działania obu silników na tym samym modelu i zbiorze danych.

Wnioski z ćwiczeń i eksperymentów
=================================

Przeprowadzone ćwiczenia pokazały, że jakość bazy danych zależy przede wszystkim
od poprawnego rozpoznania procesów biznesowych i zależności pomiędzy danymi.
Pomijanie kontekstu transakcji lub niewłaściwe odwzorowanie relacji
wiele-do-wielu prowadziłoby do utraty istotnych informacji. W projekcie problem
ten rozwiązano przez wprowadzenie tabeli ``Pozycje_Zamowienia``, która łączy
zamówienia z produktami, a jednocześnie przechowuje liczbę sztuk i cenę
historyczną.

Normalizacja do trzeciej postaci normalnej ograniczyła powielanie informacji
i ryzyko wystąpienia anomalii podczas dodawania, modyfikowania oraz usuwania
danych. Jednocześnie wykazała, że bardziej uporządkowana struktura wymaga
stosowania złączeń wielu tabel podczas odtwarzania pełnego obrazu procesu
sprzedaży. Przygotowane zapytania potwierdziły, że taki model pozwala zarówno
odtworzyć szczegóły zamówień, jak i wykonywać analizy, na przykład tworzyć
ranking klientów, obliczać sprzedaż według kategorii czy zestawiać oceny
produktów.

Implementacja w PostgreSQL i SQLite wykazała, że ten sam model logiczny może
zostać przeniesiony pomiędzy różnymi systemami bazodanowymi, lecz wymaga
dostosowania typów danych, sposobu generowania identyfikatorów i niektórych
elementów składni. PostgreSQL oferuje bardziej precyzyjne typy, takie jak
``NUMERIC`` i ``TIMESTAMP``, natomiast SQLite wykorzystuje prostszy system klas
przechowywania. Mimo tych różnic oba rozwiązania mogą realizować te same reguły
biznesowe i zwracać zgodne wyniki zapytań.

Eksperymenty z importem danych potwierdziły znaczenie walidacji, więzów
integralności oraz transakcji. Dane muszą być dodawane w kolejności wynikającej
z zależności między tabelami, a błędny rekord nie powinien pozostawiać bazy
w stanie częściowo zmodyfikowanym. Zastosowanie sprawdzania danych, zatwierdzania
poprawnych operacji i wycofywania błędnych pozwala zachować spójność bazy również
podczas automatycznego zasilania jej większą liczbą rekordów.

Całość prac pokazała również, że samo poprawne zaprojektowanie tabel nie
wyczerpuje zagadnienia utrzymania bazy danych. W rzeczywistym środowisku równie
ważne są konfiguracja serwera, monitorowanie, bezpieczeństwo, kopie zapasowe
i planowanie wydajności. Projektowanie, implementacja, testowanie zapytań
oraz administracja tworzą jeden powiązany proces, którego celem jest uzyskanie
systemu spójnego, niezawodnego i możliwego do dalszego rozwoju.


Spis wszystkich użytych w raporcie repozytoriów
================================================

Repozytoria tematyczne
-----------------------

* `Sprzęt dla bazy danych <https://github.com/karaskamil/Sprzet-dla-bazy-danych.git>`_
* `Konfiguracja bazy danych PostgreSQL <https://github.com/Youarecheck/Bazy_Danych_Tematyczne_Repo_MK.git>`_
* `Kontrola i konserwacja bazy danych <https://github.com/pawlos1337/Bazy-danych-temat.git>`_
* `Monitorowanie i diagnostyka <https://github.com/OskarProgrammer/monitorowanie_i_diagnostyka.git>`_
* `Wydajność, skalowanie i replikacja danych <https://github.com/KMachoK/Tematyczne.git>`_
* `Partycjonowanie danych <https://github.com/domino0472/Partycjonowani-Danych.git>`_
* `Bezpieczeństwo baz danych <https://github.com/oski486/BazyDanych-Subject.git>`_
* `Kopie zapasowe i odzyskiwanie danych <https://github.com/Koko9077/Kopie-zapasowe-i-odzyskiwanie-danych.git>`_

Modele
------

* `Model konceptualny, logiczny i fizyczny <https://github.com/OskarProgrammer/model-konceptualny-logiczny-fizyczny.git>`_

Implementacja
-------------

* `Implementacja bazy danych <https://github.com/OskarProgrammer/implementacja-bazy-danych.git>`_

Repozytorium główne
--------------------

* `Repozytorium główne <https://github.com/OskarProgrammer/bazy_danych_glowne_3.git>`_
