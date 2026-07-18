import random
'''
1 for snake
-1 for water
0 for gun

'''
computer = random.choice([-1 ,0 ,1])
youstr = input("Enter your choice: ")
youDict = {"s" : 1 , "w" : -1 , "g" : 0}
reverseDict = {1: "snake" , -1: "water" , 0: "gun"}

you = youDict[youstr]

# BY NOW WE HAVE TWO NUMBERS (VARIABLES) YOU AND COMPUTER 

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("YOU WIN !")

    elif(computer == -1 and you == 0):
        print("YOU LOSE !")

    elif(computer == 1 and you == -1):
        print("YOU LOSE !")

    elif(computer == 1 and you == 0):
        print("YOU WIN !")

    elif(computer == 0 and you == -1):
        print("YOU WIN !")

    elif(computer == 0 and you == 1):
        print("YOU LOSE !")

    else:
        print("Something went wrong")    



