'''
Created on Jun 19, 2018

@author: ajacobs
'''
import logging
import json

logging.basicConfig(filename=r'D:\myStuff\logs\test.log', level=logging.DEBUG)

class Characters():
    def __init__(self):
        self.name=''
        self.race=''
        self.armorClass=0
    
    def setName(self, name):
        '''Sets name of Person.'''
        self.name=name

    def setRace(self, race):
        '''Sets Race of Person.'''
        self.Race=race

    def setArmorClass(self, armorClass):
        '''Sets armor class.'''
        self.armorClass=armorClass

class Player(Characters):
    def __init__(self):
        super(Player, self).__init__()
        self.logger = logging.getLogger(__name__)
        
        self.level=0
        self.health=0
        self.initiative=4
        self.attackBonus=0
        self.spellModifier=0
        self.spellSave=0
        self.background=''
        self.spells=[]
        self.chrClass={'Fighter':5}
        self.abilities=[]
        
        self.jsonFile=r'C:\Users\ajacobs\Desktop\DnD\export.json'
    
        self._buildStats()
        self._buildSkills()
        
    def _buildStats(self):
        '''Creates a Stat instance for each of the base stats.'''
        self.str=Stat('Strength')
        self.dex=Stat('Dextarity')
        self.con=Stat('Constitution')
        self.int=Stat('Intelegence')
        self.wis=Stat('Wisdom')
        self.cha=Stat('Charisma')
        
    def _buildSkills(self):
        self.actobatics=Skill('Acrobatics', self.dex)
        self.animalHandling=Skill('Animal Handling', self.wis)
        self.arcana=Skill('Arcana', self.int)
        self.athletics=Skill('Athletics', self.str)
        self.deception=Skill('Deception', self.cha)
        self.history=Skill('History', self.int)
        self.insight=Skill('Insight', self.wis)
        self.intimidation=Skill('Intimidation', self.cha)
        self.investigation=Skill('Investigation', self.int)
        self.medicine=Skill('Medicine', self.wis)
        self.nature=Skill('Nature', self.int)
        self.perception=Skill('Perceptpion', self.wis)
        self.performance=Skill('Performance', self.cha)
        self.persuasion=Skill('Persuasuion', self.cha)
        self.religion=Skill('Religion', self.int)
        self.slightOfHand=Skill('Slight of Hand', self.dex)
        self.stealth=Skill('Stealth',self.dex)
        self.survival=Skill('Survival', self.wis)
    
    def getStats(self):
        '''Retunrs a list of all the player stats.'''
        return [self.str, self.dex, self.con,
                self.int, self.wis, self.cha]
        
    def getSkills(self):
        '''Returns a list of all the player skills. Be deault returns a list of all skills.
        Can be filtered by associated stat.'''
        return [self.actobatics, self.animalHandling, self.arcana, self.athletics,
                self.deception, self.history, self.insight, self.intimidation,
                self.investigation, self.medicine, self.nature, self.perception,
                self.performance, self.persuasion, self.religion, self.slightOfHand,
                self.stealth, self.survival]
        
        
    def setLvl(self, lvl):
        '''Checks that "lvl" is and int and is 20 or under. If so sets the level
        logs and error and does nothing.'''
        if isinstance(lvl, int):
            if lvl<21:
                self.level=lvl
        else:
            pass
    
    def setHealth(self, health):
        self.health=health
    
    def setBackground(self, background):
        self.background=background
    
    def setInitiative(self, intitiative):
        self.initiative=intitiative
    
    def getInitiative(self):
        '''Returns what the initiative is based on level and modifiers.
        Currently only returs base initiative. Will need to add function
        to search for feats and items'''
        initiative = self.dex.getModifier()
        return initiative
    
    def getProfBonus(self):
        '''Returns players proficency bonus based on their level.'''
        levels = [5,9,12,16]
        
        for l in levels:
            if self.level<l:
                return levels.index(l)+2

    def setAttackBonus(self, attackBonus):
        self.attackBonus=attackBonus
    
    def setSpellModifier(self, spellModifier):
        self.spellModifier=spellModifier
    
    def setSpellSave(self, spellSave):
        self.spellSave=spellSave
    
    def _gatherData(self):
        stats={}
        for stat in self.stats:
            infoDict={'value':stat.value,
                      'prof':stat.prof,
                      'modifier':stat.modifier}
            stats[stat.name]=infoDict
        
        dataDict={'level':self.level,
                  'health':self.health,
                  'background':self.background,
                  'modifier':self.modifier,
                  'initiative':self.initiative,
                  'attackBonus':self.attackBonus,
                  'spellModifier':self.spellModifier,
                  'spellSave':self.spellSave,
                  'stats':stats}
        
        return dataDict
            
    def save(self):
        data=self._gatherData()
        with open(self.jsonFile, 'w') as outfile:  
            json.dump(data, outfile)    

class Stat():
    def __init__(self, name, value=0, prof=False):
        self.name=name
        self.value=value
        self.prof=prof

    def set(self, val):
        '''sets stat value'''
        self.value=int(val)
    
    def setProf(self, val):
        '''sets stat proficiency'''
        self.prof=val
    
    def getModifier(self):
        '''returns stat modifier proficiency'''
        modifier=0
        #If value is over 10 subtracts 10 and divides by 2 to give you the modifier
        if self.value>=10:
            modifier=int((self.value-10)/2)
        #Under 10 determines if its odd or even
        #If off subtracts 1
        #Divides by 2 and then subtracts total from 5
        else:
            if self.value%2:
                modifier=int(-(5-(self.value-1)/2))
            else:
                modifier=int(-(5-(self.value/2)))
                
        return modifier

'''Container for skills. Takes in the corresponding stat in order to return proper values.'''
class Skill():
    def __init__(self, name, Stat):
        self.name=name
        self.Stat=Stat
        self.prof=False
        self.expert=False
    
    def getModifier(self):
        return self.Stat.getModifier()
    
    def getStat(self):
        '''Returns the stat name accociated with the skill.'''
        return self.Stat.getName()
    
    def setProf(self, prof):
        '''Sets if skill is proficient'''
        self.prof=prof
    
    def setExpert(self, expert):
        '''Sets if skill is expert.'''
        self.expert=expert

Player()