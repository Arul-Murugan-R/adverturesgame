answer=input("Are u ready to Start the Game yes or no :")

if answer.lower() == "yes":
    answer=input("Ok lets Begin which direction would u like to choose right or left :")
    
    if answer.lower() =="right":
        answer = input("There is a pond Do u like to Get some water yes or no :")

        if answer.lower() == 'yes':
            print("GAME OVER ,since the water consists of poisons gases ")

        else :
            print("S u had been escaped bec the pond consists of poisons gases ")
        

    elif answer.lower() == "left":
        answer = input("Elephants had been surrounded ur area do u like to run or hide")
        
        if answer.lower() == 'run':
            print("Sorry to say this GAME OVER u had been killed by Elephants")
        
        else :
            print("you r Safe now ")
    else :
        print("Since u r answered rough ur game is over")
else :
    print("Ok hope u will try this game next time when u r free ")

