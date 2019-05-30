'''
Created on May 24, 2019

@author: ajacobs
'''
import os

class A():
    def __init__(self):
        self.name='Tim'
        self.AC=10
    
    def func(self):
        return self.AC

class B(A):
    def __init__(self):
        pass

print (B().func())