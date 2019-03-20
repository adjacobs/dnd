'''
Created on Jun 19, 2018

@author: ajacobs
'''
import json

class Characters():
    def __init__(self):
        self.name=''
        self.race=''
        self.armorClass=''
    
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
        self.level=0
        self.health=0
        self.modifier=0
        self.initiative=0
        self.attackBonus=0
        self.spellModifier=0
        self.spellSave=0
        self.background=''
        self.spells=[]
        self.charClass=[]
        self.abilities=[]
        self.stats=[self.str=Stat(), self.dex=Stat(), self.con,
                    self.int, self.wis, self.cha]
        
        self.skills=[self.actobatics, self.animalHandling, self.arcana, self.athletics,
                    self.deception, self.history, self.insight, self.intimidation,
                    self.investigation, self.medicine, self.nature, self.perception,
                    self.performance, self.persuasion, self.religion, self.slightOfHand,
                    self.stealth, self.survival]
        
        self.jsonFile=r'C:\Users\ajacobs\Desktop\DnD\export.json'
    
        self._buildStatClassList()
        
    def _buildStatClassList(self):
        '''Creates a Stat instance for each of the base stats.'''
        for stat in self.stats:
            stat=Stat()
    
    def _buildSkillClassList(self):
        pass 
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
    def __init__(self):
        self.value=0
        self.prof=False
    
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
    def __init__(self, Stat):
        self.Stat=Stat
        self.prof=False
        self.expert=False
        
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
        
    