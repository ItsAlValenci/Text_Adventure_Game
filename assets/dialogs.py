greetings_log = ["Hail and well met, adventurer!","Greetings, brave hero.",
            "May the gods bless your journey.","Well hello there, fellow traveler.",
            "Good morrow, fair maiden.","Salutations, esteemed wizard.",
            "Ahoy, matey! What brings you to these waters?","It's not often we see outsiders around here.",
            "Hello, hello! are you up for an adventure?","Greetings and felicitations, dear friend!"]

cave_start = ("You just left your cave located in the south of a dense forest.\nNow, you are in the main path and each house is located in different areas of the forest.\n")

cave_log = ["You stumble and fall into a trap.\nThe pigs are laughing at you.",
               "As you close in on the pigs, you suddenly remember you're a vegetarian and decide to let them go.",
               "One of the pigs turns out to be much smarter than you expected and leads you into a trap.",
               "The pigs gang up on you and chase you away from their territory.",
               "You realize that chasing pigs is a fruitless pursuit and decide to give up and find some easier prey.",
               "You have decided to become vegan.\nYou are back into your cave and decide to hibernate."]

def get_welcome_message(player_name):
    return f"""   
Welcome {player_name} to 'The Wolf\'s Tale'
A dynamic game based on the story of 'The 3 Little Pigs'
          
In this world, you play as the wolf, which is really hungry and just recently 
found out that there were three little pigs wondering in his forest and
your goal is to find their houses to eat each pig
          
This is your story so you can go any way you want. Just remember... don't visit the same place twice.
Let the hunt begin!!
                    
Press "Enter" to start: """

winner_log = ("""You did it!!\nYou have caught all three little pigs. It is time to enjoy a feast!!""")

