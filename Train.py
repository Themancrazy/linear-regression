import re
import sys
import os.path

def writeWeightsInFile(b0, b1):
	f = open('weights.txt', "w+")
	f.write(str(b0) + "\n" + str(b1))
	f.close()

def fileExist():
	if os.path.isfile('weights.txt'):
		return True
	else:
		return False

def lossFunction(maxX):
	
	
# # for each X in between 0 and max X, if there is an observation on that X, calculate Y difference with predicted current regression
# # and apply loss equation to solve

def trainModel():
	tmpB0 = 0
	tmpB1 = 0
	L = 0.0001
	iterations = int(input("Number of iterations requested: "))
	for i in range(iterations):
		
	writeWeightsInFile(tmpB0, tmpB1)

trainModel()