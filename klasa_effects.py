import random

import random

class StatusEffect:
    def __init__(self, name, duration, apply_effect):
        self.name = name
        self.duration = duration
        self.apply_effect = apply_effect 

    def trigger(self, target):
        self.apply_effect(target)
        self.duration -= 1

    def is_expired(self):
        return self.duration <= 0


    def poison(target):
        print(f"{target.imie} traci 5 HP z powodu zatrucia!")
        target.odejmij_hp(5)

    def buff_attack(target):
        print(f"{target.imie} zyskuje +10 do ataku!")
        target.atak += 10
