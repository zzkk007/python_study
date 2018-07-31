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


























