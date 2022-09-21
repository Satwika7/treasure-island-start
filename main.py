print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("where do you wanna go left or right\n")
dir = direction.lower()
if dir == "right":
  print("oops that's a dead end ,better luck next time\n game over")
elif dir == "left":
  way = input("you wanna go on a cycle or by a car\n")
  way1 = way.lower()
  if way=="cycle":
    print("oh no!🤦‍♂️ the tyre is flat\n game over")
  elif way == "car":
    print("great you have reached the house😃")
    color = input("there are three doors ,which one you wanna open yellow,red or blue\n")
    col = color.lower()
    if col == "red":
       print("ohh no it's fire🔥\n game over")
    elif col == "blue":
       print("ohhhhh it's water\n game over")
    elif col == "yellow":
       print("Hurraaaah! you won the treasure")
       print('''                      /^\
                        /     \
     |               | (       ) |               |
    /^\  |          /^\ \     / /^\          |  /^\
    |O| /^\        (   )|-----|(   )        /^\ |O|
    |_| |-|    |^-^|---||-----||---|^-^|    |-| |_|
    |O| |O|    |/^\|/^\||  |  ||/^\|/^\|    |O| |O|
    |-| |-|    ||_|||_||| /^\ |||_|||_||    |-| |-|
    |O| |O|    |/^\|/^\||(   )||/^\|/^\|    |O| |O|
    |-| |-|    ||_|||_||||   ||||_|||_||    |-| |-|
    |O| |_|----|___|___|||___|||___|_|_|    |O| |O|
    |_|                                         |_|
       /_______________________________________\
    __|_______________________________________|___|''')
    else:
      print("invalid  \n game over.")
  else:
      print("invalid  \n game over.")
else:
      print("invalid  \n game over.")    


