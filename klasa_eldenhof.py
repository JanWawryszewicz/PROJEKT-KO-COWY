import random



class M_eldenhof:
    def __init__(self):
        self.nazwa = "Eldenhof"
        self.opis = "Stare miasto handlowe z silnymi murami i wielkim targiem."
        self.populacja = 1200
        self.sklepy = ["alchemik", "kowal"]
        self.zadania = []

    def pokaz_info(self):
        print(f"=== {self.nazwa.upper()} ===")
        print(f"Opis: {self.opis}")
        print(f"Populacja: {self.populacja}")
        print(f"Dostępne sklepy: {', '.join(self.sklepy)}")

    def alchemik(self,s):
        print("Witaj podróżniku, co cię tu sprowadza?")
        print("Pewnie chciałbyś kupić jakieś eliksiry lub składniki do nich, lub móc stworzyć eliksir tu i teraz pod moim czujnym okiem.")
        print("Lepiej nie mogłeś trafić! Tylko tu możesz kupić nerkę goblina oraz zioła z głębin podziemi!")
        pkp = int(input("Wpisz 1 aby kupić potki, 2 aby kupić zioła, 3 aby scraftować potkę, 4 aby zobaczyć regionalne produkty 5 aby wyjść: "))
        while True:
            if pkp == 1:
                print("ACH, mamy ogromny wybór potek od tych życiodajnych po te bardziej tajemnicze :>.")
                print("Aby kupić p_życia kliknij a, p_staminy b, p_ucieczki c, p_teleportacji d, p_śmierci e")
                kp = input().lower()
                if kp == "a" and s.saldo >= 200:
                    ile = int(input("Ile chcesz kupić potek życia? "))
                    koszt = 200 * ile
                    if s.saldo >= koszt:
                        s.saldo -= koszt
                        s.ekwipunek_p["p_zycia(1)"] += ile
                    else:
                        print("Nie masz wystarczająco złota.")
                elif kp == "b" and s.saldo >= 150:
                    ile = int(input("Ile chcesz kupić potek staminy? "))
                    koszt = 150 * ile
                    if s.saldo >= koszt:
                        s.saldo -= koszt
                        s.ekwipunek_p["p_stamina(2)"] += ile
                    else:
                        print("Nie masz wystarczająco złota.")
                elif kp == "c":
                    print("Opcja potek ucieczki nie zaimplementowana.")
                elif kp == "d" and s.saldo >= 400:
                    ile = int(input("Ile chcesz kupić potek teleportacji? "))
                    koszt = 400 * ile
                    if s.saldo >= koszt:
                        s.saldo -= koszt
                        s.ekwipunek_p["p_teleportacji(3)"] += ile
                    else:
                        print("Nie masz wystarczająco złota.")
                elif kp == "e" and s.saldo >= 600:
                    ile = int(input("Ile chcesz kupić potek śmierci? "))
                    koszt = 600 * ile
                    if s.saldo >= koszt:
                        s.saldo -= koszt
                        s.ekwipunek_p["p_smierci(4)"] += ile
                    else:
                        print("Nie masz wystarczająco złota.")
                else:
                    print("Niepoprawny wybór lub brak środków.")

            elif pkp == 2:
                print("Więc chcesz kupić zioła, oto nasz asortyment a może chcesz sprzedac zioła jak tak to klikinij s, jeśli nie to klikinij k:")
                pop = input()
                if pop == "k":
                    print("a - kroplomiecz (30), b - srebroliść (55), c - ciernoliść (45), d - duszobłysk (85), e - jasnorost (55), f - gniewnica (100), g - nocznica (85)")
                    plp = input().lower()
                    if wybor == "a" and s.saldo >= 30:
                        ile = int(input("Ile nerek goblina chcesz kupić? "))
                        if ile * 40 <= s.saldo:
                            s.saldo -= 40 * ile
                            s.ekwipunek_z["kroplomiecz"] += ile
                        else:
                            print("Nie stać Cię na to :(")
                    
                    elif wybor == "b" and s.saldo >= 55:
                        ile = int(input("Ile porcji pyłu duszy chcesz kupić? "))
                        if ile * 70 <= s.saldo:
                            s.saldo -= 70 * ile
                            s.ekwipunek_z["srebrolisc"] += ile
                        else:
                            print("Nie stać Cię na to :(")
                    
                    elif wybor == "c" and s.saldo >= 45:
                        ile = int(input("Ile porcji pyłu duszy chcesz kupić? "))
                        if ile * 70 <= s.saldo:
                            s.saldo -= 70 * ile
                            s.ekwipunek_z["ciernolisc"] += ile
                        else:
                            print("Nie stać Cię na to :(")
                    
                    elif wybor == "d" and s.saldo >= 85:
                        ile = int(input("Ile porcji pyłu duszy chcesz kupić? "))
                        if ile * 70 <= s.saldo:
                            s.saldo -= 70 * ile
                            s.ekwipunek_z["duszoblysk"] += ile
                        else:
                            print("Nie stać Cię na to :(")
                    
                    elif wybor == "e" and s.saldo >= 55:
                        ile = int(input("Ile porcji pyłu duszy chcesz kupić? "))
                        if ile * 70 <= s.saldo:
                            s.saldo -= 70 * ile
                            s.ekwipunek_z["jasnorost"] += ile
                        else:
                            print("Nie stać Cię na to :(")
                    
                    elif wybor == "f" and s.saldo >= 100:
                        ile = int(input("Ile porcji pyłu duszy chcesz kupić? "))
                        if ile * 70 <= s.saldo:
                            s.saldo -= 70 * ile
                            s.ekwipunek_z["gniewnica"] += ile
                        else:
                            print("Nie stać Cię na to :(")
                    
                    elif wybor == "g" and s.saldo >= 85:
                        ile = int(input("Ile porcji pyłu duszy chcesz kupić? "))
                        if ile * 70 <= s.saldo:
                            s.saldo -= 70 * ile
                            s.ekwipunek_z["nocznica"] += ile
                        else:
                            print("Nie stać Cię na to :(")

                elif pop == "s":
                    print("Co chcesz sprzedać?")
                    print("a - kroplomiecz (sprzedaż: 21), b - srebroliść (sprzedaż: 38), c - ciernoliść (sprzedaż: 31),")
                    print("d - duszobłysk (sprzedaż: 59), e - jasnorost (sprzedaż: 38), f - gniewnica (sprzedaż: 70), g - nocznica (sprzedaż: 59)")
                    
                    wybor = input("Wybierz przedmiot do sprzedaży (a-g): ").lower()
                    
                    if wybor == "a" and s.ekwipunek_z.get("kroplomiecz", 0) > 0:
                        ile = int(input("Ile kroplomieczy chcesz sprzedać? "))
                        if ile <= s.ekwipunek_z["kroplomiecz"]:
                            s.ekwipunek_z["kroplomiecz"] -= ile
                            s.saldo += 21 * ile
                            print(f"Sprzedałeś {ile}x kroplomiecz za {21 * ile} złota.")
                        else:
                            print("Nie masz tylu kroplomieczy!")

                    elif wybor == "b" and s.ekwipunek_z.get("srebrolisc", 0) > 0:
                        ile = int(input("Ile srebrolistów chcesz sprzedać? "))
                        if ile <= s.ekwipunek_z["srebrolisc"]:
                            s.ekwipunek_z["srebrolisc"] -= ile
                            s.saldo += 38 * ile
                            print(f"Sprzedałeś {ile}x srebrolist za {38 * ile} złota.")
                        else:
                            print("Nie masz tylu srebrolistów!")

                    elif wybor == "c" and s.ekwipunek_z.get("ciernolisc", 0) > 0:
                        ile = int(input("Ile ciernolistów chcesz sprzedać? "))
                        if ile <= s.ekwipunek_z["ciernolisc"]:
                            s.ekwipunek_z["ciernolisc"] -= ile
                            s.saldo += 31 * ile
                            print(f"Sprzedałeś {ile}x ciernolisc za {31 * ile} złota.")
                        else:
                            print("Nie masz tylu ciernolistów!")

                    elif wybor == "d" and s.ekwipunek_z.get("duszoblysk", 0) > 0:
                        ile = int(input("Ile duszobłysków chcesz sprzedać? "))
                        if ile <= s.ekwipunek_z["duszoblysk"]:
                            s.ekwipunek_z["duszoblysk"] -= ile
                            s.saldo += 59 * ile
                            print(f"Sprzedałeś {ile}x duszobłysk za {59 * ile} złota.")
                        else:
                            print("Nie masz tylu duszobłysków!")

                    elif wybor == "e" and s.ekwipunek_z.get("jasnorost", 0) > 0:
                        ile = int(input("Ile jasnorostów chcesz sprzedać? "))
                        if ile <= s.ekwipunek_z["jasnorost"]:
                            s.ekwipunek_z["jasnorost"] -= ile
                            s.saldo += 38 * ile
                            print(f"Sprzedałeś {ile}x jasnorost za {38 * ile} złota.")
                        else:
                            print("Nie masz tylu jasnorostów!")

                    elif wybor == "f" and s.ekwipunek_z.get("gniewnica", 0) > 0:
                        ile = int(input("Ile gniewnic chcesz sprzedać? "))
                        if ile <= s.ekwipunek_z["gniewnica"]:
                            s.ekwipunek_z["gniewnica"] -= ile
                            s.saldo += 70 * ile
                            print(f"Sprzedałeś {ile}x gniewnica za {70 * ile} złota.")
                        else:
                            print("Nie masz tylu gniewnic!")

                    elif wybor == "g" and s.ekwipunek_z.get("nocznica", 0) > 0:
                        ile = int(input("Ile nocznic chcesz sprzedać? "))
                        if ile <= s.ekwipunek_z["nocznica"]:
                            s.ekwipunek_z["nocznica"] -= ile
                            s.saldo += 59 * ile
                            print(f"Sprzedałeś {ile}x nocznica za {59 * ile} złota.")
                        else:
                            print("Nie masz tylu nocznic!")

                    else:
                        print("Nie masz tego przedmiotu lub wybrałeś błędnie.")
            elif pkp == 4:
                print("Witaj w alchemicznym sklepie Endelhof! Oto nasze lokalne produkty a może chcesz je sprzedac jak tak to kliknij s jeśli nie to kliknij k:")
                popy = input()
                if popy == "k":
                    print("Wybierz: a - nerka goblina (40), b - pył duszy (70), c - ciecz z liszaja (55),d - sok z żyłorośli (90), e - kość wróżki (120), f - skrystalizowany jad (80)")

                    wybor = input().lower()

                    if wybor == "a" and s.saldo >= 40:
                        ile = int(input("Ile nerek goblina chcesz kupić? "))
                        if ile * 40 <= s.saldo:
                            s.saldo -= 40 * ile
                            s.ekwipunek_z["nerka_goblina"] += ile
                        else:
                            print("Nie stać Cię na to :(")

                    elif wybor == "b" and s.saldo >= 70:
                        ile = int(input("Ile porcji pyłu duszy chcesz kupić? "))
                        if ile * 70 <= s.saldo:
                            s.saldo -= 70 * ile
                            s.ekwipunek_z["pyl_duszy"] += ile
                        else:
                            print("Nie stać Cię na to :(")

                    elif wybor == "c" and s.saldo >= 55:
                        ile = int(input("Ile jednostek cieczy z liszaja chcesz kupić? "))
                        if ile * 55 <= s.saldo:
                            s.saldo -= 55 * ile
                            s.ekwipunek_z["ciecz_liszaj"] += ile
                        else:
                            print("Nie stać Cię na to :(")

                    elif wybor == "d" and s.saldo >= 90:
                        ile = int(input("Ile butelek soku z żyłorośli chcesz kupić? "))
                        if ile * 90 <= s.saldo:
                            s.saldo -= 90 * ile
                            s.ekwipunek_z["sok_zylorosl"] += ile
                        else:
                            print("Nie stać Cię na to :(")

                    elif wybor == "e" and s.saldo >= 120:
                        ile = int(input("Ile kości wróżki chcesz kupić? "))
                        if ile * 120 <= s.saldo:
                            s.saldo -= 120 * ile
                            s.ekwipunek_z["kosc_wrozki"] += ile
                        else:
                            print("Nie stać Cię na to :(")

                    elif wybor == "f" and s.saldo >= 80:
                        ile = int(input("Ile jednostek skrystalizowanego jadu chcesz kupić? "))
                        if ile * 80 <= s.saldo:
                            s.saldo -= 80 * ile
                            s.ekwipunek_z["jad_skrystalizowany"] += ile
                        else:
                            print("Nie stać Cię na to :(")

                    else:
                        print("Niepoprawny wybór lub za mało złota.")
                elif popy == "s":
                        print("Co chcesz sprzedać?")
                        print("a - nerka goblina (sprzedaż: 28), b - pył duszy (sprzedaż: 49), c - ciecz z liszaja (sprzedaż: 38),")
                        print("d - sok z żyłorośli (sprzedaż: 63), e - kość wróżki (sprzedaż: 84), f - skrystalizowany jad (sprzedaż: 56)")

                        wybor = input("Wybierz składnik do sprzedaży (a-f): ").lower()

                        if wybor == "a" and s.ekwipunek_z.get("nerka_goblina", 0) > 0:
                            ile = int(input("Ile nerek goblina chcesz sprzedać? "))
                            if ile <= s.ekwipunek_z["nerka_goblina"]:
                                s.ekwipunek_z["nerka_goblina"] -= ile
                                s.saldo += 28 * ile
                                print(f"Sprzedałeś {ile}x nerka goblina za {28 * ile} złota.")
                            else:
                                print("Nie masz tylu nerek goblina!")

                        elif wybor == "b" and s.ekwipunek_z.get("pyl_duszy", 0) > 0:
                            ile = int(input("Ile porcji pyłu duszy chcesz sprzedać? "))
                            if ile <= s.ekwipunek_z["pyl_duszy"]:
                                s.ekwipunek_z["pyl_duszy"] -= ile
                                s.saldo += 49 * ile
                                print(f"Sprzedałeś {ile}x pył duszy za {49 * ile} złota.")
                            else:
                                print("Nie masz tylu porcji pyłu duszy!")

                        elif wybor == "c" and s.ekwipunek_z.get("ciecz_liszaj", 0) > 0:
                            ile = int(input("Ile jednostek cieczy z liszaja chcesz sprzedać? "))
                            if ile <= s.ekwipunek_z["ciecz_liszaj"]:
                                s.ekwipunek_z["ciecz_liszaj"] -= ile
                                s.saldo += 38 * ile
                                print(f"Sprzedałeś {ile}x ciecz z liszaja za {38 * ile} złota.")
                            else:
                                print("Nie masz tylu jednostek cieczy!")

                        elif wybor == "d" and s.ekwipunek_z.get("sok_zylorosl", 0) > 0:
                            ile = int(input("Ile butelek soku z żyłorośli chcesz sprzedać? "))
                            if ile <= s.ekwipunek_z["sok_zylorosl"]:
                                s.ekwipunek_z["sok_zylorosl"] -= ile
                                s.saldo += 63 * ile
                                print(f"Sprzedałeś {ile}x sok z żyłorośli za {63 * ile} złota.")
                            else:
                                print("Nie masz tylu butelek!")

                        elif wybor == "e" and s.ekwipunek_z.get("kosc_wrozki", 0) > 0:
                            ile = int(input("Ile kości wróżki chcesz sprzedać? "))
                            if ile <= s.ekwipunek_z["kosc_wrozki"]:
                                s.ekwipunek_z["kosc_wrozki"] -= ile
                                s.saldo += 84 * ile
                                print(f"Sprzedałeś {ile}x kość wróżki za {84 * ile} złota.")
                            else:
                                print("Nie masz tylu kości wróżki!")

                        elif wybor == "f" and s.ekwipunek_z.get("jad_skrystalizowany", 0) > 0:
                            ile = int(input("Ile jednostek skrystalizowanego jadu chcesz sprzedać? "))
                            if ile <= s.ekwipunek_z["jad_skrystalizowany"]:
                                s.ekwipunek_z["jad_skrystalizowany"] -= ile
                                s.saldo += 56 * ile
                                print(f"Sprzedałeś {ile}x skrystalizowany jad za {56 * ile} złota.")
                            else:
                                print("Nie masz tylu jednostek jadu!")

                        else:
                            print("Nie masz tego składnika lub podałeś zły wybór.")
            
            if pkp == 3:
                print("Dostępne eliksiry do stworzenia:")
                print("a - Eliksir życia (kroplomiecz + jasnorost)\nb - Eliksir staminy (nocznica + gniewnica)\nc - Eliksir trucizny (ciecz liszaja + jad skrystalizowany)")
                wybor_potki = input("Wybierz eliksir: ").lower()

                receptury = {
                    "a": {"nazwa": "p_zycia(1)", "skladniki": {"kroplomiecz": 1, "jasnorost": 1}},
                    "b": {"nazwa": "p_stamina(2)", "skladniki": {"nocznica": 1, "gniewnica": 1}},
                    "c": {"nazwa": "p_trucizna", "skladniki": {"ciecz_liszaj": 1, "jad_skrystalizowany": 1}}
                }

                if wybor_potki in receptury:
                    przepis = receptury[wybor_potki]
                    skladniki = przepis["skladniki"]

                    if all(s.ekwipunek_z.get(skladnik, 0) >= ilosc for skladnik, ilosc in skladniki.items()):
                        for skladnik, ilosc in skladniki.items():
                            s.ekwipunek_z[skladnik] -= ilosc
                        s.ekwipunek[przepis["nazwa"]] += 1
                        print(f"Udało się stworzyć {przepis['nazwa']}!")
                    else:
                        print("Brakuje składników!")
                else:
                    print("Nie ma takiego eliksiru.")
            elif pkp == 5:
                break
            else:
                print("nie ma takiej komendy")
    def kowal(self,s):
        while True:
            print("Witaj podróżniku! Co cię tu sprowadza?")
            print("Pewnie chciałbyś kupić jakieś bronie lub zbroje, lub móc stworzyć coś pod moim czujnym okiem. Lepiej nie mogłeś trafić!")
            pkp = int(input("Wpisz 1 aby kupić broń, 2 aby kupić zbroję, 3 aby stworzyć przedmiot, 4 aby zobaczyć lokalne materiały 5 aby wyjść: "))
            
            if pkp == 1:
                print("ACH, mamy ogromny wybór broni od mieczy po topory.")
                print("Aby kupić miecz kliknij a, aby kupić topór kliknij b, c aby kupić łuk.")
                kp = input().lower()
                if kp == "a" and s.saldo >= 300:
                    ile = int(input("Ile chcesz kupić mieczy? "))
                    s.saldo -= 300 * ile
                    s.ekwipunek["miecz"] += ile
                
                elif kp == "b" and s.saldo >= 400:
                    ile = int(input("Ile chcesz kupić toporów? "))
                    s.saldo -= 400 * ile
                    s.ekwipunek["topor"] += ile
                
                elif kp == "c" and s.saldo >= 250:
                    ile = int(input("Ile chcesz kupić łuków? "))
                    s.saldo -= 250 * ile
                    s.ekwipunek["łuk"] += ile
            
            elif pkp == 2:
                print("Więc chcesz kupić zbroje? Oto nasz asortyment.")
                print("Wybierz a - zbroja skórzana, b - zbroja stalowa, c - zbroja płytowa.")
                plp = input().lower()
                if plp == "a" and s.saldo >= 150:
                    pile = int(input("Ile chcesz kupić zbroi skórzanych? "))
                    s.saldo -= 150 * pile
                    s.ekwipunek["zbroja_skórzana"] += pile
                elif plp == "b" and s.saldo >= 300:
                    pile = int(input("Ile chcesz kupić zbroi stalowych? "))
                    s.saldo -= 300 * pile
                    s.ekwipunek["zbroja_stalowa"] += pile
                elif plp == "c" and s.saldo >= 500:
                    pile = int(input("Ile chcesz kupić zbroi płytowych? "))
                    s.saldo -= 500 * pile
                    s.ekwipunek["zbroja_płytowa"] += pile
            
            elif pkp == 4:
                print("Witaj w kowalni Eldenhof! Oto nasze lokalne materiały:")
                print("Wybierz: a - stal (50), b - drewno (30), c - skóra (20), d - żelazo (40)")

                wybor = input().lower()

                if wybor == "a" and s.saldo >= 50:
                    ile = int(input("Ile jednostek stali chcesz kupić? "))
                    if ile * 50 <= s.saldo:
                        s.saldo -= 50 * ile
                        s.ekwipunek_z["stal"] += ile
                    else:
                        print("Nie stać Cię na to :(")

                elif wybor == "b" and s.saldo >= 30:
                    ile = int(input("Ile jednostek drewna chcesz kupić? "))
                    if ile * 30 <= s.saldo:
                        s.saldo -= 30 * ile
                        s.ekwipunek_z["drewno"] += ile
                    else:
                        print("Nie stać Cię na to :(")

                elif wybor == "c" and s.saldo >= 20:
                    ile = int(input("Ile jednostek skóry chcesz kupić? "))
                    if ile * 20 <= s.saldo:
                        s.saldo -= 20 * ile
                        s.ekwipunek_z["skóra"] += ile
                    else:
                        print("Nie stać Cię na to :(")

                elif wybor == "d" and s.saldo >= 40:
                    ile = int(input("Ile jednostek żelaza chcesz kupić? "))
                    if ile * 40 <= s.saldo:
                        s.saldo -= 40 * ile
                        s.ekwipunek_z["żelazo"] += ile
                    else:
                        print("Nie stać Cię na to :(")

            elif pkp == 3:
                print("Dostępne przedmioty do stworzenia:")
                print("a - Miecz (stal + drewno)\nb - Zbroja (skóra + stal)\nc - Topór (żelazo + drewno)")
                wybor_przedmiotu = input("Wybierz przedmiot: ").lower()

                receptury = {
                    "a": {"nazwa": "miecz", "skladniki": {"stal": 1, "drewno": 1}},
                    "b": {"nazwa": "zbroja", "skladniki": {"skóra": 2, "stal": 1}},
                    "c": {"nazwa": "topór", "skladniki": {"żelazo": 1, "drewno": 1}}
                }

                if wybor_przedmiotu in receptury:
                    przepis = receptury[wybor_przedmiotu]
                    skladniki = przepis["skladniki"]

                    if all(s.ekwipunek_z.get(skladnik, 0) >= ilosc for skladnik, ilosc in skladniki.items()):
                        for skladnik, ilosc in skladniki.items():
                            s.ekwipunek_z[skladnik] -= ilosc
                        s.ekwipunek[przepis["nazwa"]] += 1
                        print(f"Udało się stworzyć {przepis['nazwa']}!")
                    else:
                        print("Brakuje składników!")
                else:
                    print("Nie ma takiego przedmiotu.")
            elif pkp == 5:
                break
            else:
                print("nie ma takiej komendy")
