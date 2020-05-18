import sys
import os
import time
from os import system
import random
import pickle
import cmd
import textwrap

playing = True
title = "Gamer Moment"


###### Menu Screens ######
# Grabs input from the player for commands
# No Parameters
# No Returns
def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        pass
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    elif option.lower() not in ["play", "help", "quit"]:
        print("Command not valid.")
        title_screen_selections()


# Prints Main Menu(title screen) to the console and shows command options
# No Parameters
# No Returns
def title_screen():
    os.system('cls')
    print("############################")
    print("#Welcome to this Shithole!!#")
    print("############################")
    print("          ~ Play ~          ")
    print("          ~ Help ~          ")
    print("          ~ Quit ~          ")
    print("  Made by Pedro Aguilar Jr  ")
    print("    and Jazmin Contreras    ")
    title_screen_selections()


# Prints Help screen to console telling how to use commands and play
# No Parameters
# No Returns
def help_menu():
    print("############################")
    print("#      -<Help Menu!>-      #")
    print("############################")
    print("")
    print(" Type commands to use them! ")
    print("   Use 'look' to inspect!   ")
    print("  Finally try to have fun!  ")
    title_screen_selections()


###### Game Functionality ######
# Class for creating player stats to reference from during game
class Character:
    Health = 100
    Mana = 50
    XP = 0
    Gold = 0
    Hp_Potion = 0
    Sword = None
    dead = False


# Class from Creating Doggo
class Dog:
    Health = 50
    XP = 0
    Gold = 0
    dead = False


# Grabs input from user for player name
# No Parameters
# Returns the player name
def player_name():
    os.system('cls')
    print("Enter your name adventurer.")
    pname = input("> ")
    return pname


# Players stats bar
# No Parameters
# Returns the stats bar to be used by name variable
def player_stats():
    stats = ("~", name + "'s", "HP:", Character.Health, "MP:", Character.Mana, "Gold", Character.Gold, "XP:",
             Character.XP, "~")
    return stats


# Dog Stats bar
# No Parameters
# No Returns~
def dog_stats():
    stats = ("~ Doggo's", "HP:", Dog.Health, "Gold:", Dog.Gold, "XP:", Dog.XP, "~")
    return stats


# Uses health potion and gives player 30 health
# No Parameters
# Returns if the player has no potions left
def use_hp_potion():
    if Character.Hp_Potion > 0:
        Character.Health += 45
        Character.Hp_Potion -= 1
        if Character.Health > 100:
            Character.Health = 100
    else:
        no_potions = "You don't have any potions left."
        return no_potions


# Function for dealing damage to player
# Amount of damage dealt to the player
# No Returns
def player_damage(amount):
    Character.Health -= amount
    if Character.Health < 1:
        Character.dead = True
        print(name, "has perished!")
        end()#### not fully complete yet ####


# Function for dealing damage to Doggo
# amount of damage dealt to doggo
# No Returns
def dog_damage(amount):
    Dog.Health -= amount
    if Dog.Health < 1:
        Dog.dead = True
        print("Your doggo has perished!")


# Takes potion from the player when giving it to the dog friend
# No Parameters
# Returns if you have not potions and that the doggo has been healed
def give_dog_potion():
    if Character.Hp_Potion > 0:
        Character.Hp_Potion -= 1
        Dog.Health += 45
        doggo_healed = "You're furry friend wags its tail with joy as it heals."
        if Dog.Health > 50:
            Dog.Health = 50
        return doggo_healed
    else:
        no_potions = "You don't have any potions left."
        return no_potions


# Resets the player stats for replaying
# No Parameters
# No Returns
def game_reset():
    Character.Health = 100
    Character.Mana = 50
    Character.Hp_Potion = 0
    Character.XP = 0
    Character.Sword = None
    Character.Gold = 0
    Character.dead = False


###### Game Plot Functions ######
# First encounter of the game and first choice player makes besides a name
# No Parameters
# No Returns
def first_choice():
    print("You wake up and a dreadful stench fills the air.\n"
          "Standing up you scan your surroundings.\n"
          "You notice a chest would you like to open it? Yes/No")
    choice = input("> ")
    if choice.lower() == "yes":
        Character.Sword = "Long Sword"
        Character.Hp_Potion += 5
        print("Upon opening the chest you find a Long Sword and some potions.")
        door1()
    elif choice.lower() == "no":
        door2()
    else:
        print("Please you a correct choice.")
        first_choice()


# Prompts player with monster encounter
# No Parameters
# No Returns
def door1():
    print("A door appears in front of you and you walk through it.\n"
          "The door leads to a long hallway and another door appears in\n"
          "front of you. You open the door and walk through.\n"
          "The dreadful stench becomes stronger while a crack illuminates the room.\n"
          "You continue to walk when you suddenly bump into something.\n"
          "Face to face with a monster do you slay it or run away? Slay/Run")
    choice = input("> ")
    if choice.lower() == "slay":
        Character.XP += 1
        player_damage(45)
        print(*player_stats(), "\n"
              "You kill the monster and you gain 1 XP.\n"
              "The ground beneath you collapses and you find yourself in a dungeon.\n"
              "You take significant damage would you like to drink a potion? Yes/No")
        choice = input("> ")
        if choice.lower() == "yes":
            use_hp_potion()
            print(*player_stats(), "\n"
                  "Your health returns to max and the potion is wasted.")
            sulfur_two_pathways()
        elif choice.lower() == "no":
            print(*player_stats(), "\n"
                  "You decide not to heal and your health stays diminished.")
            sulfur_two_pathways()
        else:
            print("Please you a correct choice.")
            door1()
    elif choice.lower() == "run":
        door1_run()
    else:
        print("Please you a correct choice.")
        door1()


# Prompts player with bandit choice
# No Parameters
# No Returns
def door1_run():
    dog_damage(35)
    print(*player_stats(), "\n"
          "You run away but see a group of bandits surrounding something!\n"
          "Upon unsheathing your sword the bandits scurry away revealing\n"
          "an injured dog, would you like to give it a potion? Yes/No")
    choice = input("> ")
    if choice.lower() == "yes":
        if Character.Hp_Potion > 0:
            print(give_dog_potion())
            door1_run_a()
    elif choice.lower() == "no":
        print("You leave the dog there to suffer, who is the real monster here.")
        door1_run_b()
    else:
        print("Please you a correct choice.")
        door1_run()


# Prompts player with dungeon after run/heal dog option
# No Parameters
# No Returns
def door1_run_a():
    player_damage(45)
    dog_damage(45)
    print(*player_stats())
    print(*dog_stats(), "\n"
          "The ground underneath you collapses, and you find yourself in a dungeon. \n"
          "You and your new companion have taken a significant amount of damage. \n"
          "Would you like to drink a potion or give it to your furry friend? Drink/Give")
    choice = input("> ")
    if choice.lower() == "drink":
        use_hp_potion()
        print(*player_stats())
        print(*dog_stats(), "\n"
              "Your health returns to max and the potion is wasted.\n"
              "The doggo whimpers a little before getting back up.")
        sulfur_two_pathways_dog()
    elif choice.lower() == "give":
        give_dog_potion()
        sulfur_two_pathways_dog()
    else:
        print("Please you a correct choice.")
        door1_run_a()


# Prompts player with dungeon after run/don't heal dog option
# No Parameters
# No Returns
def door1_run_b():
    player_damage(45)
    print(*player_stats(), "\n"
          "The ground beneath you collapses and you find yourself in a dungeon.\n"
          "You take significant damage and the dog from earlier has perished. \n"
          "Would you like to drink a potion? Yes/No")
    choice = input("> ")
    if choice.lower() == "yes":
        if Character.Hp_Potion > 0:
            use_hp_potion()
        sulfur_two_pathways()
    elif choice.lower() == "no":
        print("You decide not to heal yourself and your health stays diminished.")
        sulfur_two_pathways()
    else:
        print("Please you a correct choice.")
        door1_run_b()


# Prompts player with choice between two pathways after smelling sulfur
# No Parameters
# No Returns
def sulfur_two_pathways():
    print("The dungeon reeks of sulfur and two pathways appear before you.\n"
          "Do you walk down path 1 or path 2. Path 1/Path 2")
    choice = input("> ")
    if choice.lower() == "path 1":
        print("The smell of sulfur grows stronger. You follow the scent.")
        ogre_path()
    elif choice.lower() == "path 2":
        print("You hear a faint clanging noise. You follow the noise and to your\n"
              "surprise its a blacksmith. But wait! He's levitating over lava.\n"
              "He Slowly turns around to look at you, and you begin to feel\n"
              "spiders crawling down your back.")
    else:
        print("Please use a correct choice.")
        sulfur_two_pathways()


# Prompts player with choice between two pathways after smelling sulfur with a companion
# No Parameters
# # No Returns
def sulfur_two_pathways_dog():
    print("The dungeon reeks of sulfur and two pathways appear before you.\n"
          "Do you walk down path 1 or path 2. Path 1/Path 2")
    choice = input("> ")
    if choice.lower() == "path 1":
        print("The smell of sulfur grows stronger. You follow the scent\n"
              "with your doggo close behind.")
        ogre_path()
    elif choice.lower() == "path 2":
        print("You hear a faint clanging noise and your companion whimpers.\n"
              "You follow the noise and to your surprise its a blacksmith.\n"
              "But wait! He's levitating over lava. He slowly turns around\n "
              "to look at you, and you begin to feel spiders crawling down your back.")
    else:
        print("Please use a correct choice.")
        sulfur_two_pathways()


# Prompts player with ogre choice between sneaking or taking the pouch
# No Parameters
# No Returns
def ogre_path():
    print("You find an Ogre holding a pouch. What will you do? Take/Sneak")
    choice = input("> ")
    if choice.lower() == "take":
        ogre_take()
    elif choice.lower() == "sneak":
        ogre_sneak()
    else:
        print("Please use a correct choice.")
        ogre_path()


# Player takes pouch and fights the ogre
# No Parameters
# No Returns
def ogre_take():
    print("You walk near the ogre and quickly snatch the pouch.\n"
          "Success! However the you have angered the Ogre you begin to battle.\n"
          "Slashing at the Ogre you miss, and it swings its club at you.\n"
          "Managing to dodge it you slash it with your sword and succeed.\n"
          "It took little damage nonetheless the Ogre flees and you open the pouch\n"
          "YOU FIND GOLD!! Maybe you can use it to escape.")


# Player sneaks away from ogre into next room
# No Parameters
# No Returns
def ogre_sneak():
    print("You stealthily sneak past the Ogre and book it as soon as possible.\n"
          "There's a switch at the end of this room and when you look back\n"
          "the path you came from is but a plain wall. You flip the switch.")


# Prompts player with choice b
# No Parameters
# No Returns
def door2():
    print("A door appears in front of you and you walk through it.\n"
          "You exit and the sun blinds you, but when you turn back you\n"
          "see a castle and the door you came from has vanished.\n"
          "You walk around and decide to explore, seeing the entrance\n"
          "to the castle would you like to enter for food or explore the forest.\n"
          "Castle/Forest")
    choice = input("> ")
    if choice.lower() == "castle":
        castle_entrance()
    elif choice.lower() == "forest":
        explore_forest()
    else:
        print("Please use a correct choice.")
        door2()


# Player chooses to walk into the dungeon to scavenge for food
# No Parameters
# No Returns
def castle_entrance():
    print("You scavenge the castle but there was nothing but broken tools.")


# Player Explores forest and prompts for trade option
# No Parameters
# No Returns
def explore_forest():
    Character.Hp_Potion += 1
    print("You decide to explore more of the peculiar forest.\n"
          "The wind howls as you walk deeper and you see a light.\n"
          "It's a potion! You take it and put it into your pocket.\n"
          "The air is cold and the stars light up the sky. \n"
          "As you continue walking you hear fire crackling and see \n"
          "ashes rising. You see a group of people surrounding the fire.\n"
          "They're merchants. You see useful objects that can come in handy.\n"
          "But you only have potion to trade. Trade/Move On")
    choice = input("> ")
    if choice.lower() == "trade":
        potion_trade()
    elif choice.lower() == "move on":
        keep_walking()
    else:
        print("Please use a correct choice.")
        explore_forest()


# Takes players potion and gives them rusty knife then prompts if they want to clean it
# No Parameters
# No Returns
def potion_trade():
    Character.Hp_Potion -= 1
    Character.Sword = "Rusty Knife"
    print("A merchant give you a rusty knife, you can clean it off at a lake.\n"
          "You thank them and go on your way, hearing running water you come\n"
          "across a lake. Would you like to clean the rusty knife? Clean/Don't")
    choice = input("> ")
    if choice.lower() == "clean":
        Character.Sword = "Knife"
        print("You clean the knife and now have a new knife.")
    elif choice.lower() == "don't":
        print("You decide to not clean the knife and keep walking.")
    else:
        print("Please use a correct choice.")
        potion_trade()


# Player gets chased by merhcants and ends up near a lake
# No Parameters
# No Returns
def keep_walking():
    print("You continue to walk past them, however it seems they're looking for\n"
          "trouble. Some Merchants start to follow you and that knife\n"
          "they had would've come in handy right now. You run away and\n"
          "while trying to lose them you take cove in a bush while they scatter.\n"
          "After hearing water you realize you've ended up near a lake.")


# Prompts player with whether they want to play again or not
# No Parameters
# No Returns
def end():
    global playing
    print("Would you like to play again? Yes/No")
    choice = input("> ")
    if choice.lower() == "yes":
        game_reset()
        playing = True
    elif choice.lower() == "no":
        game_reset()
        playing = True
        title_screen()
    else:
        print("Please use a correct choice.")
        end()


system("title " + title)
title_screen()
###### Main Game Loop ######
while playing:
    # function(encounter, etc) call order
    name = player_name()
    first_choice()
    end()
while Character.dead:
    playing = False

