'''
Created on Jun 13, 2018

@author: ajacobs
'''
import os
import xml

class Campaign():
    def __init__(self):
        self.player = None
        self.party = {}
        self.locations = {}
        self.people = {}
        self.items = {}
        
    def start(self, folderLoc, name):
        '''Checks to make sure that the folderLoc is valid and if so builds out the folder structure needed.'''
        if os.path.exists(folderLoc):
            campDir= folderLoc +'\\'+name
            subDirs=['player', 'party', 'locations', 'people', 'items']
            os.mkdir(campDir)
            for sub in subDirs:
                os.mkdir(campDir+'\\'+sub)
    
    def continueCamp(self, campaignDir=None):
        pass
        
    
Campaign().start('test', None)