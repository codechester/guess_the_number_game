import random,math

print "Hello there, welcome to guess the number game."
print "Rules :-"
print "  "
print "1. Just guess the right number between 1 to 10 (1 and 10 inclusive)"
print "2. You get 7 chances for each number guess"
print "3. +5 for correct guess :D "
print "4. -1 in case you couldn't guess :("
print "  "
print "  "
print "  "

point=0

while(1):
    print """------------|start guessing|----------------
                  \  /
                   \/"""
    a=random.randint(1,10)
    for i in range(0,7):
        c=input()
        if a==c:
            print "right guess :D"
            point=point+5
            break
        else:
            if i==6:
                point-=1
                print "Better luck next time"
            else:
                if abs(a-c) <=2:
                    print "Your almost there :)"
                if abs(a-c) >=4:
                    if c>a:
                        print """Too high :\ """
                    else:
                        print """Too low  :\ """
                if abs(a-c) >2 and abs(a-c)<4:
                    print "Not bad, getting closer "
            

    print "---------------------------------------------"
    print "Do yo wish to play again YES-1 ,NO-0"
    a=input()
    if a!=1:
        if point<0:
            print "Your score =",0
        else:
            print 'Your score =',point
        break
    else:
        continue
    




    
    

