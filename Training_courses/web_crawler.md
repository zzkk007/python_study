"-----------------------------------------------"

				网络爬虫 web crawler

"-----------------------------------------------"

1、爬虫:

	根据使用的场景，网络爬虫可分为通用爬虫和聚焦爬虫两种

	通用爬虫：根据搜索引擎抓取系统(Baidu、Google、Yahoo等)
	的重用组成部分，主要目的是将互联网上的页面下载到本地
	形成一个互联网内容的镜像备份。

2、通用搜索引擎(Search Engine)工作原理：

	通用网络爬虫从互联网中搜集网页，采集信息，这些网页信息用于
	为搜索引擎建立索引而提供支持，它决定这整个引擎系统的内容
	是否丰富，信息是否及时，因此其性能的优劣直接影响着搜索的效果。

	
	第一步：抓取网页

		搜索引擎网络爬虫的基本工作流程如下：

		1. 首先选取一部分的种子URL，将这些URL放入待抓取URL队列；

		2. 取出待抓取URL，解析DNS得到主机的ip，并将URL对应的网页下载下来
			存储进已下载网页库中，并且将这些URL放进已抓取的URL队列。
		
		3. 分析已抓取的URL队列中的URL，分析其中的其他URL，并且将URL
			放入待抓取URL队列，从而进入下一个循环....

	第二步：数据存储

		搜索引擎通过爬虫取得的页面，将数据存入原始网页数据库，其中的页面数据
		和用户浏览器得到的HTML是完全一样的，

		搜索引擎蜘蛛在抓取页面时，也做一定的重复内容检测，一旦遇到访问权重
		很低的网站上有大量的抄袭，采集或者复制的内容，很可能就不用再爬行。

	第三步：预处理

		搜索引擎将爬虫抓取回来的页面，进行各种步骤的预处理

			1.提取文字

			2.中文分词

			3.消除噪音（比如版权声明，导航条，广告等）

			4.索引处理

			5.链接关系计算

			6.特殊文件处理

		除了HTML文件外，搜索引擎通常还能抓取和索引以文字为基础的多种文件类型，
		如 PDF、Word、WPS、XLS、PPT、TXT 文件等。我们在搜索结果中也经常会看到这些文件类型。

		但搜索引擎还不能处理图片、视频、Flash 这类非文字内容，也不能执行脚本和程序。

	第四步：提供搜索服务，网站排名

		搜索引擎在对信息进行组织和处理后，为用户提供关键字检索服务，将用户检索相关的信息展示给用户。

		同时会根据页面的PageRank值（链接的访问量排名）来进行网站排名，这样Rank值高的网站在
		搜索结果中会排名较前，当然也可以直接使用 Money 购买搜索引擎网站排名，简单粗暴。

	但是，这些通用性搜索引擎也存在着一定的局限性：

		1.通用搜索引擎所返回的结果都是网页，而大多情况下，网页里90%的内容对用户来说都是无用的。

		2.不同领域、不同背景的用户往往具有不同的检索目的和需求，搜索引擎无法提供针对具体某个用户的搜索结果。

		3.万维网数据形式的丰富和网络技术的不断发展，图片、数据库、音频、
			视频多媒体等不同数据大量出现，通用搜索引擎对这些文件无能为力，不能很好地发现和获取。
		
		4.通用搜索引擎大多提供基于关键字的检索，难以支持根据语义信息提出的查询，无法准确理解用户的具体需求。

3、聚焦爬虫：

	聚焦爬虫，是"面向特定主题需求"的一种网络爬虫程序，它与通用搜索引擎爬虫的区别在于： 
	聚焦爬虫在实施网页抓取时会对内容进行处理筛选，尽量保证只抓取与需求相关的网页信息。
	
	而我们今后学习的，就是聚焦爬虫。

'--------------------------------------------------------------------------------'

HTTP 和 HTTPS:

	HTTP协议：超文本传输协议
	HTTPS：在HTTP下加入SSL层
	SSL：主要用于Web的安全传输协议，在传输层对网络连接进行加密，保障在Internet上数据传输的安全。
	
	HTTP的端口号为80，HTTPS的端口号为443
		

	客户端HTTP请求:

		URL只是标识资源的位置，而HTTP是用来提交和获取资源。
		客户端发送一个HTTP请求到服务器的请求消息，包括以下格式：

		请求行、请求头部、空行、请求数据


	HTTP/1.1协议中共定义了八种方法（也叫“动作”）来以不同方式操作指定的资源：

		1.GET : 
		
			向指定的资源发出"显示"请求，使用GET方法应该只用在读取数据，而不应当被用于产生“副作用”的操作中。
			请求指定的页面信息，并返回实体主体。
			
		2.HEAD:
			
			与GET方法一样，都是向服务器发出指定资源的请求，只不过服务器将不传回资源的本文部分。
			它的好处在于，使用这个方法可以在不必传输全部内容的情况下，
			就可以获取其中“关于该资源的信息”（元信息或称元数据）。

			类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头

		3.POST:

			向指定资源提交数据，请求服务器进行处理(例如提交表单或者上传文件)。数据被包含在请求文本中
			这个请求可能或创建新的资源或修改现有资源，或二者皆有可能。

		4.PUT：

			向指定资源位置上传其最新内容
			从客户端向服务器传送的数据取代指定的文档的内容。

		5.DELETE：

			请求服务器删除Request-URI所标识的资源。
			请求服务器删除指定的页面。

		6.CONNECT：

			HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
			通常用于SSL加密服务器的链接（经由非加密的HTTP代理服务器）。

		7.TRACE:

			回显服务器收到的请求，主要用于测试或诊断。

		8.OPTIONS:

			这个方法可使服务器传回该资源所支持的所有HTTP请求方法。
			用'*'来代替资源名称，向Web服务器发送OPTIONS请求，可以测试服务器功能是否正常运作。
			允许客户端查看服务器的性能。


	HTTP请求主要分为GET 和 POST 两种方法

		GET 是从服务器上获取数据，POST是想服务器传送数据

		GET 请求参数显示，都显示在浏览器网址上，HTTP服务器根据该请求
		所包含的URL中的参数来产生响应内容，即get请求的参数是URL的一部分。

		POST 请求参数在请求体当中，消息长度没有限制而且以隐式的方式进行发送
		通常用来向HTTP服务器提交量比较大的数据，请求的参数包含在“Content-Type”消息头里，
		指明该消息体的媒体类型和编码。

		注意：避免使用Get方式提交表单，因为有可能会导致安全问题。 比如说在登陆表单中用Get方式，
		用户输入的用户名和密码将在地址栏中暴露无遗。
	
	常用的请求报头：

		1. Host：主机和端口

			Host：对应网址URL中的Web名称和端口号，用于指定请求资源的Inernet
			主机和端口号，通常属于URL的一部分。

		2. Connection: 链接类型
			
			Connection：表示客户端与服务连接类型

			a. Client 发起一个包含 Connection:keep-alive 的请求，HTTP/1.1使用keep-alive为默认值。

			b. Server收到请求后：

				如果server支持Keep-alive，回复一个包含Connection:keep-alive的响应，不关闭链接

				如果Server不支持keep-alive，回复一个包含Connection:close的响应，关闭连接

			c.如果clent收到包含Connection:keep-alive的响应，向同一个链接发送下一个请求，
			知道一方主动关闭链接。

			keep-alive在很多情况下能够重用链接，减少资源消耗，缩短响应时间，比如当浏览器
			需要多个文件时，不需要每次都去请求建立连接。

		3. Upgrade-insecure-Requests(升级HTTPs请求)

			Upgrade-Insecure-Requests：升级不安全的请求，意思是会在加载 http 资源时自动替换成 https 请求，
			让浏览器不再显示https页面中的http请求警报。

			HTTPS 是以安全为目标的http通道，所以在HTTPs承载的页面上不允许出现HTTP请求，一旦出现就
			会提示或报错。

		4. User-Agent: 浏览器名称

			User-Agent 是客户端浏览器的名称

		5. Accept : 传输文件类型

			指浏览器或其他客户端可以接受的MIME文件类型，服务器可以根据它判断并返回适当的文件格式。

			Accept: */*：表示什么都可以接收。

			Accept：image/gif：表明客户端希望接受GIF图像格式的资源；

			Accept：text/html：表明客户端希望接受html文本。

			Accept: text/html, application/xhtml+xml;q=0.9, image/*;q=0.8：表示浏览器支持的 MIME 
			类型分别是 html文本、xhtml和xml文档、所有的图像格式资源。

			q是权重系数，范围 0 =< q <= 1，q 值越大，请求越倾向于获得其“;”之前的类型表示的内容。
			若没有指定q值，则默认为1，按从左到右排序顺序；若被赋值为0，则用于表示浏览器不接受此内容类型。

			Text：用于标准化地表示的文本信息，文本消息可以是多种字符集和或者多种格式的；
			Application：用于传输应用程序数据或者二进制数据。

		6.Referer:页面跳转处

			Referer：表明产生请求的网页来自于那个URL,用户是从该 Referer页面访问到当前请求的页面。
			这个属性可以用来跟踪Web请求来自哪个页面，是从什么网站来的等。

			有时候遇到下载某网站图片，需要对应的referer，否则无法下载图片，那是因为人家做了防盗链，
			原理就是根据referer去判断是否是本网站的地址，如果不是，则拒绝，如果是，就可以下载；

		7.Accept-Encoding（文件编解码格式）

			Accept-Encoding：指出浏览器可以接受的编码方式.
			编码方式不同于文件格式，它是为了压缩文件并加速文件传递速度。
			浏览器在接收到Web响应之后先解码，然后再检查文件格式，许多情形下这可以减少大量的下载时间。

			举例：Accept-Encoding:gzip;q=1.0, identity; q=0.5, *;q=0
			如果有多个Encoding同时匹配, 按照q值顺序排列，本例中按顺序支持 gzip, identity压缩编码，
			支持gzip的浏览器会返回经过gzip编码的HTML页面。 
			如果请求消息中没有设置这个域服务器假定客户端对各种内容编码都可以接受。

		8.Accept-Language（语言种类）

			Accept-Langeuage：指出浏览器可以接受的语言种类，如en或en-us指英语，
			zh或者zh-cn指中文，当服务器能够提供一种以上的语言版本时要用到。

		9.Accept-Charset（字符编码）

			Accept-Charset：指出浏览器可以接受的字符编码。

			举例：Accept-Charset:iso-8859-1,gb2312,utf-8

			ISO8859-1：通常叫做Latin-1。Latin-1包括了书写所有西方欧洲语言不可缺少的附加字符，
			英文浏览器的默认值是ISO-8859-1.
			
			gb2312：标准简体中文字符集;
			utf-8：UNICODE 的一种变长字符编码，可以解决多种语言文本显示问题，从而实现应用国际化和本地化。
			如果在请求消息中没有设置这个域，缺省是任何字符集都可以接受。

		10.Cookie （Cookie）

			Cookie：浏览器用这个属性向服务器发送Cookie。Cookie是在浏览器中寄存的小型数据体，
			它可以记载和服务器相关的用户信息，也可以用来实现会话功能.

		11.Content-Type (POST数据类型)

			Content-Type：POST请求里用来表示的内容类型。

			举例：Content-Type = Text/XML; charset=gb2312：

			指明该请求的消息体中包含的是纯文本的XML类型的数据，字符编码采用“gb2312”。


	服务端HTTP响应:

		1. Cache-Control：must-revalidate, no-cache, private。

			这个值告诉客户端，服务端不希望客户端缓存资源，在下次请求资源时，
			必须要从新请求服务器，不能从缓存副本中获取资源。

			Cache-Control是响应头中很重要的信息，当客户端请求头中包含Cache-Control:max-age=0请求，
			明确表示不会缓存服务器资源时,Cache-Control作为作为回应信息，通常会返回no-cache，
			意思就是说，"那就不缓存呗"。
			
			当客户端在请求头中没有包含Cache-Control时，服务端往往会定,不同的资源不同的缓存策略，
			比如说oschina在缓存图片资源的策略就是Cache-Control：max-age=86400,
			这个意思是，从当前时间开始，在86400秒的时间内，
			客户端可以直接从缓存副本中读取资源，而不需要向服务器请求.


		2. Connection：keep-alive

			这个字段作为回应客户端的Connection：keep-alive，告诉客户端服务器的tcp连接也是一个长连接，
			客户端可以继续使用这个tcp连接发送http请求。

		3. Content-Encoding:gzip

			告诉客户端，服务端发送的资源是采用gzip编码的，客户端看到这个信息后，应该采用gzip对资源进行解码。


		4.Content-Type：text/html;charset=UTF-8

			告诉客户端，资源文件的类型，还有字符编码，客户端通过utf-8对资源进行解码，
			然后对资源进行html解析。通常我们会看到有些网站是乱码的，往往就是服务器端没有返回正确的编码。

		5.Date：Sun, 21 Sep 2016 06:18:21 GMT

			这个是服务端发送资源时的服务器时间，GMT是格林尼治所在地的标准时间。
			http协议中发送的时间都是GMT的，这主要是解决在互联网上，不同时区在相互请求资源的时候，时间混乱问题。

		6.Expires:Sun, 1 Jan 2000 01:00:00 GMT

			这个响应头也是跟缓存有关的，告诉客户端在这个时间前，可以直接访问缓存副本，
			很显然这个值会存在问题，因为客户端和服务器的时间不一定会都是相同的，
			如果时间不同就会导致问题。所以这个响应头是没有Cache-Control：max-age=*这个响应头准确的，
			因为max-age=date中的date是个相对时间，不仅更好理解，也更准确。

		7.Pragma:no-cache

			这个含义与Cache-Control等同。

		8.Server：Tengine/1.4.6

			这个是服务器和相对应的版本，只是告诉客户端服务器的信息。

		9.Transfer-Encoding：chunked

			这个响应头告诉客户端，服务器发送的资源的方式是分块发送的。
			一般分块发送的资源都是服务器动态生成的，在发送时还不知道发送资源的大小，所以采用分块发送，
			每一块都是独立的，独立的块都能标示自己的长度，最后一块是0长度的，
			当客户端读到这个0长度的块时，就可以确定资源已经传输完了。

		10.Vary: Accept-Encoding

			告诉缓存服务器，缓存压缩文件和非压缩文件两个版本，现在这个字段用处并不大，
			因为现在的浏览器都是支持压缩的。
	
	响应状态码:

		响应状态代码有三位数字组成，第一个数字定义了响应的类别，且有五种可能取值。

		常见状态码：

		100~199：表示服务器成功接收部分请求，要求客户端继续提交其余请求才能完成整个处理过程。

		200~299：表示服务器成功接收请求并已完成整个处理过程。常用200（OK 请求成功）。

		300~399：为完成请求，客户需进一步细化请求。例如：请求的资源已经移动一个新地址、
				常用302（所请求的页面已经临时转移至新的url）、307和304（使用缓存资源）。

		400~499：客户端的请求有错误，常用404（服务器无法找到被请求的页面）、403（服务器拒绝访问，权限不够）。
		
		500~599：服务器端出现错误，常用500（请求未完成。服务器遇到不可预知的情况）。

	Cookie 和 Session：

		服务器和客户端的交互仅限于请求/响应过程，结束之后便断开，在下一次请求时，服务器会认为新的客户端。

		为了维护他们之间的链接，让服务器知道这是前一个用户发送的请求，必须在一个地方保存客户端的信息。

		Cookie：通过在 客户端 记录的信息确定用户的身份。

		Session：通过在 服务器端 记录的信息确定用户的身份。

"---------------------------------------------------------------------------------------"

Python2 中的 urllib、URLlib2和 Python3中的urllib.request and urllib.error及第三方模块requests
	
	所谓的网页抓取，就是把URL地址中的指定的网络资源从网络流中读取出来，保存到本地。
	Python中有很多库可以用来抓取页面。

	urllib2 在 python3.x 中被改为urllib.request 和 urllib.error

	1、在python2中的，urllib和URLlib2都是接受URL请求的相关模块，两个模块主要区别如下：

		1. urllib2 可以接受一个Request对象，并以此来设置URL的headers。
			例如：
			
			req = urllib2.Request(url=url,data=postdata,headers=headers)
			result = urllib2.urlopen(req)
		
			我们知道，HTTP是无连接的状态协议，但是客户端和服务器端需要保持一些相互信息，
			比如cookie，有了cookie，服务器才能知道刚才是这个用户登录了网站，
			才会给予客户端访问一些页面的权限。所以我们需要保存cookie，之后附带cookie再来访问网站，
			才能够达到效果。这里就需要Python的cookielib和urllib2等的配合，将cookielib绑定到urllib2在一起，
			就能够在请求网页的时候附带cookie。在构造req请求之前可以获取一个保存cookies的对象，
			并把该对象和http处理器、http的handler资源以及urllib2的对象绑定在一起：
		
			cj = cookielib.LWPCookieJar()
			cookie_support = urllib2.HTTPCookieProcessor(cj)
			# 创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
			opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
			# 将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
			urllib2.install_opener(opener)
				
		2. urllib仅可以接受URL。这意味着，你不可以伪装你的User Agent字符串等。
			但是urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。
			这是就是为何urllib常和urllib2一起使用的原因，如下：
	
			postdata = urllib.urlencode(postdata)
			


	2、URLlib2概述：

		URLlib2模块定义的函数和类用来获取URL(主要是HTTP)，他提供了一下复杂的接口用于处理
		基本认证、重定向、Cookies等。

		常用的方法和类：

		1. urllib2.urlopen(url[,data[,timeout]])
			
			urlopen方法是URLlib2模块最常用也是最简单的方法，它打开URL网址，
			url参数可以是一个字符串url或者是一个Request对象。

			对于可选的参数timeout，阻塞操作以秒为单位，(如果没有指定，将使用全局默认timeout值)
			
			a、先看只包含URL的请求的例子：

				import URLlib2
				response = urllib2.urlopen('http://python.org/')
				html = response.read()

			b、urlopen方法也可以通过建立一个Request对象来明确想获取的URL。
				调用urlopen函数对请求的URL返回一个response对象，
				这个response类似一个file对象，所以用.read()函数可以操作
				这个response对象。

				import urllib2
				req = urllib2.Requset('http://python.org/')
				response = urllib2.urlopen(req)
				the_page = response.read()
				
				这里调用了urllib2.Request类，我们只是通过URL实例化了Request类的对象
				其实Request类还有其他的参数。

		2. class urllib2.Request(url[,data][,headers][,origin_req_host][,unverifiable])

			Request类的是一个抽象的URL请求，5个参数说明如下：

			URL -- 是一个字符串，其中包含一个有效的URL

			data -- 是一个字符串，指定额外的数据发送到服务器，如果没有data需要发送可以为"None"
				 目前使用data的HTTP请求是唯一的。当请求含有data参数时，HTTP的请求为POST，而不是GET。
				 数据应该是缓存在一个标准的application/x-www-form-urlencoded格式中。
				
				 urllib.urlencode()函数用映射或2个元组，返回一个这种格式的字符串。
				 通俗的说就是想向一个URL发送数据，对于HTTP来说这个动作叫Post。
				 例如在网上填写form表单时，浏览器会post表单内容，这些数据需要被
				 以标准的格式编码(encode)，然后作为一个数据参数传送给Request对象
				 Encoding是在urllib模块中完成的，而不是urllib2中完成的。

				 import urllib2
				 import urllib

				 url = 'http://www.someserver.com/cgi-bin/register.cgi'

				 values = {
					 'name':'Michael Foord'
					 'language':'Python'}

				data = urllib.urlencode(values)
				req = urllib2.Request(url,data)
				response = urllib2.urlopen(req)
				the_page = response.read()

			headers --	是字典类型，头字典可以作为参数在request时直接传入，也可以把每一个键和值
					作为参数调用add_header()方法来添加，作为辨别浏览器身份的User-Agent header是经常被用来
					恶搞和伪装的，因为一些http服务只允许某些请求来自常见的浏览器而不是脚本，
					下面的例子和上面的区别就是在请求时加了一个headers，模仿IE浏览器提交请求。

					import urllib
					import urllib2

					url = 'http://www.someserver.com/cgi-bin/register.cgi'
					user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
					values = {
						'name' : 'Michael Foord',
						'location' : 'Northampton',
						'language' : 'Python' }
					headers = {'User-Agent':user_agent}
					data = urllib.urlencode(values)
					req = urllib2.Request(url,data,headers)
					response = urllib2.urlopen(req)
					the_page = response.read()


					标准的headers组成是(Content-Length,Content-Type and Host)
					使用headers参数构造Request对象，如上例在生成Request对象时已经
					初始化header,而下例是Request对象调用add_header(key,val)方法附加header

					import urllib2
					req = urllib2.Request('http://www.example.com/')
					req.add_headers = [('User-agent','Mozilla/5.0')]
					r = urllib2.urlopen(req)

					
					OpenerDirector为每一个Request自动加上一个User-Agent header，
					所以第二种方法如下（urllib2.build_opener会返回一个OpenerDirector对象	
					
					import urllib2
					opener = urllib2.build_opener()
					opener.addheaders = [('User-agent', 'Mozilla/5.0')]
					opener.open('http://www.example.com/')


			最后两个参数仅仅是对正确的操作第三方HTTP cookies感兴趣，很少用到。

			origin_req_host -是RFC2965定义的源交互的request-host。
						默认的取值是cookielib.request_host(self)。
						这是由用户发起的原始请求的主机名或IP地址		

			unverifiable ——代表请求是否是无法验证的，它也是由RFC2965定义的。默认值为false。
						一个无法验证的请求是，其用户的URL没有足够的权限来被接受。
		

		3. urllib2.install_opener(opener)和urllib2.build_opener([handler, ...])

			install_opener和build_opener这两个方法通常都是在一起用,
			也有时候build_opener单独使用来得到OpenerDirector对象。

			install_opener实例化得到OpenerDirector对象用来赋予全局变量opener。
			如果想用这个opener来调用urlopen，那么就必须实例化得到OpenerDirector；
			这样就可以简单的调用OpenerDirector.open()来代替urlopen()。

			build_opener实例化也会得到OpenerDirector对象，
			其中参数handlers可以被BaseHandler或他的子类实例化。
			子类中可以通过以下实例化：ProxyHandler (如果检测代理设置用), 
			UnknownHandler, HTTPHandler, HTTPDefaultErrorHandler, 
			HTTPRedirectHandler, FTPHandler, FileHandler, HTTPErrorProcessor。

				import urllib2
				req = urllib2.Request('http://www.python.org/')
				opener=urllib2.build_opener()
				urllib2.install_opener(opener)
				f = opener.open(req)
				
			如上使用 urllib2.install_opener()设置 urllib2 的全局 opener。
			这样后面的使用会很方便，但不能做更细粒度的控制，比如想在程序中使用两个不同的 Proxy 设置等。
			比较好的做法是不使用 install_opener 去更改全局的设置，
			而只是直接调用 opener的open 方法代替全局的 urlopen 方法。

			
			说到这Opener和Handler之间的操作听起来有点晕。整理下思路就清楚了。当获取一个URL时，
			可以使用一个opener（一个urllib2.OpenerDirector实例对象，可以由build_opener实例化生成）。
			正常情况下程序一直通过urlopen使用默认的opener（也就是说当你使用urlopen方法时，
			是在隐式的使用默认的opener对象），但也可以创建自定义的openers
			（通过操作器handlers创建的opener实例）。所有的重活和麻烦都交给这些handlers来做。
			每一个handler知道如何以一种特定的协议（http，ftp等等）打开url，
			或者如何处理打开url发生的HTTP重定向，或者包含的HTTP cookie。

			创建openers时如果想要安装特别的handlers来实现获取url
			（如获取一个处理cookie的opener，或者一个不处理重定向的opener）的话，
			先实例一个OpenerDirector对象，然后多次调用.add_handler(some_handler_instance)来创建一个opener。
			或者，你可以用build_opener，这是一个很方便的创建opener对象的函数，
			它只有一个函数调用。build_opener默认会加入许多handlers，
			它提供了一个快速的方法添加更多东西和使默认的handler失效。

			install_opener如上所述也能用于创建一个opener对象，但是这个对象是（全局）默认的opener。
			这意味着调用urlopen将会用到你刚创建的opener。也就是说上面的代码可以等同于下面这段。
			这段代码最终还是使用的默认opener。一般情况下我们用build_opener为的是生成自定义opener，
			没有必要调用install_opener，除非是为了方便。

				import urllib2
				req = urllib2.Request('http://www.python.org/')
				opener=urllib2.build_opener()
				urllib2.install_opener(opener)
				f = urllib2.urlopen(req)
		
		4.异常处理

			当我们调用urllib2.urlopen的时候不会总是这么顺利，就像浏览器打开url时有时也会报错，
			所以就需要我们有应对异常的处理。
			说到异常，我们先来了解返回的response对象的几个常用的方法：


			a、geturl() — 返回检索的URL资源，这个是返回的真正url，通常是用来鉴定是否重定向的，
				如下面代码4行url如果等于“http://www.python.org/ ”说明没有被重定向。
			
			b、info() — 返回页面的原信息就像一个字段的对象， 
				如headers，它以mimetools.Message实例为格式(可以参考HTTP Headers说明)。

			c、getcode() — 返回响应的HTTP状态代码。

			
				import urllib2
				req = urllib2.Request('http://baidu.com/')
				response=urllib2.urlopen(req)
				url=response.geturl()
					'http://baidu.com/'
				info=response.info()
					<httplib.HTTPMessage instance at 0x7ff86210b2d8>
				code=response.getcode()
					200

			当不能处理一个response时，urlopen抛出一个URLError
			HTTPError是HTTP URL在特别的情况下被抛出的URLError的一个子类。
			下面就详细说说URLError和HTTPError。

			URLError——handlers当运行出现问题时（通常是因为没有网络连接也就是没有路由到指定的服务器，
					或在指定的服务器不存在），抛出这个异常.它是IOError的子类.这个抛出的异常
					包括一个reason属性,他包含一个错误编码和一个错误文字描述。
					如下面代码，request请求的是一个无法访问的地址，
					捕获到异常后我们打印reason对象可以看到错误编码和文字描述。


				import urllib2
				req = urllib2.Request('http://www.python11.org/')
				try:
				     response=urllib2.urlopen(req)
				except urllib2.URLError,e:
				     print e.reason
				     print e.reason[0]
				     print e.reason[1]

			HTTPError——HTTPError是URLError的子类。每个来自服务器HTTP的response都包含“status code”.
			有时status code不能处理这个request. 默认的处理程序将处理这些异常的responses。
			例如，urllib2发现response的URL与你请求的URL不同时也就是发生了重定向时，会自动处理。
			对于不能处理的请求, urlopen将抛出HTTPError异常. 典型的错误包含‘404’ (没有找到页面), 
			‘403’ (禁止请求),‘401’ (需要验证)等。它包含2个重要的属性reason和code。

		　　当一个错误被抛出的时候，服务器返回一个HTTP错误代码和一个错误页。
			你可以使用返回的HTTP错误示例。这意味着它不但具有code和reason属性，
			而且同时具有read，geturl，和info等方法，如下代码和运行结果。
			
				











	3、Python3x中的urllib包、http包以及其他比较好使的第三方包

		










































































