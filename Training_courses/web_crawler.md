"=========================================================="

				网络爬虫 web crawler

"==========================================================="

"----------------------------------------------------------"

			第一章 爬虫原理和数据抓取

"----------------------------------------------------------"

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
		

			子类中可以通过以下实例化：
			
				HTTPHandler			  : HTTP
				HTTPSHandler		  : HTTPS
				HTTPBasicAuthHandler  : Web客户端授权验证
				ProxyHandler          : 代理设置
				ProxyBasciAuthHandler : 验证代理设置
				HTTPCookieProcessor   : 主要作用是处理这些cookie对象，并构建handler对象.
				UnknownHandler
				HTTPDefaultErrorHandler
				HTTPRedirectHandler
				FTPHandler
				FileHandler
				HTTPErrorProcessor

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
					
					需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。
					有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。
					这种 JSON 会被解码返回。要检查请求是否成功，
					请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。

			原始响应内容:

				在罕见的情况下，你可能想获取来自服务器的原始套接字响应，那么你可以访问 r.raw。
				如果你确实想这么干，那请你确保在初始请求中设置了 stream=True。
				具体你可以这么做：

				>>> r = requests.get('https://api.github.com/events', stream=True)
				>>> r.raw
				<requests.packages.urllib3.response.HTTPResponse object at 0x101194810>
				>>> r.raw.read(10)
					'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
			
			响应状态码:

				我们可以检测响应状态码：
				>>> r = requests.get('http://httpbin.org/get')
				>>> r.status_code
					200
				为方便引用，Requests还附带了一个内置的状态码查询对象：
				>>> r.status_code == requests.codes.ok
				True

				如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，
				我们可以通过 Response.raise_for_status() 
				来抛出异常：
				
				d_r = requests.get('http://httpbin.org/status/404')
				>>> bad_r.status_code
					404
				
				>>> bad_r.raise_for_status()
				Traceback (most recent call last):
					  File "requests/models.py", line 832, in raise_for_status
					      raise http_error
					  requests.exceptions.HTTPError: 404 Client Error

			响应头:

				我们可以查看以一个 Python 字典形式展示的服务器响应头：

				>>> r.headers
				{

					'content-encoding': 'gzip',
					'transfer-encoding': 'chunked',
					'connection': 'close',
					'server': 'nginx/1.0.4',
					'x-runtime': '148ms',
					'etag': '"e1ca502697e5c9317743dc078f67693f"',
					'content-type': 'application/json'
				}

				但是这个字典比较特殊：它是仅为 HTTP 头部而生的。
				根据 RFC 2616， HTTP 头部是大小写不敏感的。

				因此，我们可以使用任意大写形式来访问这些响应头字段：

				>>> r.headers['Content-Type']
				'application/json'
				
				>>> r.headers.get('content-type')
				'application/json'
						
		
		(5) 定制请求头:

			如果你想为请求添加HTTP头部，只要简单地传递一个dict给 headers参数就可以了。	

			在前一个示例中我们没有指定 content-type:

			>>> url = 'https://api.github.com/some/endpoint'
			>>> headers = {'user-agent': 'my-app/0.0.1'}
			>>> r = requests.get(url, headers=headers)

			注意: 定制 header 的优先级低于某些特定的信息源，例如：

				如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。
				而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
				如果被重定向到别的主机，授权 header 就会被删除。
				代理授权 header 会被 URL 中提供的代理身份覆盖掉。
				在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
		
			更进一步讲，Requests 不会基于定制 header 的具体情况改变自己的行为。
			只不过在最后的请求中，所有的 header 信息都会被传递进去。

			注意: 所有的 header 值必须是 string、bytestring 或者 unicode。
			尽管传递 unicode header 也是允许的，但不建议这样做。

		
		(6)更加复杂的 POST 请求:

			通常，你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单。
			要实现这个，只需简单地传递一个字典给 data 参数。
			你的数据字典在发出请求时会自动编码为表单形式：

			>>> payload = {'key1': 'value1', 'key2': 'value2'}
			
			>>> r = requests.post("http://httpbin.org/post", data=payload)
			>>> print(r.text)



			import requests
			formdata = {

					"type":"AUTO",
					"i":"i love python",
					"doctype":"json",
					"xmlVersion":"1.8",
					"keyfrom":"fanyi.web",
					"ue":"UTF-8",
					"action":"FY_BY_ENTER",
					"typoResult":"true"
				}

			url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule
					&smartresult=ugc&sessionFrom=null"

			headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) 
				AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

			response = requests.post(url, data = formdata, headers = headers)

			print response.text

			很多时候你想要发送的数据并非编码为表单形式的。
			如果你传递一个 string 而不是一个 dict，那么数据会被直接发布出去。

			>>> import json
			>>> url = 'https://api.github.com/some/endpoint'
			>>> payload = {'some': 'data'}
			>>> r = requests.post(url, data=json.dumps(payload))
			
			此处除了可以自行对 dict 进行编码，你还可以使用 json 参数直接传递，
			然后它就会被自动编码。这是 2.4.2 版的新加功能：

			>>> url = 'https://api.github.com/some/endpoint'
			>>> payload = {'some': 'data'}
			>>> r = requests.post(url, json=payload)

		
		(7) POST一个多部分编码(Multipart-Encoded)的文件

			Requests 使得上传多部分编码文件变得很简单：

			>>> url = 'http://httpbin.org/post'
			>>> files = {'file': open('report.xls', 'rb')}
			>>> r = requests.post(url, files=files)
			>>> r.text

			你可以显式地设置文件名，文件类型和请求头:

			>>> url = 'http://httpbin.org/post'
			>>> files = {
				'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {
						'Expires': '0'})}
			
			>>> r = requests.post(url, files=files)
			>>> r.text

		(8) 代理（proxies参数）:

			如果需要使用代理，你可以通过为任意请求方法提供proxies参数来配置单个请求:

			import requests

			根据协议类型，选择不同的代理
			proxies = {
				"http":"http://10.10.1.10:3128"
				"https": "http://10.10.1.10:1080",
			}
			response = requests.get("http://www.baidu.com",proxies = proxies)
			
			也可以通过本地环境变量HTTP_PROXy 和HTTPS_PROXY 来代理配置

				>>> export HTTP_PROXY="http://12.34.56.79:9527"
				>>> export HTTPS_PROXY="https://12.34.56.79:9527"

				>>> import requests
				>>> requests.get("http://www.baidu.com")

		(9) 私密代理验证（特定格式） 和 Web客户端验证（auth 参数）:
			
			私密代理:
				若你的代理需要使用HTTP Basic Auth，可以使用 http://user:password@host/语法：
	
				import requests
				proxies = {

					    "http": "http://user:pass@10.10.1.10:3128/",
				}

				response = requests.get("http://www.baidu.com", proxies = proxy)	
				print response.text

			web客户端验证:

				如果是Web客户端验证，需要添加 auth = (账户名, 密码)

				import requests

				auth=('test', '123456')
				
				response = requests.get('http://192.168.199.107', auth = auth)
				
				print response.text


		(10) Cookie:

			如果某个响应中包含一些 cookie，你可以快速访问它们：
			>>>response = requests.get("http://www.baidu.com/")
			>>>cookiejar= response.cookies #返回RequestsCookieJar对象:
				<RequestsCookieJar[Cookie(version=0, name='BDORZ', value='27315', 
				port=None, port_specified=False, domain='.baidu.com', domain_specified=True, 
				domain_initial_dot=True, path='/', path_specified=True, secure=False, 
				expires=1536989870, discard=False, comment=None, comment_url=None,
				rest={}, rfc2109=False)]>
			
			将RequestsCookieJar转为字典：

			>>>cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
			>>> print cookiedict
				{'BDORZ': '27315'}

			Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，
			但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar 传到 Requests 中：

			>>> jar = requests.cookies.RequestsCookieJar()
			>>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
			>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
			>>> url = 'http://httpbin.org/cookies'
			>>> r = requests.get(url, cookies=jar)
			>>> r.text
				'{
					"cookies": {
					"tasty_cookie": "yum"}
				}'

		

		(11)Sission:

			在requests里，session 对象是一个非常常用的对象，这个对象代表一次用户会话
			从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。

			会话能让我们在夸请求时候保持某些参数，比如同一个Session实例发出的所有
			请求之间保持cookie

			例子 实现人人网登录：

			import requests

			1.创建session对象，可以保存Cookie值
			ssion = requests.session()

			2.处理headers
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
				AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36}

			3.需要登录的用户名和密码
			data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

			4.发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
			ssion.post("http://www.renren.com/PLogin.do", data = data)

			5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
			response = ssion.get("http://www.renren.com/410043129/profile")

			6. 打印响应内容
			print response.text

			
		(12)处理HTTPS请求 SSL证书验证

			Requests也可以为HTTPS请求验证SSL证书：
			要想检查某个主机的SSL证书，你可以使用 verify 参数（也可以不写）

				import requests
				response = requests.get("https://www.baidu.com/", verify=True)
			
				# 也可以省略不写
				# response = requests.get("https://www.baidu.com/")
				print r.text

			如果SSL证书验证不通过，或者不信任服务器的安全证书，则会报出SSLError，
			据说 12306 证书是自己做的：
			
				import requests
				response = requests.get("https://www.12306.cn/mormhweb/")
				print response.text

				果然：

					SSLError: ("bad handshake: Error([('SSL routines', 'ssl3_get_server_certificate',
							'certificate verify failed')],)",)
			如果我们想跳过 12306 的证书验证，把 verify 设置为 False 就可以正常请求了。
				r = requests.get("https://www.12306.cn/mormhweb/", verify = False)
	
		(13)超时

			你可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。
			基本上所有的生产代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应：

			>>> requests.get('http://github.com', timeout=0.001)
			Traceback (most recent call last):
				  File "<stdin>", line 1, in <module>
				  requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80):
				  Request timed out. (timeout=0.001)
			
			注意：
				timeout 仅对连接过程有效，与响应体的下载无关。 
				timeout 并不是整个下载响应的时间限制，而是如果服务器在 
				timeout 秒内没有应答，将会引发一个异常（更精确地说，是在 
				timeout 秒内没有从基础套接字上接收到任何字节的数据时）
				If no timeout is specified explicitly, requests do not time out.

		(14)错误与异常

			遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
			如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。
			若请求超时，则抛出一个 Timeout 异常。
			若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
			所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。
			

"-------------------------------------------------------------------"

		第二章  非结构化数据与结构化数据提取

"------------------------------------------------------------------"

实际上爬虫一共就四个主要步骤：

	1、明确目标(要知道你准备在那个范围或者网站去搜索)
	2、爬(将所有网站的内容全部爬下来)
	3、取(去掉对我们没有用处的数据)
	4、处理数据(按照我们想要的方式存储和使用)

1、XML 简介：

	有同学说，我正则用的不好，处理HTML文档很累，有没有其他的方法？
	有！那就是XPath，我们可以先将 HTML文件 转换成 XML文档，
	然后用 XPath 查找 HTML 节点或元素。


	1.什么是XML:

		XML 指可扩展标记语言(EXtensible Markup Language)
		XML 是一种标记语言，很类似HTML
		XML 的设计宗旨是传输数据，而非显示数据
		XML 的标签需要我们自行定义
		XML 被设计为具有自我描述性
		XML 是W3C的推荐标准

	2.XML 与 HTML 的主要差异：

		XML 不是 HTML的替代
		XML 和HTML 为不同的目的而设计
		XML 被设计为了传输和存储数据，其焦点是数据的内容
		HTML 被设计用来显示数据，器焦点是数据的外观
		HTML 旨在显示信息，而XML 旨在传输信息。
		XML 是独立于软件和硬件的信息传输工具。

	3.XML的本质：

		没有任何行为的XML，XML是不作为的，也许这有点难以理解，
		但是XML不会做任何事情，XML被设计用来结构化，存储以及传输信息。

		XML 仅仅是纯文本,并没有什么特别之处，有能力处理纯文本的软件都可以处理XML。
		不过，能够读懂 XML 的应用程序可以有针对性地处理 XML 的标签。
		标签的功能性意义依赖于应用程序的特性。

2、XML的用途：

	XML 应用于 web 开发的许多方便，常用于简化数据的存储和共享。
	
	1. XML 把数据从HTML 分离:
		
		如果你需要在HTML文档中显示动态数据，那么每当数据改变时将花费大量的时间来编辑HTML。
		
		通过 XML，数据能够存储在独立的XML文件中。这样你就可以专注于使用HTML进行布局和显示，
		并确保修改底层数据不再需要对 HTML 进行任何的改变。

		通过使用几行 JavaScript，你就可以读取一个外部 XML 文件，然后更新 HTML 中的数据内容。

	2. XML 简化数据共享
		
		在真实的世界中，计算机系统和数据使用不兼容的格式来存储数据。
		XML 数据以纯文本格式进行存储，因此提供了一种独立于软件和硬件的数据存储方法。
		这让创建不同应用程序可以共享的数据变得更加容易。

	3. XML 简化数据传输

		通过 XML，可以在不兼容的系统之间轻松地交换数据。
		对开发人员来说，其中一项最费时的挑战一直是在因特网上的不兼容系统之间交换数据。
		由于可以通过各种不兼容的应用程序来读取数据，以 XML 交换数据降低了这种复杂性。


	4. XML 简化平台的变更

		升级到新的系统（硬件或软件平台），总是非常费时的。必须转换大量的数据，不兼容的数据经常会丢失。
		XML 数据以文本格式存储。这使得 XML 在不损失数据的情况下，
		更容易扩展或升级到新的操作系统、新应用程序或新的浏览器。

	5. XML 使您的数据更有用

		由于 XML 独立于硬件、软件以及应用程序，XML 使您的数据更可用，也更有用。
		不同的应用程序都能够访问您的数据，不仅仅在 HTML 页中，也可以从 XML 数据源中进行访问。
		通过 XML，您的数据可供各种阅读设备使用（手持的计算机、语音设备、新闻阅读器等），
		还可以供盲人或其他残障人士使用。


3、XML 树结构：

	XML 文档形成了一种树结构，它从"根部"开始，然后扩展到"枝叶"

	1. 一个XML 文档实例：

		XML 使用简单的具有自我描述性的语法：

		<?xml version="1.0" encoding="ISO-8859-1"?>
		<note>
		<to>George</to>
		<from>John</from>
		<heading>Reminder</heading>
		<body>Dont forget the meeting!</body>
		</note>

		第一行是XML声明。它定义XML的版本 1.0)和所使用的编码(ISO-8859-1 = Latin-1/西欧字符集)。

		下一行描述文档的根元素（像在说：“本文档是一个便签”）：
			
			<note>

		接下来 4 行描述根的 4 个子元素（to, from, heading 以及 body）：

			<to>George</to>
			<from>John</from>
			<heading>Reminder</heading>
			<body>Dont forget the meeting!</body>

		最后一行定义根元素的结尾：

			</note>

	2. XML 文档形成的一种树结构

		XML 文档必须包含根元素，改元素是所有其他元素的父元素。
		XML 文档中的元素形成了一颗文档树，这课树从根部开始，并扩展树的最底端，
		所有元素均可拥有子元素。
		父、子以及同胞等术语用于描述元素之间的关系。父元素拥有子元素。
		相同层级上的子元素成为同胞（兄弟或姐妹）。
		所有元素均可拥有文本内容和属性(类似HTML中)

4、XML 语法规则：

	XML 的语法规则很简单，且很有逻辑。
	
	1. 所有XML 元素都必须有关闭标签：

		在HTML，经常会看到没有关闭标签的元素：
			<p>This is a paragraph
			<p>This is another paragraph
		在XML中，省略关闭标签违法，所有元素必须有关闭标签
			<p>This is a paragraph</p>
			<p>This is another paragraph</p>  

		注释：您也许已经注意到 XML 声明没有关闭标签。这不是错误。
		声明不属于XML本身的组成部分。它不是XML元素，也不需要关闭标签。

	2. XML 标签对大小写敏感：

		XML 元素使用XML标签进行定义
		XML 标签对大小写敏感，在XML中，标签<Letter>与标签 <letter> 是不同的。
		必须使用相同的大小写来编写打开标签和关闭标签：

		<Message>这是错误的。</message>
		<message>这是正确的。</message>

		注释：打开标签和关闭标签通常被称为开始标签和结束标签。
		不论您喜欢哪种术语，它们的概念都是相同的。

	3. XML必须正确地嵌套：

		在HTML中，常会看到没有正确嵌套的元素：
			<b><i>This text is bold and italic</b></i>
		在XML中，所有元素都必须彼此正确地嵌套：
			<b><i>This text is bold and italic</i></b>

	4. XML 文档必须有根元素：
		
		XML 文档必须有一个元素是其所有元素的父元素，改元素称为根元素。
		<root>
			<child>
				<subchild>.....</subchild>
			</child>
		</root>

	5.	XML的属性值须加引号：

		与 HTML 类似，XML 也可拥有属性（名称/值的对）。
		在 XML 中，XML 的属性值须加引号。请研究下面的两个 XML 文档。
		第一个是错误的，第二个是正确的：

		<note date=08/08/2008>
		<to>George</to>
		<from>John</from>
		</note> 

		<note date="08/08/2008">
		<to>George</to>
		<from>John</from>
		</note> 

	6. 实体引用：
		
		在 XML 中，一些字符拥有特殊的意义。
		如果你把字符 "<" 放在 XML 元素中，会发生错误，这是因为解析器会把它当作新元素的开始。
		这样会产生 XML 错误：
			<message>if salary < 1000 then</message>
		为了避免这个错误，请用实体引用来代替 "<" 字符：
			<message>if salary &lt; 1000 then</message> 

		在 XML 中，有 5 个预定义的实体引用：
	
			&lt;	<	小于
			&gt;	>	大于
			&amp;	&	和号
			&apos;	'	单引号 '
			&quot;	"	引号 "
			
	7. XML 中的注释:

		在 XML 中编写注释的语法与 HTML 的语法很相似：
		<!-- This is a comment --> 

	8. 在XML中,空格会被保留:

		HTML 会把多个连续的空格字符裁减（合并）为一个：

		HTML:	Hello           my name is David.
		输出:	Hello my name is David.

		在 XML 中，文档中的空格不会被删节。

5、XML 元素：

	XML 文档包含XML 元素，

	1. 什么是XML 元素

		XML 元素指的是从(且包括) 开始标签直到(且包括)结束标签的部分。

		元素可以包括其他元素、文本或者两者的混合物，元素也可以拥有属性。

		<bookstore>
			<book category="CHILDREN">
				<title>Harry Potter</title> 
				<author>J K. Rowling</author> 
				<year>2005</year> 
				<price>29.99</price> 
			</book>
			<book category="WEB">
				<title>Learning XML</title> 
				<author>Erik T. Ray</author> 
				<year>2003</year> 
				<price>39.95</price> 
			</book>
		</bookstore> 
		
		<bookstore> 和 <book> 都拥有元素内容，因为它们包含了其他元素。
		<author> 只有文本内容，因为它仅包含文本。
		只有 <book> 元素拥有属性 (category="CHILDREN")。

	2. XML 命名规则：

		XML 元素必须遵守以下命名规则：

			名称可以包含字母、数据以及其他的字符
			名称不能以数字或者标点符号开始
			名称不能以字符 “xml”（或者 XML、Xml）开始
			名称不能包含空格

	3. 最佳命名习惯：

		使名称具有描述性。使用下划线的名称也很不错。
		名称应当比较简短，比如：<book_title>，而不是：<the_title_of_the_book>。
		避免 "-" 字符。如果您按照这样的方式进行命名："first-name"，会误认为你需要提取第一个单词。
		避免 "." 字符。如果您按照这样的方式进行命名："first.name"，会误认为"name"是对象"first"的属性。
		避免 ":" 字符。冒号会被转换为命名空间来使用

		XML 文档经常有一个对应的数据库，其中的字段会对应 XML 文档中的元素。
		有一个实用的经验，即使用数据库的名称规则来命名 XML 文档中的元素。
		
	4. XML 元素是扩展的：

		XML 元素是可扩展，以携带更多的信息。
		请看下面这个 XML 例子：

			<note>
			<to>George</to>
			<from>John</from>
			<body>Dont forget the meeting!</body>
			</note> 

		让我们设想一下，我们创建了一个应用程序可将<to><from>
		以及<body>元素提取出来，并产生以下的输出：

			MESSAGE
			To: George
			From: John

			Dont forget the meeting!

		想象一下，之后这个 XML 文档作者又向这个文档添加了一些额外的信息：
			<note>
			<date>2008-08-08</date>
			<to>George</to>
			<from>John</from>
			<heading>Reminder</heading>
			<body>Dont forget the meeting!</body>
			</note>
			
		那么这个应用程序会中断或崩溃吗？
		不会。这个应用程序仍然可以找到XML文档中的<to><from>以及<body>元素，并产生同样的输出。
		XML 的优势之一，就是可以经常在不中断应用程序的情况进行扩展。

6、 XML 属性：

	XML 元素可以在开始标签中包含属性，类似 HTML。属性 (Attribute) 提供关于元素的额外（附加）信息。

	1. XML 属性必须加引号
		
		属性值必须被引号包围，不过单引号和双引号均可使用。
		比如一个人的性别，person 标签可以这样写：
			<person sex="female">
		或者这样也可以：
			<person sex='female'>

	2. XML 元素 vs. 属性

		<person sex="female">
			<firstname>Anna</firstname>
			<lastname>Smith</lastname>
		</person> 
			
		<person>
			<sex>female</sex>
			<firstname>Anna</firstname>
			<lastname>Smith</lastname>
		</person>

		在第一个例子中，sex 是一个属性。在第二个例子中，sex 则是一个子元素。两个例子均可提供相同的信息。
		没有什么规矩可以告诉我们什么时候该使用属性，而什么时候该使用子元素。
		属性用起来很便利，但是在 XML 中，您应该尽量避免使用属性。
		如果信息感觉起来很像数据，那么请使用子元素吧。

	3. 避免 XML 属性？

		因使用属性而引起的一些问题：
			属性无法包含多重的值（元素可以）
			属性无法描述树结构（元素可以）
			属性不易扩展（为未来的变化）
			属性难以阅读和维护
		请尽量使用元素来描述数据。而仅仅使用属性来提供与数据无关的信息。
		
	4. 针对元数据的 XML 属性

		有时候会向元素分配 ID 引用。这些 ID 索引可用于标识 XML 元素，
		它起作用的方式与 HTML 中 ID 属性是一样的。
		这个例子向我们演示了这种情况：

		<messages>
			<note id="501">
				<to>George</to>
			    <from>John</from>
				<heading>Reminder</heading>
				<body>Dont forget the meeting!</body>
			</note>
			<note id="502">
				<to>John</to>
				<from>George</from>
				<heading>Re: Reminder</heading>
				<body>I will not</body>
			</note> 
		</messages>

		上面的 ID 仅仅是一个标识符，用于标识不同的便签。它并不是便签数据的组成部分。

		元数据（有关数据的数据）应当存储为属性，而数据本身应当存储为元素。

7、XML 验证：

	拥有正确语法的 XML 被称为“形式良好”的 XML。
	通过 DTD 验证的 XML 是“合法”的 XML。

	1.形式良好的 XML 文档：

		"形式良好" 或"结构良好"的 XML 文档拥有正确的语法。
		"形式良好"（Well Formed）的 XML 文档会遵守前几章介绍过的 XML 语法规则：
		XML 文档必须有根元素
		XML 文档必须有关闭标签
		XML 标签对大小写敏感
		XML 元素必须被正确的嵌套
		XML 属性必须加引号
	
	2. 验证 XML 文档：

		合法的 XML 文档是“形式良好”的 XML 文档，
		同样遵守文档类型定义 (DTD) 的语法规则：

		<?xml version="1.0" encoding="ISO-8859-1"?>
		<!DOCTYPE note SYSTEM "Note.dtd">
		<note>
		<to>George</to>
		<from>John</from>
		<heading>Reminder</heading>
		<body>Dont forget the meeting!</body>
		</note> 

		DOCTYPE 声明是对外部 DTD 文件的引用。

	3.XML DTD：

		DTD的作用是定义XML文档的结构。它使用一系列合法的元素来定义文档结构：
	
"------------------------------------------------------------------------"

XPath:

	XPath (XML Path Language)是一门在XML文档中查找信息的语言，
	可以用来在XML文档中对元素和属性进行遍历。

1、XPath 简介：

	1. 什么是 XPath：

		XPath 使用路径表达式在XML文档中进行导航。
		XPath 包含一个标准的函数库
		Xpath 是XSLT 中的主要元素
		XPath 是一个W3C标准

	2. XPath 路径表达式：
		
		XPath 使用路径表达式来选取 XML 中的节点或者节点集。
		这些路径表达式和我们在常规的电脑系统中开打的表达式非常相似。

	3. XPath 标准函数

		XPath 含有超过 100 个内建函数，这些函数用于字符串值、数值、
		日期和时间比较、节点和QName 处理、序列处理、逻辑值等等。

2、XPath 节点：

	在XPath中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档节点(即根节点)

	1.XPath术语

		节点(Node) ：XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。

			请看下面这个 XML 文档：
			<?xml version="1.0" encoding="ISO-8859-1"?>
		
			<bookstore>
		
				<book>
					<title lang="en">Harry Potter</title>
					<author>J K. Rowling</author> 
					<year>2005</year>
					<price>29.99</price>
				</book>
				
			</bookstore>
		
			上面的XML文档中的节点例子：

			<bookstore> （文档节点）
			<author>J K. Rowling</author> （元素节点）
			lang="en" （属性节点）

		基本值(或称原子值，Atomic value):

			基本值是无父或无子的节点。
			基本值的例子：
			J K. Rowling
			"en"

		项目（Item）:
			项目是基本值或者节点。
			
	2. 节点关系：

		父（Parent）
			每个元素以及属性都有一个父。
			在下面的例子中，book 元素是 title、author、year 以及 price 元素的父：

			<book>
				<title>Harry Potter</title>
				<author>J K. Rowling</author>
				<year>2005</year>
				<price>29.99</price>
			</book>
	

		子（Children）

			元素节点可有零个、一个或多个子。
			在下面的例子中，title、author、year 以及 price 元素都是 book 元素的子：

				<book>
					<title>Harry Potter</title>
				    <author>J K. Rowling</author>
					<year>2005</year>
					<price>29.99</price>
				</book>
		
		同胞（Sibling）

			拥有相同的父的节点
			在下面的例子中，title、author、year 以及 price 元素都是同胞：
			<book>
				<title>Harry Potter</title>
			    <author>J K. Rowling</author>
				<year>2005</year>
				<price>29.99</price>
			</book>
			
		先辈（Ancestor）

			某节点的父、父的父，等等。
			在下面的例子中，title 元素的先辈是 book 元素和 bookstore 元素：

			<bookstore>

				<book>
					<title>Harry Potter</title>
					<author>J K. Rowling</author>
					<year>2005</year>
				    <price>29.99</price>
				</book>

			</bookstore>

		后代（Descendant）
		
			某个节点的子，子的子，等等。
			在下面的例子中，bookstore 的后代是 book、title、author、year 以及 price 元素：

			<bookstore>

			<book>
				  <title>Harry Potter</title>
				  <author>J K. Rowling</author>
				  <year>2005</year>
				  <price>29.99</price>
			</book>

			</bookstore>
		
3、XPath 语法：

	XPath 使用路径表达式来选取 XML 文档中的节点或节点集。
	节点是通过沿着路径 (path) 或者步 (steps) 来选取的。

	XML 实例文档
	我们将在下面的例子中使用这个 XML 文档。

		<?xml version="1.0" encoding="ISO-8859-1"?>
		
		<bookstore>
		
			<book>
				<title lang="eng">Harry Potter</title>
				<price>29.99</price>
			</book>
			
			<book>
				<title lang="eng">Learning XML</title>
			    <price>39.95</price>
			</book>
				
		</bookstore>


	1.选取节点：

		XPath 使用路径表达式在 XML 文档中选取节点。
		节点是通过沿着路径或者 step 来选取的。

		下面列出了最有用的路径表达式：

		表达式             描述

		nodename           选取此节点的所有子节点

		/                  从根节点选取

		//                 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置

		.                  选取当前节点

		..                 选取当前节点的父节点

		@                  选取属性

		实例：

		在下面的表格中，我们已经列出了一些路径表达式以及表达式的效果：

		路径表达式           结果

		bookstore            选取bookstore元素的所有子节点

		/bookstore           选取根元素 bookstore

		bookstore/book       选取属于bookstore的子元素的所有book元素

		//book               选取所有book子元素，而不考虑它们在文档中的位置

		bookstore//book     选择属于 bookstore 元素的后代的所有book元素而不管它们位于bookstore之下的什么位置。

		//@lang             选取名为lang的所有属性

	2. 谓语(Predicates):

		谓语用来查找某个特定的节点或者包含某个指定的值的节点。
		谓语被嵌在方括号中。

		路径表达式							结果

		/bookstore/book[1]				选取属于 bookstore 子元素的第一个 book 元素。
		
		/bookstore/book[last()]			选取属于 bookstore 子元素的最后一个 book 元素。
		
		/bookstore/book[last()-1]		选取属于 bookstore 子元素的倒数第二个 book 元素。
		
		/bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
		
		//title[@lang]	                选取所有拥有名为 lang 的属性的 title 元素。
		
		//title[@lang='eng']	        选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
		
		/bookstore/book[price>35.00]	选取bookstore元素的所有book元素且其中的price元素的值须大于35.00。
		
		/bookstore/book[price>35.00]/title	选取bookstore元素中的book元素的所有title元素
											且其中的price元素的值须大于35.00。

	3. 选取未知节点:

		XPath 通配符可用来选取未知的XML元素。

		通配符          描述

		 *              匹配任何元素节点

		 @*             匹配任何属性节点

		 node()         匹配任何类型的节点


		 路径表达式	      结果
		 /bookstore/*	选取 bookstore 元素的所有子元素。
		 //*	        选取文档中的所有元素。
		 //title[@*]	选取所有带有属性的 title 元素。

	4. 选取若干路径

		通过在路径表达式中使用"|"运算符，您可以选取若干个路径。
		
		路径表达式							结果
		//book/title | //book/price		选取 book 元素的所有 title 和 price 元素。
		//title | //price				选取文档中的所有 title 和 price 元素。
		/bookstore/book/title | //price	选取属于bookstore元素的book元素的所有title元素及文档中所有的price元素。

4、XPath Axes(轴):

	轴可定义相对于当前节点的节点集。
	
	1.XPath 轴：

		轴名称				结果
	
		ancestor			选取当前节点的所有先辈（父、祖父等）。
		ancestor-or-self	选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
		attribute			选取当前节点的所有属性。
		child				选取当前节点的所有子元素。
		descendant			选取当前节点的所有后代元素（子、孙等）。
		descendant-or-self	选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
		following			选取文档中当前节点的结束标签之后的所有节点。
		namespace			选取当前节点的所有命名空间节点。
		parent				选取当前节点的父节点。
		preceding			选取文档中当前节点的开始标签之前的所有节点。
		preceding-sibling	选取当前节点之前的所有同级节点。
		self				选取当前节点。

	2. 位置路径表达式：

		位置路径可以是绝对的，也可以是相对的。
		绝对路径起始于正斜杠(/)，而相对路径不会这样。
		在两种情况中，位置路径均包括一个或多个步，每个步均被斜杠分割：
		
		绝对位置路径：/step/step/...

		相对位置路径：step/step/...

	3. 步（step）包括：

		轴(axis):定义所选节点与当前节点之间的树关系
		节点测试(node-test):识别某个轴内部的节点
		零个或者更多谓语(predicate):更深入地提炼所选的节点集

		步的语法：轴名称::节点测试[谓语]

		例子					 结果

		child::book				选取所有属于当前节点的子元素的 book 节点。
		attribute::lang			选取当前节点的 lang 属性。
		child::*				选取当前节点的所有子元素。
		attribute::*			选取当前节点的所有属性。
		child::text()			选取当前节点的所有文本子节点。
		child::node()			选取当前节点的所有子节点。
		descendant::book		选取当前节点的所有 book 后代。
		ancestor::book			选择当前节点的所有 book 先辈。
		ancestor-or-self::book	选取当前节点的所有 book 先辈以及当前节点（如果此节点是 book 节点）
		child::*/child::price	选取当前节点的所有 price 孙节点。



5、XPath 运算符:

	XPath 表达式可返回节点集、字符串、逻辑值以及数字。

	运算符		描述		实例		返回值

	|		计算两个节点集	//book|//cd	返回所有拥有 book 和 cd 元素的节点集
	+			加法		6 + 4			10
	-			减法		6 - 4			2
	*			乘法		6 * 4			24
	div			除法		8 div 4			2
	=			等于		price=9.80	如果 price 是 9.80，则返回 true。如果 price 是 9.90，则返回 false。
	!=			不等于		price!=9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。
	<			小于		price<9.80	如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。
	<=			小于或等于	price<=9.80	如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。
	>			大于		price>9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。
	>=			大于或等于	price>=9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.70，则返回 false。
	or			或price=9.80orprice=9.70如果 price 是 9.80，则返回 true。如果 price 是 9.50，则返回 false。
	and			与price>9.00andprice<9.90	如果 price 是 9.80，则返回 true。如果 price 是 8.50，则返回 false。
	mod			计算除法的余数	5 mod 2		1

	

6、lxml库：

	lxml 是一个HTML/XML的解析库，主要的功能是如何解析和提取HTML/XML数据。

	lxml和正则一样，也是用 C 实现的，是一款高性能的 Python HTML/XML解析器，
	我们可以利用之前学习的XPath语法，来快速的定位特定元素以及节点信息。
	需要安装C语言库，可使用 pip 安装：pip install lxml （或通过wheel方式安装）

	1. 初步使用：

		我们利用它来解析HTML代码，简单示例：

		# 使用 lxml 的 etree 库
		from lxml import etree 

		text = '''
			<div>
				<ul>
					<li class="item-0"><a href="link1.html">first item</a></li>
					<li class="item-1"><a href="link2.html">second item</a></li>
					<li class="item-inactive"><a href="link3.html">third item</a></li>
					<li class="item-1"><a href="link4.html">fourth item</a></li>
					<li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
				</ul>
			</div>
		'''

		#利用etree.HTML，将字符串解析为HTML文档
		html = etree.HTML(text) 

		# 按字符串序列化HTML文档
		result = etree.tostring(html) 

		print(result)

		输出结果：

			<html><body>
			<div>
			    <ul>
					<li class="item-0"><a href="link1.html">first item</a></li>
					<li class="item-1"><a href="link2.html">second item</a></li>
					<li class="item-inactive"><a href="link3.html">third item</a></li>
					<li class="item-1"><a href="link4.html">fourth item</a></li>
					<li class="item-0"><a href="link5.html">fifth item</a></li>
				</ul>
			</div>
			</body></html>

		lxml 可以自动修正 html 代码，例子里不仅补全了li标签，还添加了body，html标签。
	

	2.文件读取：

		除了直接读取字符串，lxml还支持从文件里读取内容。
		我们新建一个hello.html文件：
		再利用etree.parse()方法来读取文件。
		
		# lxml_parse.py
		from lxml import etree

		# 读取外部文件 hello.html
		html = etree.parse('./hello.html')
		result = etree.tostring(html, pretty_print=True)		
		print(result)

"-----------------------------------------------------------------------"	
		
CSS 选择器：BeautifulSoup4:

	Beautiful Soup 是一个从HTML或XML文件中提取的数据的Python库。
	它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.

1、安装Beautiful Soup：

	如果你用是新版的Debian或ubuntu,那么可以通过系统的软件包管理来安装:	
		apt-get install Python-bs4
	
	Beautiful Soup 4 是通过PyPi发布的，所以如果你无法使用系统包管理安装，
	那么也可以通过esay_install 或pip来安装，包的名字是beautifulsoup4
		esay_install beautifulsoup4
		pip install beautifulsoup4

	如果你没有安装easy_install 或pip，那你可以通过下载源码，然后通过setup.py
	来安装：
		Python setup.py install

2、安装解析器：

	Beautiful Soup 支持Python 标准库中的HTML解析器，还支持一下第三方的解析器
	其中一个是lxml，根据操作系统不同，可以选择下列方式安装lxml：
		$ apt-get install Python-lxml
		$ easy_install lxml
		$ pip install lxml

	另一个可供选择的解析器是纯Python实现的 html5lib , html5lib的解析方式与浏览器相同,
	可以选择下列方法来安装html5lib:
		$ apt-get install Python-html5lib
		$ easy_install html5lib
		$ pip install html5lib

	下表列出的解析器，以及它们的优缺点：

	解析器              使用方法                            优势                        

	Python标准库     BeautifulSoup(markup,"html.parse")   内置标准库，速度快，容错能力强 

	lxml HTML解析器  BeautifulSoup(markup,"lxml")          速度快、文档容错能力强

	lxml XML解析器	 BeautifulSoup(markup,["lxml-xml"])    速度快，唯一支持xml的解析器
					 BeautifulSoup(markup, "xml")

	html5lib         BeautifulSoup(markup,"html5lib")      以浏览器的方式解析文档


	推荐使用lxml作为解析器,因为效率更高. 


3、如何使用:

	将一段文档传入BeautifulSoup 的构造方法，就能得到一个文档的对象，可以传入一段字符或这个文件句柄。

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(open("index.html"))
	soup = BeautifulSoup("<html>data</html>")

	首先,文档被转换成Unicode,并且HTML的实例都被转换成Unicode编码。
	BeautifulSoup("Sacr&eacute; bleu!")
	<html><head></head><body>Sacré bleu!</body></html>

	示例：

		首先必须导入bs4库
		from bs4 import BeautifulSoup

		html = """
		<html><head><title>The Dormouse's story</title></head>
		<body>
		<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
		<p class="story">Once upon a time there were three little sisters; and their names were
		<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
		<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		and they lived at the bottom of a well.</p>
		<p class="story">...</p>
		"""

		#创建 Beautiful Soup 对象
		soup = BeautifulSoup(html)

		#打开本地 HTML 文件的方式来创建对象
		#soup = BeautifulSoup(open('index.html'))
		
		#格式化输出 soup 对象的内容
		print soup.prettify()

		如果在IPython2 下执行，会看到这样的一段警告：

		/usr/local/Python-2.7.14/lib/python2.7/site-packages/bs4/__init__.py:181
		: UserWarning: No parser was explicitly specified, 
		so I'm using the best available HTML parser for this system ("lxml"). 
		This usually isn't a problem, but if you run this code on another system, 
		or in a different virtual environment, it may use a different 
		parser and behave differently.
		
		The code that caused this warning is on line 1 of the file <stdin>. 
		To get rid of this warning, change code that looks like this:
		BeautifulSoup(YOUR_MARKUP})
		to this
		BeautifulSoup(YOUR_MARKUP, "lxml")
		markup_type=markup_type))

		意思是，如果我们没有显式地指定解析器，所以默认使用这个系统的最佳可用HTML解析器("lxml")。
		如果你在另一个系统中运行这段代码，或者在不同的虚拟环境中，使用不同的解析器造成行为不同。

		但是我们可以通过soup = BeautifulSoup(html,“lxml”)方式指定lxml解析器。
		


4、对象的种类：

	Beautiful Soup 将复杂HTML文档转换成一个复杂的树形结构，每一个节点都是Python对象。
	所有对象可以归纳为4种：Tag、NavigableString、BeautifulSoup、Comment.
	
	1、Tag
		
		Tag 通俗的讲就是HTML中的一个标签，例如:
		<head><title>The Dormouse story</title></head>
		<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
		<p class="title" name="dromouse"><b>The Dormouse story</b></p>

		上面的head、title、a、p 等等HTML标签加上里面包括的内容就是Tag
		那么试着用Beautiful Soup 来获取Tags:

		from bs4 import BeautifulSoup

		html = """
		<html><head><title>The Dormouses story</title></head>
		<body>
		<p class="title" name="dromouse"><b>The Dormouses story</b></p>
		<p class="story">Once upon a time there were three little sisters; and their names were
		<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
		<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
		and they lived at the bottom of a well.</p>
		<p class="story">...</p>
		"""
		#创建 Beautiful Soup 对象
		soup = BeautifulSoup(html)

		print soup.title
		# <title>The Dormouses story</title>
		
		print soup.head
		# <head><title>The Dormouses story</title></head>
		
		print soup.a
		# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
		
		print soup.p
		# <p class="title" name="dromouse"><b>The Dormouses story</b></p>
		
		print type(soup.p)
		# <class 'bs4.element.Tag'>

	我们可以利用soup加标签签名轻松的获取这些标签的内容，这些对象的类型是bs4.element.Tag。
	但是注意，它查找的所有内容的第一个符合要求的标签，如果要查询所有标签，后面进行介绍。

	对于Tag,它有两个重要的属性，是name 和 attrs:

		print soup.name
		# [document] #soup 对象本身比较特殊，它的 name 即为 [document]

		print soup.head.name
		# head #对于其他内部标签，输出的值便为标签本身的名称

		print soup.p.attrs
		# {'class': ['title'], 'name': 'dromouse'}
		# 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
		
		print soup.p['class'] # soup.p.get('class')
		# ['title'] #还可以利用get方法，传入属性的名称，二者是等价的
			
		soup.p['class'] = "newClass"
		print soup.p # 可以对这些属性和内容等等进行修改
		# <p class="newClass" name="dromouse"><b>The Dormouses story</b></p>
			
		del soup.p['class'] # 还可以对这个属性进行删除
		print soup.p
		# <p name="dromouse"><b>The Dormouses story</b></p>


	2、NavigableString:
		
		既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？
		很简单，用 .string 即可，例如

		print soup.p.string
		#The Dormouses story
		
		print type(soup.p.string)
		# In [13]: <class 'bs4.element.NavigableString'>
		

	3、BeautifulSoup:

		BeautifulSoup 对象表示的是一个文档的内容。
		大部分时候,可以把它当作Tag对象，是一个特殊的Tag，
		我们可以分别获取它的类型，名称，以及属性来感受一下

		print type(soup.name)
		# <type 'unicode'>
		
		print soup.name 
		# [document]
		
		print soup.attrs # 文档本身的属性为空
		# {}
	

	4、Comment：

		Comment 对象是一个特殊类型的NavigableString 对象，其输出的内容不包括注释符号。

		print soup.a
		# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
		
		print soup.a.string
		# Elsie 
		
		print type(soup.a.string)
		# <class 'bs4.element.Comment'>
		
5 遍历文档树：

	1、直接子节点 ：.contents .children 属性：

		.contents:
			
			tag 的.content 属性可以将tag的子节点以列表的方式输出
			print soup.head.contents
			#[<title>The Dormouses story</title>]

			输出方式为列表，我们可以用列表索引来获取它的某一个元素
			print soup.head.contents[0]
			#<title>The Dormouses story</title>
	
		.children:
			
			它返回的不是一个list，不过我们可以通过遍历获取所有子节点。
			我们打印输出 .children看一下，可以发现它是一个list生成器对象

			print soup.head.children
			#<listiterator object at 0x7f71457f5710>

			for child in  soup.body.children:
				print child

	2、所有子孙节点：.descendants 属性：

		.contents 和 .children 属性仅包含tag的直接子节点，.descendants属性
		可以对所有tag的子孙节点进行递归循环，和children类似，我么需要遍历器内容

			for child in soup.descendants:
				print child

	3、节点内容：.string 属性：

		如果tag 只有一个NavigableString类型的子节点，那么这个tag可以使用
		.string得到子节点。如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,
		输出结果与当前唯一子节点的 .string 结果相同。

		通俗点说就是：如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
		如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。例如：

		print soup.head.string
		#The Dormouses story
		print soup.title.string
		#The Dormouses story

5、搜索文档树：

	1、find_all(name, attrs, recursive, text, **kwargs)

		name 参数：name参数可以查找所有名字为name的tag,字符串对象会被自动忽略掉

		A.传字符串
			最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,
			Beautiful Soup会查找与字符串完整匹配的内容,
			下面的例子用于查找文档中所有的<b>标签:

			soup.find_all('b')
			# [<b>The Dormouses story</b>]
			
			print soup.find_all('a')
			#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
			<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
			<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
		
		B.传正则表达式

			如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的match()来匹配内容.
			下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到

			import re
			for tag in soup.find_all(re.compile("^b")):
				print(tag.name)
			# body
			# b

		C.传列表

			如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.
			下面代码找到文档中所有<a>标签和<b>标签:

			soup.find_all(["a", "b"])
			# [<b>The Dormouses story</b>,
			#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
			#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
			#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
		
	2 keyword 参数:

		soup.find_all(id='link2')
		# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

	3 text 参数

		通过text参数可以搜搜文档中的字符串内容，与name参数的可选值一样, 
		text参数接受字符串 , 正则表达式 , 列表

		soup.find_all(text="Elsie")
		# [u'Elsie']
		
		soup.find_all(text=["Tillie", "Elsie", "Lacie"])
		# [u'Elsie', u'Lacie', u'Tillie']
		
		soup.find_all(text=re.compile("Dormouse"))
		[u"The Dormouse's story", u"The Dormouse's story"]


CSS选择器:

	这就是另一种与 find_all 方法有异曲同工之妙的查找方法.

	写 CSS 时，标签名不加任何修饰，类名前加.，id名前加#
	在这里我们也可以利用类似的方法来筛选元素,用到的方法是soup.select(),返回类型是list

	1、通过标签名查找：

		print soup.select('title') 
		#[<title>The Dormouses story</title>]
		
		print soup.select('a')
		#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
		  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
	  	  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
		
		print soup.select('b')
		#[<b>The Dormouses story</b>]

	2、通过类名查找：

		print soup.select('.sister')
		#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
		  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
		  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	3、通过id名查找：

		print soup.select('#link1')
		#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
	
	4、组合查找：
		
		组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，
		例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
		
		print soup.select('p #link1')
		#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

		直接子标签查找，则使用 > 分隔

		print soup.select("head > title")
		#[<title>The Dormouses story</title>]

	5、属性查找：

		查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，
		所以中间不能加空格，否则会无法匹配到。

		print soup.select('a[class="sister"]')
		#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
		<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
		<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
		
		print soup.select('a[href="http://example.com/elsie"]')
		#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]


		同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
		print soup.select('p a[href="http://example.com/elsie"]')
		#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

	6、获取内容：

		以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用get_text()方法来获取它的内容。

		soup = BeautifulSoup(html, 'lxml')
		print type(soup.select('title'))
		print soup.select('title')[0].get_text()
		
		for title in soup.select('title'):
			 print title.get_text()

"-------------------------------------------------------------------"

数据提取之JSON与JsonPATH

	JSON(JavaScript Object Notation)是一种轻量级的数据交换格式，
	它使得人们很容易进行阅读和编写。同时方便机器解析和生产。
	适用于进行数据交互的场景，比如网站前台与后台之间的数据交互。

	JSON 和 XML的比较可谓是不相上下。

JSON：

	json 简单的说就是javascript中的对象和数组，所以这两种结构
	就是对象和数组两种结构，通过这两种结构可以表示各种复杂的结构。

	import json：

	json 模块提供四个功能：dumps、dump、loads、load
	用于字符串和python数据类型间进行转换。


JsonPath:

	JsonPath 是一种信息抽取类库，是从JSON 文档中抽取指定信息的工具，
	提供了多种语言实现版本，包括：Javascript,Python,PHP和java。

	JsonPath对于JSON来说，相当于XPATH对于XML。

	JsonPath 与 XPath 语法对比：
	Json结构清晰，可读性高，复杂度低，非常容易匹配，下表对应的XPath的用法：

		XPath       JSONPath       描述

		/             $            根节点

		.             @            现行节点

		/            . or []       取子节点

		..           n/a           取父节点，Jsonpath未支持

		//           ..            就是不管位置，选择所有符合条件的条件

		*            *             匹配所有的元素节点

		@            n/a           属性，Json不支持，因为Json是key-value结构，不需要

		[]           []            迭代器标示

		|            [,]           支持迭代器中做多选

		[]           ?()           支持过滤操作

		n/a          ()            支持表达式计算

		()           n/a           分组，JsonPath不支持


	示例：我们以拉勾网城市JSON文件 http://www.lagou.com/lbs/getAllCitySearchLabels.json为例，
	获取所有城市：

		import urllib2
		import jsonpath
		import json
		import chrdet

		url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		html = response.read()

		# 把json格式字符串转换成python对象
		jsonbj = json.loads(html)

		# 从根节点开始，匹配name节点
		citylist = jsonpath.jsonpath(jsonbj,'$..name')
		
		print citylist

		fp = open('city.json','w')

		content = json.dumps(citylist,ensure_ascii=False)
		print content

		fp.write(content.encode('utf-8'))
		fp.close()

	注意事项：

		json.loads() 是把Json格式字符串解码转换成Python对象，
		如果在Json.loads的时候出错，要注意被解码的Json字符的编码。

		如果传入的字符串编码不是UTF-8的话，需要指定字符串编码的参数encoding 

			dataDict = json.loads(jsonStrGBK);

			dataJsonStr是JSON字符串，假设其编码本身是非UTF-8的话而是GBK，
			那么上述代码会导致错误，应修改为：
			dataDict = json.loads(jsonStrGBK, encoding="GBK");

		如果 dataJsonStr通过encoding指定了合适的编码，但是其中又包含了其他编码的字符，
		则需要先去将dataJsonStr转换为Unicode，然后再指定编码格式调用json.loads()
			dataJsonStrUni = dataJsonStr.decode("GB2312"); 
			dataDict = json.loads(dataJsonStrUni, encoding="GB2312");

字符串编码转换：

	这是中国程序员最苦逼的地方，什么乱码之类的几乎都是由汉字引起的。
	其实编码问题很好搞定，只要记住一点：

	任何平台的任何编码 都能和 Unicode 互相转换
	UTF-8 与 GBK 互相转换，那就先把UTF-8转换成Unicode，再从Unicode转换成GBK，反之同理。

	这是一个 UTF-8 编码的字符串
		utf8Str = "你好地球"
				
	1. 将UTF-8编码的字符串 转换成 Unicode 编码
		unicodeStr = utf8Str.decode("UTF-8")
				
	2. 再将 Unicode 编码格式字符串 转换成 GBK 编码
		gbkData = unicodeStr.encode("GBK")
				
	1. 再将 GBK 编码格式字符串 转化成 Unicode
		unicodeStr = gbkData.decode("gbk")
				
	2. 再将 Unicode 编码格式字符串转换成 UTF-8
		utf8Str = unicodeStr.encode("UTF-8")

	decode的作用是将其他编码的字符串转换成 Unicode 编码
	encode的作用是将 Unicode 编码转换成其他编码的字符串
	一句话：UTF-8是对Unicode字符集进行编码的一种编码方式



"-------------------------------------------------------------------"

		第三章  动态HTML处理和机器图像

"-------------------------------------------------------------------"
		
爬虫(Spider)，反爬虫(Anti-Spider)，反反爬虫(Anti-Anti-Spider) 之间恢宏壮阔的斗争...

	通常情况下，在爬虫与反爬虫的对弈中，爬虫一定会胜利。
	换言之，只要人类能够正常访问的网页，爬虫在具备同等资源的情况下就一定可以抓取到。

	关于爬虫部分一些建议：

		1、尽量减少请求次数，能抓列表页就不抓详情页，减轻服务器压力，程序员都是混口饭吃不容易。

		2、不要只看 Web 网站，还有手机 App 和 H5，这样的反爬虫措施一般比较少。

		3、实际应用时候，一般防守方做到根据 IP 限制频次就结束了，除非很核心的数据，
			不会再进行更多的验证，毕竟成本的问题会考虑到。

		4、如果真的对性能要求很高，可以考虑多线程(一些成熟的框架如 Scrapy都已支持)，甚至分布式...

JavaScript:

	JavaScript 是网络上最常用也是支持者最多的客户端脚本语言。
	它可以收集用户的跟踪数据，不需要重载页面直接提交表单，
	在页面嵌入多媒体文件，甚至运行网络游戏。

	我们可以在网页源代码的<scripy>标签里看到，比如：
		<script type="text/javascript" src="https://statics.huxiu.com/w/mini/static_2015/js/sea.js?
		v=201601150944"></script>

jQuery：

	jQuery是一个十分常见的库,70%最流行的网站(约 200 万)和约30%的其他网站(约2亿)都在使用。
	一个网站使用jQuery的特征,就是源代码里包含了jQuery入口,比如:
	
	<script type="text/javascript" src="https://statics.huxiu.com/w/mini
	/static_2015/js/jquery-1.11.1.min.js?v=201512181512"></script>

	如果你在一个网站上看到了 jQuery，那么采集这个网站数据的时候要格外小心。
	jQuery可 以动态地创建 HTML 内容,只有在 JavaScript 代码执行之后才会显示。
	如果你用传统的方 法采集页面内容,就只能获得 JavaScript 代码执行之前页面上的内容。

Ajax：

	我们与网站服务器通信的唯一方式，就是发出 HTTP 请求获取新页面。
	如果提交表单之后，或从服务器获取信息之后，网站的页面不需要重新刷新，
	那么你访问的网站就在用Ajax 技术。

	Ajax 其实并不是一门语言,而是用来完成网络任务(可以认为它与网络数据采集差不多)的一系列技术。
	Ajax 全称是 Asynchronous JavaScript and XML(异步 JavaScript 和 XML)，
	网站不需要使用单独的页面请求就可以和网络服务器进行交互 (收发信息)。

DHTML：

	Ajax 一样，动态 HTML(Dynamic HTML, DHTML)也是一系列用于解决网络问题的 技术集合。
	DHTML是用客户端语言改变页面的HTML元素(HTML、CSS，或者二者皆 被改变)。
	比如页面上的按钮只有当用户移动鼠标之后才出现,背景色可能每次点击都会改变，
	或者用一个 Ajax 请求触发页面加载一段新内容，网页是否属于DHTML，
	关键要看有没有用 JavaScript 控制 HTML 和 CSS 元素。


	那么，如何搞定？

		那些使用了Ajax或DHTML技术改变/加载内容的页面，可能有一些采集手段。
		但是用 Python 解决这个问题只有两种途径:

		1、直接从 JavaScript 代码里采集内容（费时费力）
		2、用 Python的第三方库运行 JavaScript，直接采集你在浏览器里看到的页面（这个可以有）。


"--------------------------------------------------------------------------------"


Selenium:

	Selenium 是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，
	类型像我们玩游戏用的按键精灵(按键精灵是一款模拟鼠标键盘动作的软件。
	通过制作脚本，可以让按键精灵代替双手，自动执行一系列鼠标键盘动作。
	按键精灵简单易用，不需要任何编程知识就可以作出功能强大的脚本。)
	可以按指定的命令自动操作，不同是Selenium 可以直接运行在浏览器上，
	它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器）。

	Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据。
	甚至页面截屏，或者判断网站上某些动作是否发生。

	Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。
	但是我们有时候需要让它内嵌在代码中运行，
	所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器。

	pip用命令安装：pip install selenium


PhantomJS:

	PhantomJS 是一个基于Webkit的"无界面"(headless)浏览器，
	它会把网站加载到内存并执行页面上的 JavaScript，因为不会展示图形界面，
	所以运行起来比完整的浏览器要高效。

	如果我们把 Selenium 和 PhantomJS 结合在一起，就可以运行一个非常强大的网络爬虫了，
	这个爬虫可以处理 JavaScrip、Cookie、headers，以及任何我们真实用户需要做的事情。

	注意：PhantomJS 只能从它的官方网站http://phantomjs.org/download.html) 下载。 
	因为 PhantomJS 是一个功能完善(虽然无界面)的浏览器而非一个 Python 库，
	所以它不需要像 Python 的其他库一样安装，但我们可以通过Selenium调用PhantomJS来直接使用。

	PhantomJS 官方参考文档：http://phantomjs.org/documentation
	
	Webkit:

		Webkit 是一个开源的浏览器引擎，与之相对应的引擎有Gecko(Mozilla Firefox 等使用)
		Trident(也称MSHTML, IE使用)
		同时WebKit 也是苹果Mac OS X系统引擎框架版本的名称，
		主要用于Safari，Dashboard，Mail 和其他一些Mac OS X 程序。

快速入门:

	Selenium 库里有个叫 WebDriver 的API。WebDriver 有点像可以加载网站的浏览器，
	但是它也可以像BeautifulSoup 或者其他Selector对象一样用来查找页面元素，与
	页面元素进行交互(发送文本，点击等)以及执行其他动作来运行网络爬虫。
	
		# IPython2 测试代码

		# 导入 webdriver
		from selenium import webdriver

		# 要想调用键盘按键操作需要引入keys包
		from selenium.webdriver.common.keys import Keys

		# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
		driver = webdriver.PhantomJS()

		# 如果没有在环境变量指定PhantomJS位置
		# driver = webdriver.PhantomJS(executable_path="./phantomjs"))
	
		# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
		driver.get("http://www.baidu.com/")
	
		# 获取页面名为 wrapper的id标签的文本内容
		data = driver.find_element_by_id("wrapper").text
	
		# 打印数据内容
		print data
	
		# 打印页面标题 "百度一下，你就知道"
		print driver.title
	
		# 生成当前页面快照并保存
		driver.save_screenshot("baidu.png")
	
		# id="kw"是百度搜索输入框，输入字符串"长城"
		driver.find_element_by_id("kw").send_keys(u"长城")
	
		# id="su"是百度搜索按钮，click() 是模拟点击
		driver.find_element_by_id("su").click()
	
		# 获取新的页面快照
		driver.save_screenshot("长城.png")
	
		# 打印网页渲染后的源代码
		print driver.page_source
	
		# 获取当前页面Cookie
		print driver.get_cookies()
	
		# ctrl+a 全选输入框内容
		driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
	
		# ctrl+x 剪切输入框内容
		driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
	
		# 输入框重新输入内容
		driver.find_element_by_id("kw").send_keys("itcast")
	
		# 模拟Enter回车键
		driver.find_element_by_id("su").send_keys(Keys.RETURN)
	
		# 清除输入框内容
		driver.find_element_by_id("kw").clear()
	
		# 生成新的页面快照
		driver.save_screenshot("itcast.png")
	
		# 获取当前url
		print driver.current_url
	
		# 关闭当前页面，如果只有一个页面，会关闭浏览器
		# driver.close()
	
		# 关闭浏览器
		driver.quit()
	

页面操作：

	Selenium 的WebDriver提供了各种各样的方法来寻找元素，假设下面有一个表单输入框：

	<input type ="text" name = "user-name" id = "passwd-id"/>

	那么：

		# 获取id标签值
		element = driver.find_element_by_id("passwd-id")
		# 获取name标签值
		element = driver.find_element_by_name("user-name")
		# 获取标签名值
		element = driver.find_elements_by_tag_name("input")
		# 也可以通过XPath来匹配
		element = driver.find_element_by_xpath("//input[@id='passwd-id']")

	
定位UI元素 (WebElements)：

	关于元素的选取，有如下的API 单个元素选取

	find_element_by_id
	find_elements_by_name
	find_elements_by_xpath
	find_elements_by_link_text
	find_elements_by_partial_link_text
	find_elements_by_tag_name
	find_elements_by_class_name
	find_elements_by_css_selector

	
	1.By ID:

		<div id = "coolestWidgetEvah">...</div>
		
		实现：

		element = driver.find_element_by_id("coolestWidgetEvah")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		element = driver.find_element(by=By.ID, value="coolestWidgetEvah")

	2.By Class Name:

		<div class="cheese"><span>Cheddar</span></div>
		<div class="cheese"><span>Gouda</span></div>

		实现：

		cheeses = driver.find_elements_by_class_name("cheese")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		cheeses = driver.find_elements(By.CLASS_NAME, "cheese")

	3.By Tag Name：

		<iframe src="..."></iframe>

		实现：

		frame = driver.find_element_by_tag_name("iframe")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		frame = driver.find_element(By.TAG_NAME, "iframe")

	4.By Name:

		<input name="cheese" type="text"/>

		实现：

		cheese = driver.find_element_by_name("cheese")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		cheese = driver.find_element(By.NAME, "cheese")

	5. By Link Text

		<a href="http://www.google.com/search?q=cheese">cheese</a>

		实现：

		cheese = driver.find_element_by_link_text("cheese")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		cheese = driver.find_element(By.LINK_TEXT, "cheese")

	6.By Partial Link Text：

		<a href="http://www.google.com/search?q=cheese">search for cheese</a>

		实现：

		cheese = driver.find_element_by_partial_link_text("cheese")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		cheese = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")

	7.By CSS：

		<div id="food"><span class="dairy">milk</span><span class="dairy aged">cheese</span></div>

		实现：

		cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")


	8.By XPath:

		<input type="text" name="example" />
		<INPUT type="text" name="other" />

		实现：

		inputs = driver.find_elements_by_xpath("//input")
		------------------------ or -------------------------
		from selenium.webdriver.common.by import By
		inputs = driver.find_elements(By.XPATH, "//input")


鼠标动作链：

	有些时候，我们需要再页面上模拟一些鼠标操作，比如双击、右击、拖拽甚至按住不动等，
	我们可以通过导入 ActionChains 类来做到：

	#导入 ActionChains 类
	from selenium.webdriver import ActionChains

	# 鼠标移动到 ac 位置
	ac = driver.find_element_by_xpath('element')
	ActionChains(driver).move_to_element(ac).perform()
	
	
	# 在 ac 位置单击
	ac = driver.find_element_by_xpath("elementA")
	ActionChains(driver).move_to_element(ac).click(ac).perform()
	
	# 在 ac 位置双击
	ac = driver.find_element_by_xpath("elementB")
	ActionChains(driver).move_to_element(ac).double_click(ac).perform()
	
	# 在 ac 位置右击
	ac = driver.find_element_by_xpath("elementC")
	ActionChains(driver).move_to_element(ac).context_click(ac).perform()
	
	# 在 ac 位置左键单击hold住
	ac = driver.find_element_by_xpath('elementF')
	ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()
	
	# 将 ac1 拖拽到 ac2 位置
	ac1 = driver.find_element_by_xpath('elementD')
	ac2 = driver.find_element_by_xpath('elementE')
	ActionChains(driver).drag_and_drop(ac1, ac2).perform()
	

填充表单：

	我们已经知道了怎样向文本框中输入文字，但是有时候我们会碰到<select> </select>标签的下拉框。
	直接点击下拉框中的选项不一定可行。

	<select id="status" class="form-control valid" onchange="" name="status">
	<option value=""></option>
	<option value="0">未审核</option>
	<option value="1">初审通过</option>
	<option value="2">复审通过</option>
	<option value="3">审核不通过</option>
	</select>

	
	Selenium专门提供了Select类来处理下拉框。 其实 WebDriver 中提供了一个叫 Select 的方法，
	可以帮助我们完成这些事情：

	
	导入Select 类
	from selenium.webdriver.support.ui import Select

	找到name的选项卡
	select = Select(driver.find_element_by_name('status'))

	select.select_by_index(1)
	select.select_by_value("0")
	select.select_by_visible_text(u"未审核")

	以上是三种选择下拉框的方式，它可以根据索引来选择，可以根据值来选择，
	可以根据文字来选择。注意：

		index 索引从 0 开始
		value是option标签的一个属性值，并不是显示在下拉框中的值
		visible_text是在option标签文本的值，是显示在下拉框的值

	全部取消选择怎么办呢？很简单:

		select.deselect_all()

弹窗处理:

	当你触发了某个事件之后，页面出现了弹窗提示，处理这个提示或者获取提示信息方法如下：

	alert = driver.switch_to_alert()

页面切换：

	一个浏览器肯定会有很多窗口，所以我们肯定要有方法来实现窗口的切换。切换窗口的方法如下：
	
	driver.switch_to.window("this is window name")

	也可以使用 window_handles 方法来获取每个窗口的操作对象。例如：

	for handle in driver.window_handles:
		driver.switch_to_window(handle)

页面前进和后退：

	操作页面的前进和后退功能：

	driver.forward()     #前进
	driver.back()        # 后退

Cookies：

	获取页面每个Cookies值，用法如下：

	for cookie in driver.get_cookies():
		print "%s -> %s" % (cookie['name'], cookie['value'])

	删除Cookies，用法如下：

		# By name
		driver.delete_cookie("CookieName")
		
		# all
		driver.delete_all_cookies()"")

页面等待：

	注意：这是非常重要的一部分！！

	现在的网页越来越多采用了Ajax技术，这样程序便不能确定何时某个元素完全加载出来了。
	如果实现页面等待时间过长导致某个dom元素还没出来，但是你的代码直接使用了这个WebElement,
	那么就会抛出NullPointer的异常。

	为了避免这种元素定位困难而且会提高产生 ElementNotVisibleException 的概率。
	所以 Selenium 提供了两种等待方式，一种是隐式等待，一种是显式等待。

	隐式等待是等待特定的时间，显式等待是指定某一条件直到这个条件成立时继续执行。

	显示等待：

		显示等待指定某个条件，然后设置最长等待时间，如果这个时间还没有找到元素，
		那么就会抛出异常了。

		from selenium import webdriver
		from selenium.webdriver.common.by import By
		#WebDriverWait库，负责循环等待
		from selenium.webdriver.support.ui import WebDriverWait
		#expected_conditions 类，负责条件出发
		from selenium.webdriver.support import expected_conditions as EC

		driver = webdriver.Chrome()
		driver.get("http://www.xxxxx.com/loading")
		try:
		    # 页面一直循环，直到 id="myDynamicElement" 出现
			element = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.ID, "myDynamicElement")))
		finally:
			driver.quit()

		如果不写参数，程序默认会 0.5s 调用一次来查看元素是否已经生成，
		如果本来元素就是存在的，那么会立即返回。

		下面是一些内置的等待条件，你可以直接调用这些条件，而不用自己写某些等待条件了。

			title_is
			title_contains
			presence_of_element_located
			visibility_of_element_located
			visibility_of
			presence_of_all_elements_located
			text_to_be_present_in_element
			text_to_be_present_in_element_value
			frame_to_be_available_and_switch_to_it
			invisibility_of_element_located
			element_to_be_clickable – it is Displayed and Enabled.
			staleness_of
			element_to_be_selected
			element_located_to_be_selected
			element_selection_state_to_be
			element_located_selection_state_to_be
			alert_is_present
	
	隐式等待:

		隐式等待比较简单，就是简单地设置一个等待时间，单位为秒。

		from selenium import webdriver

		driver = webdriver.Chrome()
		driver.implicitly_wait(10) # seconds
		driver.get("http://www.xxxxx.com/loading")
		myDynamicElement = driver.find_element_by_id("myDynamicElement")
		
		当然如果不设置，默认等待时间为0。


案例一：网站模拟登陆：


	# douban.py
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	import time

	driver = webdriver.PhantomJS()
	driver.get("http://www.douban.com")

	# 输入账号密码
	driver.find_element_by_name("form_email").send_keys("xxxxx@xxxx.com")
	driver.find_element_by_name("form_password").send_keys("xxxxxxxx")

	# 模拟点击登录
	driver.find_element_by_xpath("//input[@class='bn-submit']").click()

	# 等待3秒
	time.sleep(3)

	# 生成登陆后快照
	driver.save_screenshot("douban.png")

	with open("douban.html", "w") as file:
		file.write(driver.page_source)
	
	driver.quit()


案例二：动态页面模拟点击:

	#!/usr/bin/env python
	# -*- coding:utf-8 -*-

	# python的测试模块
	import unittest
	from selenium import webdriver
	from bs4 import BeautifulSoup

	class douyuSelenium(unittest.TestCase):
		# 初始化方法
	    def setUp(self):
		self.driver = webdriver.PhantomJS()

		#具体的测试用例方法，一定要以test开头
		def testDouyu(self):
			self.driver.get('http://www.douyu.com/directory/all')
			while True:
				# 指定xml解析
				soup = BeautifulSoup(driver.page_source, 'xml')
				# 返回当前页面所有房间标题列表 和 观众人数列表
				titles = soup.find_all('h3', {'class': 'ellipsis'})
				nums = soup.find_all('span', {'class': 'dy-num fr'})
																				  
				#使用zip()函数来可以把列表合并，并创建一个元组对的列表[(1,2), (3,4)]
				for title, num in zip(nums, titles):
				print u"观众人数:" + num.get_text().strip(), u"\t房间标题: " + title.get_text().strip()

				# page_source.find()未找到内容则返回-1
				if driver.page_source.find('shark-pager-disable-next') != -1:
					break

				# 模拟下一页点击
				self.driver.find_element_by_class_name('shark-pager-next').click()
	
		 #退出时的清理方法

		def tearDown(self):
			print '加载完成...'
			self.driver.quit()
		
	if __name__ == "__main__":
		unittest.main()

案例三：执行 JavaScript 语句:

	1.隐藏百度图片

	from selenium import webdriver

	driver = webdriver.PhantomJS()
	driver.get("https://www.baidu.com/")
	
	# 给搜索输入框标红的javascript脚本
	js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"
	
	# 调用给搜索输入框标红js脚本
	driver.execute_script(js)
	
	#查看页面快照
	driver.save_screenshot("redbaidu.png")
	
	#js隐藏元素，将获取的图片元素隐藏
	img = driver.find_element_by_xpath("//*[@id='lg']/img")
	driver.execute_script('$(arguments[0]).fadeOut()',img)
	
	# 向下滚动到页面底部
	driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")
	
	#查看页面快照
	driver.save_screenshot("nullbaidu.png")
	
	driver.quit()

	2.模拟滚动条滚动到底部

	from selenium import webdriver
	import time

	driver = webdriver.PhantomJS()
	driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")
	
	# 向下滚动10000像素
	js = "document.body.scrollTop=10000"
	#js="var q=document.documentElement.scrollTop=10000"
	time.sleep(3)
	
	#查看页面快照
	driver.save_screenshot("douban.png")
	
	# 执行JS语句
	driver.execute_script(js)
	time.sleep(10)
	
	#查看页面快照
	driver.save_screenshot("newdouban.png")
	
	driver.quit()


机器视觉:

	从 Google 的无人驾驶汽车到可以识别假钞的自动售卖机，机器视觉一直都是
	一个应用广泛且具有深远的影响和雄伟的愿景的领域。

	我们将重点介绍机器视觉的一个分支：文字识别，介绍如何用一些
	Python库来识别和使用在线图片中的文字。

	我们可以很轻松的阅读图片里的文字，但是机器阅读这些图片就会非常困难，
	利用这种人类用户可以正常读取但是大多数机器人都没法读取的图片，
	验证码 (CAPTCHA)就出现了。验证码读取的难易程度也大不相同，有些验证码比其他的更加难读。

	将图像翻译成文字一般被称为光学文字识别(Optical Character Recognition, OCR)。
	可以实现OCR的底层库并不多,目前很多库都是使用共同的几个底层 OCR 库,或者是在上面 进行定制。

OCR库概述:

	所谓 OCR 是图像识别领域中的一个子领域，该领域专注于对图片中的文字信息进行识别并
	转换成能被常规文本编辑器编辑的文本。	

	在读取和处理图像、图像相关的机器学习以及创建图像等任务中
	python一直都是非常出色的语言，虽然有很多库可以进行图像处理。
	但在这里我们重点介绍：Tessercat

	Tesseract:

		Tesseract 是一个OCR库，目前是由Google赞助。Tesseract是目前公认最优秀
		最精确的开源OCR系统，除了极高的精确度，Tesseract也具有很高的灵活性。
		它可以通过训练识别出任何字体，也可以识别出任何Unicode字符。

	安装Tesseract:

		Windows 系统
		下载可执行安装文件https://code.google.com/p/tesseract-ocr/downloads/list安装。

		Linux 系统
		可以通过 apt-get 安装: $sudo apt-get tesseract-ocr

		Mac OS X系统
		用 Homebrew(http://brew.sh/)等第三方库可以很方便地安装 brew install tesseract

		要使用 Tesseract 的功能，比如后面的示例中训练程序识别字母，
		要先在系统中设置一 个新的环境变量 $TESSDATA_PREFIX，
		让Tesseract知道训练的数据文件存储在哪里，然后搞一份tessdata数据文件，
		放到Tesseract目录下。

		在大多数 Linux 系统和 Mac OS X 系统上,你可以这么设置: 
		$export TESSDATA_PREFIX=/usr/local/share/Tesseract

		在 Windows 系统上也类似,你可以通过下面这行命令设置环境变量: 
		#setx TESSDATA_PREFIX C:\Program Files\Tesseract OCR\Tesseract

	安装pytesseract:

		Tesseract 是一个 Python 的命令行工具，不是通过 import 语句导入的库。
		安装之后,要用 tesseract 命令在 Python 的外面运行，
		但我们可以通过 pip 安装支持Python 版本的 Tesseract库：

		pip install pytesseract


处理给规范的文字:

	你要处理的大多数文字都是比较干净、格式规范的。
	格式规范的文字通常可以满足一些需求，不过究竟什么是"格式混乱"
	什么算"格式规范"，确实因人而异。通常,格式规范的文字具有以下特点:

		1、使用一个标准字体(不包含手写体、草书,或者十分“花哨的”字体)
		   虽然被复印或拍照,字体还是很清晰,没有多余的痕迹或污点

		2、排列整齐,没有歪歪斜斜的字

		3、没有超出图片范围,也没有残缺不全,或紧紧贴在图片的边缘

	文字的一些格式问题在图片预处理时可以进行解决。例如,可以把图片转换成灰度图,
	调整亮度和对比度,还可以根据需要进行裁剪和旋转（详情请关注图像与信号处理），
	但是,这些做法在进行更具扩展性的 训练时会遇到一些限制。

	通过下面的命令运行Tesseract，读取文件并把结果写到一个文本文件中:
	
		tesseract test.jpg text

	通过Python代码实现:

		import pytesseract
		from PIL import Image
		image = Image.open('test.jpg')
		text = pytesseract.image_to_string(image)
		print text

	

从网站图片中抓取文字:

	用 Tesseract 读取硬盘里图片上的文字,可能不怎么令人兴奋,
	但当我们把它和网络爬虫组合使用时,就能成为一个强大的工具。
	
	网站上的图片可能并不是故意把文字做得很花哨(就像餐馆菜单的JPG图片上的艺术字),
	但它们上面的文字对网络爬虫来说就是隐藏起来了，举个例子：

		1、虽然亚马逊的robots.txt文件允许抓取网站的产品页面,但是图书的预览页通常不让网络机器人采集。

		2、 图书的预览页是通过用户触发Ajax脚本进行加载的,预览图片隐藏在div节点下面;
			其实,普通的访问者会觉得它们看起来更像是一个 Flash 动画,而不是一个图片文件。
			当然,即使我们能获得图片,要把它们读成文字也没那么简单。
		
		3、下面的程序就解决了这个问题:首先导航到托尔斯泰的《战争与和平》的大字号印刷版 
			1, 打开阅读器,收集图片的 URL 链接,然后下载图片,识别图片,最后打印每个图片的文字。
			因为这个程序很复杂,利用了前面几章的多个程序片段,
			所以我增加了一些注释以让每段代码的目的更加清晰:

		import  time

		from urllib.request import urlretrieve
		import subprocess
		from selenium import webdriver

		driver = webdriver.PhantomJS()

		# 用Selenium试试Firefox浏览器:
		# driver = webdriver.Firefox()

		driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
		# 单击图书预览按钮 driver.find_element_by_id("sitbLogoImg").click() imageList = set()
		# 等待页面加载完成
		time.sleep(5)
		# 当向右箭头可以点击时,开始翻页
		
		while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
			driver.find_element_by_id("sitbReaderRightPageTurner").click()
			time.sleep(2)
			# 获取已加载的新页面(一次可以加载多个页面,但是重复的页面不能加载到集合中) 
			pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
			for page in pages:
				image = page.get_attribute("src")
				imageList.add(image)
		driver.quit()

		# 用Tesseract处理我们收集的图片URL链接 
		for image in sorted(imageList):
			# 保存图片
			urlretrieve(image, "page.jpg")
			p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			f = open("page.txt", "r")
			p.wait() 
			print(f.read())

尝试对知乎网验证码进行处理：

	许多流行的内容管理系统即使加了验证码模块，其众所周知的注册页面也经常会遭到网络 机器人的垃圾注册。

	那么，这些网络机器人究，竟是怎么做的呢?既然我们已经，可以成功地识别出保存在电脑上 的验证码了，
	那么如何才能实现一个全能的网络机器人呢?

	大多数网站生成的验证码图片都具有以下属性。

		1、它们是服务器端的程序动态生成的图片。验证码图片的 src 属性可能和普通图片不太一 样，
		   比如 <img src="WebForm.aspx?id=8AP85CQKE9TJ">，但是可以和其他图片一样进行下载和处理。

		2、图片的答案存储在服务器端的数据库里。

		3、很多验证码都有时间限制，如果你太长时间没解决就会失效。

		4、常用的处理方法就是，首先把验证码图片下载到硬盘里，
		   清理干净，然后用 Tesseract 处理 图片，最后返回符合网站要求的识别结果。

		import requests
		import time
		import pytesseract
		from PIL import Image
		from bs4 import BeautifulSoup

		def captcha(data):
			with open('captcha.jpg','wb') as fp:
				fp.write(data)
			time.sleep(1)
			image = Image.open("captcha.jpg")
			text = pytesseract.image_to_string(image)
			print "机器识别后的验证码为：" + text
			command = raw_input("请输入Y表示同意使用，按其他键自行重新输入：")
			if (command == "Y" or command == "y"):
				return text
			else:
				return raw_input('输入验证码：')

		def zhihuLogin(username,password):

			#构建一个保存Cookie值的session对象
			sessiona = requests.Session()
			headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) 
						Gecko/20100101 Firefox/47.0'}
			
			# 先获取页面信息，找到需要POST的数据（并且已记录当前页面的Cookie）
			html = sessiona.get('https://www.zhihu.com/#signin', headers=headers).content
			
			# 找到 name 属性值为 _xsrf 的input标签，取出value里的值
			_xsrf = BeautifulSoup(html ,'lxml').find('input', attrs={'name':'_xsrf'}).get('value')

			# 取出验证码，r后面的值是Unix时间戳,time.time()
			captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
			response = sessiona.get(captcha_url, headers = headers)

			data = {
				"_xsrf":_xsrf,
				"email":username,
				"password":password,
				"remember_me":True,
				"captcha": captcha(response.content)
				}
			
			response = sessiona.post('https://www.zhihu.com/login/email', data = data, headers=headers)
			print response.text

			response = sessiona.get('https://www.zhihu.com/people/maozhaojun/activities', headers=headers)
			print response.text


		if __name__ == "__main__":
			#username = raw_input("username")
			#password = raw_input("password")
			zhihuLogin('xxxx@qq.com','ALAxxxxIME')

		
"-------------------------------------------------------------------"

		第四章  Scrapy 框架

"-------------------------------------------------------------------"

"-------------------------------------------------------------------"

		第五章  Scrapy 实战项目		

"-------------------------------------------------------------------"

"-------------------------------------------------------------------"

		第六章 scrapy-redis 分布式组件

"-------------------------------------------------------------------"


"-------------------------------------------------------------------"

		第七章 scrapy-redis实战

"-------------------------------------------------------------------"






