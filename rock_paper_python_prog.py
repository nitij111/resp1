import random
op=['r','p','s']
#windows emoji keyboard shortcut is windows key+semicolon
emoji={'r':'🪨','p':'📃','s':'✂️'}
ur_score=0
comp_score=0
while True:    
    a=random.choice(op)
    b=input('enter (r/p/s): ')
    print(f"computer's choice is {a} {emoji[a]}")
    print(f"your choice is {b} {emoji[b]}")
    if b==a:
        print("Tie")
        print("your score is:", ur_score)
        print("comp score is:", comp_score)
    elif (b=='r' and a=='s')or(b=='p' and a=='r')or(b=='s' and a=='p'):
        print("you win")
        ur_score+=1
        print("your score is:", ur_score)
        print("comp score is:", comp_score)
    else:
        print("you lose") 
        comp_score +=1
        print("your score is:", ur_score)
        print("comp score is:", comp_score)
    choice=input("do u want to play again(yes/no): ").lower()
    if choice=='yes':
        continue
    elif choice=='no':
        print("thankyou for playing!!!!")
        break

