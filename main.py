# -*- coding: utf-8 -*-
import random
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create some items
potion = Item("Potion", "potion", "heals 50 HP", 50)
hipotion = Item("Hipotion", "potion", "heals 100 HP", 100)
superpotion = Item("Superpotion", "potion", "heals 200 HP", 200)
elixir = Item("Elixir", "elixir", "fully restores HP/MP of one party member",
              9999)
hielixir = Item("MegaElixir", "elixir", "fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 300)


# Instantiate characters
player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{'item': potion, 'quantity': 5},
                {'item': hipotion, 'quantity': 3},
                {'item': superpotion, 'quantity': 2},
                {'item': elixir, 'quantity': 1},
                {'item': hielixir, 'quantity': 1},
                {'item': grenade, 'quantity': 1}]
player1 = Person("Valos ", 326, 65, 70, 34, player_spells, player_items)
player2 = Person("Thanos", 416, 65, 80, 34, player_spells, player_items)
player3 = Person("Robot ", 308, 65, 60, 34, player_spells, player_items)
players = [player1, player2, player3]

enemy_spells = [fire, meteor, cure]
enemy_items = [{'item': potion, 'quantity': 5},
               {'item': superpotion, 'quantity': 2},
               {'item': elixir, 'quantity': 1},
               {'item': grenade, 'quantity': 1}]
enemy1 = Person("Imp1  ", 280, 65, 100, 25, enemy_spells, enemy_items)
enemy2 = Person("Magus ", 920, 145, 200, 35, enemy_spells, enemy_items)
enemy3 = Person("Imp2  ", 280, 65, 200, 25, enemy_spells, enemy_items)
enemies = [enemy1, enemy2, enemy3]

# battle
running = True
round = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
print("Normal Text")

while running:

    print(bcolors.HEADER+"\n\nRound "+str(round)+bcolors.ENDC)
    round += 1
    print("=================================================" +
          "=========================")
    print("NAME                    HP                                 MP")
    for player in players:
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        if len(enemies) == 0:
            break

        if player.get_hp() > 0:

            action = player.choose_action()

            if action == 0:
                dmg = player.generate_dmg()
                enemy = player.choose_target(enemies)
                print(bcolors.FAIL+"You attacked " +
                      enemies[enemy].name.replace(" ", "") +
                      " for "+str(dmg)+" points of damage."+bcolors.ENDC)
                enemies[enemy].take_dmg(dmg)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "")+" has died!")
                    del enemies[enemy]

            elif action == 1:
                spell = player.choose_magic()
                '''
                magic_dmg = player.generate_spell_dmg(magic_choice)
                spell = player.get_spell_name(magic_choice)
                cost = player.get_spell_mp_cost(magic_choice)
                '''
                magic_dmg = spell.generate_dmg()
                current_mp = player.get_mp()
                if current_mp < spell.cost:
                    print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                    continue

                player.reduce_mp(spell.cost)
                if spell.type == 'white':
                    player.heal(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name + " heals for " +
                          str(magic_dmg) + " HP." + bcolors.ENDC)
                elif spell.type == 'black':
                    enemy = player.choose_target(enemies)
                    print(bcolors.OKBLUE + "\n" + spell.name + " deals " +
                          str(magic_dmg) + " points of damage to " +
                          enemies[enemy].name.replace(" ", "")+bcolors.ENDC)
                    enemies[enemy].take_dmg(magic_dmg)
                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") +
                              " has died!")
                        del enemies[enemy]

            elif action == 2:
                player.choose_item()
                item_choice = int(input("   Choose Item:"))-1
                item = player.items[item_choice]['item']
                player.items[item_choice]['quantity'] -= 1
                if player.items[item_choice]['quantity'] < 0:
                    print(bcolors.WARNING+"\nNone left"+bcolors.ENDC)
                    continue

                if item.type == 'potion':
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " heals for " +
                          str(item.prop) + " HP." + bcolors.ENDC)
                elif item.type == 'elixir':
                    if item.name == 'MegaElixir':
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                        print(bcolors.OKGREEN+'\n'+item.name +
                              'fully restores HP/MP of all players' +
                              bcolors.ENDC)
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        print(bcolors.OKGREEN+'\n'+item.name +
                              'fully restores HP/MP' + bcolors.ENDC)
                elif item.type == 'attack':
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_dmg(item.prop)
                    print(bcolors.OKBLUE + '\n' + item.name + ' deals ' +
                          str(item.prop) + " points of damage to " +
                          enemies[enemy].name.replace(" ", "")+bcolors.ENDC)
                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", "") +
                              " has died!")
                        del enemies[enemy]
# check if battle is over
    if len(enemies) == 0:
        print(bcolors.OKGREEN + "YOU WIN!" + bcolors.ENDC)
        running = False
    elif len(players) == 0:
        print(bcolors.FAIL + "YOU LOSE!" + bcolors.ENDC)
        running = False
# enemies' move
    else:
        for enemy in enemies:
            enemy_choice = random.randrange(0, 2)
            # chose attack
            if enemy_choice == 0:
                if len(players) == 0:
                    continue
                target = random.randrange(0, len(players))
                enemy_dmg = enemy.generate_dmg()
                players[target].take_dmg(enemy_dmg)
                print(bcolors.WARNING+"\n"+enemy.name.replace(" ", "") +
                      " attacks "+players[target].name.replace(" ", "") +
                      " for "+str(enemy_dmg)+" points of damage"+bcolors.ENDC)
                if players[target].get_hp() == 0:
                    print(players[target].name+" has died!")
                    del players[target]
            # chose magic
            elif enemy_choice == 1:
                magic_choice = random.randrange(0, len(enemy.magic))
                spell = enemy.magic[magic_choice]
                magic_dmg = spell.generate_dmg()
                current_mp = enemy.get_mp()
                if current_mp < spell.cost:
                    print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                    continue

                enemy.reduce_mp(spell.cost)
                if spell.type == 'white':
                    enemy.heal(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name + " heals for " +
                          str(magic_dmg) + " HP." + bcolors.ENDC)
                elif spell.type == 'black':
                    player = random.randrange(0, len(players))
                    print(bcolors.OKBLUE + "\n" + spell.name + " deals " +
                          str(magic_dmg) + " points of damage to " +
                          players[player].name.replace(" ", "")+bcolors.ENDC)
                    players[player].take_dmg(magic_dmg)
                    if players[player].get_hp() == 0:
                        print(players[player].name.replace(" ", "") +
                              " has died!")
                        del players[player]
