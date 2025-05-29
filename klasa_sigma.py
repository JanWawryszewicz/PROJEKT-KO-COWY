import random
import klasa_effects
import klasa_lokacja
import klasa_eldenhof
import klasa_g
import klasa_farglen

class Sigma:
    def __init__(self):
        self.hp = 100
        self.maxhp = 100
        self.atak = 10
        self.zyje = True
        self.imie = "Sigma"
        self.stamina = 100
        self.maxstamina = 115
        self.doswiadczenie = 0
        self.ekwipunek_p = {
            "p_zycia(1)": 1, "p_stamina(2)": 0, "p_teleportacji(3)": 10,
            "p_smierci(4)": 0, "p_many(5)": 0, "bomba(6)": 0,
            "shuriken(7)": 0, "opetana_kaczka(8)": 0
        }
        self.ekwipunek_z = {
            "kroplomiecz": 0, "srebrolisc": 0, "ciernolisc": 0, "duszoblysk": 0,
            "jasnorost": 0, "gniewnica": 0, "nocznica": 0,
            "nerka_goblina": 0, "pyl_duszy": 0, "ciecz_liszaj": 0,
            "sok_zylorosl": 0, "kosc_wrozki": 0, "jad_skrystalizowany": 0,
            "stal": 0, "drewno": 0, "skora": 0, "zelazo": 0,
            "krysztal_many": 0, "esencja_cienia": 0, "pyl_feniksa": 0,
        }
        self.ekwipunek_zb = {
            "miecz": 1, "topor": 1, "luk": 1,
            "zbroja_skorzana": 1, "zbroja_stalowa": 1, "zbroja_plytowa": 1,
            "rozdzka_ognia": 1, "amulet_cieni": 1, "pierscien_odrodzenia": 1,
        }
        self.saldo = 1000000
        self.poziom = 0
        self.wymagany_poziom = 40
        self.magiczne_ataki = []
        self.mana = 100
        self.maxmana = 150
        self.lokacja = klasa_eldenhof.M_eldenhof()
        self.status_effects = []
    
    def podejrzliwe(self,pol):
        print("znajdujesz podejrzango grzybka i go jesz dostajesz efekt")
        pol = random.choice([1,2])
        if pol == 1:
            s.status_effects.append(klasa_effects.StatusEffect("Zatrucie", duration=3, apply_effect=klasa_effects.StatusEffect.poison(s)))
        elif pol == 2:
            s.status_effects.append(klasa_effects.StatusEffect("buff_attack", duration=3, apply_effect=klasa_effects.StatusEffect.buff_attack(s)))
    
    def dodawanie_efektow(self):
        for effect in self.status_effects[:]:
            effect.trigger(self)
            if effect.is_expired():
                print(f"Efekt {effect.name} wygasł.")
            self.status_effects.remove(effect)
    def lokacja_p(self):
        return self.lokacja.nazwa
    
    def items(self):
        print(self.ekwipunek_zb)
        while True:
            kl = {"p_reka": 0, "l_reka": 0, "zbroja": 0, "palec":0, "szyja":0}
            pk = input("Podaj co chcesz założyć, 1 - miecz, 2 - topór, 3 - łuk, 4 - zbroja, 5 - pierścień odrodzenia, 6 - amulet cienia,7 - różdżka ognia, 8 - wyjście: ")
            if pk == "1":
                print("Możesz tu założyć miecz")
                if self.ekwipunek_zb.get("miecz", 0) >= 1:
                    print("Na która ręke chcesz założyć, 1 - prawa, 2 - lewa")
                    kkk = input(">> ")
                    if kkk == "1" and kl["p_reka"]<1:
                        kl["p_reka"]+=1
                        self.ekwipunek_zb["miecz"]-=1
                        self.atak+=15
                    elif kkk == "2" and kl("l_reka",0)<1:
                        kl["l_reka"]+=1
                        self.ekwipunek_zb["miecz"]-=1
                        self.atak+=15
                    else:
                        print("co łapek zabrakło ?????")
                        continue
                else:
                    print("nie masz żadnego miecz oszuście!!!!!")
                    continue
            elif pk == "2":
                print("Możesz tu założyć topór")
                if self.ekwipunek_zb.get("miecz", 0) >= 1:
                    print("Na która ręke chcesz założyć, 1 - prawa, 2 - lewa")
                    kkk = input(">> ")
                    if kkk == "1" and kl["p_reka"]<1:
                        kl["p_reka"]+=1
                        self.ekwipunek_zb["topor"]-=1
                        self.atak+=25
                        self.maxhp-=15
                    elif kkk == "2" and kl("l_reka",0)<1:
                        kl["l_reka"]+=1
                        self.ekwipunek_zb["topor"]-=1
                        self.atak+=25
                        self.maxhp-=15
                    else:
                        print("co łapek zabrakło ?????")
                        continue
                else:
                    print("nie masz żadnego toporu oszuście!!!!!")
                    continue
            elif pk == "3":
                print("Możesz tu założyć łuk")
                if self.ekwipunek_zb.get("luk", 0) >= 1:
                    print("Na która ręke chcesz założyć, 1 - prawa, 2 - lewa")
                    kkk = input(">> ")
                    if kkk == "1" and kl("p_reka",0)<1:
                        kl["p_reka"]+=1
                        self.ekwipunek_zb["luk"]-=1
                        self.atak+=10
                        self.maxhp+=5
                    elif kkk == "2" and kl("l_reka",0)<1:
                        kl["l_reka"]+=1
                        self.ekwipunek_zb["luk"]-=1
                        self.atak+=10
                        self.maxhp+=5
                    else:
                        print("co łapek zabrakło ?????")
                        continue
                else:
                    print("nie masz żadnego łuku oszuście!!!!!")
                    continue
            
            elif pk == "4":
                print("możesz założyć tu zbroje")
                if self.ekwipunek_zb("zbroja_skorzana",0)>=1 or self.ekwipunek_zb("zbroja_stalowa")>=1 or self.ekwipunek_zb("zbroja_plytowa")>=1:
                    if kl("zbroja")<1:
                        print("którą zbroję chcesz założyć, 1 - skórzana, 2 - stalowa, 3 - płytowa")
                        kolo = input()
                        if kolo == 1 and self.ekwipunek_zb["zbroja_skorzana"]>=1:
                            kl["zbroja"]+=1
                            self.ekwipunek_zb["zbroja_skorzana"]-=1
                            self.maxhp+=25
                        elif kolo == 2 and self.ekwipunek_zb["zbroja_stalowa"]>=1:
                            kl["zbroja"]+=1
                            self.ekwipunek_zb["zbroja_stalowa"]-=1
                            self.maxhp+=40
                        elif kolo == 3 and self.ekwipunek_zb["zbroja_plytowa"]>=1:
                            kl["zbroja"]+=1
                            self.ekwipunek_zb["zbroja_plytowa"]-=1
                            self.maxhp+=70
                        else:
                            print("co łapek zabrakło ?????")
                            continue
                    else:
                        print("nie masz żadnej zbroi oszuście!!!!!")
                        continue

            elif pk == "5":
                if self.ekwipunek_zb.get("pierscien_odrodzenia", 0) >= 1:
                    print("Jesteś pewnien że chcesz go założyc jeśli tak to kliknij 1 jeśli nie to kliknij 2 ")
                    kkk = input(">> ")
                    if kkk == "1" and kl("palec",0)<1:
                        kl["palec"]+=1
                        self.ekwipunek_zb["pierscien_odrodzenia"]-=1
                        self.atak+=30
                        self.maxhp+=50
                    else:
                        print("co łapek zabrakło ?????")
                        continue
                else:
                    print("nie masz żadnego pierścienia oszuście!!!!!")
                    continue

            elif pk == "6":
                if self.ekwipunek_zb.get("amulet_cieni", 0) >= 1:
                    print("Jesteś pewnien że chcesz go założyc jeśli tak to kliknij 1 jeśli nie to kliknij 2 ")
                    kkk = input(">> ")
                    if kkk == "1" and kl("szyja",0)<1:
                        kl["szyja"]+=1
                        self.ekwipunek_zb["amulet_cieni"]-=1
                        self.atak+=25
                        self.maxhp+=30
                    else:
                        print("co łapek zabrakło ?????")
                        continue
                else:
                    print("nie masz żadnego amuletu oszuście!!!!!")
                    continue
            
            elif pk == "7":
                print("Możesz tu założyć różdżka")
                if self.ekwipunek_zb.get("rozdzka_ognia", 0) >= 1:
                    print("Na która ręke chcesz założyć, 1 - prawa, 2 - lewa")
                    kkk = input(">> ")
                    if kkk == "1" and kl("p_reka",0)<1:
                        kl["p_reka"]+=1
                        self.ekwipunek_zb["rozdzka_ognia"]-=1
                        self.atak+=10
                        self.hp+=5
                    elif kkk == "2" and kl("l_reka",0)<1:
                        kl["l_reka"]+=1
                        self.ekwipunek_zb["rozdzka_ognia"]-=1
                        self.atak+=10
                        self.maxhp+=5
                    else:
                        print("co łapek zabrakło ?????")
                        continue
                else:
                    print("nie masz żadnej różdżki oszuście!!!!!")
                    continue
            elif pk == "8":
                break
    
    def levelowanie(self):
        if self.doswiadczenie >= self.wymagany_poziom:
            print(f"zdobyłeś nowy POZIOM !!!!!!!! to twój {self.poziom} poziom")
            self.poziom += 1
            self.wymagany_poziom *= 2  
            self.maxhp += 5
            self.maxstamina += 10

    def staty(self):
        return (f"hp = {self.hp}, max hp = {self.maxhp}, atak = {self.atak}, imie = {self.imie}, "
                f"stamina = {self.stamina}, max stamina = {self.maxstamina}, doswiadczenie = {self.doswiadczenie}, saldo = {self.saldo}")

    def uzywanie_potek(self):
        print("Aby użyć wybranej potki wpisz numer znajdujący się obok niej")
        print(self.ekwipunek_p)
        ppp = int(input(">> "))
        if ppp == 1 and self.ekwipunek_p.get("p_zycia(1)", 0) >= 1:
            if self.hp == self.maxhp:
                print("Masz już pełne życie, nie możesz dodać więcej hp")
                return
            self.ekwipunek_p["p_zycia(1)"] -= 1
            self.hp += 25
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            print(f"Życie Sigmy wynosi {self.hp} / {self.maxhp}")

        elif ppp == 2 and self.ekwipunek_p.get("p_stamina(2)", 0) >= 1:
            if self.stamina == self.maxstamina:
                print("Masz już pełną staminę, nie możesz dodać więcej staminy")
                return
            self.ekwipunek_p["p_stamina(2)"] -= 1
            self.stamina += 35
            if self.stamina > self.maxstamina:
                self.stamina = self.maxstamina
            print(f"Stamina Sigmy wynosi {self.stamina} / {self.maxstamina}")

        elif ppp == 3 and self.ekwipunek_p.get("p_teleportacji(3)", 0) >= 1:
            print("Dostępna mapa:")
            print("wpisz 2 pierwsze litery lokacji gdzie chcesz się przeteleporotwać")
            print(klasa_g.mapa())  
            kl = input("Wybierz swoje kordynaty: ").lower()
            if kl == "el":
                self.lokacja = klasa_eldenhof.M_eldenhof
            elif kl == "fa":
                self.lokacja = klasa_farglen.M_farglen
            elif kl == "oa":
                self.lokacja = klasa_farglen.M_oakhaven
            elif kl == "li":
                self.lokacja = klasa_lokacja.Lirien
            elif kl == "du":
                self.lokacja = klasa_lokacja.Dunhollow
            elif kl == "no":
                self.lokacja = klasa_lokacja.Norheim
            elif kl == "th":
                self.lokacja = klasa_lokacja.Thaldras
            elif kl == "va":
                self.lokacja = klasa_lokacja.Varnak

    def odejmij_hp(self, a):
        self.hp -= a
        if self.hp <= 0:
            self.hp = 0
            self.zyje = False
            print(f"{self.imie} zginął!")

    def czy_zyje(self):
        return self.zyje

    def specjalny_atak(self, target):
        obrazenia = random.randint(15, 25)
        print(f"{self.imie} wykonuje specjalny atak! Zadaje {obrazenia} obrażeń.")
        target.odejmij_hp(obrazenia)

    def zdobycie_doswiadczenia(self, ilosc):
        self.doswiadczenie += ilosc
        print(f"{self.imie} zdobył {ilosc} punktów doświadczenia. Aktualne doświadczenie: {self.doswiadczenie}.")

    def atak_s(self, target):
        damage = self.atak
        print(f"{self.imie} atakuje! Zadaje {damage} obrażeń.")
        target.odejmij_hp(damage)
        if self.stamina < self.maxstamina:
            self.stamina += 5
            print(f"Stamina wynosi {self.stamina} na {self.maxstamina}. HP wynosi {self.hp} na {self.maxhp}")

    def zbierz_loot(self, loot_przedmioty, zloto):
        print(f"Zdobywasz następujące przedmioty:")
        for przedmiot, ilosc in loot_przedmioty.items():
            print(f"- {przedmiot}: {ilosc}")
            if przedmiot in self.ekwipunek_z:
                self.ekwipunek_z[przedmiot] += ilosc
            else:
                self.ekwipunek_z[przedmiot] = ilosc
        self.saldo += zloto
s = Sigma()
