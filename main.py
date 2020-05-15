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
    stats = ("~", name + "'s", "HP:", Character.Health, "MP:", Character.Mana, "XP:", Character.XP, "~")
    return stats


# Uses health potion and gives player 30 health
# No Parameters
# Returns if the player has no potions left
def use_hp_potion():
    if Character.Hp_Potion > 0:
        Character.Health += 45
        if Character.Health > 100:
            Character.Health = 100
    else:
        no_potions = "You don't have any potions left."
        return no_potions


# First encounter of the game and first choice player makes besides a name
# No Parameters
# No Returns
def first_choice():
    print("You wake up and a dreadful stench fills the air.\n"
          "Standing up you scan the your surroundings.\n"
          "You notice a chest would you like to open it? Yes/No")
    choice = input("> ")
    if choice.lower() == "yes":
        Character.Sword = "Long Sword"
        Character.Hp_Potion += 5
        print("Upon opening the chest you find a Long Sword and some potions.")
        second_choice()
    elif choice.lower() == "no":
        second_choice()
    else:
        print("Please you a correct choice.")
        first_choice()


# Prompts the player with a second choice
# No Parameters
# No Returns
def second_choice():
    print("Two doors materialize to your right as you look around.\n"
          "Would you like to go through door one or two? One/Two")
    choice = input("> ")
    if choice.lower() == "one":
        print("The door leads to a long hallway and another door appears in\n"
              "front of you. You open the door and walk through.")
        second_choice_a()
    elif choice.lower() == "two":
        second_choice_b()
    else:
        print("Please you a correct choice.")
        second_choice()


# Prompts player with monster encounter
# No Parameters
# No Returns
def second_choice_a():
    print("The dreadful stench becomes stronger while a crack illuminates the room.\n"
          "You continue to walk when you suddenly bump into something.\n"
          "Face to face with a monster do you slay it or run away? Slay/Run")
    choice = input("> ")
    if choice.lower() == "slay":
        Character.XP += 1
        Character.Health -= 45
        print(*player_stats(), "\n"
              "You kill the monster and you gain 1 XP.\n"
              "The ground beneath you collapses and you find yourself in a dungeon.\n"
              "You take significant damage would you like to drink a potion? Yes/No")
        choice = input("> ")
        if choice.lower() == "yes":
            use_hp_potion()
            print(*player_stats(), "")
        elif choice.lower() == "no":
            pass  # after monster encounter
    elif choice.lower() == "run":
        second_choice_a_run()
    else:
        print("Please you a correct choice.")
        second_choice_a()


# Prompts player with bandit choice
# No Parameters
# No Returns
def second_choice_a_run():
    print(*player_stats(), "\n"
          "You run away but see a group of bandits surrounding something!\n"
          "Upon unsheathing your sword the bandits scurry away revealing "
          "an injured dog, would you like to give it a potion? Yes/No")
    choice = input("> ")
    if choice.lower() == "yes":
        if Character.Hp_Potion > 0:
            Character.Hp_Potion -= 1
            print("You give the dog a potion and he recovers from his injuries.")
    elif choice.lower() == "no":
        print("You leave the dog there to suffer, who is the real monster here.")
    else:
        print("Please you a correct choice.")
        second_choice_a_run()


# Prompts player with choice b
# No Parameters
# No Returns
def second_choice_b():
    print("You exit and the sun blinds you, but when you turn back you\n"
          "see a castle and the door you came from has vanished.")


# Prompts player with whether they want to play again or not
# No Parameters
# No Returns
def end():
    print("Would you like to play again? Yes/No")
    choice = input("> ")
    if choice.lower == "yes":
        pass
    elif choice.lower == "no":
        title_screen()


system("title " + title)
###### Main Game Loop ######
while playing:
    # function(encounter, etc) call order
    title_screen()
    name = player_name()
    first_choice()
    end()
