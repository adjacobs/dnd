'''
Created on Mar 13, 2019

@author: ajacobs
'''
import subprocess

UIPath=r'C:\Users\ajacobs\Python\tools\dnd\UI\resources'

ogFile = 'tab'
ogFilePath = r'C:\\Users\\ajacobs\\eclipseWorkSpace\\python\\temp\\'+ ogFile + '.ui'

newFile='tab'
newFilePath = r'C:\\Users\\ajacobs\\eclipseWorkSpace\\python\\temp\\'+ newFile + '.py' 

cmdLine=r'C:\Users\ajacobs\AppData\Local\Programs\Python\Python35\Scripts\pyside2-uic.exe ' + ogFilePath + ' -o ' + newFilePath

print (cmdLine)
subprocess.call(cmdLine, shell=True)