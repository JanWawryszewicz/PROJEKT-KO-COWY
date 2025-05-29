import random


class Enemy:
    def __init__(self):
        self.hp = 40
        self.atak = 5
        self.zyje = True
        self.imie = "Nieznany wróg"
        self.s_p = ""
    def odejmij_hp(self, a):
        self.hp -= a
        if self.hp <= 0:
            self.hp = 0
            self.zyje = False
            print(f"{self.imie} zginął!")

    def czy_zyje(self):
        return self.zyje

    def atak_s(self, target):
        damage = random.randint(self.atak, self.atak+5)
        print(f"{self.imie} atakuje! Zadaje {damage} obrażeń.")
        target.odejmij_hp(damage)
    
    def loot(self,zloto):
        loot_przedmioty = {"złoto": 100, self.s_p:1}
        zloto = 100
        return loot_przedmioty, zloto


class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 60
        self.atak = 8
        self.imie = "Goblin"
        self.s_p = "nerka_goblina"
    def specjalny_atak(self, target):
        damage1 = random.randint(3, 6)
        damage2 = random.randint(3, 6)
        print(f"{self.imie} wykonuje szybki podwójny atak! {damage1} + {damage2} obrażeń!")

class Demon(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.atak = 15
        self.imie = "Demon"
        self.s_p = "gniewnica"
    def specjalny_atak(self, target):
        damage = random.randint(10, 20)
        print(f"{self.imie} wykonuje potężny atak! Zadaje {damage} obrażeń.")
        target.odejmij_hp(damage)

class Spectralny_rycerz(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 75
        self.atak = 20
        self.imie = "Spectralny_rycerz"
        self.s_p = "kroplomiecz"

class Zagubiony_cien(Enemy):
    def __init__(self):
        super().__init__()
        self.hp=80
        self.atak=15
        self.imie = "Zagubiony Cień"
        self.s_p = "esencja_cienia"
class Elficki_Lucznik(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 60
        self.atak = 18
        self.imie = "Elficki Łucznik"
        self.s_p = "srebrolisc"

class Duch_Starego_Drzewa(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 80
        self.atak = 15
        self.imie = "Duch Starego Drzewa"
        self.s_p = "jasnorost"

class Krasnoludzki_Wojownik(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.atak = 22
        self.imie = "Krasnoludzki Wojownik"
        self.s_p = "stal"

class Kamienny_Golem(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 120
        self.atak = 16
        self.imie = "Kamienny Golem"
        self.s_p = "zalazo"

class Pustynny_Skorpion(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 70
        self.atak = 25
        self.imie = "Pustynny Skorpion"
        self.s_p = "jad_skrystalizowany"

class Ognisty_Szamanka(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 65
        self.atak = 30
        self.imie = "Ognisty Szamanka"
        self.s_p = "kosc_wrozki"

class Cienisty_Zabojca(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 85
        self.atak = 27
        self.imie = "Cienisty Zabójca"
        self.s_p = "pyl_duszy"

class Upiorny_Lowiec(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 90
        self.atak = 23
        self.imie = "Upiorny Łowiec"
        self.s_p = "ciernolisc"
