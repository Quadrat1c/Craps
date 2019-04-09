from random import randint
from time import sleep

# Putting a 'while' loop here could make this a lot more efficient and would kill 
# half the code it took to write this in its current state.

# Something like -If the dice added up equals any number that doesn't equate to a win or a loss, 
# then the values need to be discarded and new numbers needs to be re-rolled.-

die_1 = []
die_2 = []

chance_1 = (randint(1,6))
chance_2 = (randint(1,6))

die_1.append(chance_1)
die_2.append(chance_2) 

print("")
print("Welcome to the Craps table at Javis Casino! ")

sleep (2)

print("")
print("You wanna roll some dice or what? ")

sleep(2)

user_value = input(" ('y') or ('n') ")

sleep(2)

# Values for rolling yes or no
if user_value == 'y':
    print("")
    print("You rolled a " + str(die_1) + " and a " + str(die_2))
   

if user_value =='n':
    print("")
    print("Youre rolling anyways, buddy.")
    sleep(2)
    print("You rolled a " + str(die_1) + " and a " + str(die_2))
   

sleep(2)

# Values for yes and no rolls, combined with outcome statements
if user_value == 'y' and die_1 + die_2 == (2, 3, 12):
    print("")
    print("Ya lost, chump! ")    
            
if user_value == 'n' and die_1 + die_2 == (2, 3, 12):
    print("")
    print("Shoulda never rolled, you lost anyways, oh wait... you didnt even want to roll didya? ")
    
if user_value == 'y' and die_1 + die_2 == (7, 11):
    print("")
    print("Congratulations, you won! ")

if user_value == 'n' and die_1 + die_2 == (7, 11):
    print("")
    print("Good thing I rolled for ya! Youre a millionaire now, baby! Can I have a generous tip for my services? ")
    
# For some reason, it's not outputting the dialogue here
if user_value == 'y' and die_1 + die_2 == (4, 5, 6, 8, 9, 10):
    print("")
    print("Nothin, you wanna roll again? ")

if user_value == 'n' and die_1 + die_2 == (4, 5, 6, 8, 9, 10):
    print("")
    print("Nothin, you wanna roll again? ")

sleep(2)

user_value_2 = input("('y') or ('n') ")

sleep(2)

# Values for rolling yes or no
if user_value_2 == 'y':
    print("")
    print("You rolled a " + str(die_1) + " and a " + str(die_2))

if user_value_2 =='n':
    print("")
    print("Youre rolling anyways, buddy.")
    sleep(2)
    print("You rolled a " + str(die_1) + " and a " + str(die_2))

sleep(2)

# Values for yes and no rolls, combined with outcome statements
if user_value_2 == 'y' and die_1 + die_2 == (2, 3, 12):
    print("")
    print("Ya lost, chump! ")    
            
if user_value_2 == 'n' and die_1 + die_2 == (2, 3, 12):
    print("")
    print("Shoulda never rolled, you lost anyways, oh wait... you didnt even want to roll didya? ")
    
if user_value_2 == 'y' and die_1 + die_2 == (7, 11):
    print("")
    print("Congratulations, you won! ")

if user_value_2 == 'n' and die_1 + die_2 == (7, 11):
    print("")
    print("Good thing I rolled for ya! Youre a millionaire now, baby! Can I have a generous tip for my services? ")

#  For some reason, it's not outputting the dialogue here
if user_value == 'y' and die_1 + die_2 == (4, 5, 6, 8, 9, 10):
    print("")
    print("Nothin, you wanna roll again? ")

if user_value == 'n' and die_1 + die_2 == (4, 5, 6, 8, 9, 10):
    print("")
    print("Nothin, you wanna roll again? ")

sleep(2)
   
user_value_2 = input("('y') or ('n') ")