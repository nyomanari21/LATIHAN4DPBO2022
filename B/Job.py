class Job():

	#atribut private
	nip = "" #nomor identitas pegawai
	companyName = "" #nama perusahaan
	position = "" #jabatan


	#konstruktor
	def __init__(self, nip = "", companyName = "", position = ""):
		self.nip = nip
		self.companyName = companyName
		self.position = position

	#getter dan setter atribut nip
	def setNIP(self, nip):
		self.nip = nip

	def getNIP(self):
		return self.nip

	#getter dan setter atribut companyName
	def setCompanyName(self, companyName):
		self.companyName = companyName

	def getCompanyName(self):
		return self.companyName

	#getter dan setter atribut position
	def setPosition(self, position):
		self.position = position

	def getPosition(self):
		return self.position


	#method menampilkan data pekerjaan
	def printJob(self):
		print("NIP          : " + str(self.nip))
		print("Company Name : " + str(self.companyName))
		print("Position     : " + str(self.position))