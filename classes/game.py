# -*- coding: utf-8 -*-
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Item"]

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def choose_action(self):
        i = 1
        print("\n   " + bcolors.BOLD + self.name + bcolors.ENDC)
        print("   Actions")
        for item in self.actions:
            print("    "+str(i)+':'+item)
            i += 1
        action_choice = int(input("   Choose action:"))-1
        return action_choice

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE+"\n   Magic"+bcolors.ENDC)
        for spell in self.magic:
            print("    "+str(i)+'.'+spell.name+" (cost:"+str(spell.cost)+")")
            i += 1
        magic_choice = int(input("   Choose Magic:"))-1
        magic = self.magic[magic_choice]
        return magic

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN+"\n   Items"+bcolors.ENDC)
        for item in self.items:
            print("    "+str(i)+'.'+item['item'].name+":" +
                  item['item'].description+" (x"+str(item['quantity'])+")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print(bcolors.WARNING+"\n   Targets"+bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() > 0:
                print("    "+str(i)+'.'+enemy.name)
            i += 1
        target_choice = int(input("   Choose Target:"))-1
        return target_choice

    def get_enemy_stats(self):
        hp_bar = ""
        hp_bar_ticks = int((float(self.hp)/float(self.maxhp))*50)
        len_hp_bar = hp_bar_ticks
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len_hp_bar < 50:
            hp_bar += " "
            len_hp_bar += 1

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        cur_hp = ""
        if len(hp_string) < 7:
            reduced = 7-len(hp_string)
            while reduced > 0:
                cur_hp += " "
                reduced -= 1
            cur_hp += hp_string
        else:
            cur_hp = hp_string

        print("                       ___________________________________" +
              "_______________")
        print(bcolors.BOLD+bcolors.WARNING+self.name+":        "+cur_hp+"|" +
              bcolors.FAIL+hp_bar+bcolors.ENDC+bcolors.BOLD+"|")

    def get_stats(self):

        hp_bar = ""
        hp_bar_ticks = int((float(self.hp)/float(self.maxhp))*25)
        len_hp_bar = hp_bar_ticks
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len_hp_bar < 25:
            hp_bar += " "
            len_hp_bar += 1

        mp_bar = ""
        mp_bar_ticks = int((float(self.mp)/float(self.maxmp))*10)
        len_mp_bar = mp_bar_ticks
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len_mp_bar < 10:
            mp_bar += " "
            len_mp_bar += 1

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        cur_hp = ""
        if len(hp_string) < 7:
            reduced = 7-len(hp_string)
            while reduced > 0:
                cur_hp += " "
                reduced -= 1
            cur_hp += hp_string
        else:
            cur_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        cur_mp = ""
        if len(mp_string) < 7:
            reduced = 7-len(mp_string)
            while reduced > 0:
                cur_mp += " "
                reduced -= 1
            cur_mp += mp_string
        else:
            cur_mp = mp_string

        print("                       _________________________            " +
              "__________")
        print(bcolors.BOLD+self.name+":        "+cur_hp+"|" +
              bcolors.OKGREEN+hp_bar+bcolors.ENDC+bcolors.BOLD+"|   " +
              cur_mp+"|"+bcolors.OKBLUE+mp_bar+bcolors.ENDC+"|")
