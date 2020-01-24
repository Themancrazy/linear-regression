import re
import sys
import os.path
from matplotlib import pyplot as plt
import numpy as np
import math
from predict import predictClass
from predict import fileManip
import pandas as pd

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

class Graph:
	def __init__(self):
		pass
	def createRegressionGraph(self):
		pass
	def createErrorGraph(self):
		pass
	def updateRegressionGraph(self):
		pass
	def updateErrorGraph(self):
		pass

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
	print("SSE is", SSE / len(miles))

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

	learningRate = 0.001
	iterations = int(input("Number of iterations requested: "))

	gda = GDA(0, 0)
	graph = Graph()
	pr = predictClass()
	f = fileManip()

	if input("Reset slope and intercept values?(y/n) ") == "y":
		f.writeWeightsInFile(0, 0)
	graph.createRegressionGraph()
	graph.createErrorGraph()
	# lossFunction(pr, normalizedMiles, prices, gda)
	for _ in range(iterations):
		tmpB0 = gda.b0GDA(pr, learningRate, prices, normalizedMiles)
		tmpB1 = gda.b1GDA(pr, learningRate, prices, normalizedMiles)
		gda.setb0(tmpB0)
		gda.setb1(tmpB1)
		graph.updateRegressionGraph()
		graph.updateErrorGraph()
	gda.b1 = gda.b1 / (miles.max() - miles.min())
	f.writeWeightsInFile(gda.b0, gda.b1)

if __name__ == "__main__":
	trainModel()	