###################################################################
#Author: Gentry Atkinson                                          #
#Date: 26 April, 2021                                             #
#Description: this script will generate a level one character for #
#  Dungeons and Dragons 5th Edition. All game is from the         #
#  standard reference document.                                   #
###################################################################
from random import randint


def roll4drop1():
    roll = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    return sum(roll) - min(roll)

def roll3():
    roll = [randint(1,6), randint(1,6), randint(1,6)]
    return sum(roll)

def roll2add4():
    roll = [randint(1,6), randint(1,6)]
    return sum(roll)+4

def roll(n):
    return randint(1, n)

def rollD4():
    return roll(4)

def rollD6():
    return roll(6)

def rollD8():
    return roll(8)

def rollD10():
    return roll(10)

def rollD12():
    return roll(12)

def rollD20():
    return roll(20)

def rollD100():
    return roll(100)


if __name__ == '__main__':
    stats = [roll4drop1(),roll4drop1(),roll4drop1(),roll4drop1(),roll4drop1(),roll4drop1()]
    stats.sort()
    print(' '.join([str(i) for i in stats]))

    #Below here is an experiment to find the expected value of roll4drop1
    #The answer seems to be a little over 12.2 
    # poop = 0
    # ROLLS = 100000
    # for _ in range(ROLLS):
    #     poop += roll4drop1()
    # print(poop/ROLLS)
