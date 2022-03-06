class Person():

	#atribut private
	nik = "" #nomor induk kependudukan
	name = "" #nama
	gender = "" #jenis kelamin


	#konstruktor
	def __init__(self, nik = "", name = "", gender = ""):
		self.nik = nik
		self.name = name
		self.gender = gender

	#getter dan setter atribut nik
	def setNIK(self, nik):
		self.nik = nik

	def getNIK(self):
		return self.nik

	#getter dan setter atribut name
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	#getter dan setter atribut gender
	def setGender(self, gender):
		self.gender = gender

	def getGender(self):
		return self.gender


	#method sleep
	def sleep(self):
		print(str(self.name) + " is sleeping")

	#method menampilkan data orang
	def printPerson(self):
		print("NIK          : " + str(self.nik))
		print("Name         : " + str(self.name))
		print("Gender       : " + str(self.gender))