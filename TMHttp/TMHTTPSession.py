import uuid
class TMHTTPSession:
	
	def __init__(self,id,time=1800):
		self.__id=id
		print('888888888888888888888888888888')
		print(type(id))
		self.__time=time
		self.__data={}
	
	def setAttribute(self,key,value):
		self.__data[key]=value

	def getAttribute(self,key):
		#print(self.__data)
		#print("^^^^^^^^^^^^^^^")
		if key is None or key not in self.__data:
			return None
		return self.__data[key]

	def getSessionId(self):  #https://sites.google.com/site/usfcomputerscience/sessions
		return self.__id


def get(id,time=None):
	if time is None:
		return TMHTTPSession(id)
	else :
		return TMHTTPSession(id,time)
