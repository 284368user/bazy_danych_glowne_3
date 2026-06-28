===========================
Wprowadzenie
===========================

:Autor:
    Kamil Lewandowski

:Grupa projektowa:
    Kamil Lewandowski, Adam Tarkowski, Oskar Wrona

Rozdział stanowi indywidualne wprowadzenie do sprawozdania z kursu baz danych,
realizowanego w semestrze letnim roku akademickiego 2025/2026.


Wprowadzenie tematyczne
=======================

Ćwiczenia opisane w raporcie obejmują pełny cykl pracy z relacyjną bazą danych.
Punktem wyjścia były badania literaturowe dotyczące utrzymania baz danych na
przykładzie PostgreSQL. W tej części zebrano zagadnienia związane między innymi
z doborem sprzętu, konfiguracją serwera, kontrolą i konserwacją bazy,
monitorowaniem, diagnostyką, partycjonowaniem danych, bezpieczeństwem,
tworzeniem kopii zapasowych oraz planowaniem wydajności, skalowania i replikacji.
Pozwoliło to spojrzeć na bazę danych nie tylko jako na zestaw tabel, lecz także
jako na system wymagający stałej administracji i świadomego utrzymania.

Część projektowa raportu została oparta na przykładzie systemu obsługującego
sprzedaż w sklepie internetowym. W modelu uwzględniono klientów, produkty,
producentów, kategorie, kody rabatowe, zamówienia, płatności, wysyłki oraz
opinie. Na tej podstawie przygotowano model konceptualny, model logiczny
z uwzględnieniem normalizacji oraz dwa modele fizyczne: osobny dla PostgreSQL
i osobny dla SQLite. Istotne było zachowanie spójności pomiędzy modelami, a także
takie odwzorowanie relacji, aby baza poprawnie przechowywała informacje
o zamówieniach, pozycjach zamówień i cenach obowiązujących w momencie zakupu.

Kolejnym etapem była implementacja bazy danych w dwóch wariantach. Dla PostgreSQL
i SQLite przygotowano definicje tabel, kluczy głównych, kluczy obcych oraz
pozostałych ograniczeń integralności. Następnie baza została zasilona danymi
z pliku CSV przy użyciu skryptów w języku Python. W tej części ważne było
zachowanie właściwej kolejności wprowadzania rekordów, walidowanie danych
wejściowych, sprawdzanie zależności między tabelami oraz obsługa sytuacji
błędnych w taki sposób, aby nie pozostawiać w bazie częściowo zapisanych
zamówień.

Ostatnia część ćwiczeń dotyczyła zapytań SQL. Przygotowane zapytania pozwoliły
sprawdzić, czy baza przechowuje dane w sposób umożliwiający uzyskanie praktycznych
informacji, takich jak szczegóły zamówień, zestawienia sprzedaży, rankingi
klientów, analiza kategorii produktów czy porównanie ocen. Zapytania zostały
opracowane oddzielnie dla PostgreSQL i SQLite, dzięki czemu można było zauważyć
zarówno podobieństwa wynikające ze wspólnego modelu relacyjnego, jak i różnice
w składni oraz sposobie pracy obu systemów.


Wnioski z ćwiczeń i eksperymentów
=================================

Po wykonaniu ćwiczeń można zauważyć, że projektowanie bazy danych wymaga przede
wszystkim dobrego zrozumienia problemu, a nie tylko znajomości składni SQL. Przed
utworzeniem tabel trzeba ustalić, jakie informacje są naprawdę potrzebne, które
z nich są od siebie zależne i które powinny zostać zapisane jako dane historyczne.
W projekcie sklepu internetowego dobrym przykładem jest cena produktu w zamówieniu.
Nie może ona zależeć wyłącznie od aktualnej ceny w katalogu, ponieważ po zmianie
cennika wcześniejsze zamówienia powinny nadal przedstawiać rzeczywisty stan
transakcji.

Model konceptualny i logiczny pomógł uporządkować sposób myślenia o danych.
Rozdzielenie klientów, produktów, zamówień, płatności, wysyłek, kodów rabatowych
i opinii zmniejsza powtarzanie danych oraz ogranicza ryzyko niespójności. Z drugiej
strony widać, że bardziej poprawny model wymaga później dokładniejszego pisania
zapytań, ponieważ wiele informacji trzeba uzyskać przez połączenie kilku tabel.
Dla mnie był to ważny wniosek, bo pokazuje kompromis między przejrzystą strukturą
bazy a wygodą pobierania danych.

Implementacja tego samego projektu w PostgreSQL i SQLite pokazała, że systemy
relacyjne są do siebie podobne na poziomie ogólnego modelu, ale różnią się
w szczegółach technicznych. PostgreSQL daje większe możliwości kontroli typów
danych, pracy serwerowej i administracji. SQLite jest prostszy i wygodny do pracy
lokalnej, ale wymaga uwzględnienia jego ograniczeń. Dlatego projekt fizyczny nie
powinien być traktowany jako automatyczne przepisanie modelu logicznego, tylko
jako dopasowanie rozwiązania do konkretnego silnika bazy danych.

Import danych z pliku CSV pokazał praktyczne znaczenie kluczy obcych, transakcji
i walidacji danych. Jeżeli rekordy są dodawane w złej kolejności albo dane
wejściowe nie są sprawdzane, łatwo doprowadzić do błędów lub częściowo zapisanego
zamówienia. Właśnie dlatego skrypt importujący powinien nie tylko wstawiać dane,
ale też kontrolować ich poprawność i reagować na błędy w przewidywalny sposób.

Zapytania SQL były dobrym sprawdzeniem, czy przygotowany model jest użyteczny.
Na ich podstawie można było uzyskać informacje o zamówieniach, klientach,
sprzedaży, ocenach produktów i kategoriach. To pokazało, że poprawnie
zaprojektowana baza nie powinna jedynie przechowywać danych, ale powinna też
umożliwiać ich sensowną analizę.

Badania literaturowe uzupełniły część projektową o szerszy kontekst utrzymania
baz danych. W praktyce nie wystarczy utworzyć schematu i napisać kilku zapytań.
Trzeba również myśleć o kopiach zapasowych, bezpieczeństwie, monitorowaniu,
diagnostyce, konfiguracji serwera i wydajności. Końcowy wniosek jest taki, że
baza danych jest częścią większego systemu, który trzeba projektować, testować
i utrzymywać w sposób uporządkowany.


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

* `Repozytorium główne <https://github.com/284368user/bazy_danych_glowne_3>`_
