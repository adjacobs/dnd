'''
Created on Mar 22, 2019

@author: ajacobs
'''
import os
addAll = (r'cd C:\\Users\\ajacobs\\eclipseWorkSpace\\python\\dnd && git add --all')
os.system(addAll)

commitAll = (r'cd C:\\Users\\ajacobs\\eclipseWorkSpace\\python\\dnd && git commit -am "this is a test checking"')
os.system(commitAll)

pushAll = (r'cd C:\\Users\\ajacobs\\eclipseWorkSpace\\python\\dnd && git push')
os.system(pushAll)
