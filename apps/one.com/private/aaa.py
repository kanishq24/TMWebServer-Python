from TMHttp import *
class aaa:
	def process(self,request,response):
		print(request)
		try:
			print("1ye chala")
			nn=request.getParameter('nm')
			print("2")
			ss=request.getParameter('sex')
			print("ab ye")
			cc=request.getParameter('ct')
			print('Request arrived')
			print('Name : '+nn)
			print('Gender : '+ss)
			print('City : '+cc)
			#some code to save data
			response.setContentType('text/html')
			response.writeResponse("<!Doctype html>")
			response.writeResponse("<html lang='en'>")
			response.writeResponse("<head>")
			response.writeResponse("<meta charset='utf-8'>")
			response.writeResponse("<title>one.com</title>")
			response.writeResponse("</head>")
			response.writeResponse("<body>")
			response.writeResponse("<h1>Data Saved</h1></body></html>")
		except Exception as e:
			print(e)
