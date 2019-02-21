import random

def guess_the_num():
    num = random.randint(1, 50)
    t=num-10
    u=num+10
    #print num
    count = 1
    while count != 4:
        guess = input("your should be between %d or %d:"%(t,u) )
        if -5<(num-guess)<5:
            print"guess is too close"
        elif num < guess:
            print"u r too high"
        elif guess < num:
            print"guess is too low"''
        else:
            print"you guessed it!"
            break
        count += 1
    if count == 3:
        print "u have reached maximum limit"

guess_the_num()
