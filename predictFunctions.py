import re
import sys
import os.path

class predict:
	def __init__(self, b0, b1):
		self.b0 = b0
		self.b1 = b1

	def getEstimateValue(self, mileage):
		price = self.b0 + (self.b1 * mileage)
		return price

class fileManip:
	def writeWeightsInFile(self, b0, b1):
		f = open('weights.txt', "w+")
		f.write(str(b0) + "\n" + str(b1))
		f.close()

	def getSlopeValue(self):
		f = open('weights.txt')
		slope = (f.readlines())[1]
		f.close()
		return slope

	def getInterceptValue(self):
		f = open('weights.txt')
		slope = (f.readlines())[0]
		f.close()
		return slope

	def fileExist(self):
		if os.path.isfile('weights.txt'):
			return True
		else:
			return False

def predictPrice():
	if len(sys.argv) != 1:
		print("Too many arguments given as parameter.")
		exit(1)
	mileage = input("Mileage of car: ")
	f = fileManip()
	if (f.fileExist() is False):
		m = 0
		p = 0
		f.writeWeightsInFile(m, p)
	else:
		m = f.getSlopeValue()
		p = f.getInterceptValue()
	try:
		p = predict(float(p), float(m))
		price = p.getEstimateValue(float(mileage))
		print("Estimate price for this vehicule would be", price)
	except Exception as e:
		print("\x1b[91merror: ", str(e), "\x1b[0m")