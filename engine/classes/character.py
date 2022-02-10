"""
Created on Nov 24, 2021

@author: ajacobs
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Base:
    def __init__(self, cls_name, hit_die, primary_abilities, saves):
        """

        @param cls_name: String
        @param hit_die: String: D6, D8, D10, D12
        @param primary_abilities: List: Strength, Dexterity, Intelligence, Charisma, Wisdom, Constitution'
        @param saves: ListL Strength, Dexterity, Intelligence, Charisma, Wisdom, Constitution'
        """
        self.cls_name = cls_name
        self.hit_die = hit_die
        self.primary_abilities = primary_abilities
        self.saves = saves
        self.armor = []
        self.weapon = []
        self.tools = []
        self._features = []
        self._skills = []

        # Variables to use to validate class skills
        self._valid_skills = []

    def __str__(self):
        """Return `str(self)`."""
        abilities = ', '.join(self.primary_abilities)
        saves = ', '.join(self.saves)
        return f'{self.cls_name.title()} class has hit die of {self.hit_die}, ' \
               f'primary abilities are {abilities}, with saves of {saves}.'

    def __repr__(self):
        return f'{self.cls_name}, Hit Die: {self.hit_die}, ' \
               f'Primary Abilities: {self.primary_abilities}, ' \
               f'Saves: {self.saves}'

    @property
    def features(self):
        """
        Returns a list of the class features
        @return:
        """
        return self._features

    @features.setter
    def features(self, feature):
        """
        Adds a feature to the features list
        @param feature: Tuple first element name, second element details
        @return:
        """
        self.features.append({feature[0]: feature[1]})

    @property
    def skills(self):
        """
        Returns a list of the skills
        @return:
        """
        return self._skills

    @skills.setter
    def skills(self, skill):
        """
        Validates skill then adds it to the list
        @param skill: String
        @return:
        """
        if skill in self._valid_skills:
            logger.debug(f'Setting skill prof: {skill}')
            self._skills.append(skill)
            return True
        logger.error(f'{skill} is not a valid skill for {self.cls_name}.')
        return False

    def set_skill_prof(self, skill):
        """
        Validates and sets skill prof.
        @return:
        """
        pass