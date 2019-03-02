from ResumeCooking.generateImpl import *
from ResumeCooking.uniqueListMaker import uniqueJobTitle, uniqueCompany

numberofresume = int(input("Enter # of resumes you want to generate: "))
generateImpl(numberofresume)
uniqueJobTitle()
uniqueCompany()