import re
import sys
import os.path
from matplotlib import pyplot as plt
import numpy as np
import math
from predict import predictClass
from predict import fileManip
import pandas as pd

#-----------------------------------------------------------------------
#	Class used to modify slope and intercept at every iteration
#-----------------------------------------------------------------------

class GDA:
	def __init__(self, b0, b1):
		self.b0 = b0
		self.b1 = b1

	def b0GDA(self, pr, learningRate, prices, miles):
		nbO = len(miles)
		sumDeltaPrices = 0
		for p, m in zip(prices, miles):
			sumDeltaPrices += float(pr.getEstimateValue(m, self.b0, self.b1) - p)
		sumDeltaPrices = self.b0 - sumDeltaPrices * (learningRate/nbO)
		return sumDeltaPrices 
		
	def b1GDA(self, pr, learningRate, prices, miles):
		nbO = len(miles)
		sumDeltaPrices = 0
		for p, m in zip(prices, miles):
			sumDeltaPrices += float((pr.getEstimateValue(m, self.b0, self.b1) - p) * m)
		sumDeltaPrices = self.b1 - sumDeltaPrices * (learningRate/nbO)
		return sumDeltaPrices 

	def setb0(self, b0):
		self.b0 = b0

	def setb1(self, b1):
		self.b1 = b1
#-----------------------------------------------------------------------
#	Class used to plot and scatter graphs (error graph + regression line)
#-----------------------------------------------------------------------

class Graph:
	def __init__(self, plt):
		self.plt = plt
		pass
	def createRegressionGraph(self, mi, pr, m, p):
		y = (m * mi) + p
		self.plt.figure(1)
		self.plt.plot(mi, y, label='regression line', color='r')
		self.plt.scatter(mi, pr, label='observations', color='b')
		self.plt.xlabel('Miles')
		self.plt.ylabel('Price')
		self.plt.title('Linear Regression')
		self.plt.legend()

	def createErrorGraph(self, x, y):
		self.plt.figure(2)
		self.plt.plot(x, y, label='Precision Curve', color='r')
		self.plt.xlabel('Learn Time (Nb of iterations)')
		self.plt.ylabel('Model\'s precision (Loss function)')
		self.plt.title('Precision of model over time')
		self.plt.legend()
		self.plt.show()

#-----------------------------------------------------------------------
#	This function normalizes the miles values to be contained between
#	0 (minimum data value given) and 1 (max data value given).
#-----------------------------------------------------------------------

def normalize(oldM):
	mMax = oldM.max()
	mMin = oldM.min()
	for i in range(0, len(oldM)):
		oldM[i] = float((oldM[i] - mMin) / (mMax - mMin))
	return oldM

#-----------------------------------------------------------------------
#	This function calculates the loss cost for the GDA algorithm.
#	It serves as basis to determine the accuracy of the model.
#-----------------------------------------------------------------------

def lossFunction(pr, miles, prices, gda):
	SSE = 0
	for m, p in zip(miles, prices):
		SSE += (pr.getEstimateValue(m, gda.b0, gda.b1) - p) ** 2
	return (SSE / len(miles))

#-----------------------------------------------------------------------
#	This function is the main function that trains the model using the
#	GDA algorithm.
#-----------------------------------------------------------------------

def trainModel():
	file = r'data.csv'
	df = pd.read_csv(file)
	normalizedMiles = normalize(df['km'].astype('float64'))
	miles = df['km']
	prices = df['price']

	learningRate = 0.01
	iterations = int(input("Number of iterations requested: "))

	gda = GDA(0, 0)
	graph = Graph(plt)
	pr = predictClass()
	f = fileManip()

	reset = input("Reset slope and intercept values?(y/n) ")
	if reset == "y":
		f.writeWeightsInFile(0, 0)
	elif reset == "n":
		pass
	else:
		print("Error: please enter y or n")
		exit(1)
	SSE = []
	currIter = []
	for i in range(iterations):
		tmpB0 = gda.b0GDA(pr, learningRate, prices, normalizedMiles)
		tmpB1 = gda.b1GDA(pr, learningRate, prices, normalizedMiles)
		gda.setb0(tmpB0)
		gda.setb1(tmpB1)
		SSE.append(lossFunction(pr, normalizedMiles, prices, gda))
		currIter.append(i)
	gda.b1 = gda.b1 / (miles.max() - miles.min())
	graph.createRegressionGraph(miles, prices, gda.b1, gda.b0)
	graph.createErrorGraph(currIter, SSE)
	f.writeWeightsInFile(gda.b0, gda.b1)

if __name__ == "__main__":
	trainModel()	