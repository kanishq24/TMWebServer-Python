from TMHttp import *
class bbb:
	def process(self,request,response):
		print(request)
		print(response)
		try:
			nn=request.getParameter('nm')
			ss=request.getParameter('sex')
			print('Request arrived at bbb')
			print('Name : '+nn)
			print('Sex : '+ss)
			#some code to save data
			response.setContentType('text/html')
			response.writeResponse("<!Doctype html>")
			response.writeResponse("<html lang='en'>")
			response.writeResponse("<head>")
			response.writeResponse("<meta charset='utf-8'>")
			response.writeResponse("<title>two.com</title>")
			response.writeResponse("</head>")
			response.writeResponse("<body>")
			response.writeResponse("<center>")
			response.writeResponse("<h1>Session Tracking Example</h1>")
			response.writeResponse("<h4><u>Using Hidden Form Field</u></h4>")
			response.writeResponse("<h2>Personal Information - Page 3</h2>")
			response.writeResponse("Name : <b"+nn+"</b></br>")
			response.writeResponse("Sex : <b>"+ss+"</b></br>")
			response.writeResponse("<form action='/two.com/ccc' onsubmit='return ramu(this)'>")
			response.writeResponse("<input type='hidden' name='nm' id='nm' value='"+nn+"'>")
			response.writeResponse("<input type='hidden' name='sex' id='sex' value='"+ss+"'>")
			response.writeResponse("<table>")
			response.writeResponse("<tr><td>")
			response.writeResponse("Select city</td><td>")
			response.writeResponse("<select name='ct' id='ct'>")
			response.writeResponse("<option value='-1'>&lt;Select&gt;</option>")
			response.writeResponse("<option value='101'>Pune</option>")
			response.writeResponse("<option value='102'>Ujjain</option>")
			response.writeResponse("<option value='103'>Indore</option>")
			response.writeResponse("</select></td></tr></tr><tr>")
			response.writeResponse("<td colspan='2' align='center'>")
			response.writeResponse("<input type='submit' value='Save'></td></tr></table>")
			response.writeResponse("</form>")
			response.writeResponse("</center>")
			response.writeResponse("</body>")
			response.writeResponse("</html>")
			print('bbb ka kaam khtm')
		except Exception as e:
			print('exception in bbb.py :'+e)
