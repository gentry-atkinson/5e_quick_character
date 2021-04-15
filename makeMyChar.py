###################################################################
#Author: Gentry Atkinson                                          #
#Date: 15 April, 2021                                             #
#Description: this script will generate a level one character for #
#  Dungeons and Dragons 5th Edition. All game is from the         #
#  standard reference document.                                   #
###################################################################

from random import randint, shuffle, choice

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
        self.skills = set()
        self.tProfs = set()
        self.langs = set(['Common'])
        self.aProfs = set()
        self.wProfs = set()
        self.size = ""
        self.speed = 0
        self.gold = 0

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
        elif self.cl == 'sorcerer':
            races.append('Human')
            races.append('Drow')
        elif self.cl == 'tank cleric':
            races.append('Human')
            races.append('Hill Dwarf')
        elif self.cl == 'tank fighter':
            races.append('Human')
            races.append('Mountain Dwarf')
        elif self.cl == 'warlock':
            races.append('Drow')
            races.append('Half Elf')
        elif self.cl == 'wizard':
            races.append('Human')
            races.append('High Elf')
        else:
            raise Exception("Bad class {} when picking race.".format(self.cl))

        shuffle(races)
        self.race = races[0];

    def updateAttrForRace(self):
        if self.race==('Wood Elf'):
            self.stats['dex'] += 2
            self.stats['wis'] += 1
        elif self.race==('Half Elf'):
            self.stats['cha'] += 2
            self.stats['dex'] += 1
            self.stats['con'] += 1
        elif self.race==('Rock Gnome'):
            self.stats['int'] += 2
            self.stats['con'] += 1
        elif self.race==('High Elf'):
            self.stats['dex'] += 2
            self.stats['int'] += 1
        elif self.race==('Human'):
            self.stats['str'] += 1
            self.stats['con'] += 1
            self.stats['dex'] += 1
            self.stats['int'] += 1
            self.stats['wis'] += 1
            self.stats['cha'] += 1
        elif self.race==('Half Orc'):
            self.stats['str'] += 2
            self.stats['con'] += 1
        elif self.race==('Lightfoot Halfling'):
            self.stats['dex'] += 2
            self.stats['cha'] += 1
        elif self.race==('Hill Dwarf'):
            self.stats['con'] += 2
            self.stats['wis'] += 1
        elif self.race==('Mountain Dwarf'):
            self.stats['con'] += 2
            self.stats['str'] += 2
        elif self.race==('Drow'):
            self.stats['dex'] += 2
            self.stats['cha'] += 1
        else:
            raise Exception("Bad race {} when updating attributes.".format(self.race))

    def updateAttrForClass(self):
        attributes = []
        if self.cl == 'archer ranger':
            attributes = ['dex', 'wis', 'con', 'int', 'str', 'cha']
        elif self.cl == 'artificer':
            attributes = ['int', 'dex', 'con', 'wis', 'cha', 'str']
        elif self.cl == 'barbarian':
            attributes = ['str', 'con', 'dex', 'int', 'wis', 'cha']
        elif self.cl == 'bard':
            attributes = ['cha', 'dex', 'con', 'int', 'str', 'wis']
        elif self.cl == 'caster ranger':
            attributes = ['wis', 'str', 'con', 'dex', 'int', 'cha']
        elif self.cl == 'druid':
            attributes = ['wis', 'str', 'con', 'dex', 'int', 'cha']
        elif self.cl == 'healer cleric':
            attributes = ['wis', 'str', 'con', 'dex', 'int', 'cha']
        elif self.cl == 'melee fighter':
            attributes = ['str', 'con', 'dex', 'cha', 'int', 'wis']
        elif self.cl == 'paladin':
            attributes = ['str', 'cha', 'con', 'dex', 'wis', 'int']
        elif self.cl == 'rogue':
            attributes = ['dex', 'cha', 'int', 'wis', 'con', 'str']
        elif self.cl == 'sorcerer':
            attributes = ['dex', 'wis', 'con', 'int', 'str', 'cha']
        elif self.cl == 'tank cleric':
            attributes = ['con', 'str', 'wis', 'dex', 'int', 'cha']
        elif self.cl == 'tank fighter':
            attributes = ['con', 'str', 'cha', 'dex', 'int', 'wis']
        elif self.cl == 'warlock':
            attributes = ['cha', 'dex', 'con', 'str', 'int', 'wis']
        elif self.cl == 'wizard':
            attributes = ['int', 'dex', 'con', 'cha', 'wis', 'str']
        else:
            raise Exception("Bad class {} when updating attributes.".format(self.cl))
            return

        if len(attributes) != 6:
            raise Exception("Wrong number of attributes to update.")
            return

        newAttr = list(self.stats.values())
        newAttr.sort(reverse=True)
        for i in range(6):
            self.stats[attributes[i]] = newAttr[i]

    def setBackground(self):
        if self.dispClass == 'Artificer':
            bg = ['Guild Artisan', 'Sage']
        elif self.dispClass == 'Barbarian':
            bg = ['Outlander', 'Soldier']
        elif self.dispClass == 'Bard':
            bg = ['Entertainer', 'Charlatan']
        elif self.dispClass == 'Cleric':
            bg = ['Acolyte', 'Hermit']
        elif self.dispClass == 'Fighter':
            bg = ['Folk Hero', 'Soldier']
        elif self.dispClass == 'Paladin':
            bg = ['Noble', 'Acolyte']
        elif self.dispClass == 'Ranger':
            bg = ['Hermit', 'Folk Hero']
        elif self.dispClass == 'Rogue':
            bg = ['Urchin', 'Criminal']
        elif self.dispClass == 'Sorcerer':
            bg = ['Noble', 'Charlatan']
        elif self.dispClass == 'Warlock':
            bg = ['Guild Artisan', 'Noble']
        elif self.dispClass == 'Wizard':
            bg = ['Sage', 'Noble']
        else:
            raise Exception("Bad class {} when setting backgrounds.".format(self.dispClass))
            return

        shuffle(bg)
        self.bg = bg[0]

    def setSkillsForRace(self):
        if self.race==('Wood Elf'):
            self.skills.add('Perception')
            self.langs.add('Elven')
            self.wProfs.add('longsword')
            self.wProfs.add('shortsword')
            self.wProfs.add('shortbow')
            self.wProfs.add('longbow')
            self.size = 'Medium'
            self.speed = 30
        elif self.race==('Half Elf'):
            self.langs.add('Elvish')
            self.langs.add('Dwarvish')
            self.skills.add('Perception')
            self.skills.add('Stealth')
            self.skills.add('Acrobatics')
            self.wProfs.add('longsword')
            self.wProfs.add('shortsword')
            self.wProfs.add('shortbow')
            self.wProfs.add('longbow')
            self.size = 'Medium'
            self.speed = 35
        elif self.race==('Rock Gnome'):
            self.langs.add('Gnomish')
        elif self.race==('High Elf'):
            self.skills.add('Perception')
            self.langs.add('Elven')
            self.wProfs.add('longsword')
            self.wProfs.add('shortsword')
            self.wProfs.add('shortbow')
            self.wProfs.add('longbow')
            self.size = 'Medium'
            self.speed = 30
        elif self.race==('Human'):
            self.langs.add('Dwarvish')
        elif self.race==('Half Orc'):
            self.skills.add('Intimidation')
            self.langs.add('Orc')
        elif self.race==('Lightfoot Halfling'):
            self.langs.add('Halfling')
        elif self.race==('Hill Dwarf'):
            self.wProfs.add('battleaxe')
            self.wProfs.add('hand axe')
            self.wProfs.add('light hammer')
            self.wProfs.add('warhammer')
            self.tProfs.add(choice(['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools']))
            self.langs.add('Dwarvish')
        elif self.race==('Mountain Dwarf'):
            self.wProfs.add('battleaxe')
            self.wProfs.add('hand axe')
            self.wProfs.add('light hammer')
            self.wProfs.add('warhammer')
            self.tProfs.add(choice(['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools']))
            self.langs.add('Dwarvish')
            self.aProfs.add('light')
            self.aProfs.add('medium')
        elif self.race==('Drow'):
            self.skills.add('Perception')
            self.langs.add('Elven')
            self.wProfs.add('rapier')
            self.wProfs.add('shortsword')
            self.wProfs.add('hand crossbow')
        else:
            raise Exception("Bad race {} when setting languages.".format(self.race))

    def setSkillsForBackground(self):
        if self.bg == 'Guild Artisan':
            self.skills.add('Insight')
            self.skills.add('Persuasion')
            if 'smith\'s tools' in self.tProfs:
                self.tProfs.add('carpenter\'s tools')
            else:
                self.tProfs.add('smith\'s tools')
            if 'Gnomish' in self.langs:
                self.langs.add('Dwarvish')
            else:
                self.langs.add('Gnomish')
        elif self.bg == 'Sage':
            self.skills.add('Arcana')
            self.skills.add('History')
            if 'Elvish' in self.langs:
                self.langs.add('Gnomish')
            else:
                self.langs.add('Elvish')
            self.langs.add('Draconic')
        elif self.bg == 'Outlander':
            self.skills.add('Athletics')
            self.skills.add('Survival')
            if 'Elvish' in self.langs:
                self.langs.add('Orcish')
            else:
                self.langs.add('Elvish')
            self.tProfs.add('flute')
        elif self.bg == 'Soldier':
            self.skills.add('Athletics')
            self.skills.add('Intimidation')
            self.tProfs.add('cards')
            self.tProfs.add('vehicles(land)')
        elif self.bg == 'Entertainer':
            self.skills.add('Acrobatics')
            self.skills.add('Performance')
            self.tProfs.add('disguise kit')
            self.tProfs.add('lute')
        elif self.bg == 'Charlatan':
            self.skills.add('Deception')
            self.skills.add('Slight of Hand')
            self.tProfs.add('disguise kit')
            self.tProfs.add('forgery kit')
        elif self.bg == 'Acolyte':
            self.skills.add('Insight')
            self.skills.add('Religion')
            if 'Elvish' in self.langs:
                self.langs.add('Gnomish')
            else:
                self.langs.add('Elvish')
            if 'Dwarvish' in self.langs:
                self.langs.add('Orcish')
            else:
                self.langs.add('Dwarvish')
        elif self.bg == 'Hermit':
            self.skills.add('Medicine')
            self.skills.add('Religion')
            if 'Elvish' in self.langs:
                self.langs.add('Gnomish')
            else:
                self.langs.add('Elvish')
        elif self.bg == 'Folk Hero':
            self.skills.add('Animal Handling')
            self.skills.add('Survival')
            if 'smith\'s tools' in self.tProfs:
                self.tProfs.add('carpenter\'s tools')
            else:
                self.tProfs.add('smith\'s tools')
        elif self.bg == 'Noble':
            self.skills.add('History')
            self.skills.add('Persuasion')
            if 'Elvish' in self.langs:
                self.langs.add('Gnomish')
            else:
                self.langs.add('Elvish')
            self.tProfs.add('dice')
        elif self.bg == 'Urchin':
            self.skills.add('Sleight of Hand')
            self.skills.add('Stealth')
            self.tProfs.add('disguise kit')
            self.tProfs.add('thieves\' tools')
        elif self.bg == 'Criminal':
            self.skills.add('Deception')
            self.skills.add('Stealth')
            self.tProfs.add('dice')
            self.tProfs.add('thieves\' tools')
        else:
            raise Exception("Bad background {} when setting skills.".format(self.bg))



if __name__ == "__main__":
        myChar = Character()
        print('Greeings, I am ' + myChar.name + ' of ' + myChar.origin.split(',')[0])
        myChar.setClass()
        myChar.setRace()
        print('I am a mighty '+myChar.race + ' ' + myChar.dispClass)
        print(myChar.stats)
        myChar.updateAttrForRace()
        print(myChar.stats)
        myChar.updateAttrForClass()
        print(myChar.stats)
        myChar.setBackground()
        print('My humble background is as a ' + myChar.bg)
        myChar.setSkillsForRace()
        myChar.setSkillsForBackground()
        print('I speak ' + ' '.join(list(myChar.langs)))
        print('I do ' + ' '.join(list(myChar.skills)))
