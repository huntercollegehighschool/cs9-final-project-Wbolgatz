"""
Name(s):Wrye Bolgatz  
Name of Project:Quest for the Holy Grail
"""
def start():
  print("Your Name is Wilbur Watson, Famous British archeologist, and you have arrived at the abandoned Pebergly castle in search of the long lost holy grail. As you approach the walls you need a way in. You can try and open the front gate or go around the walls for another option")
  choice = input("Enter 1 for front gate or 2 for Around walls.")
  if choice == "1":
    Frontgate()
  elif choice == "2":
    Aroundwalls()
def Frontgate():
  print("You manage to find a way through the deteriorating gate as you think to yourself \"the direct approach is always best\" As you make your way inside the castle you see a great hall in front of you as well as stairs on your right, these lead down and up.")
  choice = input("Enter 1 to take down stairs, 2 to enter the great hall, or 3 to go upstairs.")
  if choice == "1":
    Stairsdown()
  elif choice == "2":
    Enterhall()
  elif choice =="3":
    Upstairs()
def Stairsdown():
  print("As you make your way down the windy staircase the crafted stone brick transitions into cold mossy cobblestone. You are in the castle dungeon. As you venture deeper in you see a creepy room at the end of the corridor you're walking through it is half hidden by design and you can't see much of it without going in. This could be the perfect hiding place for the grail or simply a wild goose chase. You can head back upstairs or enter the room.")
  choice = input("Enter 1 to explore the dungeon and enter 2 to go back.")
  if choice == "1" : 
    Dungeon()
  elif choice == "2" :
    Back()
def Back():
  print ("You make your way back up the stairs and again see a great hall in front of you as well as stairs on your right, these lead down and up.")
  choice = input("Enter 1 to take down stairs, 2 to enter the great hall, or 3 to go upstairs.")
  if choice == "1":
    Stairsdown()
  elif choice == "2":
    Enterhall()
  elif choice =="3":
    Upstairs()
def Dungeon():
  print("As you warily proceed down the cold corridor a cold breeze coming from the mist puts you on edge. You walk into the room and look around slowly realizing where you are. With a clang the door of the cell that you just walked into falls into place. You try and open the bars but age has made them immovable. You are trapped. You can yell for help or try and break a tunnel through the walls.")
  choice = input("Enter 1 to shout for help and enter 2 to break your way through the walls.")
  if choice == "1" :
    Shoutforhelp()
  elif choice == "2":
    Breakout()
def Shoutforhelp():
  print("As you anxiously realize your predicament you start looking for a way to get help. All of your forms of communication are dead under the castle walls and you scream and shout for help until your breath runs out. In the end all that come are the rats. You die trapped in the dungeon of Pebergly Castle, the long dead architechs claiming another victim.")
  choice = input("GAME OVER")
def Breakout():
  print("As panic sets in you remind yourself of your goal and who you are. With some determination you know you can get out of this. As you dig with some small tools you have in your bag you manage to carve some of the aging wall away into a small passageway you can fit through. You manage to make your way into a seemingly unknown part of the castle. The only way to describe the abominations that line the walls around you would be torture devices. Your prize still could be close, or you could try and find a way out.")
  choice = input ("Enter 1 to continue exploring or 2 to try and find a way back")
  if choice == "1" :
    Continueexploring()
  elif choice == "2" :
    Findawayback()
def Continueexploring():
  print ("As you go to examine a large sharp saw, at the slightest touch it falls off the wall, impaling your leg. You dislocate it from your limb but the damage has been done. As you hobble off you quickly lose the strength to go on and bleed out on the dungeon floor.")
  choice = input("GAME OVER")
def Findawayback ():
  print ("As you make your way out of the dungeon you climb back up the staircase into the entrance to the hall. You can go upstairs or into the hall.")
  choice = input("Enter 1 to go upstairs or 2 to enter hall")
  if choice == "1" :
    Upstairs()
  elif choice == "2" :
    Enterhall()
def Enterhall(): 
  print("As you walk through what must have been a grand pair of wooden doors but are now rotting.You see a grand banquet hall with a long table surrounded with chairs. As you walk past the chairs you see a Luxurious Throne and a hallway going to the left seeming to go to a kitchen ")
  choice = input ("Enter 1 to go to the throne or 2 to go into the kitchen.")
  if choice == "1" :
    Examinethrone()
  elif choice == "2" :
    IntoKitchen()
def Examinethrone():
  print("While you walk towards the elegant throne you see a number of gargoyles that seem to be watching you. The throne has jewels or clearly places for them lining it. As you get closer you can make out what looks to be a human skeleton beside it. Right in front of the throne there seems to be a wooden plate in place of the natural floor. It could have blended in in the past but it is apparent now. You can examine the wooden floor piece or sit on the throne. ")
  choice = input ("Enter 1 to sit on the throne or 2 to examine floor.")
  if choice == "1":
    Sitthrone()
  elif choice == "2":
    examinetrapdoor
def Examinetrapdoor():
  print("As you get close to the ground to look at the wooden panel you see a small hinge right before you put your full body weight onto it. You feel the floor going out beneath you as you fall into a locked cell. The apparent trap door closes above you as you realize what you have done,You are trapped. You can yell for help or try and break a tunnel through the walls.")
  choice = input("Enter 1 to shout for help and enter 2 to break your way through the walls.")
  if choice == "1" :
    Shoutforhelp()
  elif choice == "2":
    Breakout()
def Sitthrone():
  print ("As you sit on the throne you get the eerie feeling that the gargoyles are watching your every move. But when you look closer it seems that only one is amiss. A hands distance apart you touch a small button, only visible from the throne and hear a whoosh. Behind you a small staircase has unveiled itself. You can go up the staircase or down it.")
  choice = input ("Press 1 to go downstairs press 2 to go upstairs")
  if choice == "1":
    Torturechamber()
  elif choice == "2" :
    Secretpassage()
def Torturechamber():
  print("You manage to make your way into a seemingly unknown part of the castle. The only way to describe the abominations that line the walls around you would be torture devices. Your prize still could be close, or you could try and find a way out.")
  choice = input ("Enter 1 to continue exploring or 2 to try and find a way back")
  if choice == "1" :
    Continueexploring()
  elif choice == "2" :
    Findawayback()
def IntoKitchen():
  print ("Going through a servants door of to the side of the grand hall you make your way into the kitchen. You see islands with rusted cast iron cutlury and dishes lining the walls and sinks. Hooks hang over firepits that can turn to roast and animal from all sides. This place was clearly evacuated in a hurry. After investigating all of the nooks and crannies of the place you deduce that the grail is not hidden here. You can go back and investigate the throne for the grail or take the door to the courtyard.")
  choice = input ("Enter 1 to Go back to the throne or 2 to explore the courtyard")
  if choice == "1":
    Examinethrone()
  elif choice == "2":
    Entercourtyard()
def  Entercourtyard():
  print("As you look around the courtyard you realize that a lot of the backside of the castle has gone to ruins, Wildlife has overrun the area. As you go towards the hole in the walls you see the surrounding forests to the south. You then hear a blood curdling howl as a small pack of wolves returns to their territory, unhappy about the intruder. You can only run. Do you run towards the walls and try and get out of the castle or back into the kitchen?")
  choice = input ("Enter 1 to run back into the kitchen or enter 2 to run to the walls to escape")
  if choice == "1" :
    Kitchenrun()
  elif choice =="2":
    Wallrun()
def Kitchenrun():
  print("You run back into the kitchen with the wolves right on your tail. Being an unfamiliar environment for them it takes them time to find you but you aren't able to hide forever.")
  Choice = input ("GAME OVER")
def Wallrun():
  print ("As you make your mad dash to the walls the wolves run you down. You are unable to out run them and they kill you.")
  choice = input ("GAME OVER")
def Secretpassage():
  print("As you climb the staircase you find yourself somewhere betweeen the upper floors. As you walk down a hallway you enter a room at then end. The Kings secret treasures. His vault. Silver and gold beyond imaginations surround you but they are not your goal. You walk past the artifacts into a room with a stained glass panel showing a chest. There are two levers that look like they upen the door to the room.You can pull the one on the left or the one on the right.")
  choice = input("Enter 1 to pull the one on the right or 2 to pull the one on the left")
  if choice == "1":
    Pitofspikes()
  elif choice == "2" :
    Claimthegrail()
def Pitofspikes():
  print ("As you pull the lever the floor falls out from under you giving you no time to react. You fall into a pit of spikes, being instantly impaled. You look up to see the trapdoor closing and you notice multiple skeletons around you. As everything fades to black you barely make out a cackle as well as writing on the wall saying  \"their was a reason everyone left in a hurry... although none of them made it out\"")
  choice = input("GAME OVER")
def Claimthegrail():
  print ("As you pull the lever the door opens to unveil the chest. As you pull it open You can't believe your eyes. You have found the grail. As you take out the golden cup the jewls shimmer in the light. You make your way out of the castle triumphantly carrying the most important find in centuries.")
  print ("CONGRATULATIONS YOU WIN!")
def Upstairs():
  print("As you climb the spiral staircase you walk along a corridor You can either walk down a path you see to the courtyard or head back to the entrance.")
  choice = input ("Enter 1 to go to the courtyard or 2 to go back.")
  if choice == "1":
     Entercourtyard()
  elif choice == "2" :
      Back()
def Aroundwalls():
  print("You choose to walk around the castle looking for a better way in. You find a over hanging tree near a broken down part of the wall and a small hidden door near the back. You can climb the tree or go through the side passage.")
  choice = input("Enter 1 climb the tree or 2 to go through the side passage.")
  if choice == "1" :
    Climbtree()
  elif choice == "2":
    Sidepassasge()
def Sidepassage():
  print("As you enter the side door you think to yourself \"Brains over brawn, better to acess the situation than charge straight in.\"You find yourself in a hallway with a kitchen on your right and a passage going twords a large room on your left.")
  choice = input("Enter 1 to enter kitchen or enter 2 to go into the large room")
  if choice == "1" :
    IntoKitchen()
  elif choice == "2" :
    Enterhall()
def climbtree():
  print("You manage to climb an overgrown tree and jump on the castle walls. You fall pretty hard and hurt your legs as think \"Im to old for this\". But as you walk through the overgrown courtyard you see a couple of wolves that seem to have made their home in these ruins. As the smell you they start to chase you down, and with your injured leg you are no match.")
  print("GAME OVER")


start()

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
