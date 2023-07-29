import random

snake = {17:4,19:7,21:9,27:1}
ladder = {3:22,5:8,11:26,20:29}
n=0
m=0
c=0

def Play(n,c):

    while True :
        r = random.randrange(1,7)
        c+=1
        print("DICE : ",r)
        n=n+r
    
        if n==30:
            print("TOTAL MOVES : ",c)
            return c

        if n > 30:
            n=n-r 

        if n<30:
            if n in snake:
                n = snake[n]
                print("EATEN BY SNAKE AT : ",n)
                
            elif n in ladder:
                n = ladder[n]
                print("MOVED AT",n)

        print("POSITION : ",n)


print("         ----- PLAYER 1 IS PLAYING ------")
a=Play(n,c)
print("         ----- PLAYER 2 IS PLAYING ------")
b=Play(n,c)
if a < b:
    print("PLAYER 1 IS WINNER")
else:
    print("PLAYER 2 IS WINNER")
