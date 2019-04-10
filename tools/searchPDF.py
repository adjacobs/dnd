'''
Created on Apr 5, 2019

@author: ajacobs
'''
import PyPDF2 as PDF
import re

pdfFile=r'C:\Users\ajacobs\Google Drive\DnD\books\dnd5eng.pdf'
#pdfFile=r'C:\Users\ajacobs\Google Drive\Python\resources\spells.pdf'
def readPDF(pdfFile):
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PDF.PdfFileReader(pdfFileObj)
    
    for i in range(188, 189):
        pageObj = pdfReader.getPage(i)
        
        print(pageObj.extractText().encode('utf8'))

        '''
        levelRegex = re.compile(r'\d\w+\s\w+')
        grp = levelRegex.search(text)
        print(grp.group())
        '''
    
readPDF(pdfFile)
