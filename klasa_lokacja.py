import random
import klasa_enemies

class Location:
    def __init__(self, name, description):
        self.nazwa = name
        self.opis = description
        self.enemies = []
        self.sklepy = []

    def wejscie(self, player):
        print(f"{player.name} wchodzi do {self.nazwa}. {self.opis}")
    
    def spawn_enemy(self, player):
        if self.enemies:
            enemy = random.choice(self.enemies)
            print(f"Pojawia się {enemy.imie}!")
            enemy.walka(player) 

class Norheim(Location):
    def __init__(self):
        super().__init__("Norheim", "Starożytne ruiny pełne duchów przeszłości.")
        self.enemies = [klasa_enemies.Spectralny_rycerz(), klasa_enemies.Zagubiony_cien()]
        self.sklepy = ["jest to struktura w której nie ma żadnych sklepów"]

class Lirien(Location):
    def __init__(self):
        super().__init__("Lirien", "Zielone, mistyczne lasy pełne magii i pradawnych sekretów.")
        self.enemies = [klasa_enemies.Elficki_Lucznik(), klasa_enemies.Duch_Starego_Drzewa()]
        self.sklepy = ["jest to struktura w której nie ma żadnych sklepów"]

class Thaldras(Location):
    def __init__(self):
        super().__init__("Thaldras", "Kamienne wzgórza i jaskinie zamieszkane przez twardych wojowników.")
        self.enemies = [klasa_enemies.Krasnoludzki_Wojownik(), klasa_enemies.Kamienny_Golem()]
        self.sklepy = ["jest to struktura w której nie ma żadnych sklepów"]

class Varnak(Location):
    def __init__(self):
        super().__init__("Varnak", "Pustynne ruiny i spalone ziemie, pełne zdradliwych potworów.")
        self.enemies = [klasa_enemies.Pustynny_Skorpion(), klasa_enemies.Ognisty_Szamanka()]
        self.sklepy = ["jest to struktura w której nie ma żadnych sklepów"]

class Dunhollow(Location):
    def __init__(self):
        super().__init__("Dunhollow", "Mroczne podziemia pełne cieni, upiorów i zagadek.")
        self.enemies = [klasa_enemies.Cienisty_Zabojca(), klasa_enemies.Upiorny_Lowiec()]
        self.sklepy = ["jest to struktura w której nie ma żadnych sklepów"]
