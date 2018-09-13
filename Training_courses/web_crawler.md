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

			编码工作使用urllib的urlencode()函数，帮我们将key:value这样的键值对
			转换成"key=value"这样的字符串，解码工作可以使用urllib的unquote()函数。
			（注意，不是urllib2.urlencode() 
				
				
				import urllib
				word = {"wd" : "传智播客"}
				#通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
				urllib.urlencode(word)  
					"wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2"
				#通过urllib.unquote()方法，把 URL编码字符串，转换回原先字符串。
				print urllib.unquote("wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2")
					wd=传智播客

			一般HTTP请求提交数据，需要编码成 URL编码格式，然后做为url的一部分，
			或者作为参数传到Request对象中。


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
					
					通过调用Request·add_header() 添加/修改一个特定的header

					request.add_headers('Connection',"keep-alive")
					req.add_headers = [('User-agent','Mozilla/5.0')]
					r = urllib2.urlopen(req)
					print r.code     #可以查看响应状态码
	

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
		

		3. Handler处理器和自定义Opener:

			opener是urllib2.OpenerDirector 的实例，我们之前一直使用的urlopen
			是一种特殊的opener(也就是模块帮我们构建好的)

			但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。
			所以要支持这些功能：

				a. 使用相关的 Handler处理器来创建特定功能的处理器对象

				b. urllib2.build_opener()方法使用这些处理器对象，
					创建自定义的opener对象。
				c. 使用自定义的opener对象，调用open()方法发送请求

			如果程序里所有的请求都使用自定义的opener，可以使用urllib2.install_opener() 
			将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，
			都将使用这个opener（根据自己的需求来选择）



			urllib2.install_opener(opener)和urllib2.build_opener([handler, ...])

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

			简单的自定义opener():

				import urllib2

				#构建一个HTTPHandler处理器对象，支持处理HTTP请求
				http_handler = urllib2.HTTPHandler()
				#构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
				# http_handler = urllib2.HTTPSHandler()

				#调用urllib2.build_opener()方法，创建支持处理HTTP请求的Opener对象
				opener = urllib2.build_opener(http_handler)

				# 构建 Request请求
				request = urllib2.Request("http://www.baidu.com/")

				# 调用自定义opener对象的open()方法，发送request请求
				response = opener.open(request)

				# 获取服务器响应内容
				print response.read()
				

			这种方式发送请求得到的结果，和使用urllib2.urlopen()发送HTTP/HTTPS请求得到的结果是一样的。

			如果在 HTTPHandler()增加 debuglevel=1参数，还会将 Debug Log 打开，这样程序在执行的时候，
			会把收包和发包的报头在屏幕上自动打印出来，方便调试，有时可以省去抓包的工作。

				# 仅需要修改的代码部分：

				# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求，同时开启Debug Log，debuglevel 值默认 0
				http_handler = urllib2.HTTPHandler(debuglevel=1)

				# 构建一个HTTPHSandler 处理器对象，支持处理HTTPS请求，同时开启Debug Log，debuglevel 值默认 0
				https_handler = urllib2.HTTPSHandler(debuglevel=1)


		4. ProxyHandler处理器（代理设置）
		
			urllib2中通过ProxyHandler来设置使用代理服务器，下面代码说明如何使用自定义opener来使用代理：

			import urllib2
			
			proxy_list = [
			    {"http" : "124.88.67.81:80"},
				{"http" : "124.88.67.81:80"},
				{"http" : "124.88.67.81:80"},
				{"http" : "124.88.67.81:80"},
				{"http" : "124.88.67.81:80"}]

			# 随机选择一个代理
			proxy = random.choice(proxy_list)


			#构建两个代理Handler，一个有代理ip,一个没有代理IP
			
			httpproxy_handler = urllib2.ProxyHandler(proxy)
			httpproxy_handler = urllib2.ProxyHandler({"http" : "124.88.67.81:80"})
			nullproxy_handler = urllib2.ProxyHandler({})

			proxySwitch = True #定义一个代理开关

			# 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
			# 根据代理开关是否打开，使用不同的代理模式
			if proxySwitch:  
			    opener = urllib2.build_opener(httpproxy_handler)
			else:
				opener = urllib2.build_opener(nullproxy_handler)

			request = urllib2.Request("http://www.baidu.com/")
	
			# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，
			#而urlopen()则不使用自定义代理。
			
			response = opener.open(request)
	
			# 2. 如果这么写，就是将opener应用到全局，之后所有的，
			#不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。

			# urllib2.install_opener(opener)
			# response = urlopen(request)
	
			print response.read()
			
		
		5. HTTPPasswordMgrWithDefaultRealm()

			HTTPPasswordMgrWithDefaultRealm()类将创建一个秘密管理对象，
			用来保存HTTP请求相关的用户名和密码，主要应用两个场景：

				a、验证代理授权的用户名和密码(ProxyBasicAuthHandler())
				b、验证Web客户端的用户名和密码(HTTPBasicAuthHandler())

			
			ProxyBasicAuthHandler(代理授权验证)
			
				如果我们使用之前的代码来使用私密代理，会报HTTP 407错误，
				表示代理没有通过身份认证：

				urllib2.HTTPError:HTTP Error 407: Proxy Authentication Required

				所以我们需要通过:

				HTTPPasswordMgrWithDefaultRealm()：来保存私密代理的用户密码
				ProxyBasicAuthHandler()：来处理代理的身份验证。

				import urllib2
				import urllib

				# 私密代理授权的账户
				user = "mr_mao_hacker"
				# 私密代理授权的密码
				passwd = "sffqry9r"
				# 私密代理 IP
				proxyserver = "61.158.163.130:16816"

				# 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
				passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

				# 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，
				# 后面三个参数分别是 代理服务器、用户名、密码
				passwdmgr.add_password(None, proxyserver, user, passwd)


				# 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，
				#	 参数是创建的密码管理对象
				#   注意，这里不再使用普通ProxyHandler类了
				proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)


				# 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，
				#参数包括构建的 proxy_handler 和 proxyauth_handler
				opener = urllib2.build_opener(proxyauth_handler)

				# 5. 构造Request 请求
				request = urllib2.Request("http://www.baidu.com/")
	
				# 6. 使用自定义opener发送请求
				response = opener.open(request)
	
				# 7. 打印响应内容
				print response.read()
			

			HTTPBasicAuthHandler处理器（Web客户端授权验证）
			
				有些Web服务器（包括HTTP/FTP等）访问时，需要进行用户身份验证，
				爬虫直接访问会报HTTP 401 错误，表示访问身份未经授权：
			
				urllib2.HTTPError: HTTP Error 401: Unauthorized
				如果我们有客户端的用户名和密码，我们可以通过下面的方法去访问爬取：

				import urllib
				import urllib2

				# 用户名
				user = "test"
				# 密码
				passwd = "123456"
				
				# Web服务器 IP
				webserver = "http://192.168.199.107"

				# 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
				passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

				# 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，
				#后面三个参数分别是 Web服务器、用户名、密码
				passwdmgr.add_password(None, webserver, user, passwd)

				# 3. 构建一个HTTP基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象
				httpauth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

				# 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，
				#参数包括构建的 proxy_handler
				opener = urllib2.build_opener(httpauth_handler)

				# 5. 可以选择通过install_opener()方法定义opener为全局opener
				urllib2.install_opener(opener)

				# 6. 构建 Request对象
				request = urllib2.Request("http://192.168.199.107")
	
				# 7. 定义opener为全局opener后，可直接使用urlopen()发送请求
				response = urllib2.urlopen(request)
	
				# 8. 打印响应内容
				print response.read()


		6. Cookie 

			Cookie 是指某些网站服务器为了辨别用户身份和进行Session跟踪，而存储在用户浏览器上的文本文件。
			Cookie 可以保持登录信息到用户下一次与服务器的会话。

			Cookie原理：
			
			HTTP是无状态的面向连接的协议，为了保持连接状态，引入了Cookie机制，
			Cookie是http消息头中的一种属性，包括：
			
				Cookie 名字(Name)
				Cookie 的值(Value)
				Cookie 的过期时间(Expires/Max-Age)
				Cookie 作用路径(Path)
				Cookie 所在域名(Domain)
				使用Cookie进行安全连接(Secure)
				前两个参数是Cookie应用的必要条件，另外，
				还包括Cookie大小(Size，不同浏览器对Cookie个数及大小限制是有差异的)。
				Cookie由变量名和值组成，根据 Netscape公司的规定，Cookie格式如下：
					Set-Cookie: NAME=VALUE；Expires=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE
			
			Cookie应用:

			Cookies在爬虫方面最典型的应用是判定注册用户是否已经登录网站，
			用户可能会得到提示，是否在下一次进入此网站时保留用户信息以便简化登录手续。

			# 获取一个有登录信息的Cookie模拟登陆
				
			# 1. 构建一个已经登录过的用户的headers信息

			headers = {

				"Host":"www.renren.com",
				"Connection":"keep-alive",
				"Upgrade-Insecure-Requests":"1",
				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
					(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
				"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
				"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
										
				# 便于终端阅读，表示不支持压缩文件
				# Accept-Encoding: gzip, deflate, sdch,
										
				# 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，
				#这个Cookie里记录了用户名，密码(通常经过RAS加密)
										    
				"Cookie": "anonymid=ixrna3fysufnwv; depovince=GW; _r01_=1; 
				JSESSIONID=abcmaDhEdqIlM7riy5iMv; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7C
				c13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484060607173; 
				jebecookies=26fb58d1-cbe7-4fc3-a4ad-592233d1b42e|||||;
				ick_login=1f2b895d-34c7-4a1d-afb7-d84666fad409; 
				_de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; 
				p=99e54330ba9f910b02e6b08058f780479; ap=327550029; 
				first_login_flag=1; ln_uact=mr_mao_hacker@163.com; 
				ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_
				9A3Z_e0c300019f6a195a.jpg; t=214ca9a28f70ca6aa0801404dda4f6789; 
				societyguester=214ca9a28f70ca6aa0801404dda4f6789; 
				id=327550029; xnsid=745033c5; ver=7.0; loginfrom=syshome"
			}

			# 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象
			
			urllib2.Request("http://www.renren.com/", headers = headers)

			# 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），
			#判断这是一个已经登录的用户，并返回相应的页面

			response = urllib2.urlopen(request)

			# 4. 打印响应内容
			print response.read()
				
			
		但是这样做太过复杂，我们先需要在浏览器登录账户，并且设置保存密码，
		并且通过抓包才能获取这个Cookie，那有么有更简单方便的方法呢？

		cookielib库 和 HTTPCookieProcessor处理器:

			在Python处理Cookie，一般是通过cookielib模块和urllib2模块的HTTPCookieProcessor处理器类一起使用。

			cookielib模块：主要作用是提供用于存储cookie的对象
			HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象。
		
		cookielib 库:

			该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

				CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
				整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

				FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，
				用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。
				filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，
				即只有在需要时才读取文件或在文件中存储数据。

				MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，
				创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

				LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，
				创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。


			其实大多数情况下，我们只用CookieJar()，如果需要和本地文件交互，
			就用 MozillaCookjar() 或 LWPCookieJar()我们来做几个案例：

			1）获取Cookie，并保存到CookieJar()对象中

				import urllib2
				import cookielib

				#构建一个CookieJar对象实例保持cookie
				cookiejar = cookielib.CookieJar()

				# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
				handler = urllib2.HTTPCookieProcessor(cookiejar)

				# 通过 build_opener() 来构建opener
				opener = urllib2.build_opener(handler)

				# 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
				opener.open("http://www.baidu.com")

				## 可以按标准格式将保存的Cookie打印出来
				cookieStr = ""
				for item in cookiejar:
				    cookieStr = cookieStr + item.name + "=" + item.value + ";"
					
				## 舍去最后一位的分号
				print cookieStr[:-1]
			
			我们使用以上方法将Cookie保存到cookiejar对象中，然后打印出了cookie中的值，
			也就是访问百度首页的Cookie值。


			2) 访问网站获得cookie，并把获得的cookie保存在cookie文件中

				import cookielib
				import urllib2
				
				保存cookie的本地磁盘文件名
				filename = 'cookie.txt'

				声明一个MozillaCookieJar(有save实现)对象实例来保存Cookie，之后写入文件
				cookiejar = cookielib.MozillaCookieJar(filename)
			
				使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
				handler = urllib2.HTTPCookieProcessor(cookiejar)
				
				通过build_opener()来构建opener
				opener = urllib2.build_opener(handler)

				response = opener.open("http://www.baidu.com")

				# 保存cookie到本地文件
				cookiejar.save()
				
			3) 从文件中获取cookies，做为请求的一部分去访问

				import cookielib
				import urllib2

				创建MozillaCookieJar(有load实现)实例对象
				cookiejar = cookielib.MozillaCookieJar()
				
				从文件中读取cookie内容到变量
				cookie.load('cookie.txt')

				使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
				handler = urllib2.HTTPCookieProcessor(cookiejar)

				opener = urllib2.build_opener(handler)
				
				response = opener.open("http://www.baidu.com")
			
			4) 利用cookielib和post登录人人网

				import urllib
				import urllib2
				import cookielib

				# 1. 构建一个CookieJar对象实例来保存cookie
				cookie = cookielib.CookieJar()

				# 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
				cookie_handler = urllib2.HTTPCookieProcessor(cookie)

				# 3. 通过 build_opener() 来构建opener
				opener = urllib2.build_opener(cookie_handler)

				# 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
				opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
						AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
	
				# 5. 需要登录的账户和密码
				data = {"email":"mr_mao_hacker@163.com", "password":"alaxxxxxime"}  
		
				# 6. 通过urlencode()转码
				postdata = urllib.urlencode(data)
	
				# 7. 构建Request请求对象，包含需要发送的用户名和密码
				request = urllib2.Request("http://www.renren.com/PLogin.do", data = postdata)
	
				# 8. 通过opener发送这个请求，并获取登录后的Cookie值，
				opener.open(request)                                              
	
				# 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
				response = opener.open("http://www.renren.com/410043129/profile")  
	
				# 10. 打印响应内容
				print response.read()

		
			模拟登录要注意几点：

				登录一般都会先有一个HTTP GET，用于拉取一些信息及获得Cookie，然后再HTTP POST登录。
				HTTP POST登录的链接有可能是动态的，从GET返回的信息中获取。
				password 有些是明文发送，有些是加密后发送。有些网站甚至采用动态加密的，
				同时包括了很多其他数据的加密信息，只能通过查看JS源码获得加密算法，再去破解加密，非常困难。
			
				大多数网站的登录整体流程是类似的，可能有些细节不一样，所以不能保证其他网站登录成功。
				这个测试案例中，为了想让大家快速理解知识点，
				我们使用的人人网登录接口是人人网改版前的隐藏接口(嘘....)，登录比较方便。

				当然，我们也可以直接发送账号密码到登录界面模拟登录，但是当网页采用JavaScript动态技术以后，
				想封锁基于 HttpClient 的模拟登录就太容易了，
				甚至可以根据你的鼠标活动的特征准确地判断出是不是真人在操作。

				所以，想做通用的模拟登录还得选别的技术，
				比如用内置浏览器引擎的爬虫(关键词：Selenium ，PhantomJS)，这个我们将在以后会学习到。


		7.异常处理

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


			URLError 产生的原因主要有：
				没有网络连接
				服务器连接失败
				找不到指定的服务器


			URLError——handlers当运行出现问题，抛出这个异常.它是IOError的子类.
				这个抛出的异常包括一个reason属性,他包含一个错误编码和一个错误文字描述。
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
			当一个错误被抛出的时候，服务器返回一个HTTP错误代码和一个错误页。
			你可以使用返回的HTTP错误示例。这意味着它不但具有code和reason属性，
			而且同时具有read，geturl，和info等方法，如下代码和运行结果。
			
				import urllib2
				req = urllib2.Request('http://www.python.org/fish.html')
				try:
				    response=urllib2.urlopen(req)
				except urllib2.HTTPError,e:
					print e.code
					print e.reason
					print e.geturl()
					print e.read()


			如果我们想同时处理HTTPError和URLError，因为HTTPError是URLError的子类，
			所以应该把捕获HTTPError放在URLError前面，如不然URLError也会捕获一个HTTPError错误，
			代码参考如下：

				import urllib2
				req = urllib2.Request('http://www.python.org/fish.html')
				try:
				    response=urllib2.urlopen(req)
				except urllib2.HTTPError,e:
					print 'The server couldn\'t fulfill the request.
					print 'Error code: ',e.code
					print 'Error reason: ',e.reason   
				except urllib2.URLError,e:
				    print 'We failed to reach a server.'
					print 'Reason: ', e.reason
				else:
					response.read()

			这样捕获两个异常看着不爽，而且HTTPError还是URLError的子类，我们可以把代码改进如下：

				import urllib2
				req = urllib2.Request('http://www.python.org/fish.html')
				try:
				    response=urllib2.urlopen(req)
				except urllib2.URLError as e:
					if hasattr(e, 'reason'):
						#HTTPError and URLError all have reason attribute.
						print 'We failed to reach a server.'
					    print 'Reason: ', e.reason
					elif hasattr(e, 'code'):
						#Only HTTPError has code attribute.
						print 'The server couldn\'t fulfill the request.
						print 'Error code: ', e.code
				else:
						# everything is fine
						response.read()
		
	
		8.获取AJAX加载的内容:
		
			AJAX 即"Asynchronous JavaScript and XML" 异步的JavaScript与XML技术，
			指的是一套综合了多项技术的浏览器端网页开发技术。Ajax的概念由杰西·詹姆士·贾瑞特所提出。

			传统的Web应用允许用户端填写表单（form），当提交表单时就向网页服务器发送一个请求。
			服务器接收并处理传来的表单，然后送回一个新的网页，但这个做法浪费了许多带宽，
			因为在前后两个页面中的大部分HTML码往往是相同的。由于每次应用的沟通都需要向服务器发送请求，
			应用的回应时间依赖于服务器的回应时间。这导致了用户界面的回应比本机应用慢得多。

			与此不同，AJAX应用可以仅向服务器发送并取回必须的数据，
			并在客户端采用JavaScript处理来自服务器的回应。
			因为在服务器和浏览器之间交换的数据大量减少，服务器回应更快了。
			同时，很多的处理工作可以在发出请求的客户端机器上完成，因此Web服务器的负荷也减少了。

			类似于DHTML或LAMP，AJAX不是指一种单一的技术，而是有机地利用了一系列相关的技术。
			虽然其名称包含XML，但实际上数据格式可以由JSON代替，进一步减少数据量，形成所谓的AJAJ。
			而客户端与服务器也并不需要异步。


			有些网页内容使用AJAX加载，只要记得，AJAX一般返回的是JSON,
			直接对AJAX地址进行post或get，就返回JSON数据了。

			"作为一名爬虫工程师，你最需要关注的，是数据的来源"

				import urllib
				import urllib2

				# demo1

				url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
		
				headers={"User-Agent": "Mozilla...."}
					
				# 变动的是这两个参数，从start开始往后显示limit个
				formdata = {
						    'start':'0',
							'limit':'10'}
				
				data = urllib.urlencode(formdata)
	
				request = urllib2.Request(url, data = data, headers = headers)
				response = urllib2.urlopen(request)
				print response.read()
	
	
				# demo2
	
				url = "https://movie.douban.com/j/chart/top_list?"
				headers={"User-Agent": "Mozilla...."}
		
				# 处理所有参数
				formdata = {
					'type':'11',
				    'interval_id':'100:90',
					'action':'',
					'start':'0',
					'limit':'10'}
				data = urllib.urlencode(formdata)
				request = urllib2.Request(url, data = data, headers = headers)
				response = urllib2.urlopen(request)
				print response.read()

		9.	为什么有时候POST也能在URL内看到数据？

			GET方式是直接以链接形式访问，链接中包含了所有的参数，
			服务器端用Request.QueryString获取变量的值。如果包含了密码的话是一种不安全的选择，
			不过你可以直观地看到自己提交了什么内容。

			POST则不会在网址上显示所有的参数，服务器端用Request.Form获取提交的数据，
			在Form提交的时候。但是HTML代码里如果不指定 method 属性，
			则默认为GET请求，Form中提交的数据将会附加在url之后，以?分开与url分开。

			表单数据可以作为 URL 字段（method="get"）或者 HTTP POST （method="post"）的方式来发送。
			比如在下面的HTML代码中，表单数据将因为 （method="get"） 而附加到 URL 上：

				<form action="form_action.asp" method="get">
					<p>First name: <input type="text" name="fname" /></p>
					<p>Last name: <input type="text" name="lname" /></p>
					<input type="submit" value="Submit" />
				</form>


		10. 处理HTTPS请求 SSL证书验证:

			现在随处可见 https 开头的网站，urllib2可以为 HTTPS 请求验证SSL证书，
			就像web浏览器一样，如果网站的SSL证书是经过CA认证的，
			则能够正常访问，如：https://www.baidu.com/等...

			如果SSL证书验证不通过，或者操作系统不信任服务器的安全证书，
			比如浏览器在访问12306网站如：https://www.12306.cn/mormhweb/的时候，
			会警告用户证书不受信任。（据说 12306 网站证书是自己做的，没有通过CA认证）

			urllib2在访问的时候则会报出SSLError：

				import urllib2
				url = "https://www.12306.cn/mormhweb/"
				headers = {
					"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
						AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}	
				request = urllib2.Request(url, headers = headers)
				response = urllib2.urlopen(request)
				print response.read()

			运行结果：

			urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed 

			如果以后遇到这种网站，我们需要单独处理SSL证书，让程序忽略SSL证书验证错误，
			即可正常访问。

				import urllib
				import urllib2
				# 1. 导入Python SSL处理模块
				import ssl

				# 2. 表示忽略未经核实的SSL证书认证
				context = ssl._create_unverified_context()

				url = "https://www.12306.cn/mormhweb/"
	
				headers = {
					"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
					(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
				request = urllib2.Request(url, headers = headers)
	
				# 3. 在urlopen()方法里 指明添加 context 参数
				response = urllib2.urlopen(request, context = context)
				print response.read()

			关于CA证书：
		
				CA(Certificate Authority)是数字证书认证中心的简称，是指发放、管理、
				废除数字证书的受信任的第三方机构，如北京数字认证股份有限公司、
				上海市数字证书认证中心有限公司等.

				CA的作用是检查证书持有者身份的合法性，并签发证书，以防证书被伪造或篡改，
				以及对证书和密钥进行管理。


	3、Python3x中的urllib包、http包以及其他比较好使的第三方包

		Python3 中使用urllib库,urllib是基于http的高层库，
			它有以下三个主要功能：

			(1) request 处理客户端的请求

			(2) response 处理服务端的响应

			(3) parse会解析url

		在Pytho2.x中使用urllib2对应Python3中:urllib.request、urllib.error。
		在Pytho2.x中使用urllib 对应python3中:urllib.request、urllib.error、urllib.parse。
		在Pytho2.x中使用urlparse对应的，在Python3使用import urllib.parse。
		在Pytho2.x中使用urlopen对应的，在Python3.x中会使用import urllib.request.urlopen。
		在Pytho2.x中使用urlencode对应的，在Python3.x中会使用import urllib.parse.urlencode。
		在Pytho2.x中使用urllib.quote对应的，在Python3.x中会使用import urllib.request.quote。
		在Pytho2.x中使用cookielib.CookieJar对应的，在Python3.x中会使用http.CookieJar。
		在Pytho2.x中使用Request对应的，在Python3.x中会使用urllib.request.Request。


		下面是使用Python3中urllib来获取资源的一些示例：

			1. 最简单
				
				import urllib.request
				response = urllib.request.urlopen('http://python.org/')
				html = response.read()

			2. 使用Request
				
				import urllib.request
				req = urllib.request.Request('http://python.org/')
				response = urllib.request.urlopen(req)
				the_page = response.read()

			3. 发送数据

				import urllib.parse
				import urllib.request

				url = ""
				
				values = {
					'act' : 'login',
					'login[email]':'',
					'login[passeord]':''
				}

				data = urllib.parse.urlencode(values)
				req = urllib.request.Request(url,data)
				req.add_header('Referer','http://www.python.org/')
				response = urllib.request.urlopen(req)
				the_page = response.read()
				print(the_page.decode('utf-8'))


			4. 发送数据和header

				import urllib.parse
				import urllib.request

				url1 = = ''
				user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
				values = {

					'act' : 'login',
					'login[email]' : '',
					'login[password]' : ''
					}
				headers = {'User-Agent' : user_agent }
				data = urllib.parse.urlencode(values)
				req = urllib.request.Request(url, data, headers)
				response = urllib.request.urlopen(req)
				the_page = response.read()
				print(the_page.decode('utf-8'))
				
			5. http 错误

				import urllib.request
				req = urllib.request.Request('')
				try:
					urllib.request.urlopen(req)
				except urllib.error.HTTPError as e:
					print(e.code)
					print(e.read).decode('utf8')

			6.异常处理1

				from urllib.request import Request, urlopen
				from urllib.error import URLError, HTTPError
				req = Request("http://www..net /")
				try:
					response = urlopen(req)
				except HTTPError as e:
					print('The server couldnt fulfill the request.')
					print('Error code:', e.code)
				except URLError as e:
					print('We failed to reach a server.')
					print('Reason: ', e.reason)
				else:
					print("good!")
					print(response.read().decode("utf8"))
			
			7.异常处理2

				from urllib.request import Request, urlopen
				from urllib.error import  URLError
				req = Request("http://www.Python.org/")
				try:
					response = urlopen(req)
				except URLError as e:
					if hasattr(e, 'reason'):
						print('We failed to reach a server.')
						print('Reason: ', e.reason)
					elif hasattr(e, 'code'):
						print('The server couldnt fulfill the request.')
						print('Error code: ', e.code)
				else:
				print("good!")
				print(response.read().decode("utf8"))

			8.使用代理

				import urllib.request
				proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
				opener = urllib.request.build_opener(proxy_support)  
				urllib.request.install_opener(opener)  
				a = urllib.request.urlopen("").read().decode("utf8")

	4、第三方模块Requests:让HTTP 服务人类
	
		虽然Python的标准库中 urllib2 模块已经包含了平常我们使用的大多数功能，
		但是它的 API 使用起来让人感觉不太好，而 Requests 自称 “HTTP for Humans”，说明使用更简洁方便。

		Requests 继承了urllib2的所有特性。Requests 完全满足如今网络的需求，其功能有以下：
			国际化域名和 URLs
			Keep-Alive & 连接池
			持久的 Cookie 会话
			类浏览器式的 SSL 加密认证
			基本/摘要式的身份认证
			优雅的键/值 Cookies
			自动解压
			Unicode 编码的响应体
			多段文件上传
			连接超时
			支持 .netrc
			适用于 Python 2.7—3.6
			线程安全
	
		(1) 安装方式:

			pip install requests

			easy_install requests

		(2)发送请求:
			
			使用Requests发送网络请求非常简单。
			一开始导入模块Requests模块，然后，尝试获取某个网页，得到一名为"r"的Response对象
			我们可以从这个对象中获取我们想要的信息。

			
			Requsts简单的API意味着所有的HTTP 请求类型都是显而易见的：

			import requests
			r = requests.get('http://api.gethub.com.events')
			r = requests.head('http://httpbin.org/get')
			
			r = requests.post('http://httpbin.org/post', data = {'key':'value'})
			r = requests.put('http://httpbin.org/put', data = {'key':'value'})

			r = requests.delete('http://httpbin.org/delete')
			r = requests.options('http://httpbin.org/get')

		(3) 传递URL参数:

			为URL 的查询字符串(query string)传递某种数据。如果你是手工构建 URL，
			那么数据会以键/值对的形式置于 URL 中，跟在一个问号的后面。
			例如， httpbin.org/get?key=val。 Requests 允许你使用 params 关键字参数，
			以一个字符串字典来提供这些参数。

			举例来说，如果你想传递 key1=value1 和 key2=value2 到 httpbin.org/get ，
			那么你可以使用如下代码：
			>>> payload = {'key1': 'value1', 'key2': 'value2'}
			>>> r = requests.get("http://httpbin.org/get", params=payload)
			

			通过打印输出该 URL，你能看到 URL 已被正确编码：
			>>> print(r.url)
			http://httpbin.org/get?key2=value2&key1=value1

			
			注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。
			你还可以将一个列表作为值传入：
			>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
				
			>>> r = requests.get('http://httpbin.org/get', params=payload)
			>>> print(r.url)
				http://httpbin.org/get?key1=value1&key2=value2&key2=value3
			
		(4) 响应参数：

			我们能读取服务器响应的内容。

			>>> import requests
			>>> r = requests.get('https://api.github.com/events')
			
			# 查看完整url地址
			>>> r.url
				https://api.github.com/events


			文本响应内容：
			
				>>> r.text
					u'[{"repository":{"open_issues":0,"url":"https://github.com/...'
					使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，
					大多数 Unicode 字符集都能被无缝地解码。

				并且能够使用 r.encoding编码格式：
				>>> r.encoding
					'utf-8'
				>>> r.encoding = 'ISO-8859-1'
				如果你改变了编码，每当你访问 r.text ，Request 都将会使用 r.encoding 的新值。

		
			二进制响应内容:
				
				你也能以字节的方式访问请求响应体，对于非文本请求
				>>> r.content
					b'[{"repository":{"open_issues":0,"url":"https://github.com/...'
				Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据。

				以请求返回的二进制数据创建一张图片，你可以使用如下代码：
				>>> from PIL import Image
				>>> from io import BytesIO
				>>> i = Image.open(BytesIO(r.content))

			JSON 响应内容：

				Requests 中也有一个内置的 JSON 解码器，助你处理 JSON 数据：
				>>> import requests

				>>> r = requests.get('https://api.github.com/events')
				>>> r.json()
					[{
						u'repository': {
							u'open_issues': 0, u'url': 'https://github.com/...'}
					}]

					如果 JSON 解码失败， r.json() 就会抛出一个异常。
					例如，响应内容是 401 (Unauthorized)，尝试访问r.json()将会抛出 
					ValueError: No JSON object could be decoded 异常。





























































































