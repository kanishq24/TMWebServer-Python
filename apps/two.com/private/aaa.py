from TMHttp import *
class aaa:
	def process(self,request,response):
		print(request)
		try:
			nn=request.getParameter('nm')
			print('Request arrived')
			print('Name : '+nn)
			#some code to save data
			response.setContentType('text/html')
			response.writeResponse("<!Doctype html>");
			response.writeResponse("<html lang='en'>");
			response.writeResponse("<head>");
			response.writeResponse("<meta charset='utf-8'>");
			response.writeResponse("<title>two.com</title>");
			response.writeResponse("<script>");
			response.writeResponse("function ramu(f)");
			response.writeResponse("{");
			response.writeResponse("if(f.sex[0].checked==false && f.sex[1].checked==false)");
			response.writeResponse("{");
			response.writeResponse("alert(\"Select gender\");");
			response.writeResponse("return false;");
			response.writeResponse("}");
			response.writeResponse("return true;");
			response.writeResponse("}");
			response.writeResponse("</script>");
			response.writeResponse("</head>");
			response.writeResponse("<body>");
			response.writeResponse("<center>");
			response.writeResponse("<h1>Session Tracking Example</h1>");
			response.writeResponse("<h4><u>Using Hidden Form Field</u></h4>");
			response.writeResponse("<h2>Personal Information - Page 2</h2>");
			response.writeResponse("Name : <b>"+nn+"</b></br>");
			response.writeResponse("<form action='/two.com/bbb' onsubmit='return ramu(this)'>");
			response.writeResponse("<input type='hidden' name='nm' id='nm' value='"+nn+"'>");
			response.writeResponse("<table border='0'>");
			response.writeResponse("<tr><td>");
			response.writeResponse("Gender</td><td>");
			response.writeResponse("Male <input type='radio' name='sex' id='ml' value='M'>");
			response.writeResponse("&nbsp;&nbsp;&nbsp;");
			response.writeResponse("Female <input type='radio' name='sex' id='fe' value='F'>");
			response.writeResponse("</td></tr>");
			response.writeResponse("</tr><tr>");
			response.writeResponse("<td colspan='2' align='center'>");
			response.writeResponse("<input type='submit' value='Next'></td></tr></table>");
			response.writeResponse("</form>");
			response.writeResponse("</center>");
			response.writeResponse("</body>");
			response.writeResponse("</html>");
		except Exception as e:
			print(e)
