import re
import sys
import os.path
from predictFunctions import predict
from predictFunctions import fileManip
import pandas as pd

def lossFunction(miles, prices, b0, b1):
	for m in miles:
		print(m)
		# predictY = 
		# if nmile is at same position as an observation
			# add difference to SSE total.

def trainModel():
	file = r'data.csv'
	df = pd.read_csv(file)
	miles = df['km']
	prices = df['price']
	tmpB0 = 0
	tmpB1 = 0
	L = 0.0001
	iterations = int(input("Number of iterations requested: "))
	p = predict(tmpB0, tmpB1)
	f = fileManip()
	lossFunction(miles, prices, tmpB0, tmpB1)
	# for i in range(iterations):
	f.writeWeightsInFile(tmpB0, tmpB1)