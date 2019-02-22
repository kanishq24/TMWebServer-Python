from http import cookies
import TMHttp
from TMHttp import TMHTTPSession

class TMHTTPRequest:
	def __init__(self,handler,session,data):
		self.__handler=handler
		self.__data=data
		self.__session=session
	def getParameter(self,key):
		if self.__data is None:
			return None
		if key in self.__data:
			return self.__data[key]
		else:
			return None
	def getCookies(self):
		c=self.__handler.headers.get('Cookie')
		if type(c) is str:
			arr=c.split(' ')
			c={}
			for a in arr:
				if a.endswith(':') or a.endswith(';'):
					a=a[:-1]
				d=a.split('=')
				if len(d)>=2:
					c[d[0]]=d[1]
			return c
		else:
			return dict()
	def getSession(self,state=True):
		print("session chla")
		if self.__session is not None:
				return self.__session
		if state is True:
			self.__session=self.__handler.getSession(uuid.uuid4())
			return self.__session
			#New object is created and returned
		else:
			return self.__session
			#Object is returned if exist otherwise returned NULL

			
		
def get(handler,session,data=None):
	return TMHTTPRequest(handler,session,data)
