import random
import klasa_enemies
import klasa_effects
import klasa_lokacja
import klasa_farglen
import klasa_eldenhof


du = klasa_lokacja.Dunhollow()
va = klasa_lokacja.Varnak()
th = klasa_lokacja.Thaldras()
li = klasa_lokacja.Lirien()
no = klasa_lokacja.Norheim()
me = klasa_eldenhof.M_eldenhof() 
fa = klasa_farglen.M_farglen()

def walka(akcja=None, pok=None, kok=None):
    import klasa_sigma  
    s = klasa_sigma.Sigma() 
    
    if s.lokacja.nazwa == "Eldenhof":
        pok = random.choice([klasa_enemies.Goblin(), klasa_enemies.Demon()])
    elif s.lokacja.nazwa == "Farglen":
        pok = random.choice([klasa_enemies.Goblin(), klasa_enemies.Demon()])
    elif s.lokacja.nazwa == "Norheim":
        pok = random.choice([klasa_enemies.Spectralny_rycerz(), klasa_enemies.Zagubiony_cien()])
    elif s.lokacja.nazwa == "Lirien":
        pok = random.choice([klasa_enemies.Elficki_Lucznik(), klasa_enemies.Duch_Starego_Drzewa()])
    elif s.lokacja.nazwa == "Thaldras":
        pok = random.choice([klasa_enemies.Krasnoludzki_Wojownik(), klasa_enemies.Kamienny_Golem()])
    elif s.lokacja.nazwa == "Varnak":
        pok = random.choice([klasa_enemies.Pustynny_Skorpion(), klasa_enemies.Ognisty_Szamanka()])
    elif s.lokacja.nazwa == "Dunhollow":
        pok = random.choice([klasa_enemies.Cienisty_Zabojca(), klasa_enemies.Upiorny_Lowiec()])
    else:
        print("Nieznana lokacja, nie można rozpocząć walki.")
        return

    print(f"\n{pok.imie} pojawił się! Ma {pok.hp} HP i {pok.atak} ataku.")
    while pok.czy_zyje() and s.czy_zyje():
        akcja = input("Wybierz akcję: (1) atak zwykły, (2) atak specjalny, (3) użycie potek, (4) zjedzenie grzybka, (5) - ucieczka: ")
        if akcja == "1":
            s.atak_s(pok)
        elif akcja == "2":
            s.specjalny_atak(pok)
        elif akcja == "3":
            s.uzywanie_potek()
        elif akcja == "4":
            s.podejrzliwe(pol=random)
        elif akcja == "5":
            break
        else:
            print("Nieprawidłowa akcja!")

        if pok.czy_zyje():
            if isinstance(pok, (klasa_enemies.Goblin, klasa_enemies.Demon)):
                if random.choice([1, 2]) == 1:
                    pok.atak_s(s)
                else:
                    pok.specjalny_atak(s)
            else:
                pok.atak_s(s)
        else:
            loot_przedmioty, zloto = pok.loot(zloto=100)
            s.zbierz_loot(loot_przedmioty, zloto)

    if s.czy_zyje():
        print(f"{s.imie} wygrał walkę!")
        s.zdobycie_doswiadczenia(20)


def mapa():
    print("        1         10        20        30        40        50")
    print("         |---------|---------|---------|---------|---------|")
    print("         A   ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("         B ▲      Góry Północy      ▲      ▲  * Norheim   ▲")
    print("         C ▲   * Thaldras        ▲ ▲       ▲             ▲")
    print("         D ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲ ♣♣   ♣♣♣♣")
    print("         E ▲   ♣♣   * Eldenhof     ▲   ♣♣♣♣        ♣♣♣♣")
    print("         F ▲   ♣♣♣♣ (Stolica)      ▲   ♣  * Lirien    ♣♣")
    print("         G ▲ ♣♣♣        ♣♣♣♣       ▲     ♣♣♣♣        ♣♣")
    print("         H ▲ ♣  * Narthwood        ▲     ♣♣     ♣♣")
    print("         I ▲   ♣♣  (osada)         ▲  * Dunhollow   ♣♣♣")
    print("         J ▲     ♣♣♣♣             ▲▲   ♣♣♣♣      ♣♣♣")
    print("         K ▲                     ▲       ♣♣♣♣    ♣♣")
    print("         L ▲     * Brumhill      ▲       ♣   * Oakhaven")
    print("         M ▲     (leśne wzg.)    ▲      ♣♣♣♣    (wioska)")
    print("         N ▲                     ▲  ♣♣♣♣       ♣♣♣♣")
    print("         O ▲         * Varnak    ▲       ♣♣♣♣♣♣♣♣")
    print("         P ▲ * Dorun             ▲   ♣♣    ♣♣♣  ♣")
    print("         Q ▲ (handlowe)          ▲  ♣♣♣♣♣      ♣♣♣")
    print("         R ▲    ♣♣               ▲       * Farglen")
    print("         S ▲   ♣♣♣             * Griz     (miasto)")
    print("         T ▲   ♣♣               (kras.)     ♣♣♣♣♣♣♣")
    print("         U ▲                     ▲     ♣♣♣♣♣♣♣♣♣")
    print("         V ▲         * Sahra     ▲         ♣♣♣♣♣♣♣")
    print("         W ▲                     ▲")
    print("         X ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")

def main():
    import klasa_sigma
    s = klasa_sigma.Sigma()  

    while s.czy_zyje():
        print("\nWybierz opcję: a - pokaż statystyki, b - pokaż ekwipunek potek, c - zobacz swoje obecne położenie, d - pokaż mape i zaplanuj podróż, x - zawalcz z mobkami, q - wyjście z gry, r - zobacz lokalne sklepy, e - ekwipunek przedmitów, m - ekwipunek składników, p - użyj potek")
        wybor = input(">> ").lower()
        if wybor == "a":
            print(s.staty())
        elif wybor == "b":
            print(s.ekwipunek_p)
        elif wybor == "c":
            print(s.lokacja_p())
        elif wybor == "d":
            mapa()
        elif wybor == "r":
            print(s.lokacja.sklepy)
            print("który sklep chcesz odwiedzić, jeśli alchemika wpisz a, jeśli kowala wpisz k, jeśli czarny rynek wpisz c, jeśli mag wpisz m")
            lop = input().lower()
            if lop == "a" and "alchemik" in s.lokacja.sklepy:
                print(me.alchemik())
            elif lop == "k":
                print(me.kowal())
            elif lop == "c":
                print(fa.czarny_rynek())
            elif lop == "m":
                print(fa.mag())
        elif wybor == "e":
            s.items()
        elif wybor == "m":
            print(s.ekwipunek_z)
        elif wybor == "x":
            print(walka(akcja=None, kok=random, pok=None))
        elif wybor == "q":
            print("Koniec gry.")
            break
        else:
            print("Nieznana opcja!")

if __name__ == "__main__":
    main()
