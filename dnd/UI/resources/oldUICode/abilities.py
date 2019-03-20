'''
Created on Jun 19, 2018

@author: ajacobs
'''
class Ability():
    def __init__(self, name):
        self.name=name
        self.description=''
    
    def setName(self, name):
        self.name=name
    
    def getName(self):
        return self.name
    
    def setDescription(self, description):
        self.description=description
    
    def getDescription(self):
        return self.description
        
        