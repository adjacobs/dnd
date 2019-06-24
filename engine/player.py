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


class Player:

    def __init__(self, load=False):
        super(Player, self).__init__()
        if load:
            self._load_xml()
        else:
            # temp commenting out class attributes in order to better test
            """
            self.name = ''
            self.race = ''
            self.level = 0
            self.health = 0
            self.temp_health = 0
            self.chr_class = {}
            self.background = None
            self.stats = self._build_stats()
            """
            self.name = 'Double Dragon'
            self.race = 'Goliath'
            self.level = 10
            self.health = 107
            self.temp_health = 0
            self.chr_class = {'Fighter': 9, 'Wizard': 1}
            self.background = 'Pit Fighter'

        self.stats = self._build_stats()
        self.prof_bonus = self.get_prof_bonus()
        self.initiative = self.get_initiative()
        # self.ac = self.get_ac()

        # Temp file name hardcoded for testing porpuse. Will need to be populated by code at some point
        self.save_file_xml = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                       '_docs', 'saves', 'Double Dragon_save_temp.xml'))

        logger.warning('Warning')
        logger.info('Info')
        logger.debug('Debug')

    @staticmethod
    def _build_stats():
        """Creates a Stat instance for each of the base stats."""
        return {'strength': Stat('strength'), 'dexterity': Stat('dexterity'),
                'constitution': Stat('constitution'), 'intelligence': Stat('intelligence'),
                'wisdom': Stat('wisdom'), 'charisma': Stat('charisma')}
        
    def get_skills(self, stat_name=None):
        """Returns a list of all the player skills. Be default returns a list of all skills.
        Can be filtered by associated stat."""
        if stat_name:
            if stat_name in self.stats.keys():
                return self.stats[stat_name].skills
            else:
                logger.error('%s is not a valid stat.' % stat_name)
        else:
            skills = {}
            for stat in self.stats.values():
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
    
    def get_initiative(self):
        """Returns what the initiative is based on dexterity"""
        # TODO: Needs extra functions to search for feats or anything else that may change the initiative
        return self.stats['dexterity'].get_modifier()
    
    def get_prof_bonus(self):
        """Returns players proficiency bonus based on their level."""
        levels = [5, 9, 12, 16]
        for lvl in levels:
            if self.level < lvl:
                return levels.index(lvl)+2

    def get_attack_bonus(self, stat, proficiency=False):
        """Gets the stat attack bonus. Works for spell or weapon. Adds proficiency if called"""
        # TODO: May need to add functionality to add any additional weapon or other bonus
        if stat in self.stats.keys():
            if proficiency:
                return self.stats[stat].get_modifier() + self.get_prof_bonus()
            else:
                return self.stats[stat].get_modifier()
    
    def get_spell_save_dc(self, stat):
        """Returns the spell save DC based on the given stat"""
        if stat in self.stats.keys():
            return self.stats[stat].get_modifier() + self.get_prof_bonus() + 8
        else:
            logger.error('%s is not a valid stat' % stat)
            return None

    def _save_xml(self):
        # Gathers up all the player data and writes it out to an xml file.
        root = et.Element('Player')

        # get basic class information and create a sub element of the rood for each item
        et.SubElement(root, 'base', name=str(self.name), race=str(self.race), level=str(self.level),
                      health=str(self.health), temp_health=str(self.temp_health), background=str(self.background),
                      chr_class=self.chr_class)

        # goes through the stats and saves each one to the root
        # in doing that each stat saves out its own skills
        for stat in self.stats.values():
            stat.save(root)

        # builds out the string in a more user readable fashion
        xml_str = minidom.parseString(et.tostring(root, 'utf-8')).toprettyxml(indent="   ")

        # opens up the xml file and saves the string
        with open(self.save_file_xml, 'w') as f:
            f.write(xml_str)

    def _load_xml_test(self):
        tree = et.parse(self.save_file_xml)
        root = tree.getroot()

        self.chr_class={}
        self.chr_class = root.find('base').get('chr_class')
        print(self.chr_class)

    def _load_xml(self):
        logger.debug('Testing load function')
        tree = et.parse(self.save_file_xml)
        root = tree.getroot()

        # goes over base attributes and assigns them to class attribute
        base_var = root.find('base')
        self.name = base_var.get('name')
        self.race = base_var.get('race')
        self.level = int(base_var.get('level'))
        self.health = int(base_var.get('health'))
        self.temp_health = int(base_var.get('temp_health'))
        self.background = base_var.get('background')
        self.chr_class = base_var.attrib['chr_class']

        self.stats = {}
        for stat in root.iter('stats'):
            logger.debug('Testing stat loaders')
            name = stat.get('name')
            self.stats[name] = Stat(name, value=stat.get('value'))
            self.stats[name].set_prof(stat.get('proficiency'))
            for skill in stat.iter('skills'):
                logger.debug('Testing skill loaders')
                self.stats[name].skills[skill.get('name')].prof = skill.get('proficiency')
                self.stats[name].skills[skill.get('name')].expert = skill.get('expert')

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
        skills_dict = {'strength': ['athletics'],
                       'dexterity': ['acrobatics', 'slight_of_hand', 'stealth'],
                       'constitution': [],
                       'intelligence': ['arcana', 'history', 'investigation', 'nature', 'religion'],
                       'wisdom': ['animal_handling', 'insight', 'medicine', 'perception', 'survival'],
                       'charisma': ['deception', 'intimidation', 'performance', 'persuasion']}

        for skill in skills_dict[self.name]:
            self.skills[skill] = Skill(skill)

    def save(self, root):
        # save out stat information
        stat = et.SubElement(root, 'stats',  name=self.name, value=str(self.value), proficiency=str(self.prof))

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
        et.SubElement(root, 'skills', name=self.name, proficiency=str(self.prof), expert=str(self.expert))

    def test(self):
        return 'testing skill'
