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
#Create greatings for Program
print("Welcome to Treasure Island.")
#Create a Title program
print("Your mission is to find the treasure.")
#User give input from keyboards, ask to give input left or right in new line
direction = input("You are at a cross road. Where you want to go ? Type 'left' or 'right' \n")
#if input direction true (left), ask user to give input swim or wait
if direction == "left":
  #sow = swim or wait
    sow = input("You've come to a lake. There is an island in the middle of the lake. Type wait to 'wait' for a boat. Type 'swim' to swim across.\n")
    #if input sow true (wait), ask user to give input, which one doors want you choose, based on 4 condition (yellow, red,blue, and anything else)
    if sow == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        #if condition 1 true, you win! but, if its is not true, check condition 2 (elif)
        if door == "yellow":
            print("You win!")
        #if condition 2 not true, check condition 3 (elif)
        elif door == "red": 
            print("Burned by fire. Game Over.")
        #if condition 3 not true check condition 4 (else condition)
        elif door == "blue":
            print("Eaten by beats. Game over.")
        #if all of 3 condition not true, print condition 4 (Game Over)
        else:
            door == "yellow" or door == "red" or door == "blue"
            print("Game Over.")    
     #if sow != wait print else statment below
    else:
        print("Attacked by trout. Game over")
 #if direction != left print else statment below
else:
    print("Fall into a hole. Game Over.")
    
    
        
        
#ASCII Art
    #https://ascii.co.uk/art
