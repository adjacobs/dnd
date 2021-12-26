""""
Created on Jun 12, 2019

@author: ajacobs
"""
import random
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def roll_stats(number_count: int, rolls: int, die_type = 6):
    """rolls out stats based on the number of dice, the amount of rolls
    and the die type. Returns a list."""
    stats = []
    for r in range(rolls):
        rolls = []
        for d in range(number_count):
            rolls.append(random.randint(1, die_type))
    
        stats.append({sum(sorted(rolls)[1:]): sorted(rolls)[1:]})
    
    return stats


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


def die_range(die):
    """
    Returns a tubple of the die range.
    @param die:String (D4, D6, D8, D10, D12, D20)
    @return: Tuple
    """
    return 1, int(die.split('d')[-1])
