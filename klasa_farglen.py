import random

import klasa_eldenhof

class M_farglen(klasa_eldenhof.M_eldenhof):
    def __init__(self):
        super().__init__()
        self.nazwa = "Eldenhof"
        self.opis = "Dobrze skomunikowane miasto z krasnoludami i innymi miastami."
        self.populacja = 800
        self.sklepy = ["czarny rynek, mag"]
        self.zadania = []
    
    def czarny_rynek(s):
        while True:
            print("Witaj w czarnym rynku... Ciszej, nie każdy musi wiedzieć, że tu jesteś.")
            print("Mam tu kilka nietypowych towarów zakazane artefakty, rzadkie składniki, no i oczywiście... broń.")
            pkp = int(input("Wpisz 1 aby kupić zakazaną broń, 2 aby kupić rzadkie składniki, 3 aby stworzyć tajny przedmiot 4 aby wyjść: "))

            if pkp == 1:
                print("Dostępna broń: a - bomba (800), b - shurikeny (700), c - opetana_kaczka (1000)")
                kp = input().lower()
                if kp == "a" and s.saldo >= 800:
                    ile = int(input("Ile bomb chcesz kupić? "))
                    s.saldo -= 800 * ile
                    s.ekwipunek_z["bomba"] += ile
                elif kp == "b" and s.saldo >= 700:
                    ile = int(input("Ile shurikenów chcesz kupić? "))
                    s.saldo -= 700 * ile
                    s.ekwipunek_z["shuriken"] += ile
                elif kp == "c" and s.saldo >= 1000:
                    ile = int(input("Ile opentanych kaczek chcesz kupić? "))
                    s.saldo -= 1000 * ile
                    s.ekwipunek_z["opetana_kaczka"] += ile
                else:
                    print("Nie stać Cię albo nieprawidłowy wybór.")

            elif pkp == 2:
                print("Rzadkie składniki: a - Jad skrystalizowany (500), b - Pyl duszy (300), c - Nerka goblina (200)")
                wybor = input().lower()

                if wybor == "a" and s.saldo >= 500:
                    ile = int(input("Ile jadu chcesz kupić? "))
                    s.saldo -= 500 * ile
                    s.ekwipunek_z["jad_skrystalizowany"] += ile
                elif wybor == "b" and s.saldo >= 300:
                    ile = int(input("Ile pyłu duszy chcesz kupić? "))
                    s.saldo -= 300 * ile
                    s.ekwipunek_z["pyl_duszy"] += ile
                elif wybor == "c" and s.saldo >= 200:
                    ile = int(input("Ile nerek goblina chcesz kupić? "))
                    s.saldo -= 200 * ile
                    s.ekwipunek_z["nerka_goblina"] += ile
                else:
                    print("Nie masz wystarczająco złota albo zły wybór.")

            elif pkp == 3:
                print("Tajne przedmioty do stworzenia: a - Sztylet Cienia (jad + stal), b - Maska Złodzieja (skóra + pyl duszy)")
                wybor = input("Wybierz przedmiot: ").lower()

                receptury = {
                    "a": {"nazwa": "sztylet_cienia", "skladniki": {"jad_skrystalizowany": 1, "stal": 1}},
                    "b": {"nazwa": "maska_zlodzieja", "skladniki": {"skóra": 1, "pyl_duszy": 1}}
                }

                if wybor in receptury:
                    przepis = receptury[wybor]
                    if all(s.ekwipunek_z.get(skladnik, 0) >= ilosc for skladnik, ilosc in przepis["skladniki"].items()):
                        for skladnik, ilosc in przepis["skladniki"].items():
                            s.ekwipunek_z[skladnik] -= ilosc
                        s.ekwipunek_z[przepis["nazwa"]] = s.ekwipunek_z.get(przepis["nazwa"], 0) + 1
                        print(f"Stworzyłeś {przepis['nazwa']}!")
                    else:
                        print("Brakuje ci składników.")
                else:
                    print("Nieprawidłowy wybór.")
            elif pkp == 4:
                break
            else:
                print("Nie znam takiej opcji.")
    
    
    def mag(s):
        while True:
            print("Witaj, śmiertelniku... Twoja aura jest... intrygująca.")
            print("Czego pragniesz? Wiedzy zaklętej w zwojach? Mistycznych esencji? A może chcesz stworzyć coś wyjątkowego?")
            pkp = int(input("Wpisz 1 aby kupić zaklęcia, 2 aby kupić komponenty magiczne, 3 aby stworzyć magiczny przedmiot 4 aby wyjść: "))

            if pkp == 1:
                print("Dostępne zaklęcia: a - Kula Ognia (500), b - Lodowy Pocisk (400), c - Leczenie (350)")
                kp = input().lower()
                if kp == "a" and s.saldo >= 500:
                    ile = int(input("Ile zwojów Kuli Ognia chcesz kupić? "))
                    s.saldo -= 500 * ile
                    s.ekwipunek_z["kula_ognia"] += ile
                elif kp == "b" and s.saldo >= 400:
                    ile = int(input("Ile zwojów Lodowego Pocisku chcesz kupić? "))
                    s.saldo -= 400 * ile
                    s.ekwipunek_z["lodowy_pocisk"] += ile
                elif kp == "c" and s.saldo >= 350:
                    ile = int(input("Ile zwojów Leczenia chcesz kupić? "))
                    s.saldo -= 350 * ile
                    s.ekwipunek_z["leczenie"] += ile
                else:
                    print("Nie stać Cię albo nieprawidłowy wybór.")

            elif pkp == 2:
                print("Komponenty magiczne: a - Kryształ Many (300), b - Esencja Cienia (250), c - Pył Feniksa (600)")
                wybor = input().lower()

                if wybor == "a" and s.saldo >= 300:
                    ile = int(input("Ile Kryształów Many chcesz kupić? "))
                    s.saldo -= 300 * ile
                    s.ekwipunek_z["krysztal_many"] += ile
                elif wybor == "b" and s.saldo >= 250:
                    ile = int(input("Ile Esencji Cienia chcesz kupić? "))
                    s.saldo -= 250 * ile
                    s.ekwipunek_z["esencja_cienia"] += ile
                elif wybor == "c" and s.saldo >= 600:
                    ile = int(input("Ile Pyłu Feniksa chcesz kupić? "))
                    s.saldo -= 600 * ile
                    s.ekwipunek_z["pyl_feniksa"] += ile
                else:
                    print("Nie masz wystarczająco złota albo zły wybór.")

            elif pkp == 3:
                print("Dostępne przedmioty magiczne do stworzenia:")
                print("a - Różdżka Ognia (kryształ many + kula ognia)")
                print("b - Amulet Cieni (esencja cienia + lodowy pocisk)")
                print("c - Pierścień Odrodzenia (pył feniksa + leczenie)")
                wybor = input("Wybierz przedmiot: ").lower()

                receptury = {
                    "a": {"nazwa": "rozdzka_ognia", "skladniki": {"krysztal_many": 1, "kula_ognia": 1}},
                    "b": {"nazwa": "amulet_cieni", "skladniki": {"esencja_cienia": 1, "lodowy_pocisk": 1}},
                    "c": {"nazwa": "pierscien_odrodzenia", "skladniki": {"pyl_feniksa": 1, "leczenie": 1}},
                }

                if wybor in receptury:
                    przepis = receptury[wybor]
                    if all(s.ekwipunek_z.get(skladnik, 0) >= ilosc for skladnik, ilosc in przepis["skladniki"].items()):
                        for skladnik, ilosc in przepis["skladniki"].items():
                            s.ekwipunek_z[skladnik] -= ilosc
                        s.ekwipunek_z[przepis["nazwa"]] = s.ekwipunek_z.get(przepis["nazwa"], 0) + 1
                        print(f"Stworzyłeś {przepis['nazwa']}!")
                    else:
                        print("Brakuje ci składników.")
                else:
                    print("Nieprawidłowy wybór.")
            elif pkp == 4:
                break
            else:
                print("Nie znam takiej opcji.")

class M_oakhaven(M_farglen):
    def __init__(self):
        super().__init__()
        self.nazwa = "Oakhaven"
        self.opis = "Wioska położona niedaleko  wybrzeża ."
        self.populacja = 800
        self.sklepy = ["kowal","czarny_rynek"]
        self.zadania = []
