import re
import sys
import os.path

class predictClass:
	def getEstimateValue(self, mileage, b0, b1):
		price = b0 + (b1 * mileage)
		return price

class fileManip:
	def writeWeightsInFile(self, b0, b1):
		f = open('weights', "w+")
		f.write(str(b0) + "\n" + str(b1))
		f.close()

	def getSlopeValue(self):
		f = open('weights')
		slope = (f.readlines())[1]
		f.close()
		try:
			float(slope)
		except ValueError:
			print("\x1b[91mError line 2 is not a valid number.\x1b[0m")
			exit(1)
		return slope

	def getInterceptValue(self):
		f = open('weights')
		intercept = (f.readlines())[0]
		f.close()
		try:
			float(intercept)
		except ValueError:
			print("\x1b[91mError line 1 is not a valid number.\x1b[0m")
			exit(1)
		return intercept

	def fileExist(self):
		if os.path.isfile('weights') and os.path.getsize('weights') > 0:
			count = len(open('weights').readlines())
			if count != 2:
				return False
			return True
		else:
			return False

def predictPrice():
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
		pr = predictClass()
		price = pr.getEstimateValue(float(mileage), float(p), float(m))
		print("Estimate price for this vehicule would be", price)
	except Exception as e:
		print("\x1b[91merror: ", str(e), "\x1b[0m")

if __name__ == "__main__":
	predictPrice()	