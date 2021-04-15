###################################################################
#Author: Gentry Atkinson                                          #
#Date: 15 April, 2021                                             #
#Description: this script will generate a level one character for #
#  Dungeons and Dragons 5th Edition. All game is from the         #
#  standard reference document.                                   #
###################################################################

from random import randint, shuffle

def rollAttr():
    roll = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    return sum(roll) - min(roll)

class Character:
    def __init__(self):
        self.stats = {
            'str' : rollAttr(),
            'dex' : rollAttr(),
            'con' : rollAttr(),
            'int' : rollAttr(),
            'wis' : rollAttr(),
            'cha' : rollAttr(),
        }


        fnFile = open('first_name.txt', 'r');
        fNames = fnFile.read().strip().split('\n')
        fnFile.close()

        lnFile = open('last_name.txt', 'r');
        lNames = lnFile.read().strip().split('\n')
        lnFile.close()

        oFile = open('origins.txt', 'r');
        origins = oFile.read().strip().split('\n')
        oFile.close()

        shuffle(fNames)
        shuffle(lNames)
        shuffle(origins)
        self.name = fNames[0] + ' ' + lNames[0]
        self.origin = origins[0]
        self.skills = []

    def setClass(self):
        classes = []
        main = max(self.stats.values())
        if self.stats['str'] == main:
            classes.append('melee fighter')
            classes.append('barbarian')
        if self.stats['con'] == main:
            classes.append('tank fighter')
            classes.append('tank cleric')
        if self.stats['dex'] == main:
            classes.append('archer ranger')
            classes.append('rogue')
        if self.stats['int'] == main:
            classes.append('wizard')
            classes.append( 'artificer')
        if self.stats['wis'] == main:
            classes.append('healer cleric')
            classes.append( 'caster ranger')
        if self.stats['cha'] == main:
            classes.append('bard')
            classes.append('sorcerer')
        shuffle(classes)
        self.cl = classes[0]
        self.dispClass = (self.cl.split()[-1]).capitalize()

    def setRace(self):
        races = []
        if self.cl == 'archer ranger':
            races.append('Wood Elf')
            races.append('Half Elf')
        elif self.cl == 'artificer':
            races.append('Rock Gnome')
            races.append('High Elf')
        elif self.cl == 'barbarian':
            races.append('Human')
            races.append('Half Orc')
        elif self.cl == 'bard':
            races.append('Half Elf')
            races.append('Lightfoot Halfling')
        elif self.cl == 'caster ranger':
            races.append('Wood Elf')
            races.append('Hill Dwarf')
        elif self.cl == 'druid':
            races.append('Human')
            races.append('Wood Elf')
        elif self.cl == 'healer cleric':
            races.append('Human')
            races.append('Hill Dwarf')
        elif self.cl == 'melee fighter':
            races.append('Human')
            races.append('Half Orc')
        elif self.cl == 'paladin':
            races.append('Human')
            races.append('Half Elf')
        elif self.cl == 'rogue':
            races.append('Lightfoot Halfling')
            races.append('Drow')
        elif self.cl == 'melee fighter':
            races.append('Human')
            races.append('Half Orc')
        elif self.cl == 'sorcerer':
            races.append('Human')
            races.append('Drow')
        elif self.cl == 'tank cleric':
            races.append('Human')
            races.append('Hill Dwarf')
        elif self.cl == 'tank fighter':
            races.append('Human')
            races.append('Mountain Dwarf')
        elif self.cl == 'drow':
            races.append('Drow')
            races.append('Half Elf')
        elif self.cl == 'Wizard':
            races.append('Human')
            races.append('High Elf')
        else:
            raise Exception("Bad class when picking race.")

        shuffle(races)
        self.race = races[0];


if __name__ == "__main__":
        myChar = Character()
        print('Greeings, I am ' + myChar.name + ' of ' + myChar.origin.split(',')[0])
        myChar.setClass()
        print('I am a mighty ' + myChar.dispClass)
        print(myChar.stats)
        myChar.setRace()
        print('I was born a ' + myChar.race)
