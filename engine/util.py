""""
Created on Jun 12, 2019

@author: ajacobs
"""
import random


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
