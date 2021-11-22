import logging
import xml.etree.ElementTree as eT
from xml.dom import minidom

from engine.util import str_to_bool

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

skills_dict = {'strength': ['athletics'],
               'dexterity': ['acrobatics', 'slight_of_hand', 'stealth'],
               'constitution': [],
               'intelligence': ['arcana', 'history', 'investigation', 'nature', 'religion'],
               'wisdom': ['animal_handling', 'insight', 'medicine', 'perception', 'survival'],
               'charisma': ['deception', 'intimidation', 'performance', 'persuasion']}


class Stat:
    def __init__(self, name, value=0, prof=False):
        self.name = name
        self._value = value
        self._prof = prof
        self._skills =[]
        for skill in skills_dict[self.name]:
            self._skills.append(Skill(name=skill, parent_stat=self))

    def __str__(self):
        """Return `str(self)`."""
        if self.prof:
            prof = 'you are'
        else:
            prof = 'you are not'
        return f'{self.name} has a value of {self.value}, and {prof} proficient.'

    def __repr__(self):
        return f'Stat {self.name} value {self.value}.'

    @property
    def prof(self):
        """
        Returns stat proficiency
        @return: Bool
        """
        return self._prof

    @prof.setter
    def prof(self, value):
        """
        Sets proficiency
        @param value: Bool
        @return:
        """
        self._prof = value

    @property
    def value(self):
        """
        Returns stat value
        @return: Int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value
        @param value: Int
        @return:
        """
        try:
            self._value = int(value)
        except ValueError:
            logger.error(f' {value} can not be converted into an int.')

    @property
    def modifier(self):
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
        stat = eT.SubElement(root, 'stats',  name=self.name, value=str(self.value), proficiency=str(self.prof))

        # goes through the stats and saves out each one associated to the class
        for s in self.skills.values():
            s.save(stat)


class Skill:
    """Container for skills. Takes in the corresponding stat in order to return proper values."""
    def __init__(self, name, parent_stat):
        self.name = name
        self._prof = False
        self._expert = False
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

    @property
    def prof(self):
        """
        Returns proficiency
        @return:Bool
        """
        return self._prof

    @prof.setter
    def prof(self, value):
        """
        Sets proficiency
        @param value:Bool
        @return:
        """
        self._prof = value

    @property
    def expert(self):
        """
        Returns expert
        @return: Bool
        """
        return self._expert

    @expert.setter
    def expert(self, value):
        """
        Sets the value of expert
        @param value: Bool
        @return:
        """
        self._expert = value

    def get_bonus(self, prof_bonus=0):
        """Figures out the modifier by getting the base stat modifier and adding
        any prof or expert modifiers."""
        bonus = self.parent_stat.modifier
        if self.prof:
            bonus += prof_bonus
            if self.expert:
                bonus += prof_bonus
        return bonus

    def save(self, root):
        eT.SubElement(root, 'skills', name=self.name, proficiency=str(self.prof), expert=str(self.expert))
