import socket
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
import sys
from pydoc import locate
import os
import urllib3
from query_string import query_string
from mimetypes import MimeTypes
from TMHttp import *
import uuid
#deta structure object
class WebApplication:
	def __init__(self):
		#more for app.conf json properties
		self.__homepage=""
		self.__pyMapping={}
	def setHomepage(self,homepage):
		self.__homepage=homepage
	def getHomepage(self):
		return self.__homepage
	def setPyMapping(self,pyMapping):
		self.__pyMapping=pyMapping
	def getPyValue(self,key):
		if key in self.__pyMapping:
			print(self.__pyMapping[key]+"value of key+++++++++")
			return self.__pyMapping[key]
		else: 
			return None
	def getPyMapping(self):
		return self.__pyMapping

#end of class WebApplication
class SessionData:
	def __init__(self,context_name,session=None):
		self.__context_name=context_name
		self.__session=session
		self.__request=None
		self.__response=None
	def getSession(self):
		return self.__session
	def setRequest(self,request):
		self.__request=request
	def setResponse(self,response):
		self.__response=response
	def getRequest(self):
		return self.__request
	def getResponse(self):
		return self.__response
	def setRequestAndResponse(self,request,response):
		self.__request=request
		self.__response=response
	def isRequestAndResponseExists(self):
		return	self.__request is not None and self.__response is not None

def getObject(context,fqn):
	spath=sys.path
	sys.path.insert(0,'./apps/'+context+'/private')
	cls=locate(fqn+'.'+fqn.split('.')[-1])
	o=cls()
	sys.path=sys.path[1:]
	return o

PORT_NUMBER=0
IP_ADDRESS=None
try:

	with open('server.conf') as json_data:
		d = json.load(json_data)
		IP_ADDRESS=d['ip_address']
		PORT_NUMBER=d['port']
		
except FileNotFoundError:
	print("server.conf file not found.")
	sys.exit()

#This class will handles any incoming request from
#the browser 

#MyHandler class


class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		print(self.path)
#		print(self.headers)
#		print(self.client_address)
		direct=False
		if self.path=='/favicon.ico':
			return	
		if self.path=='/':
			self.path='/default/index.html'	
			default=True  # indicator that tells us to serve default folder items
			mime=MimeTypes() #creation of a MimeTypes class object which is asigned to mime or named mime
			mime_type = mime.guess_type(self.path) #check -------------------FTP serving items giving error----- min.js file
			#session creation
			context=self.path.split('/')[1]
		#	if context not in sessionMap:
		#		session=TMHTTPSession.get()
		#		arr=[] #watcher wala kam 
		#		arr.append(session)
		#		sessionMap[context]=arr
		#	session=sessionMap[context][0]
		#	id=session.getSessionId()
		#	if id not in sessionDataMap:
		#		sessionDataMap[id]=SessionData(context,session)
		#		id=None
		#		session=None
			self.send_response(200)
			self.send_header('Content-type',mime_type[0])
			self.end_headers()
			f=open('.'+self.path,"rb")
			self.wfile.write(f.read())
			f.close()
		else: #path which is directing to other than / (default) folder
			if self.path.endswith('/'):
				self.path=self.path[:-1]
			if len(self.path.split('/'))==2 and self.path!='/favicon.ico' :
				context=self.path.split('/')[1]
		#		if context not in sessionMap.keys():
		#			session=TMHTTPSession.get()
		#			arr=[] #watcher wala kam 
		#			arr.append(session)
		#			sessionMap[context]=arr
		#		if sessionMap[context][0].getSessionId() not in sessionDataMap.keys():
		#			id=sessionMap[context][0].getSessionId()
		#			sessionDataMap[id]=SessionData(context,id)
		#			id=None
								
				homepage=contextMap[context].getHomepage()
				if homepage.startswith('/'):
					homepage=homepage[1:]
				if os.path.isfile('./apps/'+context+'/'+homepage):
					self.send_response(301)
					new_path='%s%s'%('http://192.168.1.175:6060',self.path+'/'+homepage)
					self.send_header('Location',new_path)
					self.end_headers()
				else :
					if os.path.isfile("./apps"+self.path+"/index.html"):
						self.send_response(301)
						new_path = '%s%s'%('http://192.168.1.175:6060', self.path+"/index.html")
						self.send_header('Location',new_path)
						self.end_headers()	
					else:
						if os.path.isfile("./apps"+self.path+"/index.htm"):
							self.send_response(301)
							new_path='%s%s'%('http://192.168.1.175:6060',self.path+"/index.htm")
							self.send_header('Location',new_path)
							self.end_headers()
						else:
							if os.path.isfile('./apps'+self.path+"/index.py"):
								print('yet to be implemented')
							pass
							#obj=getObject()      #socket ka object bana
							#if obj:
							#	print("++++++++++++++++++++++++++++++++++")
							#	print("query string from the server ",queryString)
							#	request=TMHTTPRequest.get(queryString)
							#	response=TMHTTPResponse.get(self)
							#	obj.process(request,response)
							#else:
							#	self.send_error(404,'NOT FOUND')
							
			else:
				queryString={}
				if self.path.startswith('/default'):
					hpath='.'+self.path
					direct=True
					if(os.path.isfile(hpath)):
						pass
					else:
						self.send_error(404,'NOT FOUND')
				else:
						#Resource for Anything else
						queryString=query_string(self.path)
						if queryString:
							webpageName=self.path.split('?')[0].split('/')[-1];
						else:
							webpageName=self.path.split('/')[-1]
						context=self.path.split('/')[1]
		#				if context not in sessionMap.keys():
		#					session=TMHTTPSession.get()
		#					arr=[] #watcher wala kam 
		#					arr.append(session)
		#					sessionMap[context]=arr
		#				if sessionMap[context][0].getSessionId() not in sessionDataMap.keys():
		#					id=sessionMap[context][0].getSessionId()
		#					sessionDataMap[id]=SessionData(context,id)
		#					id=None
						c=self.headers.get('Cookie')
						id=uuid.UUID(c[len('id='):c.find('; ')])
						print(type(id))
						p=contextMap[context].getPyValue(webpageName)
						if p != None:
							session=self.getSession()
							if context not in sessionMap:
								session=self.getSession()
								arr=[]
								arr.append(session)
								sessionMap[context]=arr
							else:
								pass
								#if id in SessionDataMap
								#	session=sessionDataMap[id].getSession()
								#
							#	session=sessionMap[context][0]
							id=session.getSessionId()
							if id not in sessionDataMap:
								sessionDataMap[id]=SessionData(context,session)
							# context me webpage h jo mapping me dekhna h
							obj=getObject(context,p)      #socket ka object bana
							if obj:
								sessionData=sessionDataMap[id]
								if not sessionData.isRequestAndResponseExists():
									request=TMHTTPRequest.get(self,session,queryString)
									response=TMHTTPResponse.get(self,id)
									sessionData.setRequestAndResponse(request,response)
								else:
									request=sessionData.getRequest()
									request=TMHTTPRequest.get(self,request.getSession(),queryString)
									response=TMHTTPResponse.get(self,request.getSession().getSessionId())
								obj.process(request,response)
							else:
								self.send_error(404,'NOT FOUND')
						else:
								direct=True
								hpath='./apps'+self.path
						#yaha sahi karna h 
						#direct serve karna h
		if direct:
			if queryString:
				pass #direct request me query string ke elements
			else:
				pass
			if os.path.isfile(hpath):
				mime=MimeTypes()
				mime_type = mime.guess_type(self.path)
				self.send_response(200)
				self.send_header('Content-type',mime_type[0])
				self.end_headers()
				f=open(hpath,"rb")
				self.wfile.write(f.read())
			else:
				self.send_error(404,'NOT FOUND')
			
				
					
				#f=open(hpath,"rb")
				#self.wfile.write(f.read())
		# multiple condition check karna h ki html nahi to kya and so on
		#doGet ends here
		return

	def getSession(self,id=None):
		if id is None:
			id=uuid.uuid4()
			return self.getSession(id)
		context=self.path.split('/')[1]
		if id is not None and id not in sessionDataMap:
			session=TMHTTPSession.get(id)
			sessionDataMap[id]=SessionData(context,session)
			if context in sessionMap:
				sessionMap[context].append(session)
			else:
				arr=[]
				arr.append(session)
				sessionMap[context]=arr
			return session
		else:
			if id in sessionDataMap:
				return sessionDataMap[id].getSession()



#end of MyHandler class


def getApps():
	for (r,d,fi) in os.walk('./apps'):
		return d

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer((IP_ADDRESS, PORT_NUMBER), myHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
                #preparing all the required data structure
	apps=getApps()
# using regular expression to extract certain part from string (or to say extract apps name from root and matching it with our apps list.
	contextMap={}
	for context in apps:
		w = WebApplication()
		contextMap[context]=w
	
	context=""
	private=False
	for (r,d,fi) in os.walk('./apps'):
		if r.endswith('/'):
			r=r[:-1]
		splittedPath=r.split('/')
		if len(splittedPath)>2:	
			if r.split('/')[2] in apps and len(r.split('/'))==3:
				context=r.split('/')[2]
				if 'private' in d:
					private=True
				else: 
					private=False			
			else:
				
			
				#------------------------------
				#private folder exists karta h and relative path me sirf privae folder tak h (r)
				if private and len(r.split('/'))>=4 and r.split('/')[3]=='private':
					try:
						with open(r+'/app.conf') as f:
							
							try :
								data = json.load(f)
								if 'homepage' in data:
									contextMap[context].setHomepage(data['homepage'])
								if 'pyMapping' in data:
									map={}
									for url,path in data['pyMapping'].items():
										map[url]=path
									contextMap[context].setPyMapping(map)
										
											
									
							except:
								print(r)
								print("apps.conf is incorect")
					except FileNotFoundError:
						pass
				else:
					#private folder exists nahi karta h
					private=False
					
					#private=False
					
	#DS for maintaining session
	sessionMap={}
	sessionDataMap={}


	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')

	server.socket.close()


