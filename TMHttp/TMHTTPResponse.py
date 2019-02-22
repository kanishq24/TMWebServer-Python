from http.server import BaseHTTPRequestHandler
from http import cookies
from urllib import parse
import inspect
import time
class TMHttpResponse:
	def __init__(self,handler,id):
		self.__handler=handler
		self.__send_response=False
		self.__end_headers=False
		self.__session_id=id
	def sendResponse(self):
		print('N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	NN  N N N N N N N N N N N N N N N N N N N N N N N N N N NN  N N N N N N N N N N N N N N N N N N N N N N N N N N NN  N N N N N N N N N N N N N N N N N N N N N N N N N N N',self.__send_response)
		if self.__send_response is False:
			print('sendResponse chala h dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
			self.__handler.send_response(200)
			self.__send_response=True
			self.setCookie('id',self.__session_id)
			print('session id cookie me response >>',self.__handler.headers.get('Cookie'))
			return True
		else:
			return False
	def setContentType(self,string):
		if self.sendResponse():
			print('sendResponse() chala h')
		self.__handler.send_header('Content-type',string)
	def writeResponse(self,string):
		if self.__end_headers is False:
			self.__handler.end_headers()
			self.__end_headers=True
		self.__handler.wfile.write(string.encode())
	#depricated, no longer available since 10/10/18 
	def endHeaders(self,state):
		self.__end_headers=state

	def send_header(self,keyword,value=None):
		if self.sendResponse():
			print('sendResponse() chala h')
		self.__handler.send_header(keyword,value)

	
	def setCookie(self,name, value ,expires='',max_age=0, domain=None,secure=False, httponly=False, path=None):
		try :
			morsel = cookies.Morsel()
			name, value = str(name), str(value) #https://github.com/William-An/CloudPrint/blob/952f25341ea0423b83ee2ded1927ba0cf160a095/cloudprint/Lib/site-packages/web.py-0.40.dev0-py3.5.egg/web/utils.py
			morsel.set(name, value, parse.quote(value))
			if isinstance(expires, int) and expires < 0:
				expires = -1000000000
			if max_age > 0:
				morsel['max-age']=max_age
			if type(expires) is not str:
				#morsel['expires'] = self.__handler.date_time_string(time.mktime(time.gmtime(expires)))
				morsel['expires']=expires
			else:
				morsel['expires'] = expires
			if path is not None:
				morsel['path'] = path+'/'    #or ctx.homepath+'/'
			if domain:
				morsel['domain'] = domain
			if secure:
				morsel['secure'] = secure
			value = morsel.OutputString()
			if httponly:
				value += '; httponly'
			self.sendResponse()
			self.send_header('Set-Cookie',value)
			print("setcookie pura chala h",value)
		except Exception as e:
			print(e)
			print(type(e))
			print('Exception is raised on %s '% inspect.trace()[-1][3])


def get(handler,id):
	return TMHttpResponse(handler,id)
