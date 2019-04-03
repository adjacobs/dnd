'''
Created on Jun 19, 2018

@author: ajacobs
'''
import json

class Characters():
    def __init__(self):
        self.name='Dragon Pisser'
        self.race='Golioth'
        self.armorClass=18
    
    def setName(self, name):
        '''Sets name of Person.'''
        self.name=name
    def getName(self):
        '''Returns name of person.'''
        return self.name

    def setRace(self, race):
        '''Sets Race of Person.'''
        self.Race=race
    def getRace(self):
        '''Returns Race of person.'''
        return self.race

    def setArmorClass(self, armorClass):
        '''Sets armor class.'''
        self.armorClass=armorClass
    
    def getArmorClass(self):
        '''Returns armor class.'''
        return self.armorClass

class Player(Characters):
    def __init__(self):
        super(Player, self).__init__()
        self.level=5
        self.health=20
        self.modifier=3
        self.initiative=4
        self.attackBonus=0
        self.spellModifier=0
        self.spellSave=0
        self.background=''
        self.spells=[]
        self.chrClass={'Fighter':5}
        self.abilities=[]
        
        self.jsonFile=r'C:\Users\ajacobs\Desktop\DnD\export.json'
    
        self._buildStatClassList()
        self._buildSkillClassList()
        
    def _buildStatClassList(self):
        '''Creates a Stat instance for each of the base stats.'''
        self.str=Stat('Strength')
        self.dex=Stat('Dextarity')
        self.con=Stat('Constitution')
        self.int=Stat('Intelegence')
        self.wis=Stat('Wisdom')
        self.cha=Stat('Charisma')
    
    def getStats(self, filter=[]):
        '''Retunrs a list of all the player stats.'''
        if filter:
            stats=[]
            for stat in self.getStats():
                if stat.getName() in filter:
                    stats.append(stat)
            return stats
                    
        return [self.str, self.dex, self.con,
                self.int, self.wis, self.cha]
        
    def _buildSkillClassList(self):
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
    
    def getSkills(self, byStat=False):
        '''Returns a list of all the player skills. Be deault returns a list of all skills.
        Can be filtered by associated stat.'''
        if byStat:
            #Set up base keys for stat dictionary
            skills={'Strength':[],'Dextarity':[],'Constitution':[], 
                    'Intelegence':[], 'Wisdom':[], 'Charisma':[]}
            #Goes through skills and places them in a dictionary with the key being their associated stat
            for s in self.getSkills():
                skills[s.getStat()].append(s)
            return skills
                
        return [self.actobatics, self.animalHandling, self.arcana, self.athletics,
                self.deception, self.history, self.insight, self.intimidation,
                self.investigation, self.medicine, self.nature, self.perception,
                self.performance, self.persuasion, self.religion, self.slightOfHand,
                self.stealth, self.survival]
        
        
    def setLvl(self, lvl):
        self.level=lvl
    
    def getLvl(self):
        return self.level
    
    def setHealth(self, health):
        self.health=health
    
    def getHealth(self):
        return self.health
    
    def setBackground(self, background):
        self.background=background
    
    def getBackground(self):
        return self.background
    
    def setModifier(self, modifier):
        self.modifier=modifier
        
    def getModifier(self):
        return self.modifier
    
    def setInitiative(self, intitiative):
        self.initiative=intitiative
    
    def getInitiative(self):
        return self.initiative
    
    def setAttackBonus(self, attackBonus):
        self.attackBonus=attackBonus
        
    def getAttackBonus(self):
        return self.attackBonus
    
    def setSpellModifier(self, spellModifier):
        self.spellModifier=spellModifier
    
    def getSpellModifier(self):
        return self.spellModifier
    
    def setSpellSave(self, spellSave):
        self.spellSave=spellSave
    
    def getSpellSave(self):
        return self.spellSave
    
    def getClass(self):
        return self.chrClass
    
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
            
    def testFunction(self):
        print('Player function works.')
        

class Stat():
    def __init__(self, name):
        self.name=name
        self.value=0
        self.prof=False
    
    def getName(self):
        '''returns name'''
        return self.name

    def set(self, val):
        '''sets stat value'''
        self.value=int(val)
    
    def get(self):
        '''returns stat value'''
        return self.value
    
    def setProf(self, val):
        '''sets stat proficiency'''
        self.prof=val
    
    def getPorf(self):
        '''Returns True or False depending if the player is proficient in the stat.'''
        return self.prof
    
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
    
    def getName(self):
        '''Returns name of skill.'''
        return self.name
    
    def getStat(self):
        '''Returns the stat name accociated with the skill.'''
        return self.Stat.getName()
    
    def setProf(self, prof):
        '''Sets if skill is proficient'''
        self.prof=prof
        
    def getProf(self):
        '''Returns True or False depending if the player is proficient in the skill.'''
        return self.prof
    
    def setExpert(self, expert):
        '''Sets if skill is expert.'''
        self.expert=expert
    
    def getExpert(self):
        '''Returns True or False depending if the player is an expert in the skill.'''
        return self.expert