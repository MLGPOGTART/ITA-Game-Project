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
    puzzle_pouch = False
    puzzle_chances = 0
    blacksmith_path = False
    dog = False


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
    Character.puzzle_pouch = False
    Character.puzzle_chances = 0
    Character.blacksmith_path = False
    Character.dog = False

    Dog.Health = 50
    Dog.XP = 0
    Dog.Gold = 0
    Dog.dead = False


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
        Character.dog = True
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
        blacksmith_path()
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
        blacksmith_path()
    else:
        print("Please use a correct choice.")
        sulfur_two_pathways()


#
#
#
def blacksmith_path():
    print("You hear a faint clanging noise and your companion whimpers.\n"
          "You follow the noise and to your surprise its a blacksmith.\n"
          "But wait! He's levitating over lava. He slowly turns around\n "
          "to look at you, and you begin to feel spiders crawling down your back.\n"
          "He slowly levitates towards you, and you try to get away.\n"
          "He points out that there seems to be trouble ahead and asks if you need help\n"
          "Yes/No")
    choice = input("> ")
    if choice.lower() == "yes":
        Character.blacksmith_path = True
        print("You accept his aid and he teleports you to a room with a lever.\n"
              "He mentions that he will call you when he needs you.")
        symbol_puzzle()
    elif choice.lower() == "no":
        print("You decline and keep walking through the dungeon.")
        ogre_path()
    else:
        print("Please choose a correct choice.")
        blacksmith_path()


# Prompts player with ogre choice between sneaking or taking the pouch
# No Parameters
# No Returns
def ogre_path():
    print("You find an Ogre holding a pouch. What will you do? Take/Sneak")
    choice = input("> ")
    if choice.lower() == "take":
        ogre_take()
    elif choice.lower() == "sneak":
        print("You stealthily sneak past the Ogre and book it as soon as possible.")
        symbol_puzzle()
    else:
        print("Please use a correct choice.")
        ogre_path()


# Player takes pouch and fights the ogre
# No Parameters
# No Returns
def ogre_take():
    Character.Gold += 50
    Character.puzzle_pouch = True
    print("You walk near the ogre and quickly snatch the pouch.\n"
          "Success! However you have angered the Ogre you begin to battle.\n"
          "Slashing at the Ogre you miss, and it swings its club at you.\n"
          "Managing to dodge it you slash it with your sword and succeed.\n"
          "It took little damage nonetheless the Ogre flees and you open the pouch\n"
          "YOU FIND GOLD!! Maybe you can use it to escape. You move on to the next room.")
    symbol_puzzle()


# Player must complete a puzzle
# No Parameters
# No Returns
def symbol_puzzle():
    print("There's a switch at the end of this room and when you look back\n"
          "the path you came from is but a plain wall. You flip the switch.\n"
          "Strange Symbols appear on the wall Alpha, Beta, Omega. A PUZZLE!!\n"
          "There are three symbols and you have to get them in the right order\n")
    if Character.puzzle_pouch:
        print("Do you want to use the pouch of gold? Yes/No")
        choice = input("> ")
        if choice.lower() == "yes":
            Character.puzzle_pouch = False
            Character.Gold -= 50
            print("You open the pouch and select a coin randomly. Its an Alpha symbol.")
            puzzle()
        elif choice.lower() == "no":
            print("You save the gold and get a confidence boost.")
            puzzle()
        else:
            print("Please choose a correct choice.")
            symbol_puzzle()
    elif not Character.puzzle_pouch:
        puzzle()


# Executes code for calling puzzle choices and victory text
# No Parameters
# No Returns
def puzzle():
    puzzle_choice1()
    puzzle_choice2()
    puzzle_choice3()
    print("You got them all right nice. It took", Character.puzzle_chances, "tries.")
    after_puzzle()


# Gets players input for first puzzle choice
# No Parameters
# No Returns
def puzzle_choice1():
    correct = "alpha"
    choice = ""
    print("Alpha, Beta, or Omega?")
    while choice.lower() != correct:
        choice = input("> ")
        Character.puzzle_chances += 1
    print("You got the first one right whats next!")


# Gets players input for second puzzle choice
# No Parameters
# No Returns
def puzzle_choice2():
    correct = "beta"
    choice = ""
    print("Alpha, Beta, or Omega?")
    while choice.lower() != correct:
        choice = input("> ")
        Character.puzzle_chances += 1
    print("You got the second one right whats next!")


# Gets players input for third puzzle choice
# No Parameters
# No Returns
def puzzle_choice3():
    correct = "omega"
    choice = ""
    print("Alpha, Beta, or Omega?")
    while choice.lower() != correct:
        choice = input("> ")
        Character.puzzle_chances += 1


# Function for telling whether the blacksmith helped the player
# No Parameters
# No Returns
def after_puzzle():
    print("The dungeon rumble around you!")
    if Character.blacksmith_path:
        after_puzzle_blacksmith()
    elif not Character.blacksmith_path:
        after_puzzle2()


# After the puzzle blacksmith asks for your body
# No Parameters
# No Returns
def after_puzzle_blacksmith():
    print("The Blacksmith appears after you guess the order.\n"
          "He says he's been a spirit stuck in the dungeon for\n"
          "a thousand years. He needs a body to hold his curse.")
    if Character.dog:
        print("Do you give up your dog or try to trick him? Dog/Trick")
        choice = input("> ")
        if choice.lower() == "dog":
            print("He transfers his mind into your doggo and his its eyes glow red.\n"
                  "It attacks you but you cant bring yourself to hurt it and end up perishing\n"
                  "as the newly mind transferred dog tears you limb from limb.")
        elif choice.lower() == "trick":
            kill_rat_choice()
        else:
            print("Please choose a correct option.")
            after_puzzle_blacksmith()
    elif not Character.dog:
        print("Do you give yourself to him or try and trick him? You/Trick")
        choice = input("> ")
        if choice.lower() == "you":
            print("You give your body to the blacksmith and live on with someone in your head.")
        elif choice.lower() == "trick":
            kill_rat_choice()
        else:
            print("Please use a correct option.")
            after_puzzle_blacksmith()


# Prompts player for choice on whether to kill or keep your rat friend(ending)
# No Parameters
# No Returns
def kill_rat_choice():
    print("You try to think of something on the spot but by dumb luck you pick up a rat\n"
          "and his mind is transferred into it. You pick it up and inspect it then put\n"
          "it back into your pocket. You find your way to the village")
    if Character.dog:
        print("with both your furry companions.")
    print("What will you do with your new friend? Throw it into the alley full of cats or keep him.\n"
          "Cats/Keep")
    choice = input("> ")
    if choice.lower() == "cats":
        print("You throw it into the alley and watch it suffer as it tries to escape.\n"
              "The cats tear him to pieces until it is a red puddle of life juices.\n"
              "Who was the evil one in the end. You Live happily ever after in your village.\n")
    elif choice.lower() == "keep":
        print("You look at your new rat friend")
        if Character.dog:
            print("and your doggo.")
        print("and you live happily ever after")
    else:
        print("Please use a correct choice.")
        kill_rat_choice()


# End of the game by dungeon path without blacksmith
# No Parameters
# No Returns
def after_puzzle2():
    print("You wake up and hear birds chirping and people conversing.\n"
          "you find yourself laying on the ground feeling groggy, \n"
          "you stand up and start walking towards the noise. Its your village!\n"
          "You have finally found your way back.")
    if Character.puzzle_pouch:
        print("You use the ouch of gold to purchase amenities.\n"
              "You live happily ever after in the village you belong.")
    elif not Character.puzzle_pouch:
        print("You live happily ever after in the village you belong.")


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

