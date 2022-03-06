from Vehicle import Vehicle

class Ship(Vehicle):

	#atribut private
	age = 0 #usia kapal
	shipType = "" #tipe kapal
	countryOfManufacturer = "" #negara pembuat kapal


	#konstruktor
	def __init__(self, age = 0, shipType = "", countryOfManufacturer = ""):
		self.age = age
		self.shipType = shipType
		self.countryOfManufacturer = countryOfManufacturer

	#getter dan setter atribut age
	def setAge(self, age):
		self.age = age

	def getAge(self):
		return self.age

	#getter dan setter atribut shipType
	def setShipType(self, shipType):
		self.shipType = shipType

	def getShipType(self):
		return self.shipType

	#getter dan setter atribut countryOfManufacturer
	def setCountryOfManufacturer(self, countryOfManufacturer):
		self.countryOfManufacturer = countryOfManufacturer

	def getCountryOfManufacturer(self):
		return self.countryOfManufacturer

	#method menampilkan data kapal
	def printShip(self):
		self.printVehicle()
		print("Age                     : " + str(self.age))
		print("Ship Type               : " + str(self.shipType))
		print("Country of Manufacturer : " + str(self.countryOfManufacturer))