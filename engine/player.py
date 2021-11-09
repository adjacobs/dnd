"""
Created on Jun 19, 2018

@author: ajacobs
"""

import logging
import os
import xml.etree.ElementTree as et
from xml.dom import minidom

from engine.util import str_to_bool

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

folder_root = os.path.dirname(os.path.dirname(__file__))

skills_dict = {'strength': ['athletics'],
               'dexterity': ['acrobatics', 'slight_of_hand', 'stealth'],
               'constitution': [],
               'intelligence': ['arcana', 'history', 'investigation', 'nature', 'religion'],
               'wisdom': ['animal_handling', 'insight', 'medicine', 'perception', 'survival'],
               'charisma': ['deception', 'intimidation', 'performance', 'persuasion']}

class Player:
    def __init__(self, load=''):
        self.name = ''
        self.race = ''
        self.level = 0
        self.health = (0, 0)
        self.temp_health = 0
        self.speed = 0
        self.chr_class = []
        self.background = None
        self._stats = [Stat('strength'), Stat('dexterity'), Stat('constitution'),
                       Stat('intelligence'), Stat('wisdom'), Stat('charisma')]

        # figures out proficiency, initiative, and armor class based on the players level, feats, and equipment.
        self.prof_bonus = self.get_prof_bonus()
        self.initiative = self.get_initiative()
        # self.ac = self.get_ac()

        logger.warning('Warning')
        logger.info('Info')
        logger.debug('Debug')

        # TODO:remove once class is done being tested.
        if load:
            self._load_xml()

    def set_stats(self, stat, value):
        """
        Sets the stat value
        :param stat: String
        :param value: int
        """
        # Check that stat exists
        for s in self.stats:
            if s.name == stat:
                s.set_value(value)

    @staticmethod
    def _get_xml_file():
        # Temp file name hardcoded for testing porpuse. Will need to be populated by code at some point
        return os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            '_docs', 'saves', 'Double Dragon_save_temp.xml'))

    # validates new items for player, like classes, features, spells
    def _validate(self, type, feature):
        # check that feature type is valid
        if os.path.exists(os.path.join(folder_root, type)):
            pass

    def level_up(self, chr_class):
        # Check if level 0 if so call different function
        if not self.level:
            logger.warning('Player is currently level 0 setting up first level.')
            return None

        # validate that cls is valid
        # Check if player already has class
        if chr_class in self.chr_class.keys():
            pass
        # if primary, add to primary class look up cls xml and return features
        # if secondary, check if already level in class
        # if so add level to secondary cls look up cls xml and return features
        # if not check if player meets cls requirements
        # if they do add class to player and return features
        # if not log issue and return none
        pass

    @property
    def stats(self):
        """
        Returns list ot stat objects
        @return:
        """
        return self._stats

    def get_stat_by_name(self, stat):
        """
        Returns stat class
        @param stat: String
        @return: stat class obj
        """
        for s in self.stats:
            if s.name == stat:
                return s

    def get_skills(self, stat=None):
        """Returns a list of all the player skill classes. By default returns a list of all skills.
        Can be filtered by associated stat.
        @param stat: String
        @return: List of Skills
        """
        logger.debug('Getting skills')
        stat = self.get_stat(stat)
        if stat:
            return stat.skills
        else:
            skills = []
            for stat in self.stats:
                skills.append(stat.skills)
            return skills
    
    def get_initiative(self):
        """Returns what the initiative is based on dexterity"""
        logger.debug('Setting initiative')
        # TODO: Needs extra functions to search for feats or anything else that may change the initiative
        return self.get_stat_by_name('dexterity').get_modifier()
    
    def get_prof_bonus(self):
        """Returns players proficiency bonus based on their level. If prof not set by end of for loop return 6"""
        logger.debug('Setting proficiency bonus')
        levels = [5, 9, 12, 16]
        for lvl in levels:
            if self.level < lvl:
                return levels.index(lvl)+2
        return 6

    def get_attack_bonus(self, stat, proficiency=False):
        """Gets the stat attack bonus. Works for spell or weapon. Adds proficiency if called"""
        logger.debug(f"Getting attack bonus for {stat}")
        # TODO: May need to add functionality to add any additional weapon or other bonus
        if stat in self.stats.keys():
            if proficiency:
                return self.stats[stat].get_modifier() + self.get_prof_bonus()
            else:
                return self.stats[stat].get_modifier()
    
    def get_spell_save_dc(self, stat):
        """Returns the spell save DC based on the given stat"""
        logger.debug('Getting spell save DC')
        if stat in self.stats.keys():
            return self.stats[stat].get_modifier() + self.get_prof_bonus() + 8
        else:
            logger.error('%s is not a valid stat' % stat)
            return None

    def get_passive_perception(self):
        """Returns the passive wisdom which is 10 + Perception bonus"""
        stat = self.stats['wisdom']
        return 10 + stat.skills['perception'].get_modifier(self.prof_bonus, stat.get_modifier())

    def get_passive_investigation(self):
        """Returns the passive intelligence which is 10 + Investigation bonus"""
        stat = self.stats['intelligence']
        return 10 + stat.skills['investigation'].get_modifier(self.prof_bonus, stat.get_modifier())

    def get_passive_insight(self):
        """Returns the passive wisdom which is 10 + Insight bonus"""
        stat = self.stats['wisdom']
        return 10 + stat.skills['insight'].get_modifier(self.prof_bonus, stat.get_modifier())

    def _save_xml(self):
        """Saves out the class variables, stats, and skills to the xml file."""
        logger.debug('Saving out file')
        # Gathers up all the player data and writes it out to an xml file.
        root = et.Element('Player')

        # get basic class information and create a sub element of the rood for each item
        et.SubElement(root, 'base', name=str(self.name), race=str(self.race), level=str(self.level),
                      health=str(self.health), temp_health=str(self.temp_health), background=str(self.background))

        # goes over each item in the chr_class dict and builds out a sub element for them
        for cls, lvl in self.chr_class.items():
            et.SubElement(root, 'chr_class', name=cls, level=lvl)

        # goes through the stats and saves each one to the root
        # in doing that each stat saves out its own skills
        for stat in self.stats.values():
            stat.save(root)

        # builds out the string in a more user readable fashion
        xml_str = minidom.parseString(et.tostring(root, 'utf-8')).toprettyxml(indent="   ")

        # opens up the xml file and saves the string
        with open(self._get_xml_file(), 'w') as f:
            f.write(xml_str)

    # TODO:still needs more testing to make sure everything is loading properly.
    def _load_xml(self):
        """
        loads the xml up provided by the set_xml function and sets the class variables,
        builds out the stat classes, and the skill classes
        """
        logger.debug('Loading xml file')
        tree = et.parse(self._get_xml_file())
        root = tree.getroot()

        # goes over base attributes and assigns them to class attribute
        base_var = root.find('base')
        self.name = base_var.get('name')
        self.race = base_var.get('race')
        self.level = int(base_var.get('level'))
        self.health = int(base_var.get('health'))
        self.temp_health = int(base_var.get('temp_health'))
        self.background = base_var.get('background')

        # goes over each chr_class item in the xml and sets the self.chr_class dict
        for cls in root.iter('chr_class'):
            self.chr_class[cls.get('name')] = cls.get('level')

        # goes over the stats section of the xml file and builds of the stat classes and adds them to the class var.
        for stat in root.iter('stats'):
            logger.debug('Testing stat loaders')
            name = stat.get('name')
            self.stats[name].value = int(stat.get('value'))
            self.stats[name].prof = str_to_bool(stat.get('proficiency'))

            # for each stat goes over the skills and builds them out.
            for skill in stat.iter('skills'):
                logger.debug('Testing skill loaders')
                self.stats[name].skills[skill.get('name')].prof = str_to_bool(skill.get('proficiency'))
                self.stats[name].skills[skill.get('name')].expert = str_to_bool(skill.get('expert'))

        # once class vars are set, stats set and skills set calls the functions that sets some other class var
        self.prof_bonus = self.get_prof_bonus()
        self.initiative = self.get_initiative()


class Stat:
    # TODO: try to get rid of the default values here
    def __init__(self, name, value=0, prof=False):
        self.name = name
        self.value = value
        self.prof = prof
        self._skills = []

        self._set_skills()

    def __str__(self):
        """Return `str(self)`."""
        if self.prof:
            prof = 'you are'
        else:
            prof = 'you are not'
        return f'{self.name} has a value of {self.value}, and {prof} proficient.'

    def __repr__(self):
        return f'Stat {self.name} value {self.value}.'

    def set_value(self, value):
        """
        Try to set the value if it cant error out.
        @param value: Int
        """
        try:
            self.value = int(value)
        except ValueError as e:
            logger.error(f'{value} can not be converted into an int.')

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
        # Loop over list of skills that match stat and set the class
        for skill in skills_dict[self.name]:
            self._skills.append(Skill(name=skill, parent_stat=self))

    @property
    def skills(self):
        """
        Returns the list of skills
        @return:
        """
        return self._skills

    def get_skill_by_name(self, skill):
        """
        @param skill: String
        @return:Stat Class
        """
        for s in self.skills:
            if s.name == skill:
                return s
        return None

    def save(self, root):
        # save out stat information
        stat = et.SubElement(root, 'stats',  name=self.name, value=str(self.value), proficiency=str(self.prof))

        # goes through the stats and saves out each one associated to the class
        for s in self.skills.values():
            s.save(stat)


class Skill:
    """Container for skills. Takes in the corresponding stat in order to return proper values."""
    def __init__(self, name, parent_stat):
        self.name = name
        self.prof = False
        self.expert = False
        self.parent_stat = parent_stat

    def __str__(self):
        """Return `str(self)`."""
        if self.expert:
            return f'{self.name} has a value of {self.parent_stat.value}, your proficient and have expertise.'
        elif self.prof:
            return f'{self.name} has a value of {self.parent_stat.value}, your proficient.'
        else:
            return f'{self.name} has a value of {self.parent_stat.value}, your not proficient'

    def __repr__(self):
        return f'Stat {self.name} value {self.parent_stat.value}.'

    # TODO: this function feels messy. Think of a cleaner way to get the skill modifier
    def get_modifier(self, prof_bonus, stat_modifier):
        """Figures out the modifier by getting the base stat modifier and adding
        any prof or expert modifiers."""
        if self.prof:
            stat_modifier += prof_bonus
            if self.expert:
                stat_modifier += prof_bonus
        return stat_modifier

    def get_value(self):
        """
        Return value of stat with prof and expertise included
        @return:
        """
        print(self.parent_stat.value)

    def save(self, root):
        et.SubElement(root, 'skills', name=self.name, proficiency=str(self.prof), expert=str(self.expert))
