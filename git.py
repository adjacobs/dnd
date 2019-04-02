'''
Created on Mar 22, 2019

@author: ajacobs
'''
import os

workspace=(os.path.dirname(os.path.dirname((__file__))))
module='dnd'

comment=''

command=r'cd %s\\%s && git'%(workspace, module)

def push():
    addAll = (command + r' add --all')
    os.system(addAll)
    
    commitAll = (command + r' commit -am "this is a test checking"')
    os.system(commitAll)
    
    pushAll = (command + r' push')
    os.system(pushAll)

def get():
    pushAll = (command + r' pull')
    os.system(pushAll)


push()