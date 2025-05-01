from token import LEFTSHIFT
# Print the name of the game
print("Welcome to Treasure Island.")

# Print the reason for playing the game
print("Your mission is to find the treasure.")

# print the ASCII Logo
# ---------------------------------------------
print("""
         .-.
        (o.o)
         |=|
        __|__
      //.=|=.\\
     // .=|=. \\
     \\ .=|=. //
      \\(_=_)//
       (:| |:)
        || ||
        () ()
        || ||
        || ||
        == ==
""")
print("You are at a cross road. Where do you want to go? \n")

# Should we go left or right?
# ---------------------------------------------

left = input("Type 'left' or 'right?: \n").lower()
right = "right"

if left == "left" and right == "right":
    left = "Left"
    right = "Right"
    print("Whew we made it!")
    # swim = input("swim or wait: '\n")
else:
    if right == "right":
        print("You fell off a ledge! Game over.")
        exit()

# Wait or swim
# ---------------------------------------------

wait = input("swim or wait: \n").lower()
swim = "swim"

if wait == "wait" and swim == "swim":
    swim = "Swim"
    wait = "Wait"
    print("Good call, we are safe!")
else:
    if swim == "swim":
        print("You were eaten by an alligator. Game over!")
        exit()

# Which Door
# ---------------------------------------------

door = input("Which door will you choose? red, yellow, or blue?: \n").lower()

red = "red"
yellow = "yellow"
blue = "blue"

if door == "red" and blue == "blue" and door == "yellow":
    red = "Red"
    print(" You died. Burned by fire! Game over.")
    exit()
elif door == "yellow":
    yellow = "Yellow"
    print("You win!")
    exit()
else:
    blue = "Blue"
    print("You lose! We were eaten by beast! Game over.")
    exit()







