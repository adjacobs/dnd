'''
Created on Feb 15, 2019

@author: ajacobs
'''
import os
import shutil

def syncToGoogle():
    codeFolder=os.path.dirname(os.path.dirname(__file__))
    googleDrive=r'C:\Users\ajacobs\Google Drive\Python\tools'
    if os.path.isdir(googleDrive):
        shutil.rmtree(googleDrive)
    shutil.copytree(codeFolder, googleDrive, symlinks=False, ignore=None)
    
syncToGoogle()