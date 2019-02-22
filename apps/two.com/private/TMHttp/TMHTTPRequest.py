class TMHTTPRequest:
	def __init__(self,data):
		self.__data=data
	def getParameter(self,key):
		if key in self.__data:
			return self.__data[key]
		else:
			return None

def get(data):
	return TMHTTPRequest(data)
