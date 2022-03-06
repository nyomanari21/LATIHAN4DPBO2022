class Vehicle():
	
	#atribut private
	name = "" #nama kendaraan
	fuelType = "" #tipe bahan bakar kendaraan
	maxPassengers = 0 #kapasitas penumpang


	#konstruktor
	def __init__(self, name = "", fuelType = "", maxPassengers = 0):
		self.name = name
		self.fuelType = fuelType
		self.maxPassengers = maxPassengers

	#getter dan setter atribut name
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	#getter dan setter atribut fuelType
	def setFuelType(self, fuelType):
		self.fuelType = fuelType

	def getFuelType(self):
		return self.fuelType

	#getter dan setter atribut maxPassengers
	def setMaxPassengers(self, maxPassengers):
		self.maxPassengers = maxPassengers

	def getMaxPassengers(self):
		return self.maxPassengers


	#method move
	def Move(self):
		print(self.name + " is moving")

	#method menampilkan data kendaraan
	def printVehicle(self):
		print("Name                    : " + str(self.name))
		print("Fuel Type               : " + str(self.fuelType))
		print("Maximum Passengers      : " + str(self.maxPassengers))