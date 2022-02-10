""""
Created on Jun 12, 2019

@author: ajacobs
"""
import random
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def roll_stats():
    """rolls out stats based on the number of dice, the amount of rolls
    and the die type. Returns a list."""
    results = []
    # Set dice class to 4 d6
    dice = Dice(d6=4)
    # Roll 4 d6 6 times and return the results
    for roll in range(6):
        # After dice are rolled sort the list then remove the lowest number
        r = sorted(dice.get_results(details=True)['d6'])
        rolls = r[1:]
        results.append((rolls, sum(rolls)))
    return results


def str_to_bool(string):
    """Converts any string of 0 none or false to bool False else returns True"""
    false_list = ['0', 'none', 'false']
    if string.lower() in false_list:
        return False
    return True


def load_json(file_path):
    """
    Simple function to load a json file and return its dict
    @param file_path: String
    @return:
    """
    f = open(file_path)
    data = json.load(f)
    return data


class Die:
    def __init__(self, die):
        """
        A class to roll a single die.
        @param die:String (D4, D6, D8, D10, D12, D20)
        """
        self.die = die

    def get_range(self):
        """
        Gets the range of the die given.
        @return:
        """
        return 1, int(self.die.split('d')[-1])

    def get_high(self):
        """
        Returns the highest possible die roll
        @return:
        """
        return self.get_range()[-1]

    def roll(self):
        """
        Returns the roll of a single die
        @param die:String (d4, d6, d8, d10, d12, d20)
        @return:
        """
        die_range = self.get_range()
        return random.randint(die_range[0], die_range[-1])


class Dice:
    """
    A class to roll dice and be able to return the total value as well as the count of each dice rolled.
    """
    def __init__(self, d4=0, d6=0, d8=0, d10=0, d12=0, d20=0):
        """
        Set the amount of each dice to roll.
        @param d4: Int
        @param d6: Int
        @param d8: Int
        @param d10: Int
        @param d12: Int
        @param d20: Int
        """
        self._dice = {'d4': d4, 'd6': d6, 'd8': d8, 'd10': d10, 'd12': d12, 'd20': d20}

    def get_results(self, details=False):
        """
        Will roll all the dice given and return the total results. If details then will return the total as well as
        the details of which die rolled what.
        @param details: Bool
        @return:
        """
        # Set results dictionary
        results = {'d4': [], 'd6': [], 'd8': [], 'd10': [], 'd12': [], 'd20': []}

        # Loops over self._dice and builds out the dictionary for the rolls.
        for die, count in self._dice.items():
            d = Die(die)
            for c in range(count):
                results[die].append(d.roll())

        # Set total variable then loop over the results and add them up.
        total = 0
        for rolls in results.values():
            for roll in rolls:
                total += roll

        # Check if details then return the full results.
        if details:
            results['total'] = total
            return results

        return {'total': total}
