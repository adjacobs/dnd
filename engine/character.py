"""
Created on Nov 24, 2021

@author: ajacobs
"""

import logging
import json
import random
import os

import engine.util

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ChrClass:
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



class Fighter(ChrClass):
    def __init__(self):
        super(Fighter, self).__init__(cls_name='Fighter',
                                      hit_die='D10',
                                      primary_abilities=['strength', 'dexterity'],
                                      saves=['strength', 'constitution'])
        self.armor = ['all', 'shields']
        self.weapon = ['simple', 'martial']
        self.tools = ['none']

        self._valid_skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight',
                              'Intimidation', 'Perception', 'Survival']

        # Class feature variables. Used to check if feature has been used.
        self._second_wind = True

    def second_wind(self, level, roll=False, description=False, full=False):
        """
        Runs the class feature second wind. If roll gets the die range from the json file and returns the roll plus
        the level. If full is true returns the max die roll plus level. If roll is false just toggles the second wind
        availability.
        @param level: int
        @param roll: bool
        @param description: bool
        @param full: bool (Returns max health)
        @return:
        """
        logger.debug('Using Second Wind.')
        data = engine.util.load_json(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                     '_docs', 'class', 'fighter', 'features', 'second_wind.json')))

        # Return description of class feature if description is True
        if description:
            return data['description']

        # Check if second wind is available if so run it.
        if self._second_wind:
            self._second_wind = False
            # Check if user wants to roll. If so return the roll
            if roll:
                die_range = engine.util.die_range(data['die'])
                # Check for full to return max healing.
                if full:
                    return die_range[-1] + level
                return random.randint(die_range[0], die_range[-1]) + level
            else:
                return True

        return False

    def fighter_features(self, level):
        """
        Sets fighter self._features based on level
        @return:
        """

        if level <= 1:
            details = 'You have a limited well of stamina that you can draw on to protect yourself from harm. ' \
                      'On your turn, you can use a bonus action to regain hit points equal to 1d10 + your ' \
                      'fighter level. Once you use this feature, you must finish a short or long rest before ' \
                      'you can use it again.'
            self.features(('Second Wind', details))


#if __name__ == "__main__":
#    chr_class = Fighter()
#    print(chr_class.second_wind(4, roll=True))
