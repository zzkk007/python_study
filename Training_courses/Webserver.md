"--------------------------------------------------------------"

					Web服务器案例课件

"--------------------------------------------------------------"

1、TCP/IP、Http、Socket的关系理解：

	TCP/IP协议是传输层协议，主要解决数据如何在网络中传输，而HTTP是应用层协议，主要解决如何包装数据。

	关于TCP/IP和HTTP协议的关系，网络有一段比较容易理解的介绍：我们在传输数据时，
	可以只使用（传输层）TCP/IP协议，但是那样的话，如果没有应用层，便无法识别数据内容，
	如果想要使传输的数据有意义，则必须使用到应用层协议，应用层协议有很多，
	比如HTTP、FTP、TELNET等，也可以自己定义应用层协议。
	WEB使用HTTP协议作应用层协议，以封装HTTP 文本信息，然后使用TCP/IP做传输层协议将它发到网络上。

	术语TCP/IP代表传输控制协议/网际协议，"IP"代表网际协议，TCP和UDP使用该协议从一个网络传送数据报
	到另一个网络。把IP想象成一种高速公路，它允许其他协议在上面行驶并找到其它电脑的出口。
	TCP和UDP是高速公路上的"卡车"，它们携带的货物就像HTTP，文件传输协议FTP这样的协议等。

	HTTP（英文：HyperText Transfer Protocol，缩写：HTTP）
	是一种用于分布式、协作式和超媒体信息系统的应用层协议。HTTP是万维网的数据通信的基础。

	HTTP是一个客户端（用户）和服务器端（网站）之间传输信息的协议，客户端使用web浏览器发起HTTP请求
	给web服务器，web服务器发送被请求的消息给客户端。

	Socket是对TCP/IP协议的封装，Socket本身并不是协议，而是一个调用接口（API）。
	通过sockt我们才能使用TCP/IP协议。

	实际上，Socket跟TCP/IP协议没有必然的联系。Socket编程接口在设计的时候，就希望也能适应其他的网络协议。
	所以说，Socket的出现只是使得程序员更方便地使用TCP/IP协议栈而已，是对TCP/IP协议的抽象，
	从而形成了我们知道的一些最基本的函数接口，比如create、 listen、connect、accept、send、read和write等等。

	网络有一段关于Socket和TCP/IP协议关系的说法比较容易理解：TCP/IP只是一个协议栈，
	就像操作系统的运行机制一样，必须要具体实现，同时还要提供对外的操作接口。
	这个就像操作系统会提供标准的编程接口，比如win32编程接口一样，
	TCP/IP也要提供可供程序员做网络开发所用的接口，这就是Socket编程接口。

	接上述的那个例子：HTTP是轿车，提供了封装或者显示数据的具体形式；Socket是发动机，提供了网络通信的能力。

	实际上，传输层的TCP是基于网络层的IP协议的，而应用层的HTTP协议又是基于传输层的TCP协议的，
	而Socket本身不算是协议，就像上面所说，它只是提供了一个针对TCP或者UDP编程的接口。


1、HTTP协议简介：

	HTML是一种用来定义网页的文本，会HTML，就可以编写网页
	HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。
	
	HTTP请求：
		
		步骤1:浏览器首先向服务器发送HTTP请求，请求包括：

			方法：GET还是POST,GET仅请求资源，POST会附带用户数据

			路径：/full/url/path

			域名：由Host头指定

			以及其他相关的Header

			如果是POST，那么请求还包括一个Body，包含用户数据。

		
		步骤2:服务器向浏览器返回HTTP响应，响应包括：

			响应代码：200表示成功。
					  3xx表示重定向。
					  4xx表示客户端发送的请求有错误。
					  5xx表示服务器端处理时发生了错误。

			响应类型：
					  由Content-Type指定

			以及其他相关的Header:

			通常服务器的HTTP响应会携带内容，也就是一个Body,包含响应的内容，
			网页的HTML源码就在Body中。

		
		步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再发送HTTP请求，重复步骤1,2
			
			Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。
			当我们编写一个页面时，我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片，
			视频等。浏览器如何需要请求图片和视频，它会发送另外一个HTTP请求，因此，一个HTTP请求
			只处理一个资源（此时就可以理解为TCP协议中的短链接，每个链接中获取一个资源，如需要多个
			就需多个链接）


	HTTP格式：

		每个HTTP请求和响应都有遵循相同的格式，一个HTTP包含Header和Body两部分，其他Body是可选的。

		HTTP协议是一种文本协议，所以，它的格式非常简单

		HTTP GET请求格式:

			GET /path Http/1.1
			Header1: Value1
			Header2: Value2
			Header3；Value3
		每一Header一行一个，换行符\r\n

		HTTP POST请求的格式：

			POST /path HTTP/1.1
			Header1: Value1
			Header2: Value2
			Header3: Value3


			body data goes here...
			当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

		HTTP响应的格式：
			200 OK
			Header1:Value1
			Header2:Value2
			Header3:Value3

			
			body data goes here...

			HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。

			请再次注意，Body的数据类型由Content-Type头来确定，
			如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。
			
			当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，
			所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。
			压缩的目的在于减少Body的大小，加快网络传输。	


2、Web静态服务器-1显示固定的页面:


	#coding=utf-8
	import socket
	from multiprocessing import Process


	def handleClient(clientSocket):
	'用一个新的进程，为一个客户端进行服务'
		recvData = clientSocket.recv(2014)
		requestHeaderLines = recvData.splitlines()
		for line in requestHeaderLines:
		print(line)
							   
		responseHeaderLines = "HTTP/1.1 200 OK\r\n"
		responseHeaderLines += "\r\n"
		responseBody = "hello world"
										   
		response = responseHeaderLines + responseBody
		clientSocket.send(response)
	    clientSocket.close()
	
	
	def main():
	'作为程序的主控制入口'
			 
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    serverSocket.bind(("", 7788))
		serverSocket.listen(10)
	    while True:
		    clientSocket,clientAddr = serverSocket.accept()
	        clientP = Process(target = handleClient, args = (clientSocket,))
	        clientP.start()
	        clientSocket.close()
	
	
	if __name__ == '__main__':
	    main()

					
服务器端接收的请求：

	GET /favicon.ico HTTP/1.1
	Host: 172.25.16.245:7799
	Connection: keep-alive
	User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) 
				Chrome/59.0.3071.86 Safari/537.36
	Accept: image/webp,image/apng,image/*,*/*;q=0.8
	Referer: http://172.25.16.245:7799/
	Accept-Encoding: gzip, deflate
	Accept-Language: zh-CN,zh;q=0.8


客户端通过google浏览器输入：

	172.25.16.245:7799
	页面显示:hello world


3、Web静态服务器-2-显示需要的页面：

	#coding=utf-8
	import socket
	from multiprocessing import Process
	import re


	def handleClient(clientSocket):
		'用一个新的进程，为一个客户端进行服务'
		recvData = clientSocket.recv(2014)
		requestHeaderLines = recvData.splitlines()
		for line in requestHeaderLines:
			print(line)

		httpRequestMethodLine = requestHeaderLines[0]
		getFileName = re.match("[^/]+(/[^ ]*)", httpRequestMethodLine).group(1)
		print("file name is ===>%s"%getFileName) #for test

		if getFileName == '/':
			getFileName = documentRoot + "/index.html"
		else:
			getFileName = documentRoot + getFileName

		print("file name is ===2>%s"%getFileName) #for test

		try:
			f = open(getFileName)
		except IOError:
			responseHeaderLines = "HTTP/1.1 404 not found\r\n"
			responseHeaderLines += "\r\n"
			responseBody = "====sorry ,file not found===="
		else:
			responseHeaderLines = "HTTP/1.1 200 OK\r\n"
			responseHeaderLines += "\r\n"
			responseBody = f.read()
			f.close()
		finally:
			response = responseHeaderLines + responseBody
			clientSocket.send(response)
			clientSocket.close()


	def main():
		'作为程序的主控制入口'

		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serverSocket.bind(("", 7788))
		serverSocket.listen(10)
		while True:
			clientSocket,clientAddr = serverSocket.accept()
			clientP = Process(target = handleClient, args = (clientSocket,))
			clientP.start()
			clientSocket.close()


	#这里配置服务器
	documentRoot = '/home/pyhton/zhangkun'
	if __name__ == '__main__':
	main()


	文件index.heml的内容是一个简单的HTML页面：

	<html>
	<!-- 网页的标题、图标... -->
	<head>
	<mate charset="utf-8">
	<title>第一个网页</title>
	</head>
	<!-- 网页的具体内容 -->
	<body>
	这是网页的内容
	<a href="http://www.baidu.com" target="_blank">百度</a>

	<h1>666666666</h1>
	<p>ppppppppppp</p>

	<div>
	<p>ppppppppppp</p>
	</div>

	<ul>
	<li>hahaha</li>
	<li>hahaha</li>
	<li>hahaha</li>
	</ul>

	<ol>
	<li>ahahah</li>
	<li>ahahah</li>
	<li>ahahah</li>
	</ol>

	<img src="text.png">    
	</body>
	</html>


	这个页面会有两个请求：
		一个是/home/zhangkun/python/index.html，
		一个是/home/zhangkun/python/text.png。
	一个HTTP请求只处理一个资源,有过个资源就需要创建多个请求。



Web静态服务器-3-使用类:

	把上面的程序封装到一个类里面：

	#coding=utf-8
	import socket
	import sys
	from multiprocessing import Process
	import re

	class WSGIServer(object):

		addressFamily = socket.AF_INET
		socketType = socket.SOCK_STREAM
		requestQueueSize = 5

		def __init__(self, server_address):
			#创建一个tcp套接字
			self.listenSocket = socket.socket(self.addressFamily,self.socketType)
			#允许重复使用上次的套接字绑定的port
			self.listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			#绑定
			self.listenSocket.bind(server_address)
			#变为被动，并制定队列的长度
			self.listenSocket.listen(self.requestQueueSize)

		def serveForever(self):
			'循环运行web服务器，等待客户端的链接并为客户端服务'
			while True:
			#等待新客户端到来
			self.clientSocket, client_address = self.listenSocket.accept()

			#方法2，多进程服务器，并发服务器于多个客户端
			newClientProcess = Process(target = self.handleRequest)
			newClientProcess.start()

			#因为创建的新进程中，会对这个套接字+1，所以需要在主进程中减去依次，即调用一次close
			self.clientSocket.close()

		def handleRequest(self):
			'用一个新的进程，为一个客户端进行服务'
			recvData = self.clientSocket.recv(2014)
			requestHeaderLines = recvData.splitlines()
			for line in requestHeaderLines:
				print(line)

			httpRequestMethodLine = requestHeaderLines[0]
			getFileName = re.match("[^/]+(/[^ ]*)", httpRequestMethodLine.group(1))
			print("file name is ===>%s"%getFileName) #for test

			if getFileName == '/':
				getFileName = documentRoot + "/index.html"
			else:
				getFileName = documentRoot + getFileName

			print("file name is ===2>%s"%getFileName) #for test

			try:
				f = open(getFileName)
			except IOError:
				responseHeaderLines = "HTTP/1.1 404 not found\r\n"
				responseHeaderLines += "\r\n"
				responseBody = "====sorry ,file not found===="
			else:
				responseHeaderLines = "HTTP/1.1 200 OK\r\n"
				responseHeaderLines += "\r\n"
				responseBody = f.read()
				f.close()
			finally:
				response = responseHeaderLines + responseBody
				self.clientSocket.send(response)
				self.clientSocket.close()

	#设定服务器的端口
	serverAddr = (HOST, PORT) = '', 8888
	#设置服务器服务静态资源时的路径
	documentRoot = './html'

	def makeServer(serverAddr):
		server = WSGIServer(serverAddr)
		return server

		def main():
			httpd = makeServer(serverAddr)
	print('web Server: Serving HTTP on port %d ...\n'%PORT)
	  httpd.serveForever()

	  if __name__ == '__main__':
	  main()


"---------------------------------------------------------------------"

服务器动态资源请求:

1、浏览器请求动态页面过程：

	a、http请求动态资源 （浏览器--->服务器）

	b、通过wsgi调用一个属性（服务器--->应用程序框架）

	c、通过引用调用web服务器的方法，设置返回的状态和头信息（应用程序框架--->服务器）

	d、调用返回，此时web服务器保存了刚刚设置的信息（服务器--->应用程序框架）

	e、查询数据库，生成动态页面的body信息（应用程序框架）

	f、把生产的body信息返回给web服务器应用(应用程序框架--->服务器)

	g、web服务器把数据返回给浏览器(web服务器---->浏览器)



2、WSGI:

	怎么在你刚刚建立的Web服务器上运行一个 Django应用和Flask应用，如何不做任何改变而适应不同的web架构呢？

	那么，怎么才能不修改服务器和架构代码而确保可以在多个架构下运行web服务器呢？
	答案就是Python Web Server Gateway Interface(简称：WSGI，读作"wizgy")

	WSGI允许开发者将选择web框架和web服务器分开，可以混合匹配web服务器和web框架，选择一个合适的匹配。
	比如,可以在Gunicorn 或者 Nginx/uWSGI 或者 Waitress上运行 Django, Flask, 或 Pyramid。
	真正的混合匹配，得益于WSGI同时支持服务器和架构：

	web服务器必须具备WSGI接口，所有的现代Python Web框架都已具备WSGI接口，
	它让你不对代码作修改就能使服务器和特点的web框架协同工作。

	WSGI由web服务器支持，而web框架允许你选择适合自己的配对，
	但它同样对于服务器和框架开发者提供便利使他们可以专注于自己偏爱的领域和专长而不至于相互牵制。
	其他语言也有类似接口：java有Servlet API，Ruby 有 Rack。


	什么是wsgi:

		(1)RESTful只是设计风格而不是标准，而WSGI则是Python语言中所定义的Web服务器和Web应用程序之间
			或者框架之间的通用接口标准。

		(2)WSGI就是一座桥梁，桥梁的一端是服务器或网关端，另一端称为应用端或者框架，
		   WSGI的作用就是在协议之间进行转化。WSGI将Web组件分成了三类：Web 服务器(WSGI Server)
			Web中间件(WSGI MiddleWare)与Web应用程序(WSGI Application).

		(3)Web Server接收HTTP请求，封装一系列环境变量，按照WSGI接口标准调用注册WSGI Application
			最后将响应返回给客户端。


		(4)Web 应用的本质：

				浏览器发送HTTP请求
				服务器接收到请求，生成HTML文档
				服务器把HTML文档作为HTTP响应的Body发送给浏览器
				浏览器收到HTTP响应，从HTTP Body取出HTML文档进行显示

	接收HTTP请求，解析HTTP请求，发送HTTP响应都是重复的苦力活，如果我们自己来写这些底层代码，还没有
	开始写HTML，先要花把个月研读HTTP规范，所以底层的代码应该由专门的服务器软件实现，python专注于
	生产HTML文档。

	因为我们不想接触TCP连接，HTTP原始请求和响应格式，所以需要一个统一的接口，专心用Python编写业务。
	这个接口就是WSGI：web服务器网关接口


定义WSGI接口：

	WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
	我们来看一个非常简单的Web版本"Hello World"

	def application(environ,start_response):
		start_response('200 OK',[('Context-Type','text/thml')])
		return 'Hello World'
	
	上面的 application() 函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
		
		environ: 一个包含所有HTTP请求信息的dict对象；
		start_response:一个发送HTTP响应的函数
	
	在application()函数中，调用：
		start_response('200 OK',[('Content-Type','text/html')])

	就发送了HTTP响应的Header,注意Header只能发送一次，也就是只能调用一次start_response()。
	start_response()函数接收两个参数：
		一个是HTTP响应码，一个是一组元组列表list表示的HTTP Header，
		每个Header用一个包含两个str的tuple表示。
	然后，函数的返回值'Hello world'将作为HTTP响应的Body发送给浏览器。

	有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML,
	通过start_response()发送Header,最后返回Body（HTTP响应格式）

	整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们编写，
	我们只负责在更高层上考虑如何响应请求就可以了。


	不过，这个application()函数怎么调用？如果我们自己调用，两个参数environ和start_response
	我们没法提供，返回的str也没法给浏览器。

	所以application()函数必须由wsgi服务器来调用，有很多符合WSGI规范的服务器，我们可以挑选一个来用

	Python 内置了一个WSGI服务器，这个模块叫做wsgiref,它是用纯Python编写的WSGI服务器的参考实现，
	所谓的参考实现是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。


运行WSGI服务：

	编写server.py,负责启动WSGI服务器，加载应用程序application()函数。

	from wsgiref.simple_server import make_server

	def application(environ,start_response)
		start_response('200 OK',[('Content-type','text/html')])
		return "Hello World"

	print("Serving HTTP on port 8000...")
	httpd = make_server('127.0.0.1',8000,application)
	httpd.serve_forever()

	命令行运行 python server.py来启动WSGI服务器：
	 启动成功后，验证：
		(1) 打开浏览器，输入 http:://127.0.0.1:8000/,就可以看到结果了。
		(2)在另一个终端中使用curl命令发送HTTP请求 curl 127.0.0.1:8000，可以看到服务器成功应答。

	无论多么复杂的HTTP程序，入口都是WSGI处理函数，HTTP请求的所有输入信息可以通过environ环境变量
	获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为HTTP响应的body。
	但是光靠一个WSGI函数来处理还是太底层，需要在WSGI之上抽象出Web框架，进一步简化Web开发。

"-----------------------------------------------------------------------------------"


	# coding:utf-8

	import socket
	import re
	import sys

	from multiprocessing import Process

	# 设置静态文件根目录
	HTML_ROOT_DIR = "./html"

	WSGI_PYTHON_DIR = "./wsgipython"


	class HTTPServer(object):
	    """"""
	    def __init__(self):
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	    def start(self):
		self.server_socket.listen(128)
		while True:
		    client_socket, client_address = self.server_socket.accept()
		    # print("[%s, %s]用户连接上了" % (client_address[0],client_address[1]))
		    print("[%s, %s]用户连接上了" % client_address)
		    handle_client_process = Process(target=self.handle_client, args=(client_socket,))
		    handle_client_process.start()
		    client_socket.close()

	    def start_response(self, status, headers):
		"""
		 status = "200 OK"
	    headers = [
		("Content-Type", "text/plain")
	    ]
	    star 
		"""
		response_headers = "HTTP/1.1 " + status + "\r\n"
		for header in headers:
		    response_headers += "%s: %s\r\n" % header

		self.response_headers = response_headers

	    def handle_client(self, client_socket):
		"""处理客户端请求"""
		# 获取客户端请求数据
		request_data = client_socket.recv(1024)
		print("request data:", request_data)
		request_lines = request_data.splitlines()
		for line in request_lines:
		    print(line)

		# 解析请求报文
		# 'GET / HTTP/1.1'
		request_start_line = request_lines[0]
		# 提取用户请求的文件名
		print("*" * 10)
		print(request_start_line.decode("utf-8"))
		file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
		method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)

		# "/ctime.py"
		# "/sayhello.py"
		if file_name.endswith(".py"):
		    try:
			m = __import__(file_name[1:-3])
		    except Exception:
			self.response_headers = "HTTP/1.1 404 Not Found\r\n"
			response_body = "not found"
		    else:
			env = {
			    "PATH_INFO": file_name,
			    "METHOD": method
			}
			response_body = m.application(env, self.start_response)

		    response = self.response_headers + "\r\n" + response_body
		else:
		    if "/" == file_name:
			file_name = "/index.html"

		    # 打开文件，读取内容
		    try:
			file = open(HTML_ROOT_DIR + file_name, "rb")
		    except IOError:
			response_start_line = "HTTP/1.1 404 Not Found\r\n"
			response_headers = "Server: My server\r\n"
			response_body = "The file is not found!"
		    else:
			file_data = file.read()
			file.close()

			# 构造响应数据
			response_start_line = "HTTP/1.1 200 OK\r\n"
			response_headers = "Server: My server\r\n"
			response_body = file_data.decode("utf-8")

		    response = response_start_line + response_headers + "\r\n" + response_body
		    print("response data:", response)

		# 向客户端返回响应数据
		client_socket.send(bytes(response, "utf-8"))

		# 关闭客户端连接
		client_socket.close()

	    def bind(self, port):
		self.server_socket.bind(("", port))


	def main():
	    sys.path.insert(1, WSGI_PYTHON_DIR)
	    http_server = HTTPServer()
	    # http_server.set_port
	    http_server.bind(8000)
	    http_server.start()


	if __name__ == "__main__":
	    main()



	


	# coding:utf-8

	import time


	def application(environ, start_response):
	    start_response("200 OK", [("Content-Type", "text/html")])
	    return time.ctime()





















	
		
	


	









"-----------------------------------------------------------------------------------------------"


Web应用框架：

	Web应用框架（Web application framework）是一种电脑软件框架，用来支持动态网站、网络应用程序
	以及网络服务的开发，这种框架有助于减轻网页开发时共同性活动的工作负荷，例如许多框架提供数据库
	访问接口，标准模块以及会话管理，可提升代码的可再用性。

	Python Web框架做的都是同样一件事情：接收HTTP请求，分配处理的方法，生成HTML作为HTTP响应，
	返回给客户端。实际上，几乎所有的web框架都是做了这些工作。

	python 框架:django、flash、Tornado、Zope、Pylons、TurboGears

	


	
