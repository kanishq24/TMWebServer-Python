from TMHttp import *
class ccc:
	def process(self,request,response):
		print(request)
		try:
			nn=request.getParameter('nm')
			ss=request.getParameter('sex')
			cc=request.getParameter('ct')
			print('Request arrived')
			print('Name : '+nn)
			print('Sex : '+ss)
			print('city: '+cc)
			#some code to save data
			response.setContentType('text/html')
			response.writeResponse("<!Doctype html>");
			response.writeResponse("<html lang='en'>");
			response.writeResponse("<head>");
			response.writeResponse("<meta charset='utf-8'>");
			response.writeResponse("<title>two.com</title>");
			response.writeResponse("</head>");
			response.writeResponse("<body>");
			response.writeResponse("<center>");
			response.writeResponse("<h1>Session Tracking Example</h1>");
			response.writeResponse("<h4><u>Using Hidden Form Field</u></h4>");
			response.writeResponse("<h1>Data Saved !!!!!!!!!!!</h1></body></html>");
			response.writeResponse("Name : "+nn+"</br>");
			response.writeResponse("Gender : "+ss+"</br>");
			response.writeResponse("City : "+cc+"</br>");
			response.writeResponse("</center>");
		except Exception as e:
			print(e)
