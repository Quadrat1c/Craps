from random import randint


die1 = randint(1,6)
die2 = randint(1,6) 
total = die1 + die2 
#die1 + die2


user_value = input("Do you want to play dice ? 'y' or 'n' ")

if user_value == "n":
    print ("You're dead to me!")
elif user_value != "n" and user_value != "y":
    print ("Huh?")
elif user_value == "y":
    print ("You rolled: ", (die1),"&",(die2), "a total of: ", (total))
    while user_value == "y":
        if total == 2 or total == 3 or total == 12:
            print ("You crapped out rookie!")
            break
        elif total == 7 or total == 11:
            print ("Winner winner chicken dinner!")
            break
        else:
            point = total
            print ("") 
            print ("The point is now: ", total)
            break


next_roll = input("Hit enter to roll again.")

die3 = randint(1,6)
die4 = randint(1,6) 
total1 = die3 + die4


while total1 != 7:
    print ("You rolled: ", (die3),"&",(die4), "a total of: ", (total1))
    if total1 == point:
        print ("")
        print ("Winner winner chicken dinner!")
        break 
    else:
        next_roll = input("Hit enter to roll again.")
        die3 = randint(1,6)
        die4 = randint(1,6) 
        total1 = die3 + die4
    
if total1 == 7:
    print ("You rolled: ", (die3),"&",(die4), "a total of: ", (total1))
    print ("")
    print ("Seven out..")
