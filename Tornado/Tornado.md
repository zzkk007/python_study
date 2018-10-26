"==================================================="

					Tornado 

"==================================================="


"---------------------------------------------------"

			1. 关于Tornado


1.1 Tornado 是为何物:

	Tornado 全称Tornado Web Server，是一个用Python语言写成的Web服务器兼Web应用框架，
	由FriendFeed公司在自己的网站FriendFeed中使用，
	被Facebook收购以后框架在2009年9月以开源软件形式开放给大众。

	特点:

		作为Web框架，是一个轻量级的Web框架，类似于另一个Python web框架Web.py，其拥有异步非阻塞IO的处理方式。

		作为Web服务器，Tornado有较为出色的抗负载能力，官方用nginx反向代理的方式部署Tornado和
		其它Python web应用框架进行对比，结果最大浏览量超过第二名近40%。


	性能：Tornado 有着优异的性能，它试图解决C10k问题，即处理大于或等于一万的并发，
	
	Tornado框架和服务器一起组成一个WSGI的全栈替代品。单独在WSGI容器中
	使用tornado网络框架或者tornaod http服务器，有一定的局限性，为了最大化的利用tornado的性能，
	推荐同时使用tornaod的网络框架和HTTP服务器


1.2 Tornado与Django:

	Django:

		Django是走大而全的方向，注重的是高效开发，它最出名的是其全自动化的管理后台：
		只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台

		Django提供的方便，也意味着Django内置的ORM跟框架内的其他模块耦合程度高，
		应用程序必须使用Django内置的ORM，否则就不能享受到框架内提供的种种基于其ORM的便利。

		session功能
		后台管理
		ORM


	Tornado:

		Tornado走的是少而精的方向，注重的是性能优越，它最出名的是异步非阻塞的设计方式。

		HTTP服务器
		异步编程
		WebSockets

"---------------------------------------------------"

			2. 初识Tornado


知识点：

	Tornado的安装
	了解Tornado的原理
	掌握Tornado的基本写法
	掌握Tornado的基本模块
		tornado.web
		tornado.ioloop
		tornado.httpserver
		tornado.options

2.1 安装：

	1、$ pip install tornado

	2、下载安装包tornado-4.3.tar.gz（https://pypi.python.org/packages/source/t/tornado/tornado-4.3.tar.gz）
		$ tar xvzf tornado-4.3.tar.gz
		$ cd tornado-4.3
		$ python setup.py build
		$ sudo python setup.py install

	3、关于使用平台的说明

		Tornado应该运行在类Unix平台，在线上部署时为了最佳的性能和扩展性，
		仅推荐Linux和BSD（因为充分利用Linux的epoll工具和BSD的kqueue工具，
		是Tornado不依靠多进程/多线程而达到高性能的原因）。

		对于Mac OS X，虽然也是衍生自BSD并且支持kqueue，但是其网络性能通常不太给力，因此仅推荐用于开发。

		对于Windows，Tornado官方没有提供配置支持，但是也可以运行起来，不过仅推荐在开发中使用。


2.2 Hello World：


	1、上代码：新建文件hello.py 代码如下

	# coding:utf-8

	import tornado.web
	import tornado.ioloop

	class IndexHandler(tornado.web.RequestHandler):
		"""主路由处理类"""
		def get(self):
			"""对应http的get请求方式"""
			self.write("Hello World!")
											
	if __name__ == "__main__":
		app = tornado.web.Application([(r"/", IndexHandler),])
		app.listen(8000)
		tornado.ioloop.IOLoop.current().start()

	执行如下命令，开启tornado:

		$ python hello.py

	打开浏览器，输入网址127.0.0.1:8000（或localhost:8000），查看效果： 


	2、代码讲解：

	1. tornado.web  tornado的基础web框架模块

		RequestHandler:

			封装了对应一个请求的所有信息和方法，write(响应信息)就是写响应信息的一个方法；
			对应每一种http请求方式（get、post等），把对应的处理逻辑写进同名的成员方法中
			（如对应get请求方式，就将对应的处理逻辑写在get()方法中），
			当没有对应请求方式的成员方法时，会返回“405: Method Not Allowed”错误。

		Application:

			Tornado Web框架的核心应用类，是服务器对接的接口，里面保存了路由信息表，
			其初始化接收的第一个参数就是一个路由信息映射元组的列表；
			其listen(端口)方法用来创建一个http服务器实例，并绑定到给定端口（注意：此时服务器并未开启监听）。

	2. tornado.ioloop:

		tornado的核心io循环模块，封装了Linux的epoll和BSD的kqueue,tornado高性能的基石。
		以linux的epoll为例，其原理如下：

			Handlers <----> tornado.web.Application  <----> Tornado-IOLoop(Linux-epoll)

	3. IOLoop.current()

		返回当前线程的IOLoop实例。

	4. IOLoop.start()

		启动IOLoop实例的I/O循环，同时服务器监听被打开。


	总结Tornado Web程序编写思路:

	1、创建web应用实例对象，第一个初始化参数为路由映射列表。

	2、定义实现路由映射列表中的handler类。

	3、创建服务器实例，绑定服务器端口。

	4、启动当前线程的IOLoop。



2.3	httpserver

	上一节我们说在tornado.web.Application.listen()（示例代码中的app.listen(8000)）的方法中，
	创建了一个http服务器示例并绑定到给定端口，我们能不能自己动手来实现这一部分功能呢？

	现在我们修改上一示例代码如下：

		#coding:utf-8
		import tornado.web
		import tornado.ioloop
		import tornado.httpserver   #新引入httpserver模块

		class IndexHandler(tornado.web.RequestHandler):
			def get(self):
				self.write("Hello World")

		if __name__ == '__main__':
			app = tornado.web.Application([(r"/",IndexHandler)])

			#-------------------------------
			# 我们修改这个部分
			# app.listen(8000)
			
			http_server = tornado.httpserver.HTTPServer(app)
			http_server.listen(8000)
			
			#-------------------------------

			tornado.ioloop.IOLOOP.current().start()


		在这一修改版本中，我们引入了tornado.httpserver模块，顾名思义，它就是tornado的HTTP服务器实现。

		我们创建了一个HTTP服务器实例http_server，因为服务器要服务于我们刚刚建立的web应用，
		将接收到的客户端请求通过web应用中的路由映射表引导到对应的handler中，
		所以在构建http_server对象的时候需要传出web应用对象app。
		http_server.listen(8000)将服务器绑定到8000端口。

		实际上一版代码中app.listen(8000)正是对这一过程的简写。
	


	单进程与多进程:

		我们刚刚实现的都是单进程，可以通过命令来查看：		
		$ ps -ef | grep hello.py

		我们也可以一次启动多个进程，修改上面的代码如下：

			#coding:utf-8

			import tornado.web
			import tornado.ioloop
			import tornado.httpserver

			class IndexHandler(tornado.web.RequestHandler):
				def get(self):
					self.write("Hello World")

			if __name__ == "__main__":

				app = tornado.web.Application([(r"/",IndexHandler),])
				http_server = tornado.httpserver.HTTPServer(app)

				#-------------修改-------------
				http_server.bind(8000)
				http_server.start(0)
				#-----------------------------
				tornado.ioloop.IOLoop.current().start()


		http_server.bind(port)方法是将服务器绑定到指定端口。

		http_server.start(num_processes=1)方法指定开启几个进程，参数num_processes默认值为1，即默认仅开启一个进程；
		如果num_processes为None或者<=0，则自动根据机器硬件的cpu核芯数创建同等数目的子进程；
		如果num_processes>0，则创建num_processes个子进程。


		我们在前面写的http_server.listen(8000)实际上就等同于：
			http_server.bind(8000)
			http_server.start(1)

	说明:

		1. 关于app.listen()
		
			app.listen()这个方法只能在单进程模式中使用。

			对于app.listen()与手动创建HTTPServer实例

				http_server = tornado.httpserver.HTTPServer(app) 
				http_server.listen(8000)

			这两种方式，建议大家先使用后者即创建HTTPServer实例的方式，
			因为其对于理解tornado web应用工作流程的完整性有帮助，
			便于大家记忆tornado开发的模块组成和程序结构；在熟练使用后，可以改为简写。


		2. 关于多进程:

			虽然tornado给我们提供了一次开启多个进程的方法，但是由于：

			每个子进程都会从父进程中复制一份IOLoop实例，如过在创建子进程前我们的代码动了IOLoop实例，
			那么会影响到每一个子进程，势必会干扰到子进程IOLoop的工作；
			
			所有进程是由一个命令一次开启的，也就无法做到在不停服务的情况下更新代码；
			
			所有进程共享同一个端口，想要分别单独监控每一个进程就很困难。
			
			不建议使用这种多进程的方式，而是手动开启多个进程，并且绑定不同的端口。


2.4  options:

	在前面的示例中我们都是将服务端口的参数写死在程序中，很不灵活。

	tornado为我们提供了一个便捷的工具，tornado.options模块——全局参数定义、存储、转换。


	tornado.options.define():

		用来定义options选项变量的方法，定义的变量可以在全局的tornado.options.options中获取使用，
		传入参数：

			name 选项变量名，须保证全局唯一性，否则会报“Option 'xxx' already defined in ...”的错误；

			default　选项变量的默认值，如不传默认为None；

			type 选项变量的类型，从命令行或配置文件导入参数的时候tornado会根据这个类型转换输入的值，
			转换不成功时会报错，可以是str、float、int、datetime、timedelta中的某个，
			若未设置则根据default的值自动推断，若default也未设置，那么不再进行转换。
			可以通过利用设置type类型字段来过滤不正确的输入。

			multiple 选项变量的值是否可以为多个，布尔类型，默认值为False，如果multiple为True，
			那么设置选项变量时值与值之间用英文逗号分隔，而选项变量则是一个list列表
			（若默认值和输入均未设置，则为空列表[]）。

			help 选项变量的帮助提示信息，在命令行启动tornado时，通过加入命令行参数 --help　
			可以查看所有选项变量的信息（注意，代码中需要加入tornado.options.parse_command_line()）。


	tornado.options.options:

		全局的options对象，所有定义的选项变量都会作为该对象的属性。

	tornado.options.parse_command_line():

		转换命令行参数，并将转换后的值对应的设置到全局options对象相关属性上。
		追加命令行参数的方式是--myoption=myvalue

		新建opt.py，我们用代码来看一下如何使用：

			#coding:utf-8
			import tornado.web
			import tornado.ioloop
			import tornado.httpserver
			import tornado.options		#新导入的options模块

			# 定义服务器监听端口选项
			tornado.options.define("port",default=8000,type=int,help="run server on the port.") 
			
			# 无意义，演示多值情况
			tornado.options.define("itcast", default=[], type=str, multiple=True, help="itcast subjects.") 

			class IndexHandler(tornado.web.RequestHandler):
				"""主路由处理类"""
				def get(self):
					"""对应http的get请求方式"""
					self.write("Hello Itcast!")

			if __name__ == "__main__":
				tornado.options.parse_command_line()
				print tornado.optons.itcast  #输出多值项
				app = tornado.web.Application([(r"/",IndexHandler,)])
				http_server = tornado.httpserver.HTTPServer(app)
				http_server.listen(tornado.options.options.port)
				tornado.ioloop.IOLoop.current().start()
		
		执行如下命令开启程序：

			$ python opt.py --port=9000 --itcast=python,c++,java,php,ios

	
	
	tornado.options.parse_config_file(path):

		从配置文件导入option，配置文件中的选项格式如下：

			myoption = "myvalue"
			myotheroption = "myothervalue"

		我们用代码来看一下如何使用，新建配置文件config，注意字符串和列表按照python的语法格式：

			port = 8000
			itcast = ["python","c++","java","php","ios"]

		修改opt.py文件：

			# coding:utf-8

			import tornado.web
			import tornado.ioloop
			import tornado.httpserver
			import tornado.options # 新导入的options模块
			

			tornado.options.define("port", default=8000, type=int, help="run server on the given port.")
			tornado.options.define("itcast", default=[], type=str, multiple=True, help="itcast subjects.")

			class IndexHandler(tornado.web.RequestHandler):
				"""主路由处理类"""
				def get(self):
					"""对应http的get请求方式"""
					self.write("Hello world!")

			if __name__ == "__main__":
				tornado.options.parse_config_file("./config") # 仅仅修改了此处
				print tornado.options.options.itcast # 输出多值选项
				
				app = tornado.web.Application([(r"/", IndexHandler),])
				http_server = tornado.httpserver.HTTPServer(app)
				http_server.listen(tornado.options.options.port)
				tornado.ioloop.IOLoop.current().start()

	说明:

		1. 日志：

			当我们在代码中调用parse_command_line()或者parse_config_file()的方法时，
			tornado会默认为我们配置标准logging模块，即默认开启了日志功能，并向标准输出（屏幕）打印日志信息。
			
			如果想关闭tornado默认的日志功能，可以在命令行中添加--logging=none 或者在代码中执行如下操作:

				from tornado.options import options, parse_command_line
				options.logging = None
				parse_command_line()

		2. 配置文件：

			我们看到在使用prase_config_file()的时候，配置文件的书写格式仍需要按照python的语法要求，
			其优势是可以直接将配置文件的参数转换设置到全局对象tornado.options.options中；
			然而，其不方便的地方在于需要在代码中调用tornado.options.define()来定义选项，
			而且不支持字典类型，故而在实际应用中大都不使用这种方法。

			在使用配置文件的时候，通常会新建一个python文件（如config.py），
			然后在里面直接定义python类型的变量（可以是字典类型）；
			在需要配置文件参数的地方，将config.py作为模块导入，并使用其中的变量参数。


			如config.py文件：
				
			# conding:utf-8

			# Redis配置
			redis_options = {

					'redis_host':'127.0.0.1',
					'redis_port':6379,
					'redis_pass':'',}

			# Tornado app配置
			settings = {

				'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
				'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
				'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
				'xsrf_cookies':False,
				'login_url':'/login',
				'debug':True,
				}

			# 日志
			log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
					
			使用config.py的模块中导入config，如下：

			# conding:utf-8

			import tornado.web
			import config

			if __name__ = "__main__":
			    app = tornado.web.Application([], **config.settings)
			...
		
			




"---------------------------------------------------"



"-----------------------------------------------------"

			3. 深入Tornado

"----------------------------------------------------"



"-----------------------------------------------------"


			4. 模板

"-----------------------------------------------------"


"-----------------------------------------------------"

	
			5. 数据库

"-----------------------------------------------------"


"-----------------------------------------------------"

			6.安全应用

"-----------------------------------------------------"


"-----------------------------------------------------"


			7. 异步与WebSocket

"-----------------------------------------------------"




"-----------------------------------------------------"


			8. 部署

"-----------------------------------------------------"


