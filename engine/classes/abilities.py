import logging
import random
import os

import engine.util

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def second_wind(level, roll=False, description=False, full=False):
    """
    Class: Fighter,
    Details: You have a limited well of stamina that you can draw on to protect yourself from harm.
    On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level.
    Once you use this feature, you must finish a short or long rest before you can use it again.
    @param level: int
    @param roll: bool
    @param description: bool
    @param full: bool (Returns max health)
    @return:
    """
    logger.debug('Using Second Wind.')
    data = engine.util.load_json(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                           '_docs', 'class', 'fighter', 'features',
                                                           'second_wind.json')))

    # Return description of class feature if description is True
    if description:
        return data['description']

    # Check if second wind is available if so run it.
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