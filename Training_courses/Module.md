"--------------------------------------------------------------------------"

				Python 模块
	
"--------------------------------------------------------------------------"

常用标准库：

builtins:    内建函数 默认加载

	abs(x)                       返回x的绝对值
	bin(x)                       将一个整数x转换为二进制字符串
	chr(i)                       返回i对应的ASCII字符
	float([x])                   返回x对应的浮点数。
	complex([real[, imag]])      返回一个复数 read+imag1j*，或者将一个字符串或数转换为复数。
	dict()                       返回一个字典。
	globals()                    返回全局符号表字典。
	len(s)                       返回s的长度。
	type(object)                 返回object对象的类型。
	max()                        返回最大值。
	min()                        返回最小值。
	dir([object])                无参数时，返回当前局部作用域中的属性；有参数时，返回参数对象的有效属性
	enumerate(sequence，start=0) 返回可迭代对象sequence的（count，value）元组序列，其中count从start开始递增。
	filter(function，iterable)   对可迭代对象iterable中的每个元素调用function函数，返回结果序列。
	map(function，iterable，...) 应用function到每一个元素上，返回结果列表。
	frozenset([iterable])        返回一个不可变的集合对象。
	help([object])               返回帮助信息。
	hash(object)                 返回对象object的哈希值。
	id(object)                   返回对象object的唯一标识，通常是object在内存中的地址。
	input([prompt])              读取输入值。
	isinstance(object，classinfo)判断object是否是classinfo的一个实例，或者是其子类的实例
	next(iterable[,default])     返回迭代器的下一个元素。
	open(name[, mode[, buffering]]) 打开一个文件，返回文件对象。
	pow(x, y[, z])               如果z存在，返回x^y % z，否则返回x^y。
	print()                      输出
	range(stop)                  返回从0到stop-1的列表。
	reload(module)               重新导入模块module。

"-------------------------------------------------------------------"

os	              操作系统接口

	1、 os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
		os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。

		os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

			top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
			root 所指的是当前正在遍历的这个文件夹的本身的地址
			dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
			files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)

	2、os.name
		输出字符串指示正在使用的平台。如果是window 则用’nt’表示，对于Linux/Unix用户，它是’posix’。

	3、os.getcwd()
		函数得到当前工作目录，即当前Python脚本工作的目录路径。

	4、os.listdir()
		返回指定目录下的所有文件和目录名。

	5、os.remove()
		删除一个文件。
	
	6、os.system()
		运行shell命令。

	7、os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
		os.path.isdir(os.getcwd()) 
			True 
		os.path.isfile(‘a.txt’) 
			False

	8、os.path.exists()函数用来检验给出的路径是否真地存在
		os.path.exists(‘C:\Python25\abc.txt’) 
			False 
		os.path.exists(‘C:\Python25’) 
			True
	
	9、os.path.abspath(name):获得绝对路径


	10、os.path.getsize(name):获得文件大小，如果name是目录返回0L


	11、os.path.split()
		函数返回一个路径的目录名和文件名
		os.path.split(‘C:\Python25\abc.txt’) 
			(‘C:\Python25’, ‘abc.txt’)

	12、os.path.splitext():分离文件名与扩展名
			os.path.splitext(‘a.txt’) 
				(‘a’, ‘.txt’)

	13、os.path.join(path,name):连接目录与文件名或目录
			os.path.join(‘c:\Python’,’a.txt’) 
				‘c:\Python\a.txt’ 
			os.path.join(‘c:\Python’,’f1’) 
				‘c:\Python\f1’
	
	
	14、os.path.basename(path):返回文件名
			os.path.basename(‘a.txt’) 
				‘a.txt’ 
			os.path.basename(‘c:\Python\a.txt’) 
				‘a.txt’

	15、os.path.dirname(path):返回文件路径
			os.path.dirname(‘c:\Python\a.txt’) 
				‘c:\Python’

"-----------------------------------------------------------------"

sys	            Python解释器交互

	方法	使用
	sys.argv()	命令行参数List，第一个元素是程序本身路径
	
	sys.version	获取Python解释程序的版本信息
	sys.hexversion	获取Python解释程序的版本值，16进制格式如：0x020403F0
	sys.api_version	解释器的C的API版本
	sys.getwindowsversion()	获取Windows的版本
	
	sys.stdout	标准输出
	sys.stdin	标准输入
	sys.stdin.readline()	从标准输入读一行，sys.stdout.write(“a”) 屏幕输出a
	sys.stderr	错误输出
	sys.exit(n)	退出程序，正常退出时exit(0)
	
	sys.modules	返回系统导入的模块字段，key是模块名，value是模块
	sys.modules.keys()	返回所有已经导入的模块列表
	sys.builtin_module_names	Python解释器导入的模块列表
	
	sys.maxint	最大的Int值
	sys.maxunicode	最大的Unicode值
	
	sys.path	返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
	sys.platform	返回操作系统平台名称
	sys.executable	Python解释程序路径
	sys.copyright	记录python版权相关的东西
	
	sys.exc_info()	获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
	sys.exc_clear()	用来清除当前线程所出现的当前的或最近的错误信息
	sys.exec_prefix	返回平台独立的python文件安装的位置
		
	sys.getdefaultencoding()	返回当前你所用的默认的字符编码格式
	sys.getfilesystemencoding()	返回将Unicode文件名转换成系统文件名的编码的名字
	sys.setdefaultencoding(name)	用来设置当前默认的字符编码，如果name和任何一个可用的编码都不匹配，
									抛出 LookupError，这个函数只会被site模块的sitecustomize

"------------------------------------------------------------------------------"

functools	       常用的工具


	functools,用于高阶函数:指那些作用于函数或者返回其它函数的函数，
	通常只有是可以被当做函数调用的对象就是这个模块的目标。

	模块使用：

	
	1、partial: 

		functools.partial(func,*args,**keywords),装饰器函数，返回一个新的partial对象。
		调用partial对象和调用被修饰的函数func相同，只不过调用partial对象时传入的参数
		通常要少于调用func时传入的参数个数。当一个函数func可以接收很多参数，
		而某一次使用只需要更改其中的一部分参数，其他的参数都保持不变时，
		partial对象就可以将这些不变的对象冻结起来，这样调用partial对象时传入未冻结的参数，
		partial对象调用func时连同已经被冻结的参数一同传给func函数，从而可以简化调用过程。

		import functools

		def add(a,b):
			    return a + b

		add3 = functools.partial(add,3)
		add5 = functools.partial(add,5)

		print add3(4)
			7		

		print add5(10)
			15

	
	2、partialmethod
	
	3、recursive_repr
	
	4、reduce
		和内置函数reduce一样。
	
	5、singledispatch
	
	6、total_ordering
		这是一个装饰器类，这个类定义了一个或者多个比较排序方法，
		这个类装饰器将会补充其余的比较方法，减少了自己定义所有比较方法时的工作量；
		
	7、update_wrapper
		
	8、wraps



"--------------------------------------------------------------------------------"

json	        编码和解码 JSON 对象

1、JSON语法：

	JSON:JavaScript Object Notation(JavaScript 对象表示法)
	JSON 是存储和交换文本信息的语法。类似 XML
	JSON 比XML 更小、更快、更容易理解。
	json 是轻量级的文本数据交换格式
	json 独立于语言，json使用javascript语法来描述数据对象，但是JSON仍然独立于语言和平台。

	json语法：
		
		JSON语言是JavaScript对象表示语法的子集。

			(1)数据在名称/值对中
			(2)数据由逗号分隔
			(3)大括号保存对象
			(4)中括号保存数组


	json 名称/值对：

		JSON 数据的书写格式是：名称/值对
		名称/值对包括字段名称(在双引号中)，后面写一个冒号，然后是值：
		"name":"runoob"

	json值：

		JSON值可以是：

			(1)数字(整数或浮点数)
			(2)字符串(在双引号中)
			(3)逻辑值(true或false)
			(4)数组(在中括号中)
			(5)对象(在大括号中)
			(6)null


		json数字:
			{
				"age":30
			}
	
		json对象：
			json对象在大括号（{}）中书写：对象可以包含多个名称/值对：
			key必须是字符串，value可以是合法的JSON数据类型(字符串、数字、对象、数组、布尔值、null)
			key 和 value 中使用冒号(:)分割
			每个key/value对使用逗号(,)分割


			访问对象值：
				
				可以使用点号(.)来访问对象的值：

				实例：
					var myObj,x:
					myObj ={"name":"runoob","url":"www.runoob.com"};
					x=myObj.name;

				也可以使用中括号([])来访问对象的值：
				实例：

					var myObj,x:
					myObj = {"name":"runoob","url":"www.runoob.com"};
					x = myObj["name"]

			嵌套JSON对象：

				
				myObj = {

				    "name":"runoob",
					    "alexa":10000,
						    "sites": {

							"site1":"www.runoob.com",
							"site2":"m.runoob.com",
							"site3":"c.runoob.com"}
						}

				可以使用点号(.)或者中括号([])来访问嵌套的 JSON 对象。

				x = myObj.sites.site1;
				或者
				x = myObj.sites["site1"];
				
				修改值：
					myObj.sites.site1 = "www.google.com";	
					或
					myObj.sites["site1"] = "www.google.com";
					
				删除对象属性：

					可以使用 delete 关键字来删除 JSON 对象的属性：
					delete myObj.sites.site1;
					或
					delete myObj.sites["site1"]
					

		
		
		json数组：json数组在中括号中书写：
			
			JSON 数组在中括号中书写。
			JSON 中数组值必须是合法的 JSON 数据类型（字符串, 数字, 对象, 数组, 布尔值或 null）。
			{
				"sites":[
				{"name":"runoob","url":"www.runoob.com"},
				{"name":"google","url":"www.google.com"}]
			}
		
		json 布尔值：
			
			{
				"flag":true
			}

		json null:

			{
				"runoob":null
			}

	JSON 文件：
		
		JSON 文件的文件类型是".json"
		JSON 文件的MIME类型是"application/json"

python JSON:

json(JavaScript Object Notation) 一种轻量级的数据交换格式，易于人阅读和编写。
	
	impot json

	json.dumps()         将Python 对象编码成JSON字符串

		
	jsom.loads()         将已编码的JSON字符串解码为Python对象。












"---------------------------------------------------------------------------------"
logging            记录日志，调试

multiprocessing	      多进程

threading	          多线程

copy	               拷贝

time	               时间

datetime	        日期和时间

calendar	           日历

hashlib	            加密算法



"------------------------------------------------------------------------------"

random	           生成随机数

	random.seed(a=None, version=2)  # 初始化伪随机数生成器。如果未提供a或者a=None，																 则使用系统时间为种子。如果a是一个数，则作为种子。
	random.getstate()				# 返回一个当前生成器的内部状态的对象
	random.setstate(state)			# 传入一个先前利用getstate方法获得的状态对象，使得生成器恢复到这个状态。
	random.getrandbits(k)			# 返回range(0,2**k)之间的一个整数，相当于randrange(0,2**k)
	

	random.randrange(stop)			# 返回range(0,stop)之间的一个整数
	random.randrange(start, stop[, step])  # 返回range[start,stop)之间的一个整数，可加step，跟range(0,10,2)类似
	
	random.randint(a, b)			# 返回range[a,b]之间的一个整数，等价于然的range(a,b+1)
	random.choice(seq)				#从非空序列seq中随机选取一个元素。如果seq为空则弹出 IndexError异常。
	random.choices(population, weights=None, *, cum_weights=None, k=1) 
									#3.6版本新增。从population集群中随机抽取K个元素（可重复）。
	
	weights是相对权重列表，cum_weights是累计权重，两个参数不能同时存在。
	
	random.shuffle(x[, random])		# 随机打乱序列x内元素的排列顺序。只能针对可变的序列，对于不可变序列，
									请使用下面的sample()方法。
	random.sample(population, k)  # 从population样本或集合中随机抽取K个不重复的元素形成新的序列。
									常用于不重复的随机抽样。返回的是一个新的序列，不会破坏原有序列。
									要从一个整数区间随机抽取一定数量的整数，
									请使用sample(range(10000000), k=60)类似的方法，这非常有效和节省空间。
									如果k大于population的长度，则弹出ValueError异常。
	random.random()  # 返回一个介于左闭右开[0.0, 1.0)区间的浮点数
	random.uniform(a, b)  # 返回一个介于a和b之间的浮点数。如果a>b，则是b到a之间的浮点数。
							这里的a和b都有可能出现在结果中。]


"------------------------------------------------------------------------------------------"

re	             字符串正则匹配

socket	        标准的 BSD Sockets API

shutil	         文件和目录管理

glob	       基于文件通配符搜索





"--------------------------------------------------------------------------------------------"


常用扩展库:

扩展库					说明

requests	    使用的是 urllib3，继承了urllib2的所有特性

urllib	           基于http的高层库

scrapy	                 爬虫

beautifulsoup4	   HTML/XML的解析器

celery	          分布式任务调度模块

redis	                 缓存

Pillow(PIL)	          图像处理

xlsxwriter	      仅写excle功能,支持xlsx

xlwt	          仅写excle功能,支持xls ,2013或更早版office

xlrd				仅读excle功能

elasticsearch	    全文搜索引擎

pymysql	            数据库连接库

mongoengine/pymongo	mongodbpython接口

matplotlib	             画图

numpy/scipy            科学计算

django/tornado/flask	web框架

xmltodict	         xml 转 dict

SimpleHTTPServer	简单地HTTP Server,不使用Web框架

gevent	            基于协程的Python网络库

fabric	               系统管理

pandas                数据处理库

scikit-learn	      机器学习库



