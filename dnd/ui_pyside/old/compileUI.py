'''
Created on Mar 13, 2019

@author: ajacobs
'''
import subprocess

UIPath=r'C:\Users\ajacobs\Python\tools\dnd\UI\resources'
cmdLine=r'C:\Users\ajacobs\AppData\Local\Programs\Python\Python35\Scripts\pyside2-uic.exe '+UIPath+r'\mainWindow.ui -o '+r'C:\Users\ajacobs\Python\tools\dnd\UI\designer\mainWindow.py'
subprocess.call(cmdLine, shell=True)