class Building:

	def __init__(self, nStoreys, nCanbroken):
			self._storeys = []
			for i in range(nStoreys):
				if i < nCanbroken:
					self._storeys.append(1)
 				else:
					self._storeys.append(0)

	def getMaximnStoreys(self):
		return len(self._storeys)-1

	def Test(self, index):
		if self._storeys[index] == 1:
			return True
		else:
			return False

class EggDoom:
	def __init__(self, nStoreys, nCanbroken, nEggs):
		self._testBuilding = Building(nStoreys, nCanbroken)
		self._numEggs = nEggs
		self._testCount = 0

	def Start(self):
		if self._testBuilding.Test(0):
			self._testCount += 1
			max_storeys = self._testBuilding.getMaximnStoreys()
			min_storeys = 0 
			mid = max_storeys+min_storeys
			mid = mid/2
			self.TestLoop(min_storeys, mid, max_storeys)
		else:
			self._testCount += 1
			print 1


	def TestLoop(self, nMin, nMid, nMax):
		if self._numEggs > 0 and nMax - nMin > 1:
			if self._testBuilding.Test(nMid):
				self.TestLoop(nMid, (nMax+nMid)/2, nMax)
				self._testCount += 1
			else:
				self._numEggs -= 1
				self.TestLoop(nMin, (nMin+nMid)/2, nMid)
				self._testCount += 1
		else:
			print nMax+1

if __name__ == "__main__":
	Doom = EggDoom(100, 6, 55)
	Doom.Start()
	print Doom._testBuilding._storeys
	print Doom._testCount

