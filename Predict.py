import re
import sys
import os.path

def writeWeightsInFile(b0, b1):
	f = open('weights.txt', "w+")
	f.write(b0, "\n", b1)
	f.close()

def getSlopeValue():
	f = open('weights.txt')
	slope = (f.readlines())[1]
	f.close()
	return slope

def getInterceptValue():
	f = open('weights.txt')
	slope = (f.readlines())[0]
	f.close()
	return slope

def fileExist():
	if os.path.isfile('weights.txt'):
		return True
	else:
		return False

def getEstimateValue(mileage, b0, b1):
	price = b0 + (b1 * mileage)
	return price

def predictPrice():
	if len(sys.argv) != 1:
		# raise Exception("Too many arguments given as parameter.")
		print("Too many arguments given as parameter.")
		exit(1)
	mileage = input("Mileage of car: ")
	if (fileExist() is False):
		m = 0
		p = 0
		writeWeightsInFile(m, p)
	else:
		m = getSlopeValue()
		p = getInterceptValue()
	try:
		price = getEstimateValue(float(mileage), float(p), float(m))
		print("Estimate price for this vehicule would be", price)
	except Exception as e:
		print("\x1b[91merror: ", str(e), "\x1b[0m")

predictPrice()
