"""
Created on Jun 19, 2018

@author: ajacobs
"""

import logging
import os
import xml.etree.ElementTree as eT
from xml.dom import minidom

import engine.stats
from engine.util import str_to_bool

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# TODO: Get rid of these once testing is done.
import importlib
importlib.reload(engine.stats)

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
    def __init__(self):
        self.name = ''
        self.race = ''
        self.level = 0
        self.health = (0, 0)
        self.temp_health = 0
        self.speed = 0
        self.inspiration = False
        self.defenses = []
        self.conditions = []
        self.classes = []
        self.background = None
        self._stats = [engine.stats.Stat('strength'), engine.stats.Stat('dexterity'), engine.stats.Stat('constitution'),
                       engine.stats.Stat('intelligence'), engine.stats.Stat('wisdom'), engine.stats.Stat('charisma')]
        self.inventory = []

    def level_up(self, chr_class):
        # Check if level 0 if so call different function
        if not self.level:
            logger.warning('Player is currently level 0 setting up first level.')
            return None

        # validate that cls is valid
        # Check if player already has class
        if chr_class in self.classes:
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
        logger.debug(f'Getting stat: {stat}')
        for s in self.stats:
            if s.name == stat:
                return s
            elif s.name.startswith(stat):
                return s

    def get_skill_by_name(self, skill_name):
        """Returns a list of all the player skill classes. By default returns a list of all skills.
        Can be filtered by associated stat.
        @param skill_name: String
        @return: skill object
        """
        logger.debug(f'Getting {skill_name}')
        for stat in self.stats:
            skill = stat.get_skill_by_name(skill_name)
            if skill:
                return skill
        logger.warning(f'Could not find skill: {skill_name}')
        return None

    def get_skill_by_stat(self, stat_name):
        """
        Gets a list of all skills from given stat
        @param stat_name: String name of stat or all if you want all skills
        @return:List
        """
        logger.debug(f'Getting skills: {stat_name}')
        # Check if getting all stats
        if stat_name == 'all':
            skills = []
            for s in self.stats:
                skills.append(s.skills)
            return skills
        # Check if stat was found.
        elif self.get_stat_by_name(stat_name):
            return self.get_stat_by_name(stat_name)
        # Return empty list
        else:
            logger.warning(f'Could not find stat: {stat_name}')
            return []
    
    def get_initiative(self):
        """Returns what the initiative is based on dexterity"""
        logger.debug('Setting initiative')
        # TODO: Needs extra functions to search for feats or anything else that may change the initiative
        return self.get_stat_by_name('dexterity').modifier

    def get_prof_bonus(self):
        """Returns players proficiency bonus based on their level. If prof not set by end of for loop return 6"""
        logger.debug('Setting proficiency bonus')
        levels = [5, 9, 12, 16]
        for lvl in levels:
            if self.level < lvl:
                return levels.index(lvl)+2
        return 6

    def get_attack_bonus(self, stat_name):
        """Gets the stat attack bonus. Works for spell or weapon. Adds proficiency if called"""
        logger.debug(f"Getting attack bonus for {stat_name}")
        stat = self.get_stat_by_name(stat_name)
        if not stat:
            logger.error(f'Could not find stat:{stat_name}')
            return None
        else:
            # TODO: Add functionality to look for additives from items and spells
            if stat.prof:
                return self.get_prof_bonus() + stat.modifier
            else:
                return stat.modifier
    
    def get_spell_save_dc(self, stat_name):
        """
        Returns the spell save DC based on the given stat
        @param stat_name: String
        @return: Int or None
        """
        logger.debug(f'Getting spell save DC for stat{stat_name}')
        stat = self.get_stat_by_name(stat_name)
        if not stat:
            logger.warning(f'Could not find stat:{stat_name}')
            return None
        else:
            return stat.modifier + self.get_prof_bonus() + 8

    @property
    def passive_perception(self):
        """Returns the passive wisdom which is 10 + Perception bonus"""
        skill = self.get_skill_by_name('perception')
        return 10 + skill.get_bonus(self.get_prof_bonus())

    @property
    def passive_investigation(self):
        """Returns the passive intelligence which is 10 + Investigation bonus"""
        skill = self.get_skill_by_name('investigation')
        return 10 + skill.get_bonus(self.get_prof_bonus())

    @property
    def passive_insight(self):
        """Returns the passive wisdom which is 10 + Insight bonus"""
        skill = self.get_skill_by_name('insight')
        return 10 + skill.get_bonus(self.get_prof_bonus())

    def set_stats(self, stat, value):
        """
        @param stat: String
        @param value: Int
        @return:
        """
        # Check that stat exists
        stat = self.get_stat_by_name(stat)
        if stat:
            stat.value = value
        else:
            logger.warning(f'{stat} is not a valid choice.')

    def _save_xml(self):
        """Saves out the class variables, stats, and skills to the xml file."""
        logger.debug('Saving out file')
        # Gathers up all the player data and writes it out to an xml file.
        root = eT.Element('Player')

        # get basic class information and create a sub element of the rood for each item
        eT.SubElement(root, 'base', name=str(self.name), race=str(self.race), level=str(self.level),
                      health=str(self.health), temp_health=str(self.temp_health), background=str(self.background))

        # goes over each item in the chr_class dict and builds out a sub element for them
        for cls, lvl in self.chr_class.items():
            eT.SubElement(root, 'chr_class', name=cls, level=lvl)

        # goes through the stats and saves each one to the root
        # in doing that each stat saves out its own skills
        for stat in self.stats.values():
            stat.save(root)

        # builds out the string in a more user readable fashion
        xml_str = minidom.parseString(eT.tostring(root, 'utf-8')).toprettyxml(indent="   ")

        # opens up the xml file and saves the string
        with open(self._get_xml_file(), 'w') as f:
            f.write(xml_str)


def load(xml_file_path=None):
    # Temp file name hardcoded for testing purpose. Will need to be populated by code at some point
    xml_file_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                 '_docs', 'saves', 'Double Dragon_save_temp.xml'))

    logger.debug('Loading xml file')
    tree = eT.parse(xml_file_path)
    root = tree.getroot()

    player = Player()
    # goes over base attributes and assigns them to class attribute
    base_var = root.find('base')
    player.name = base_var.get('name')
    player.race = base_var.get('race')
    player.level = int(base_var.get('level'))
    player.health = int(base_var.get('health'))
    player.temp_health = int(base_var.get('temp_health'))
    player.background = base_var.get('background')

    # goes over each chr_class item in the xml and sets the self.chr_class dict
    # TODO: Gunna make character class its own class so this will need to change.
    """
    for chr_class in root.iter('chr_class'):
        player.chr_class[chr_class.get('name')] = chr_class.get('level')
    """

    # goes over the stats section of the xml file and builds of the stat classes and adds them to the class var.
    for stat in root.iter('stats'):
        logger.debug('Testing stat loaders')
        name = stat.get('name')
        player_stat = player.get_stat_by_name(name)
        player_stat.value = int(stat.get('value'))
        player_stat.prof = str_to_bool(stat.get('proficiency'))

        # for each stat goes over the skills and builds them out.
        for skill in stat.iter('skills'):
            logger.debug('Testing skill loaders')
            player_skill = player_stat.get_skill_by_name(skill.get('name'))
            player_skill.prof = str_to_bool(skill.get('proficiency'))
            player_skill.expert = str_to_bool(skill.get('expert'))

    # once class vars are set, stats set and skills set calls the functions that sets some other class var
    return player


"""
load = False
if __name__ == "__main__":
    if load:
        player = load_player()
    else:
        player = Player()
"""
