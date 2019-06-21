"""
Created on Jun 19, 2018

@author: ajacobs
"""

import logging
import os
import xml.etree.ElementTree as et
from xml.dom import minidom


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

'''
log_handle = logging.FileHandler(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                 '_docs', '_logs', 'player_test.log'))
'''
if not logger.handlers:
    log_handle = logging.StreamHandler()
    log_handle.setFormatter(logging.Formatter('%(levelname)s:%(name)s:%(message)s'))
    logger.addHandler(log_handle)


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
        self.level = 5
        self.health = 100
        self.prof_bonus = self.get_prof_bonus()
        self.initiative = 4
        self.attack_bonus = 10
        self.spell_modifier = 10
        self.spell_save = 10
        self.background = 'temp background'
        self.spells = ['Invisibility']
        self.chr_class = {'Fighter': 5}
        self.abilities = ['Second Wind']
        
        # Temp file name hardcoded for testing porpuse. Will need to be populated by code at some point
        self.save_file_json = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                        '_docs', 'saves', 'testSave.json'))

        self.save_file_xml = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                       '_docs', 'saves', 'testSave.xml'))

        self._build_stats()

        logger.warning('Warning')
        logger.info('Info')
        logger.debug('Debug')

    def _build_stats(self):
        """Creates a Stat instance for each of the base stats."""
        self.str = Stat('Strength')
        self.dex = Stat('Dexterity')
        self.con = Stat('Constitution')
        self.int = Stat('Intelligence')
        self.wis = Stat('Wisdom')
        self.cha = Stat('Charisma')
    
    def get_stats(self):
        """Returns a list of all the player stats."""
        return [self.str, self.dex, self.con,
                self.int, self.wis, self.cha]
        
    def get_skills(self, stat_name=None):
        """Returns a list of all the player skills. Be default returns a list of all skills.
        Can be filtered by associated stat."""
        if stat_name:
            for stat in self.get_stats():
                if stat.name == stat_name:
                    return stat.skills
        else:
            skills = {}
            for stat in self.get_stats():
                skills[stat.name] = stat.skills
            return skills

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
                     'initiative': self.initiative,
                     'attack_bonus': self.attack_bonus,
                     'spell_modifier': self.spell_modifier,
                     'spell_save': self.spell_save,
                     'background': self.background,
                     'chr_class': self.chr_class,
                     'abilities': self.abilities}
        
        return data_dict

    def _save_xml(self):
        # Gathers up all the player data and writes it out to an xml file.
        root = et.Element('Player')

        # get basic class information and create a sub element of the rood for each item
        for k, v in self._gather_data().items():
            et.SubElement(root, k, value=str(v), name='name', test='test')

        # goes through the stats and saves each one to the root
        # in doing that each stat saves out its own skills
        for stat in self.get_stats():
            stat.save(root)

        # builds out the string in a more user readable fashion
        xmlstr = minidom.parseString(et.tostring(root, 'utf-8')).toprettyxml(indent="   ")

        # opens up the xml file and saves the string
        with open(self.save_file_xml, 'w') as f:
            f.write(xmlstr)

    def _load_xml(self):
        tree = et.parse(self.save_file_xml)
        root = tree.getroot()
        for element in root:
            print(element)
            print(element.tag, element.items())

    def _load(self, file_path):
        if os.path.exists(file_path):
            pass
        # testing change
        else:
            logger.error('%s does not exits.' % file_path)
            raise Exception()
        print(file_path)

    def test_function(self):
        print('Cat')


class Stat:
    # TODO: try to get rid of the default values here
    def __init__(self, name, value=0, prof=None):
        self.name = name
        self.value = value
        self.prof = prof
        self.skills = {}

        self._set_skills()

    def set(self, val):
        """sets stat value"""
        self.value = int(val)
    
    def set_prof(self, val):
        """sets stat proficiency"""
        self.prof = val
    
    def get_modifier(self):
        """returns stat modifier proficiency"""
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

    def _set_skills(self):
        # sets the skills for that the stat controls based on a hard coded dictionary
        skills_dict = {'Strength': ['athletics'],
                       'Dexterity': ['acrobatics', 'slight_of_hand', 'stealth'],
                       'Constitution': [],
                       'Intelligence': ['arcana', 'history', 'investigation', 'nature', 'religion'],
                       'Wisdom': ['animal_handling', 'insight', 'medicine', 'perception', 'survival'],
                       'Charisma': ['deception', 'intimidation', 'performance', 'persuasion']}

        for skill in skills_dict[self.name]:
            self.skills[skill] = Skill(skill)

    def save(self, root):
        # save out stat information
        stat = et.SubElement(root, 'stat',  name=self.name, value=str(self.value), proficiency=str(self.prof))

        # goes through the stats and saves out each one associated to the class
        for s in self.skills.values():
            s.save(stat)

class Skill:
    """Container for skills. Takes in the corresponding stat in order to return proper values."""
    def __init__(self, name):
        self.name = name
        self.prof = False
        self.expert = False

    # TODO: this function feels messy. Think of a cleaner way to get the skill modifier
    def get_modifier(self, prof_bonus, stat_modifier):
        """Figures out the modifier by getting the base stat modifier and adding
        any prof or expert modifiers."""
        if self.prof:
            stat_modifier += prof_bonus
            if self.expert:
                stat_modifier += prof_bonus
        return stat_modifier

    def save(self, root):
        et.SubElement(root, 'skill', name=self.name, proficiency=str(self.prof), expert=str(self.expert))
