import time

defense = 1
attack = 1

def item_selection():
  
  first_item = input("What will you equip in battle traveller? Choose between a sword or a helmet or nothing.\n").lower()
  
  if first_item == "sword":
    global attack
    attack += 1
  elif first_item == "helmet":
    global defense
    defense += 1
  else:
    attack = 0
    defense = 0
  print(f"Your attack for this journey is {attack} and your defense is {defense}.\n")

def castle():
  print("You walk through the gleaming forest and across the drawbridge towards the entrance, only to be greeted by a foul odor and darkness.\n")
  time.sleep(3)
  print("You light a torch preparing to venture forth when you are greeted by two options, a broken door and a dark stairwell. Which do you choose?\n")
  time.sleep(3)
  c1 = input("Enter door or stairs to continue.\n")

  if c1 == "stairs":
    stairs()
  else:
    door()
    

def stairs():
  print("You creep towards the stairs noticing the misalignment of the beams of the stairwell.\n")
  time.sleep(3)
  print("Looking onwards and shining a light allows you to reveal the true nature of these stairs, moist wooden beams with multiple layers of rot.\n")
  time.sleep(5)
  print("Nonetheless, you gather up the courage and start to ascend. You feel the sogginess of each board as you step up them, creaking and warping around your steps.\n")
  time.sleep(6)
  print("The final step is dry, as you plant your foot you hear a loud crack.\n")
  time.sleep(3)
  print("uh oh\n")
  time.sleep(2)
  print("The stairwell crashes beneath you, sending you into freefall. You hit the ground with a large thud.\n")
  time.sleep(3)
  
  global defense
  defense -= 1
  if defense == 1:
    print(f"Your defense is now {defense}, you better be careful out there.")
    stairs_battle()
  else:
    print(f"Your defense is now {defense}.")
    print("Without a helmet you sustain serious head trauma on the way down, rendering you useless.\n")
    time.sleep(4)
    print("As the light of the torch fades, you fade along with it. Such is the way of the warrior.\n")

def stairs_battle():
    print("As you get up you see a figure approach from the distance, still unable to make out the proportions due to blurry vision.\n")
    time.sleep(3)
    sb1 = input("Unable to tell what the figure it infront of you, do you decide to fight or run?\n").lower()
    if sb1 == "fight":
        print("As you scramble to get your wits, you find a dagger covered by rubble by where you fell.\n")
        time.sleep(1)
        global attack
        attack += 1
        print(f"After equipping the dagger in a rush, your attack is now {attack}, and you prepare to take on the monster in front of you.")
        time.sleep(3)
        print("The figure finally steps forward enough to be recognized, unveiling a cloak covered in fungus and mold to reveal a yellowed skeletal body and glowing red eyes.\n")
        time.sleep(5)
        print("You attack the figure and deal one damage by slashing your dagger into it's body, crumbling the left arm and dealing 1 point of damage\n")
        time.sleep(5)
        print("The skeleton, unbothered by the loss of it's arm, lunges forwards and strikes you across the chest as you try to dodge, dealing 1 damage.\n")
        time.sleep(5)
        print("As the skeleton's blade finishes crossing your body, you're able to take a hold of the arm that did so, ripping it from it's socket.\n")
        time.sleep(5)
        print("The skeleton is rendered useless and you finish it off by punting its head from its body.\n")
        time.sleep(3)
        sb2 = input("You find a key and map in the skeleton's body, revealing the ability to safely leave now or venture forth dwon the path the skeleton came from.\n Do you leave or continue?\n").lower()
        
        if sb2 == "continue":
            print("You venture on and unlock a treasure room, revealing a powerful blade glowing red. Inscribed on it reads 'The Ebony Blade'.\nYou venture home with this new found treasure.\n")
        else:
            print("You hastily return home with no loot in hand, only a bloody shirt and chipped dagger, you survive to venture on another day.\n")
    else:
        print("You try to run, instead finding yourself unable to find a definite exit while the figure creeps towards you.\n")
        time.sleep(4)
        print("Panicked and scared you feel fear taking over and just before you're able to think about what to do, you feel a cold piercing feeling throughout your body\n")
        time.sleep(6)
        print("You collapse to the ground and see the figure laugh above your dying corpse. You bleed out as he walks away, joining the many adventurers just like you.\n") 
def door():
    print("As you head towards the door you take a look around and examine the true condition of the castle.\nMoss covered stone line the walls with many undiscovered fauna littered across the floor.\n")
    time.sleep(5)
    d1 = input("You reach the door and are able to take a peek inside before opening, do you?\nType y or n to continue.\n").lower()
    if d1 == "y":
        print("You notice the door is encased in a thin layer of an unknown cloth material.")
        time.sleep(3)
        print("You slowly peel back the cloth as it has been binded to the door by moisture and fungus after many years.\n")
        time.sleep(3)
        print("As you look into the cracks you see a large figure guarding what appears to be a chest.\n As you begin to look away you notice that it wears some sort of blindfold contraption.\n")
        time.sleep(3)
        print("You're able to slowly pry the door open to greet the beast, but quietly since you assume it cannot see.\n")
        time.sleep(2)
        d3 = input("You make your way but notice you might be able to get a sneak attack on the beast, do you take this chance?\nType y or n to continue.")
        if d3 == "y":
            global attack
            print(f"You slowly walk up the staircase and equip the weapon from your belt, which deals {attack} damage and getting ready to take the overhead angle from the balcony that sits above the now apparent troll figure.\n")
            time.sleep(6)
            if attack == 2:
                print("You successfully leap onto the troll and stab your sword into it's head, dealing 2 damage and stunning it.\n")
                time.sleep(4)
                print("The troll tries to fling you off but you're able to leap onto a nearby wooden beam and get down from there, at the expense of a few splinters in both hands.\n")
                time.sleep(6)
                print("The troll locks on to you and trudges towards you, throwing a rock which you barely avoid.\n")
                time.sleep(2)
                print("You're able to dodge one final swing from the troll because of how slow it swings, and are able to slash its ankles, and deal the killing blow.\n")
                time.sleep(5)
                print("Searching for the chest frantically while your hands bleed from splinters, you finally find it and pull out a dusty golden crown with numerious colorful gemstones inside of it.\n You wonder who once inhabited such a place with such fortune.\n")
                time.sleep(8)
                print("After equipping your new found gear, you feel stronger and lighter making you able to move faster.\n")
                time.sleep(3)
                print("You make your way home after looting the castle and bandaging your hands, to return to the village with another sucessful adventure complete.\n")
            else:
                print("You attempt to jump on the troll but your dagger isn't sharp enough to pierce its skin.\n")
                time.sleep(3)
                print("The troll flings you off and you land on a pile of bones and flesh nearby.\n")
                time.sleep(2)
                global defense
                defense -= 1
                print(f"Whole body sore and in pain, you barely manage to get up, leaving you with {defense}, you better tread carefully.\n")
                time.sleep(3)
                print("You quickly spot a lever in the distance which seems to release a spike wall trap meant for adventures like you.\n")
                time.sleep(3)
                print("Attempting to lure the troll over to where you are you begin to pelt it with rocks to try to get its attention which works as it slowly stomps over.\n")
                time.sleep(4)
                print("As the troll steps close enough to the trap, you activate it cause a hinged contraption to release and stab the troll numerous times killing it instantly in the process.\n")
                time.sleep(5)
                print("As you go to walk over to loot the chest you feel an incredible burning sensation dwon your leg and realise one of the spikes left a huge gash along your thigh.\n")
                time.sleep(4.5)
                print("Desperate to find any sort of bandaging you make a makeshift tourniquet and make your way over to the chest where you find some proper bandages, albeit for only one application.\n")
                time.sleep(6)
                print("Inside the chest you find a mace that glows green, and inscribed is text that you are unable to read but holding it gives you the feeling of strength.\n")
                time.sleep(5)
                print("You limp out of the castle with your new weapon back to your village to get treated. Everyone welcomes you as a legend for such a tale.\n")
        else:
            print("Not getting a headset seems to be a foolish move, as the beast hears you coming and swipes you with the wooden beam he holds, crushing your ribs and organs instantly.\n")
    else:
        print("Instead, you slowly reach for the handle to open the door, realizing it will take more than a simple tug.\n")
        time.sleep(2)
        print("You back up and prepare to use both hands and slowly lean back to tryand pry the door open.\n")
        time.sleep(2)
        print("The door finally gives and you're greeted with a large blueish figure holding a plank of wood you can only assume it ravaged from the castle itself.\n")
        time.sleep(4)
        print("Your heart races as you decide what to do next against what you believe to be a troll.\n")
        time.sleep(2)
        print("You don't have much time before it notices you're there.\n")
        time.sleep(1.8)
        db1 = input("There is a spiral staircase leading to an unknown room or a grate leading to an escape by river?\n Which do you choose?\n Type river or spiral to continue. Better hurry\n").lower()
        time.sleep (4)
        if db1 == "river":
            print("You quickly dive towards the grate and quickly cover yourself in as you prepare to traverse down the stream. The cold water feels refreshing.\n")
            time.sleep(5)
            print("You make it down to the exit where there's a 5 foot drop, and reluctantly plummet as there is no other way.\n")
            time.sleep(4)
            dloot = input("After you fall you find a body with a bag laying next to it? Do you decide to loot it?\nType y or n.").lower()
            if dloot == "y":
                print("You find a gold necklace with a black gem embedded inside it. You equip it and begin to head home.\n")
                time.sleep(3)
                print("As you're walking you hear a voice whisper in your ear 'your sins will be remembered.'\n")
                time.sleep(3)
                print("You decide to brush this off and continue going without telling anyone, because you don't want to be labeled a witch and die by drowning.\n")
                time.sleep(5)
                print("When you return home you sit down and instantly keel over in pain.\nUnknowingly the necklace has burned a hole through your chest and has sunk right through you.\n")
                time.sleep(6)
                print("You hear once last voice, unable to deciper what it says as your existence fades into nothingness\n")
            else:
                print("You decide to pay respects and continue on your way home, where you narrowly survive again with another tale to tell around the fire.\n")
        else: 
            print("You try to run towards the staircase but the creature beats you there and swipes the stairs from underneath of you, and you fall, trapped forever under a pile of debris.\n")
   
            
            
        
        
    
    
    
    
    
def shack():
  print("poop")


print('''
                                ,-.
                               ("O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)"-._     /   )
               "-._ "-'""( )/    
                   "-/"-._" `. 
                    /     "-.'._
                   /\       /-._"-._
    _,---...__    /  ) _,-"/    "-(_)
___<__(|) _   ""-/  / /   /
 '  `----' ""-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-""      __.,'/   /   ___                 /,
  /    ,--""/  / /   /,-""   """-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  """ ,-'
   `-._  /  / /   /_,'            ""--"
       "/  / /   /"         
       /  / /   /
      /  / /   /  
     /  |,'   /  
    :   /    /
    [  /   ,'   
    | /  ,'
    |/,-'
    P'
''')
time.sleep(3)
print("Deathfall Castle")
time.sleep(1)
print("Your mission is to find the treasure and escape alive.") 
time.sleep(2)
print("A story game by:")
time.sleep(1)
print('''
      
  █████ ▓██   ██▓ ▄▄▄       ██▀███   ▄▄▄      
▒██▒  ██▒▒██  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    
▒██░  ██▒ ▒██ ██░▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  
▒██   ██░ ░ ▐██▓░░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ 
░ ████▓▒░ ░ ██▒▓░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒
░ ▒░▒░▒░   ██▒▒▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
  ░ ▒ ▒░ ▓██ ░▒░   ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░
░ ░ ░ ▒  ▒ ▒ ░░    ░   ▒     ░░   ░   ░   ▒   
    ░ ░  ░ ░           ░  ░   ░           ░  ░
         ░ ░                                  
''')
time.sleep(2)

item_selection()

s1 = input("Are you ready to continue? y or n \n").lower()

if s1 == "y":
  s2 = input("You spot a castle in the distance and an abandoned shack, which will you go to first? Enter castle or shack to proceed.\n").lower()
  if s2 == "castle":
    castle()
  else:
    print("You hear an voice whisper 'You're an adventurer come on!' as you make your way to the castle instead of a boring old shack\n")
    time.sleep(5)
    castle()
else:
  quit()
  
  
  




