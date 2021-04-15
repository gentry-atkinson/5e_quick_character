###################################################################
#Author: Gentry Atkinson                                          #
#Date: 15 April, 2021                                             #
#Description: this script will generate a level one character for #
#  Dungeons and Dragons 5th Edition. All game is from the         #
#  standard reference document.                                   #
###################################################################

import rand

def rollAttr:
    roll = [rand.randint(1,7), rand.randint(1,7), rand.randint(1,7), rand.randint(1,7)]
    return sum(roll) - min(roll)

class character:
    __init__:
        st = 0
        de = 0
        co = 0

if __name__ == "__main__":
    for _ in range(10):
        print(rollAttr)
