import random

def guess_the_num():
    num = random.randint(1, 50)
    div=num%10
    t=num-div
    u=t+10
    print num
    count = 0
    while count != 4:
        guess = input("your should be between %d or %d:"%(t,u) )
        if num-guess != 0:
            if -2<(num-guess)<2:
                print"guess is too close"
        # elif num < guess:
        #     print"u r too high"
        # elif guess < num:
        #     print"guess is too low"''
        else:
            print"you guessed it!"
            break
        count += 1
        if count == 3:
            print "u have reached maximum limit"
            break

guess_the_num()
