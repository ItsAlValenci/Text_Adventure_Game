import random as rnd
from time import sleep  
from assets.sprits import *
from assets.dialogs import *

greetings = greetings_log

####First stage ###
def start_menu():
    #list of random greetings
    greetings = greetings_log
    
    initial_greeting = rnd.choice(greetings)
    #We ask for the name to personalize the game and start interacting
    print(wolf_icon_txt)
    sleep(1)
    print(wolf_icon)
    print(initial_greeting)
    player_name = str(input("\nPlease, type your name: \n").capitalize()) #.capitalize to make the first letter upper case
    # Introduction to the story and basic rules
    input(get_welcome_message(player_name))
    sleep(0.5)

#### Second Stage ####
def base_game():
    #list of random give up options
    go_cave = cave_log
    dead_end_joke = rnd.choice(go_cave)
    
    #Variables use as counters   
    pigs_caught = 0   #This is a counter to ensure end of loop.
    location = "forest" #starting location, it is mutable to migrate between scenes in the game.
    house_1_count = 0 #counter to kill the user if they travel twice to location north.
    house_2_count = 0 #counter to kill the user if they travel twice to same location west.
    user_choices = [] #empty list, it will be filled with the path of the user.
    
    #This is just some visual aid.
    print(cave)
    print(cave_start)
          
    # Game Loop
    while pigs_caught != 3: #The loop will continue to run until you have traveled to each playable area except south(escape).
      # Forest, main path of the mage and gate to other areas.
      if location == "forest": #Base location and trigger for direction structions.
        direction = input("In Which direction would you like to go?\nPlease type: North, West , East or South.\n").lower()
        #Optimal order based on testers(85% followed the order presented)
        if direction == "north" or "n" in direction:
          location = "pig1_house" 
        elif direction == "west" or "w" in direction:
          location = "pig2_house" 
        elif direction == "east" or "e" in direction:
          location = "pig3_house"
        elif direction == "south" or "s" in direction:
          location = "deadend"
        else:
          print("\nInvalid direction. Please try again.")
          continue

      ### Little Pig's House
      elif location == "pig1_house":
          #This option prevents the user from cheating by entering the same place twice.
          if house_1_count == 1 and location != "forest":
              user_choices.append(direction)
              print("\nI warned you...\nDo NOT travel to the same place twice!!\n\nA hunter has found you and hunted you down.")
              game_over_loser()
              break
          #This is the code for a normal run.
          else:
              #This is just some visual aid.
              print(straw_house)
              blow_down = input("\nYou have found Pig 1's house made of straw.\nWhat do you want to do??\nA) Blow the house. \nB) Knock the door and trick the pig. \n").lower()
              if blow_down == "a" or "blow" in blow_down:
                  pigs_caught += 1 #Addition to counter.
                  house_1_count += 1 #Addition to counter.
                  user_choices.append(direction) #Addition to list.
                  print("\nThe house has been blown down and the little pig has run away.\nYou are back into the main path.\n")
                  location = "forest" #Return to main path
                  sleep(1.0)
              elif blow_down == "b" or "knock" in blow_down: 
                  #There is a bug where the player can choose this option unlimited times, the fix is out of scope in this version.
                  print("\nOh, He knows you are the wolf and won't open the door. Try again.")
                  sleep(1.5)
                  continue
              else:
                  print("\nInvalid input. Please try again.")
                  continue

      ### Middle Pig's House 
      elif location == "pig2_house":
          #This option prevents the user from cheating by entering the same place twice.
          if house_2_count == 1 and location != "forest":
              user_choices.append(direction)
              print("\nI warned you,\nDo NOT travel to the same place twice!!\n\nA hunter have found you and hunt you down.")
              game_over_loser()
              break
          #This is the code for a normal run.
          else:
              #This is just some visual aid.
              print(stick_house)
              blow_down = input("\nYou have found Pig 2's house made of sticks.\nWhat do you want to do??\nA) Blow the house. \nB) Knock the door and trick the pig. \n").lower()
              if blow_down == "a" or "blow" in blow_down:
                  pigs_caught +=1 #Addition to counter.
                  house_2_count += 1 #Addition to counter.
                  user_choices.append(direction) #Addition to list.
                  print("\nThe house has been blown down and the middle pig has run away.\nYou are back into the main path.\n")
                  location = "forest"  #Return to main path.
                  sleep(1.0)
              elif blow_down == "b" or "knock" in blow_down:
                  #There is a bug where the player can choose this option unlimited times, the fix out of scope in this version.
                  print("\nOh, He knows you are the wolf and won't open the door. Try again.") 
                  sleep(1.5)
                  continue
              else:
                  print("\nInvalid input. Please try again.")
                  continue

      ### Oldest Pig's House
      elif location == "pig3_house":
          #This option prevents the user from going into the final stage without visiting the previous 2 areas.
          if pigs_caught != 2 and location != "forest":
              print("\nUps, still you are too sleepy to go this way.\nPerhaps you should try with a different location.")
              user_choices.append(direction) #Addition to list.
              location = "forest"
              sleep(1.5)
          #This is the code for a normal run.
          else:
              pigs_caught += 1 #Addition to counter.
              final_boss()     #activation for final stage
              user_choices.append(direction) #Addition to list.
              break
          
      ### failsafe, this a deadend to terminate the game at any given time from the main path.
      elif location == "deadend":
        user_choices.append(direction)  
        print(f"""
{dead_end_joke}""")
        sleep(1.5)
        game_over_loser()
        break
      else:
        pass
    print("\nIn this game, you decided to take the following paths:\n")
    #This code is just to show the user the path he took during the gameplay
    for pick in user_choices:
        print(pick)
        sleep(0.50)
    sleep(2)
    user_choices.clear()

#### Third Stage ####
def final_boss():
    while True:
        print(brick_house)

        blow_down_f = input("\nYou have found the house of the oldest pig, made of bricks.\nWhat do you want to do?? \nA) Blow the house. \nB) Knock the door and trick the pig. \n").lower()                        
        if blow_down_f == "a" or "blow" in blow_down_f:
          print("\nOh no, the house is reallly sturdy!! it has NOT been blown down.\nThe 3 pigs are safe at home... time to use some magic!")
          sleep(2.0)
          chances = 3
          print("\nYou took a magic dice out of your pocket and decided to roll it.\nYou have 3 chances to get a perfect 20")
          while chances > 0:
              sleep(0.5)
              input("\nPress ENTER to test your luck!!")
              number = rnd.randint(1, 20)
              #There is a 5% probability of winning each roll
              #The idea is that the player loses most of the time.
              if number == 21:
                  print("The magic worked!!\nYou were able to blow a storm and destroy the house!! ")
                  winner()
                  break
              elif number > 0 and number <=12:
                  chances -= 1
                  print(f"Ups, you got a {number}!!\nyou have {chances} chances left.")
                  continue
              elif number > 12 and number <=19:
                  chances -= 1
                  print(f"Almost there!! you got a {number}\nyou have {chances} chances left.")
                  continue
              else:
                pass
          if chances == 0:
              sleep(2)
              print("\n\nSeems like it is not your lucky day.")
              game_over_loser()
              break
        elif blow_down_f == "b" or "knock" in blow_down_f:
          #This is the proper winning path and twist of the story.  
          print("What is this??\nThe last pig forgot to lock the door!!\nYou have entered and eaten all the pigs.\n ")
          sleep(1.0)
          winner()
          sleep(1.0)
          break
        else:
          print("Invalid input. Please try again.")
          continue

def winner():
    print(winner_log)
    print(winning_icon)

def game_over_loser():
    print(game_over)

def ending_sec():
    sleep(1.5)
    print("\nI hope you had some fun, thank you for playing 'The Wolf's Tale'!!")

def restart():
    for times in range(3):
        replay = input("Would you like to play one more time??\nPress Y to continue\nPress N to end it\n").upper()
        if replay == "Y" or replay == "YES":
            return True  # User wants to play again
        elif replay == "N" or replay == "NO":
            print(bye_message)
            return False  # User wants to quit
        else:
            # If user enters invalid input 3 times, exit the game
            if times == 2:
                print("Too many invalid inputs. Exiting game.")
                return False
            print("\nInvalid input. Please try again.")
    return False  # Default to exit if loop completes
