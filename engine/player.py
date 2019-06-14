"""
Created on Jun 19, 2018

@author: ajacobs
"""

import logging
import json
import os

logging.basicConfig(filename=r'C:\Users\ajacobs\python\_logs\test.log', level=logging.DEBUG)


class Characters:
    def __init__(self):
        self.name = ''
        self.race = ''
        self.armor_class = 0
    
    def set_name(self, name):
        """Sets name of Person."""
        self.name = name

    def set_race(self, race):
        """Sets Race of Person."""
        self.race = race

    def set_ac(self, ac):
        """Sets armor class."""
        self.armor_class = ac


class Player(Characters):

    def __init__(self):
        super(Player, self).__init__()
        self.logger = logging.getLogger(__name__)
        
        self.level = 0
        self.health = 0
        self.prof_bonus = self.get_prof_bonus()
        self.initiative = 4
        self.attack_bonus = 0
        self.spell_modifier = 0
        self.spell_save = 0
        self.background = ''
        self.spells = []
        self.chr_class = {'Fighter': 5}
        self.abilities = []
        
        # Temp file name hardcoded for testing porpuse. Will need to be populated by code at some point
        self.save_file = os.path.join(os.path.dirname(__file__), '_dnd_test_docs', 'testSave.json')
        
        self._build_stats()
        self._build_skills()
        
    def _build_stats(self):
        """Creates a Stat instance for each of the base stats."""
        self.str = Stat('Strength')
        self.dex = Stat('Dextarity')
        self.con = Stat('Constitution')
        self.int = Stat('Intelegence')
        self.wis = Stat('Wisdom')
        self.cha = Stat('Charisma')
        
    def _build_skills(self):
        """Builds out a class per skill. With the skill name and its corresponding stat as the variables."""
        self.acrobatics = Skill('Acrobatics', self.dex)
        self.animal_handling = Skill('Animal Handling', self.wis)
        self.arcana = Skill('Arcana', self.int)
        self.athletics = Skill('Athletics', self.str)
        self.deception = Skill('Deception', self.cha)
        self.history = Skill('History', self.int)
        self.insight = Skill('Insight', self.wis)
        self.intimidation = Skill('Intimidation', self.cha)
        self.investigation = Skill('Investigation', self.int)
        self.medicine = Skill('Medicine', self.wis)
        self.nature = Skill('Nature', self.int)
        self.perception = Skill('Perceptpion', self.wis)
        self.performance = Skill('Performance', self.cha)
        self.persuasion = Skill('Persuasuion', self.cha)
        self.religion = Skill('Religion', self.int)
        self.slight_of_hand = Skill('Slight of Hand', self.dex)
        self.stealth = Skill('Stealth', self.dex)
        self.survival = Skill('Survival', self.wis)
    
    def get_stats(self):
        """Returns a list of all the player stats."""
        return [self.str, self.dex, self.con,
                self.int, self.wis, self.cha]
        
    def get_skills(self):
        """Returns a list of all the player skills. Be deault returns a list of all skills.
        Can be filtered by associated stat."""
        return [self.acrobatics, self.animal_handling, self.arcana,
                self.athletics, self.deception, self.history, 
                self.insight, self.intimidation, self.investigation, 
                self.medicine, self.nature, self.perception,
                self.performance, self.persuasion, self.religion, 
                self.slight_of_hand, self.stealth, self.survival]
        
    def set_level(self, lvl):
        """Checks that "lvl" is and int and is 20 or under. If so sets the level
        logs and error and does nothing."""
        if isinstance(lvl, int):
            if lvl < 21:
                self.level = lvl
        else:
            pass
    
    def set_health(self, health):
        self.health = health
    
    def set_background(self, background):
        self.background = background
    
    def set_initiative(self, initiative):
        self.initiative = initiative
    
    def get_initiative(self):
        """Returns what the initiative is based on level and modifiers.
        Currently only returns base initiative. Will need to add function
        to search for feats and items"""
        return self.dex.get_modifier()
    
    def get_prof_bonus(self):
        """Returns players proficiency bonus based on their level."""
        levels = [5, 9, 12, 16]
        
        for l in levels:
            if self.level < l:
                return levels.index(l)+2

    def set_attack_bonus(self, attack_bonus):
        self.attack_bonus = attack_bonus
    
    def set_spell_modifier(self, spell_modifier):
        self.spell_modifier = spell_modifier
    
    def set_spell_save(self, spell_save):
        self.spell_save = spell_save
    
    def _gather_data(self):
        stats = {}
        
        for stat in self.get_stats():
            info_dict = {'value': stat.value, 'prof': stat.prof}
            
            stats[stat.name] = info_dict
        
        data_dict = {'level': self.level,
                     'health': self.health,
                     'prof_bonus': self.prof_bonus,
                     'background': self.background,
                     'initiative': self.initiative,
                     'attack_bonus': self.attack_bonus,
                     'spell_modifier': self.spell_modifier,
                     'spell_save': self.spell_save,
                     'stats': stats}
        
        return data_dict
            
    def save(self):
        data = self._gather_data()
        with open(self.save_file, 'w') as out_file:  
            json.dump(data, out_file)    

    def test_function(self):
        print('Cat')


class Stat:
    def __init__(self, name, value=0, prof=False):
        self.name = name
        self.value = value
        self.prof = prof

    def set(self, val):
        """sets stat value"""
        self.value = int(val)
    
    def set_prof(self, val):
        """sets stat proficiency"""
        self.prof = val
    
    def get_modifier(self):
        """returns stat modifier proficiency"""
        modifier = 0

        # If value is over 10 subtracts 10 and divides by 2 to give you the modifier
        if self.value >= 10:
            modifier = int((self.value-10)/2)
        # Under 10 determines if its odd or even
        # If off subtracts 1
        # Divides by 2 and then subtracts total from 5
        else:
            if self.value % 2:
                modifier = int(-(5-(self.value-1)/2))
            else:
                modifier = int(-(5-(self.value/2)))
                
        return modifier


class Skill:
    """Container for skills. Takes in the corresponding stat in order to return proper values."""
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat
        self.prof = False
        self.expert = False
    
    def get_modifier(self, prof_bonus):
        """Figures out the modifier by getting the base stat modifier and adding
        any prof or expert modifiers."""
        modifier = self.stat.get_modifier()
        if self.prof:
            modifier += prof_bonus
            if self.expert:
                modifier += prof_bonus
        return modifier
    
    def get_stat(self):
        """Returns the stat name associated with the skill."""
        return self.stat.getName()
    
    def set_prof(self, prof):
        """Sets if skill is proficient"""
        self.prof = prof
    
    def set_expert(self, expert):
        """Sets if skill is expert."""
        self.expert = expert
