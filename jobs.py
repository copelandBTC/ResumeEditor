#!/usr/bin/python

import time
import xerox
import os
import sys
from shutil import copyfile

date       = time.strftime("%B %d, %Y")
letter     = "/home/bc/Jobs/Resumes/cover letter.txt"
replet     = "/home/bc/Jobs/Resumes/coverletter.txt"
jobHist    = "/home/bc/Jobs/jobs.txt"

jobTitle   = raw_input("Job title: ")
compName   = raw_input("Company name: ")
citySt     = raw_input("City and state: ")
resumeType = raw_input("Resume type: ")

if resumeType == "j":
	lang = "java"
elif resumeType == "p":
	lang = "python"
elif resumeType == "w":
	lang = "web development"
else:
	while resumeType != "j" or "p" or "w":
		print ("Invalid type\n\n")
		resumeType = input("Resume type: ")

""" RESUME """
"""
#Decide which resume to work on
if resumeType == 'j':
	copyfile("CopelandResumeJ.docx", "Copeland.docx")
elif resumeType == 'p':
	copyfile("CopelandResumeP.docx", "Copeland.docx")

#Check for buzzwords
if len(sys.argv) > 0:
	for word in str(sys.argv).split():
		buzz.append(word)
else:
	buzz = raw_input("Buzzwords: ")

#Insert into resume
"""


""" COVER LETTER """
file = open(letter, "r+")
data = file.read()

#replace
data = data.replace("DATE", date)
data = data.replace("JOBTITLE", jobTitle)
data = data.replace("COMPANYNAME", compName)
data = data.replace("CITY, ST", citySt)
data = data.replace("PROGLANG", lang)
data = data.decode('utf-8')

xerox.copy(data)
xerox.paste()


""" JOB HISTORY """
#Update apply history
newJob = "\n\n" + compName + "\n" + jobTitle + "\n" + date
file = open(jobHist, "a")
file.write(newJob)
file.close()