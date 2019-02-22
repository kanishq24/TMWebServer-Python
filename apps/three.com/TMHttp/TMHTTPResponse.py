from http.server import BaseHTTPRequestHandler
class TMHttpResponse:
	def __init__(self,handler):
		self.__handler=handler
	def setContentType(self,string):
		self.__handler.send_response(200)
		self.__handler.send_header('Content-type',string)
		self.__handler.end_headers()
	def writeResponse(self,string):
		self.__handler.wfile.write(string.encode())

def get(handler):
	return TMHttpResponse(handler)
