'''
Created on May 24, 2019

@author: ajacobs
'''
import logging
import json

logging.basicConfig(filename=r'D:\myStuff\logs\test.log', level=logging.DEBUG)

logging.debug('test message')

class Test():
    def __init__(self):
        self.logger=logging.getLogger(__name__)
        self.logger.debug('testign class')
        
Test()