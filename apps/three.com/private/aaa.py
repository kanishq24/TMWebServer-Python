from TMHttp import *
class aaa:
	def process(self,request,response):
		print(request)
		try:
			nn=request.getParameter('nm')
			ss=request.getParameter('sex')
			cc=request.getParameter('ct')
			print('Request arrived')
			#some code to save data
			response.setContentType('text/html')
			response.writeResponse("<!Doctype html>");
			response.writeResponse("<html lang='en'>");
			response.writeResponse("<head>");
			response.writeResponse("<meta charset='utf-8'>");
			response.writeResponse("<title>three.com</title>");
			response.writeResponse("</head>");
			response.writeResponse("<body>");
			response.writeResponse("<center>");
			response.writeResponse("<h1>Session Tracking Example</h1>");
			response.writeResponse("<h4><u>Using URL Rewriting</u></h4>");
			response.writeResponse("<a href='/three.com/bbb?nm="+URLEncoder.encode(nn)+"&ct="+URLEncoder.encode(cc)+"&sex="+URLEncoder.encode(ss)+"'>Save</a>");
			response.writeResponse("</center>");
			response.writeResponse("</body>");
			response.writeResponse("</html>");
		except Exception as e:
			print(e)
