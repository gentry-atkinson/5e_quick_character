###################################################################
#Author: Gentry Atkinson                                          #
#Date: 15 April, 2021                                             #
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

if __name__ == '__main__':
    print(roll4drop1())
