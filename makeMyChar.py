###################################################################
#Author: Gentry Atkinson                                          #
#Date: 15 April, 2021                                             #
#Description: this script will generate a level one character for #
#  Dungeons and Dragons 5th Edition. All game is from the         #
#  standard reference document.                                   #
###################################################################

import sys
from random import randint, shuffle, choice, seed
from math import floor

filePath = ""


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

        seed()
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
        self.save = set()
        self.size = ""
        self.speed = 0
        self.gold = 0
        self.arch = "None"
        self.weapons=[]
        self.armor=[]
        self.equipment=""
        self.ac=10
        self.spells = []
        self.spellBonus = 0
        self.spellSlots = [0, 0]

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
            classes.append('two-weapon ranger')
        if self.stats['int'] == main:
            classes.append('wizard')
            classes.append( 'artificer')
            classes.append('rogue')
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
        elif self.cl == 'two-weapon ranger':
            races.append('Wood Elf')
            races.append('Human')
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
        elif self.cl == 'two-weapon ranger':
            attributes = ['dex', 'con', 'wis', 'str', 'int', 'cha']
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
            attributes = ['cha', 'dex', 'con', 'str', 'wis', 'int']
        elif self.cl == 'tank cleric':
            attributes = ['str', 'con', 'wis', 'dex', 'int', 'cha']
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
        elif self.dispClass == 'Druid':
            bg = ['Outlander', 'Folk Hero']
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
            self.langs.add('Elvish')
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
            self.langs.add('Elvish')
            self.wProfs.add('longsword')
            self.wProfs.add('shortsword')
            self.wProfs.add('shortbow')
            self.wProfs.add('longbow')
            self.size = 'Medium'
            self.speed = 30
        elif self.race==('Human'):
            self.langs.add('Dwarvish')
            self.size = 'Medium'
            self.speed = 30
        elif self.race==('Half Orc'):
            self.skills.add('Intimidation')
            self.langs.add('Orc')
            self.size = 'Medium'
            self.speed = 30
        elif self.race==('Lightfoot Halfling'):
            self.langs.add('Halfling')
            self.size = 'Small'
            self.speed = 25
        elif self.race==('Hill Dwarf'):
            self.wProfs.add('battleaxe')
            self.wProfs.add('hand axe')
            self.wProfs.add('light hammer')
            self.wProfs.add('warhammer')
            self.tProfs.add(choice(['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools']))
            self.langs.add('Dwarvish')
            self.size = 'Medium'
            self.speed = 25
        elif self.race==('Mountain Dwarf'):
            self.wProfs.add('battleaxe')
            self.wProfs.add('hand axe')
            self.wProfs.add('light hammer')
            self.wProfs.add('warhammer')
            self.tProfs.add(choice(['smith\'s tools', 'brewer\'s supplies', 'mason\'s tools']))
            self.langs.add('Dwarvish')
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.size = 'Medium'
            self.speed = 25
        elif self.race==('Drow'):
            self.skills.add('Perception')
            self.langs.add('Elvish')
            self.wProfs.add('rapier')
            self.wProfs.add('shortsword')
            self.wProfs.add('hand crossbow')
            self.size = 'Medium'
            self.speed = 30
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
            self.skills.add('Sleight of Hand')
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

    def setSkillsForClass(self):
        if self.cl == 'archer ranger' or self.cl == 'two-weapon ranger':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            self.wProfs.add('martial')
            self.skills.add('Nature')
            if 'Stealth' in self.skills:
                self.skills.add('Insight')
            else:
                self.skills.add('Stealth')
            if 'Perception' in self.skills:
                self.skills.add('Animal Handling')
            else:
                self.skills.add('Perception')
        elif self.cl == 'artificer':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            self.tProfs.add('thieves\' tools')
            self.tProfs.add('tinker\'s tools')
            if 'smith\'s tools' in self.tProfs:
                self.tProfs.add('carpenter\'s tools')
            else:
                self.tProfs.add('smith\'s tools')
            if 'Arcana' in self.skills:
                self.skills.add('Investigation')
            else:
                self.skills.add('Arcana')
            if 'Perception' in self.skills:
                self.skills.add('Medicine')
            else:
                self.skills.add('Perception')
        elif self.cl == 'barbarian':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            self.wProfs.add('martial')
            if 'Perception' in self.skills:
                self.skills.add('Intimidation')
            else:
                self.skills.add('Perception')
            if 'Athletics' in self.skills:
                self.skills.add('Nature')
            else:
                self.skills.add('Athletics')
        elif self.cl == 'bard':
            self.aProfs.add('light')
            self.wProfs.add('simple')
            self.wProfs.add('hand crossbow')
            self.wProfs.add('longsword')
            self.wProfs.add('rapier')
            self.wProfs.add('shortsword')
            self.tProfs.add('drum')
            self.tProfs.add('flute')
            if 'lute' in self.tProfs:
                self.tProfs.add('maraca')
            else:
                self.tProfs.add('lute')
            if 'Persuasion' in self.skills:
                self.skills.add('Stealth')
            else:
                self.skills.add('Persuasion')
            if 'Deception' in self.skills:
                self.skills.add('Acrobatics')
            else:
                self.skills.add('Deception')
            if 'Performance' in self.skills:
                self.skills.add('Sleight of Hand')
            else:
                self.skills.add('Performance')
        elif self.cl == 'caster ranger':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            self.wProfs.add('martial')
            self.skills.add('Nature')
            if 'Stealth' in self.skills:
                self.skills.add('Insight')
            else:
                self.skills.add('Stealth')
            if 'Perception' in self.skills:
                self.skills.add('Animal Handling')
            else:
                self.skills.add('Perception')
        elif self.cl == 'druid':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('shields')
            self.wProfs.add('club')
            self.wProfs.add('dagger')
            self.wProfs.add('dart')
            self.wProfs.add('javelin')
            self.wProfs.add('mace')
            self.wProfs.add('quarterstaff')
            self.wProfs.add('scimitar')
            self.wProfs.add('sickle')
            self.wProfs.add('sling')
            self.wProfs.add('spear')
            self.tProfs.add('herbalism kit')
            if 'Nature' in self.skills:
                self.skills.add('Religion')
            else:
                self.skills.add('Nature')
            if 'Survival' in self.skills:
                self.skills.add('Medicine')
            else:
                self.skills.add('Survival')
        elif self.cl == 'healer cleric':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            if 'Medicine' in self.skills:
                self.skills.add('Insight')
            else:
                self.skills.add('Medicine')
            self.skills.add('History')
            self.arch = "Life Domain"
            self.aProfs.add('heavy')
        elif self.cl == 'melee fighter':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('heavy')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            self.wProfs.add('martial')
            if 'Athletics' in self.skills:
                self.skills.add('Perception')
            else:
                self.skills.add('Athletics')
            if 'Intimidation' in self.skills:
                self.skills.add('Survival')
            else:
                self.skills.add('Intimidation')
            self.arch="Dueling"
        elif self.cl == 'paladin':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('heavy')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            self.wProfs.add('martial')
            self.skills.add('Medicine')
            if 'Intimidation' in self.skills:
                self.skills.add('Athletics')
            else:
                self.skills.add('intimidation')
        elif self.cl == 'rogue':
            self.aProfs.add('light')
            self.wProfs.add('simple')
            self.wProfs.add('hand crossbow')
            self.wProfs.add('longsword')
            self.wProfs.add('rapier')
            self.wProfs.add('shortsword')
            self.tProfs.add('thieves\' tools')
            if 'Deception' in self.skills:
                self.skills.add('Sleight of Hand')
            else:
                self.skills.add('Deception')
            if 'Perception' in self.skills:
                self.skills.add('Persuasion')
            else:
                self.skills.add('Perception')
            self.skills.add('Acrobatics')
            self.skills.add('Intimidation')
        elif self.cl == 'sorcerer':
            self.wProfs.add('dagger')
            self.wProfs.add('dart')
            self.wProfs.add('sling')
            self.wProfs.add('quarterstaff')
            self.wProfs.add('light crossbow')
            self.skills.add('Arcana')
            if 'Deception' in self.skills:
                self.skills.add('Persuasion')
            else:
                self.skills.add('Deception')
            self.arch=choice(['Draconic', 'Storm', 'Shadow'])
        elif self.cl == 'tank cleric':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            if 'Medicine' in self.skills:
                self.skills.add('Insight')
            else:
                self.skills.add('Medicine')
            self.skills.add('History')
            self.arch = "War Domain"
            self.aProfs.add('heavy')
            self.wProfs.add('martial')
        elif self.cl == 'tank fighter':
            self.aProfs.add('light')
            self.aProfs.add('medium')
            self.aProfs.add('heavy')
            self.aProfs.add('shields')
            self.wProfs.add('simple')
            self.wProfs.add('martial')
            if 'Athletics' in self.skills:
                self.skills.add('Perception')
            else:
                self.skills.add('Athletics')
            if 'Intimidation' in self.skills:
                self.skills.add('Survival')
            else:
                self.skills.add('Intimidation')
            self.arch = "Defense"
        elif self.cl == 'warlock':
            self.aProfs.add('light')
            self.wProfs.add('simple')
            self.skills.add('Arcana')
            self.skills.add(choice(['Nature', 'History']))
            self.arch = choice(['Archfey', 'Fiend', 'Great Old One'])
        elif self.cl == 'wizard':
            self.wProfs.add('dagger')
            self.wProfs.add('dart')
            self.wProfs.add('sling')
            self.wProfs.add('quarterstaff')
            self.wProfs.add('light crossbow')
            if 'Arcana' in self.skills:
                self.skills.add('Insight')
            else:
                self.skills.add('Arcana')
            self.skills.add('Investigation')
        else:
            raise Exception("Bad class {} when setting skills.".format(self.cl))
            return

    def setHP(self):
        if self.dispClass == 'Artificer':
            self.hitDie = 'd8'
            self.save.add('con')
            self.save.add('int')
        elif self.dispClass == 'Barbarian':
            self.hitDie = 'd12'
            self.save.add('str')
            self.save.add('con')
        elif self.dispClass == 'Bard':
            self.hitDie = 'd8'
            self.save.add('dex')
            self.save.add('cha')
        elif self.dispClass == 'Cleric':
            self.hitDie = 'd8'
            self.save.add('wis')
            self.save.add('cha')
        elif self.dispClass == 'Druid':
            self.hitDie = 'd8'
            self.save.add('int')
            self.save.add('wis')
        elif self.dispClass == 'Fighter':
            self.hitDie = 'd10'
            self.save.add('str')
            self.save.add('con')
        elif self.dispClass == 'Paladin':
            self.hitDie = 'd10'
            self.save.add('wis')
            self.save.add('cha')
        elif self.dispClass == 'Ranger':
            self.hitDie = 'd10'
            self.save.add('str')
            self.save.add('dex')
        elif self.dispClass == 'Rogue':
            self.hitDie = 'd8'
            self.save.add('dex')
            self.save.add('int')
        elif self.dispClass == 'Sorcerer':
            self.hitDie = 'd6'
            self.save.add('con')
            self.save.add('cha')
        elif self.dispClass == 'Warlock':
            self.hitDie = 'd8'
            self.save.add('wis')
            self.save.add('cha')
        elif self.dispClass == 'Wizard':
            self.hitDie = 'd6'
            self.save.add('int')
            self.save.add('wis')
        else:
            raise Exception("Bad class {} when setting hitpoints.".format(self.dispClass))
            return
        self.hp = int(self.hitDie[1:]) + floor((self.stats['con']-10)/2)

    def pickEquipmentForBackground(self):
        if self.bg == 'Guild Artisan':
            self.equipment += "artisan\'s tools, letter of introduction, traveler\'s clothes, belt pouch"
            self.gold += 15
        elif self.bg == 'Sage':
            self.equipment += "bottle of ink, quill, a small knife, letter from dead colleague, common clothes, belt pouch"
            self.gold += 10
        elif self.bg == 'Outlander':
            self.equipment += "staff, hunting trap, a trophy, traveler\'s clothes, belt pouch"
            self.gold += 10
        elif self.bg == 'Soldier':
            self.equipment += "rank insignia, war trophy, set of cards, common clothes, belt pouch"
            self.gold += 10
        elif self.bg == 'Entertainer':
            self.equipment += "a lute, {}, costume clothes, belt pouch".format(choice(['a love letter', 'a lock of hair', 'a lover\'s trinket']))
            self.gold += 15
        elif self.bg == 'Charlatan':
            self.equipment += "fine clothes, disguise kit, {}, belt pouch".format(choice(['weighted dice', '10 bottles of colored liquid', 'a fake signet ring']))
            self.gold += 15
        elif self.bg == 'Acolyte':
            self.equipment += "holy symbol, a prayer book, 5 sticks of incense, common clothes, belt pouch"
            self.gold += 15
        elif self.bg == 'Hermit':
            self.equipment += "scroll case of notes, a winter blanket, common clothes, an herbalism kit"
            self.gold += 5
        elif self.bg == 'Folk Hero':
            self.equipment += "artisan\'s tools, a shovel, an iron pot, common clothes, belt pouch"
            self.gold += 10
        elif self.bg == 'Noble':
            self.equipment += "fine clothes, signet ring, scroll of pedigree, purse"
            self.gold += 25
        elif self.bg == 'Urchin':
            self.equipment += "a small knife, map of home city, pet mouse, token from parents, common clothes, belt pouch"
            self.gold += 10
        elif self.bg == 'Criminal':
            self.equipment += "a crowbar, dark hooded clothes, belt pouch"
            self.gold += 15
        else:
            raise Exception("Bad background {} when picking equipment.".format(self.bg))

    def pickEquipmentForClass(self):
        if self.cl == 'archer ranger' or self.cl == 'two-weapon ranger':
            self.armor.append('leather')
            self.weapons.append('two shortswords')
            self.equipment += ", an explorer\'s pack"
            self.weapons.append('longbow')
            self.weapons.append('quiver of 20 arrows')
        elif self.cl == 'artificer':
            self.armor.append('studded leather')
            self.weapons.append('light crossbow')
            self.weapons.append('20 bolts')
            self.weapons.append('2 daggers')
            self.equipment += ", thieves\' tools, a dungeoneer\'s pack"
        elif self.cl == 'barbarian':
            self.weapons.append('greataxe')
            self.weapons.append('two handaxes')
            self.weapons.append('4 javelins')
            self.equipment += ", an explorer\'s pack"
        elif self.cl == 'bard':
            self.weapons.append('rapier')
            self.equipment += ", an entertainer\'s pack, a flute"
            self.armor.append('leather')
            self.weapons.append('dagger')
        elif self.cl == 'caster ranger':
            self.armor.append('scale mail')
            self.weapons.append('two shortswords')
            self.equipment += ", an dungeoneer\'s pack"
            self.weapons.append('longbow')
            self.weapons.append('quiver of 20 arrows')
        elif self.cl == 'druid':
            self.armor.append('wooden shield')
            self.weapons.append('scimitar')
            self.armor.append('leather')
            self.equipment += ", an explorer\'s pack, a druidic focus"
        elif self.cl == 'healer cleric':
            self.weapons.append('mace')
            self.armor.append('scale mail')
            self.weapons.append('light crossbow')
            self.weapons.append('20 bolts')
            self.armor.append('shield')
            self.equipment += ", a priest\'s pack, a holy symbol"
        elif self.cl == 'melee fighter':
            self.armor.append('chain mail')
            self.weapons.append('longsword')
            self.armor.append('shield')
            self.weapons.append('two handaxes')
            self.equipment += ", a dungwoneer\'s pack"
        elif self.cl == 'paladin':
            self.weapons.append('longsword')
            self.armor.append('shield')
            self.weapons.append('5 javelins')
            self.armor.append('chain mail')
            self.equipment += ", an explorer\'s pack, a holy symbol"
        elif self.cl == 'rogue':
            self.weapons.append('shortsword')
            self.weapons.append('shortbow')
            self.weapons.append('20 arrows')
            self.armor.append('leather')
            self.weapons.append('2 daggers')
            self.equipment += ", a burglar\'s pack, thieves\'s tools"
        elif self.cl == 'sorcerer':
            self.weapons.append('light crossbow')
            self.weapons.append('20 bolts')
            self.weapons.append('2 daggers')
            self.equipment += ", an arcane focus, a dungeoneer\'s pack"
        elif self.cl == 'tank cleric':
            self.weapons.append('warhammer')
            self.armor.append('chain mail')
            self.weapons.append('mace')
            self.armor.append('shield')
            self.equipment += ", a priest\'s pack, a holy symbol"
        elif self.cl == 'tank fighter':
            self.armor.append('chain mail')
            self.weapons.append('longsword')
            self.armor.append('shield')
            self.weapons.append('two handaxes')
            self.equipment += ", a dungeoneer\'s pack"
        elif self.cl == 'warlock':
            self.weapons.append('light crossbow')
            self.weapons.append('20 bolts')
            self.weapons.append('2 daggers')
            self.armor.append('leather')
            self.weapons.append('mace')
            self.equipment += ", a component pouch, a dungeoneer\'s pack"
        elif self.cl == 'wizard':
            self.weapons.append('dagger')
            self.equipment += ", a component pouch, a scholar\'s pack, a spellbook"
        else:
            raise Exception("Bad class {} when picking equipment.".format(self.cl))
            return

    def determineAC(self):
        bonus = floor((self.stats['dex']-10)/2)
        if self.dispClass == 'Barbarian':
            self.ac += bonus
            self.ac += floor((self.stats['con']-10)/2)
        else:
            if 'leather' in self.armor:
                self.ac = 11
                self.ac += bonus
            elif 'studded leather' in self.armor:
                self.ac = 12
                self.ac += bonus
            elif 'scale mail' in self.armor:
                self.ac = 14
                self.ac += (2 if bonus > 2 else bonus)
            elif 'chain mail' in self.armor:
                self.ac = 16
        if 'shield' in self.armor or 'wooden shield' in self. armor:
            self.ac += 2

    def determineSpells(self):
        if self.cl == 'wizard':
            self.spells.append(['Prestidigitation', 'Light', choice(['Acid Splash', 'Fire Bolt', 'Toll the Dead'])])
            self.spells.append(['Magic Missle', 'Charm Person', 'Color Spray', 'Detect Magic'])
            self.spells[1].append(choice(['Longstrider', 'Mage Armor', 'Protection from Good and Evil']))
            self.spells[1].append(choice(['Ray of Sickness', 'Shield', 'Catapult']))
            self.spellBonus = 1 + floor((self.stats['int']-10)/2)
            self.spellSlots[1] = 2

        elif self.cl == 'warlock':
            self.spells.append(['Eldritch Blast', 'Friends']) #2
            self.spells.append([choice(['Arms of Hador', 'Cause Fear']), choice(['Charm Person', 'Expiditious Retreat'])]) #2
            self.spellBonus = 1 + floor((self.stats['cha']-10)/2)
            self.spellSlots[1] = 1

        elif self.cl == 'sorcerer':
            self.spells.append([choice(['Acid Splash', 'Fire Bolt']), 'Dancing Lights', choice(['Frostbite', 'Poison Spray', 'Shocking Grasp']), 'Mage Hand'])#4
            self.spells.append([choice(['Burning Hands', 'Fog Cloud', 'Ice Knife']), choice(['Comprehend Languages', 'Detect Magic', 'Feather Fall'])])#2
            self.spellBonus = 1 + floor((self.stats['cha']-10)/2)
            self.spellSlots[1] = 2

        elif self.cl == 'druid':
            self.spells.append(['Druidcraft', choice(['Control Flames', 'Guidance'])])#2
            self.spells.append(['Beast Bond', choice(['Cure Wounds', 'Entangle'])])#2
            self.spellBonus = 1 + floor((self.stats['wis']-10)/2)
            self.spellSlots[1] = 2

        elif self.cl == 'tank cleric' or self.cl == 'healer cleric':
            self.spells.append(['Thaumaturgy', 'Sacred Flame', 'Spare the Dying'])#3
            self.spells.append(['Bless', 'Cure Wounds'])#2
            self.spellBonus = 1 + floor((self.stats['wis']-10)/2)
            self.spellSlots[1] = 2

        elif self.cl == 'bard':
            self.spells.append(['Prestidigitation', choice(['Friends', 'Green-Flame Bleade', 'Thunderclap'])])#2
            self.spells.append(['Comprehend Languages', 'Charm Person', 'Identify', choice(['Longstrider', 'Sleep', 'Tasha\'s Hideous Laughter'])])#4
            self.spellBonus = 1 + floor((self.stats['cha']-10)/2)
            self.spellSlots[1] = 2

        elif self.cl == 'artificer':
            self.spells.append(['Sword Burst', 'Mending'])#2
            self.spells.append([])#2
            self.spellBonus = 1 + floor((self.stats['int']-10)/2)
            self.spellSlots[1] = 0

    def write(self):
        filename = '{}{}.txt'.format(filePath, self.name).replace(' ', '_')
        charFile = open(filename , 'w+')
        dexSkills = ['Acrobatics', 'Sleight of Hand', 'Stealth']
        wisSkills = ['Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival']
        intSkills = ['Arcana', 'History', 'Investigation', 'Nature', 'Religion']
        strSkills = ['Athletics']
        chaSkills = ['Deception', 'Intimidation', 'Performance', 'Persuasion']
        if not charFile.writable():
            raise Exception('Could not open character file')
            return
        charFile.write('Name: {}\t\tRace: {}\n'.format(self.name, self.race))
        charFile.write('Levels: 1 {}\t\tArchetype: {}\t\tBackground: {}\n'.format(self.dispClass, self.arch, self.bg))
        charFile.write('Origin: {}\n'.format(self.origin))
        charFile.write('\n')
        charFile.write('HP: {}\t\tHit Dice: 1{}\n'.format(self.hp, self.hitDie))
        charFile.write('Stats: \n')
        charFile.write('\t\tSTR:{}'.format(self.stats['str']))
        charFile.write('\tDEX:{}'.format(self.stats['dex'],))
        charFile.write('\tCON:{}\n'.format(self.stats['con']))
        charFile.write('\t\tINT:{}'.format(self.stats['int']))
        charFile.write('\tWIS:{}'.format(self.stats['wis'],))
        charFile.write('\tCHA:{}\n'.format(self.stats['cha']))
        charFile.write('Proficiency Bonus: +1\n')
        charFile.write('\n')
        charFile.write('Tool Proficiencies: {}\n'.format(', '.join(self.tProfs)))
        charFile.write('Weapon Proficiencies: {}\n'.format(', '.join(self.wProfs)))
        charFile.write('Armor Proficiencies: {}\n'.format(', '.join(self.aProfs)))
        charFile.write('Languages: {}\n'.format(', '.join(self.langs)))
        charFile.write('Saves: {}\n'.format(' '.join([i.upper() for i in self.save])))
        charFile.write('\t\tSTR: {}{}'.format('+' if self.stats['str'] >=10 else '', floor((self.stats['str']-10)/2) + (1 if 'str' in self.save else 0)))
        charFile.write('\t\tDEX: {}{}'.format('+' if self.stats['dex'] >=10 else '', floor((self.stats['dex']-10)/2) + (1 if 'dex' in self.save else 0)))
        charFile.write('\t\tCON: {}{}\n'.format('+' if self.stats['con'] >=10 else '', floor((self.stats['con']-10)/2) + (1 if 'con' in self.save else 0)))
        charFile.write('\t\tINT: {}{}'.format('+' if self.stats['int'] >=10 else '', floor((self.stats['int']-10)/2) + (1 if 'int' in self.save else 0)))
        charFile.write('\t\tWIS: {}{}'.format('+' if self.stats['wis'] >=10 else '', floor((self.stats['wis']-10)/2) + (1 if 'wis' in self.save else 0)))
        charFile.write('\t\tCHA: {}{}\n'.format('+' if self.stats['cha'] >=10 else '', floor((self.stats['cha']-10)/2) + (1 if 'cha' in self.save else 0)))
        charFile.write('\n')
        charFile.write('Skills:\n')
        for s in dexSkills:
            bonus = floor((self.stats['dex']-10)/2)+(1 if s in self.skills else 0)
            charFile.write('\t({}){}: {}{}'.format('P' if s in self.skills else '_', s, '+' if bonus >=0 else '',str(bonus)))
        charFile.write('\n')
        for s in wisSkills:
            bonus = floor((self.stats['wis']-10)/2)+(1 if s in self.skills else 0)
            charFile.write('\t({}){}: {}{}'.format('P' if s in self.skills else '_', s, '+' if bonus >=0 else '',str(bonus)))
        charFile.write('\n')
        for s in intSkills:
            bonus = floor((self.stats['int']-10)/2)+(1 if s in self.skills else 0)
            charFile.write('\t({}){}: {}{}'.format('P' if s in self.skills else '_', s, '+' if bonus >=0 else '',str(bonus)))
        charFile.write('\n')
        for s in strSkills:
            bonus = floor((self.stats['str']-10)/2)+(1 if s in self.skills else 0)
            charFile.write('\t({}){}: {}{}'.format('P' if s in self.skills else '_', s, '+' if bonus >=0 else '',str(bonus)))
        charFile.write('\n')
        for s in chaSkills:
            bonus = floor((self.stats['cha']-10)/2)+(1 if s in self.skills else 0)
            charFile.write('\t({}){}: {}{}'.format('P' if s in self.skills else '_', s, '+' if bonus >=0 else '',str(bonus)))
        charFile.write('\n\n')
        charFile.write('Weapons: ' + ', '.join(self.weapons))
        charFile.write('\n')
        charFile.write('Armor: ' + ', '.join(self.armor))
        charFile.write('\t\tAC: {}'.format(self.ac))
        charFile.write('\n')
        charFile.write("Equipment: " + self.equipment + '\n')
        if self.spellBonus != 0:
            charFile.write('\n')
            charFile.write('Spell Bonus: +{}\t\tSpell DC: {}\n'.format(self.spellBonus, 8+self.spellBonus))
            charFile.write('Cantrips: {}\n'.format(', '.join(self.spells[0])))
            charFile.write('Level 1 Spell Slots: {}\n'.format(self.spellSlots[1]))
            charFile.write('Level 1 Spells: {}\n'.format(', '.join(self.spells[1])))
        charFile.close()


if __name__ == "__main__":
        if len(sys.argv) == 1:
            filePath = 'chars/'
        elif len(sys.argv) == 2:
            if sys.argv[1] == 'linux':
                filePath = 'chars/'
            elif sys.argv[1] == 'windows':
                filePath = 'chars\\'
        else:
            raise Exception("Unknown OS")
        myChar = Character()
        print('Greeings, I am ' + myChar.name + ' of ' + myChar.origin.split(',')[0])
        myChar.setClass()
        myChar.setRace()
        print('I am a mighty '+myChar.race + ' ' + myChar.dispClass)
        myChar.updateAttrForClass()
        myChar.updateAttrForRace()
        myChar.setBackground()
        myChar.setSkillsForRace()
        myChar.setSkillsForBackground()
        myChar.setSkillsForClass()
        myChar.setHP()
        myChar.pickEquipmentForBackground()
        myChar.pickEquipmentForClass()
        myChar.determineAC()
        myChar.determineSpells()
        myChar.write()
