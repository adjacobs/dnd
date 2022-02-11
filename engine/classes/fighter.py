"""
Created on Nov 24, 2021

@author: ajacobs
"""

import logging
import random
import os

import engine.util
import engine.classes.character

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def second_wind(level, data, description=False, full=False):
    """
    Rolls second wind die and combines that with level to return level plus roll. If full returns the full healing
    If details returns the details of second wind.
    @param level: int
    @param description: bool
    @param data: dictionary
    @param full: bool (Returns max health)
    @return:
    """
    logger.debug('Using Second Wind.')

    # Return description of class feature if description is True
    if description:
        return data['description']

    # set die to roll
    die = engine.util.Die(data['die'])
    # Check for full to return max healing.
    if full:
        return die.get_high() + level

    return die.roll() + level


def action_surge(actions):
    """
    Takes in a dictionary of actions and resets them.
    @param actions: dictionary
    @return:
    """
    logger.debug('Using Action Surge.')
    for k, v in actions.items():
        # Check if value is a tuple if so assign the last variable as the first variable
        if type(v) == tuple:
            temp_var = list(v)
            temp_var[0] = temp_var[-1]
            actions[k] = tuple(temp_var)
            continue


class Base(engine.classes.character.Base):
    def __init__(self):
        super(Base, self).__init__(cls_name='Fighter',
                                   hit_die='D10',
                                   primary_abilities=['strength', 'dexterity'],
                                   saves=['strength', 'constitution'])
        self.armor = ['all', 'shields']
        self.weapon = ['simple', 'martial']
        self.tools = ['none']
        self.attacks = 1

        self._valid_skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight',
                              'Intimidation', 'Perception', 'Survival']

        # Class feature variables. Used to check if feature has been used.
        self._second_wind = True
        self._action_surge = 0
        self._martial_archetype = None
        self._extra_attacks = 0
        self._indomitable = 0

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
        data = engine.util.load_json(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                               '_docs', 'class', 'fighter', 'features',
                                                               'second_wind.json')))
        # Return description of class feature if description is True
        if description:
            return second_wind(level, description=True)

        # Check if second wind is available if so run it.
        if self._second_wind:
            self._second_wind = False
            # Check if user wants to roll. If so return the roll
            if roll:
                return second_wind(level=level, data=data, full=full)
            else:
                return True
        else:
            return False

    def action_surge(self, actions):
        """
        Resets the number of attacks
        @return:
        """
        if self._action_surge:
            action_surge(actions)
            self._action_surge -= 1
        else:
            logger.debug('Action surge has no more uses.')

    def martial_archetype(self):
        """
        Wrapper function for martial archetype features.
        @return:
        """
        pass

    @property
    def extra_attacks(self):
        """
        Returns the amount of attacks left.
        @return:
        """
        return self._extra_attacks

    @extra_attacks.setter
    def extra_attacks(self, count):
        """
        Sets the amount of attacks
        @param count:
        @return:
        """
        self._extra_attacks += count




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


if __name__ == "__main__":
    chr_class = Base()
    print(chr_class.second_wind(4, roll=True))
