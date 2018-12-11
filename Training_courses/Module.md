"--------------------------------------------------------------------------"

				Python 模块
	
"--------------------------------------------------------------------------"

常用标准库：

"--------------------------------------------------------------------------"

Number:

decimal: 提供十进制浮点运算

	常用方法：

		可以传递给Decimal整型或者字符串参数，但是不能是浮点数据，
		因为浮点数据本身就是不准确。要从浮点数据转换为Decimal类型。

	from decimal import *

	1、Decimal

		print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
			
			0.0

	2、要从浮点数据转换为Decimal类型

		Decimal.from_float(12.222)
	
			Decimal('12.2219999999999995310417943983338773250579833984375')

	3、通过设置有效数字，限定结果样式：

		getcontext().prec = 6
		Decimal(1)/Decimal(7)
	
			Decimal('0.142857')
	
	4、四舍五入，保留几位小数

		Decimal('50.6789').quantize(Decimal('0.00'))
			Decimal('50.68')


	5、Decimal 结果转化为string

		str(Decimal('3.40').quantize(Decimal('0.0')))
			'3.4'

分数：fractions:

	1、Fraction类
		
		from fractions  import Fraction
		x = Fraction(1,3)
		y = Fraction(4,6)
		
		printf(x + y)
			Fraction(1,1)
		
		print(x - y)
			Fraction(-1,3)

集合：set():

	set是基本数据类型中的集合类型，有可变集合set()和不可变集合frozenset两种

	1、创建集合，要创建一个集合对象，向内置的set函数传递一个序列或其他的可迭代的对象：

		x = set('abcde')
		y = set('bdxyz')

		print(x)
			set(['a', 'c', 'b', 'e', 'd'])

	2、集合添加和删除

		集合的添加方法常用方法，分别是add和update

		add方法：要把传入的元素作为一个整体添加到集合中
		
		x.add('python')
			set(['a', 'c', 'b', 'e', 'd', 'python'])

		update方法：把要传入的元素拆开，作为一个个体传入到集合中：

		x.update('xyz')
			set(['a', 'c', 'b', 'e', 'd', 'python', 'y', 'x', 'z'])

		删除方法：remove()

		x.remove('python')
			set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])


	3、集合通过表达式操作符支持一般的数学集合运算。
	   注意，不能在一般序列上应用这些表达式，必须通过序列创建集合后才能使用。

	   python 符号          含义

		  -                差集      x - y		set(['a', 'c', 'e'])

		  &                交集      x & y      set(['y', 'x', 'b', 'd', 'z'])
			
		  |                并集      x | y      set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])

	  in,not in            成员关系 'a' in x    True

		==,!=           等于，不等于  x!=y      True

		>,<              大于，小于   x>y       True


"------------------------------------------------------------------------"
	
文件：常见文件运算

	操作                        解释

	这里的输入输出是相对于程序而言，而不是外部文件。

	1、创建文件类型:

		output = open(r'C:\spam','w')   创建输出文件

		input = open('data','r')        创建输入文件，'r'默认类型
		
		input = open('data',)		    创建输入文件，'r'默认类型

	2、读取:

		aSt = input.read()            把整个文件读进单一字符串

		aSt = input.read(N)           读取之后N个字节到字符串

		aSt = input.readline()        读取一行(包括行末标识符)到一个字符串

		aSt = input.readlines()       读取整个文件到字符串列表
	
		注意：readline如果调用返回一个空字符串。这是python文件方法告诉我们已经达到文件底部。
			文件的空行是含有换行符字符串（'\n'）,而不是空字符串。
		

	3、写入

		output.write(aStr)            写入字节字符串到文件

		output.writelines(aList)      把列表内的所有字符串写入文件
		
		注意：我们必须在写入的时候把对象转换成字符串，
		写入方法不会自动地替我们做任何像字符串格式转换的工作。

			x,y,z = 43,44,45
			s = 'spam'
			D = {'a':1,'b':2}
			L = [1,2,3]
								
			F = open('/home/zhangkun/myfile.txt','w')
			F.write(s+'\n')
			F.write('%s,%s,%s\n'%(x,y,z))
			F.write(str(L) + '$' +str(D)+'\n')
			F.close()

			chars = open('/home/zhangkun/myfile.txt','r').read()
				"spam\n43,44,45\n[1, 2, 3]${'a': 1, 'b': 2}\n"
			我们不得不使用转换工具，把文本文件中的字符串转换成真正的python对象。

				line = F.readline()
					"[1, 2, 3]${'a': 1, 'b': 2}\n"
				parts = line.split('$')
					['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
				eval[parts[0]]
					[1, 2, 3]
				eval(parts[1])
					{'a': 1, 'b': 2}
				objects = [eval(p) for p in parts]
						objects
							[[1, 2, 3], {'a': 1, 'b': 2}]

	4、关闭

		output.close()                关闭文件

	5、刷新
		
		output.flush()               把输出缓冲区刷新到磁盘，但不会关闭文件

	6、位移

		anyfile.seek(N)              修改文件位置偏移到N处，以便下一步操作

	
	7、文件山下文管理器：

		文件的上下文管理器比文件自身多了一个异常处理功能，
		它允许我们把文件代码包装到一个逻辑层，以确保退出后可自动关闭文件，而不是依赖垃圾收集。

			with open(r'C:\misc\data.txt') as myfile:
				for line in myfile:
					...use line here...
								
									
			myfile = open(r'C:\misc\data.txt')
				try:
					for line in myfile:
						...use line here...
				finally:
					myfile.close()

	8、打印流重定向：

		print 和sys.stdout的关系如下：
		print(x,y) 等价于 sys.stdout.write(str(x)+''+str(y)+'\n')

		可以让print语句将文字传送到其他地方：
			
			import sys
			tmep = sys.out
			sys.out = open('log.txt','a')
			print(x,y,z)  打印到文件中
			sys.stdout.close()
			sys.stdout=temp

		python3中file关键字允许单个print调用将其发送给一个文件write方法。

			log = open('log.txt','a')
			print(x,y,z,file=log)
			log.close()


		
"-------------------------------------------------------------------------"

python3中保留33个关键字


	import   from    as

	try     except   finally  raise

	for     in       while    with   assert  
	
	break   continue   return

	class  global    nonlcoal

	def     lambda    yield

	if      else     elif

	and     or     not   is

	None    pass    del
	
	True     Flase


"------------------------------------------------------------------------"

Python类型模块：types

	types模块中定义了Python中所有的类型，
	包括NoneType,  TypeType,  IntType,  FloatType,  BooleanType,  BufferType,  
	BuiltinFunctionType,  BuiltinMethodType,   ClassType,  CodeType,  ComplexType,  
	DictProxyType,  DictType,  DictionaryType等。

	Python内建函数type(object)，用于返回当前object对象的类型。例如：

	  >>> type(1)
			<type 'int'>
	  >>> type("1")
			<type 'str'>	
	  >>> type(True)
	　		<type 'bool'>
	　>>> type(2.3)
	　　	<type 'float'>
	　>>> type(1+3j)
	　　	<type 'complex'>
	　>>> type(type(2))
	　　	<type 'type'>
	　>>> type(type)
	　　	<type 'type'>

	实现方法很简单，把对应的类型赋值给变量：

		import types

		#定义了一个类
		class Person(object):
			num = 0
			def __init__(self, name = None, age = None):
				self.name = name
				self.age = age
			def eat(self):
				print("eat food")
		
		#定义一个实例方法
		def run(self, speed):
			print("%s在移动, 速度是 %d km/h"%(self.name, speed))

		#创建一个实例对象
		P = Person("老王", 24)

		#给这个对象添加实例方法
		P.run = types.MethodType(run, P)
		
		#调用实例方法
		P.run(180)


"-------------------------------------------------------------------------"

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
	reload(module)               重新导入模块module。


	range类似，map、zip、以及filter内置函数，在python3中也转变成迭代器以节约内存空间，
	而不再内存中一次性生产结果类表。和range不同，他们都有自己的迭代器。

	range(stop)                  返回从0到stop-1的列表。
	
		在python3中，range返回一个迭代器，该迭代器根据需要产生范围中的数字，
		而不是一个内存中构建一个结果列表。	
		python3中的range对象支持迭代、索引以及len函数，不支持任何其他序列操作（可使用list(...)）
		python3:
		R = range(10)
		R
			range(0, 10)
		I = iter(R)
		next(I)
			0
		next(I)
			1
		...
		
		list(range(10))
			[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



		python2中:
		R = range(10)
		R
			[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		


	zip()						 返回并行元素的元组的列表
		
		1、zip会取得一个或多个序列为参数，然后返回元组的列表，这些序列中的并排的元素配成对。
			L1 = [1,2,3,4]
			L2 = [5,6,7,8]

		要合并这些列表中的元素，可以使用zip来创建一个元组对的列表
		和rang一样，zip在python3.0中也是一个可迭代对象,list调用中以便一次性显示所有结果。
		
			list(zip(L1,L2))
				[(1, 5), (2, 6), (3, 7), (4, 8)]

		2、当参数不同时，zip会以最短的序列的长度为准来截取所得到的元组。
		
			S1 = 'abc'
			S2 = 'xyz123'
			list(zip(S1,S2))
				[('a', 'x'), ('b', 'y'), ('c', 'z')]

		3、zip()构造字典

			keys  = ['spam','eggs','toast']
			vals = [1,3,5]
			D2 = {}
			for (k,v) in zip(keys,vals):
				D2[k] = v

		4、不过在python2.2后续版本中，可以跳过for循环，直接把zip过的键/值列表传给内置的dict构造函数。

			D3 = dict(zip(keys,vals))
				{'toast': 5, 'eggs': 3, 'spam': 1}
			

	map() 根据提供的函数对指定序列做映射。

		语法：
			map(function, iterable, ...)

			function -- 函数，有两个参数
			iterable -- 一个或多个序列

		第一个参数 function 以参数序列中的每一个元素调用 function 函数，
		返回包含每次 function 函数返回值的新列表。

		返回值
			Python 2.x 返回列表。
			Python 3.x 返回迭代器。

		list(map(None,s1,s2))
			[('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]


	filter(function，iterable)   对可迭代对象iterable中的每个元素调用function函数，返回结果序列。
	filter内置函数，对于传入的函数返回True的可迭代对象中的每一项（非空对象）
	
	filter(bool,['spam','','ni'])
	list(filter(bool,['spam','','ni']))
		['spam','ni']
	


	enumerate(sequence，start=0) 返回可迭代对象sequence的（count，value）元组序列，其中count从start开始递增。
	
		enumerate(sequence, [start=0])
		
		参数：
			sequence -- 一个序列、迭代器或其他支持迭代对象。
		    start -- 下标起始位置。

			S = 'spam'
			for (offset,item) in enumerate(S):
				print(item,'appears at offset',offset)
								
				('s', 'appears at offset', 0)
				('p', 'appears at offset', 1)
				('a', 'appears at offset', 2)
				('m', 'appears at offset', 3)

			enumerate函数返回一个生成器对象。
			
		

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

	7、os.getenv()  获取一个环境变量，如果没有返回none

	8、os.putenv(key, value)    设置一个环境变量值

	9、	os.curdir        返回当前目录 ('.')
		os.mkdir(path)    创建一个目录
		os.makedirs(path)    递归的创建目录
		os.chdir(dirname)    改变工作目录到dirname       

	10、os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
		os.path.isdir(os.getcwd()) 
			True 
		os.path.isfile(‘a.txt’) 
			False

	11、os.path.exists()函数用来检验给出的路径是否真地存在
		os.path.exists(‘C:\Python25\abc.txt’) 
			False 
		os.path.exists(‘C:\Python25’) 
			True
	
	12、os.path.abspath(name):获得绝对路径


	13、os.path.getsize(name):获得文件大小，如果name是目录返回0L


	14、os.path.split()
		函数返回一个路径的目录名和文件名
		os.path.split(‘C:\Python25\abc.txt’) 
			(‘C:\Python25’, ‘abc.txt’)

	15、os.path.splitext():分离文件名与扩展名
			os.path.splitext(‘a.txt’) 
				(‘a’, ‘.txt’)

	16、os.path.join(path,name):连接目录与文件名或目录
			os.path.join(‘c:\Python’,’a.txt’) 
				‘c:\Python\a.txt’ 
			os.path.join(‘c:\Python’,’f1’) 
				‘c:\Python\f1’
	
	
	17、os.path.basename(path):返回文件名
			os.path.basename(‘a.txt’) 
				‘a.txt’ 
			os.path.basename(‘c:\Python\a.txt’) 
				‘a.txt’

	18、os.path.dirname(path):返回文件路径
			os.path.dirname(‘c:\Python\a.txt’) 
				‘c:\Python’
	19、文件时间
	os.path.getmtime(name) ＃获取文件的修改时间 

	os.stat(path).st_mtime＃获取文件的修改时间

	os.stat(path).st_ctime #获取文件修改时间

	os.path.getctime(name)#获取文件的创建时间


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
	sys.getrefcount(1)   引用1的个数


"------------------------------------------------------------------------------"

functools	       常用的工具


	1、partial函数(偏函数)

		把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单。

		import functools

		def showarg( *args, **kw):
			print(args)
			print(kw)

		p1=functools.partial(showarg, 1,2,3)
		p1()
		p1(4,5,6)
		p1(a='python', b='itcast')

		运行结果：

			>>> p1()
				(1, 2, 3)
				{}
			>>> p1(4,5,6)
				(1, 2, 3, 4, 5, 6)
				{}

			>>> p1(a='python', b='itcast')
				(1, 2, 3)
				{'a': 'python', 'b': 'itcast'}

		p2=functools.partial(showarg, a=3,b='linux')
		p2()
			()
			{'a': 3, 'b': 'linux'}
		p2(1,2)
			(1, 2)
			{'a': 3, 'b': 'linux'}
		p2(a='python', b='itcast')
			()
			{'a': 'python', 'b': 'itcast'}

	2、wraps函数

		使用装饰器时，有一些细节需要被注意。
		例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）。

		添加后由于函数名和函数的doc发生了改变，对测试结果有一些影响，例如:

		def note(func):
			"note function"
			def wrapper():
				"wrapper function"
				print('note something')
				return func()
			return wrapper
														 
		@note
		def test():
			"test function"
			print('I am test')
																		 
		test()
		print(test.__doc__)
		
		运行结果：

			note something
			I am test
			wrapper function
		
		所以，Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用。例如：

		import functools
		def note(func):
			"note function"
			@functools.wraps(func)	
			def wrapper():
				"wrapper function"
				print('note something')
				return func()
			return wrapper
													  
			@note
			def test():
				"test function"
			print('I am test')
																	  
		test()
		print(test.__doc__)
	
	运行结果:

		note something
		I am test
		test function


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

	1、json.dumps()         将Python 对象编码成JSON字符串
	
		语法：json.dumps(obj,skipkeys=False,ensure_ascii=True,check_circular=True,allow_man=True,cls=None,
						ident=None,separators=None,encoding='utf-8',default=None,sort_keys=Flase,**KW)

		实例：

			data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]
			json = json.dumps(data)
			print(json)
				[{"a":1,"c":3,"b":2,"e":5,"d":4}]


			print(json.dumps({'a':'Runoob','b':7},sort_keys=True,indent=4,sparators=(',',':')))
				{
					"a":"Runoob",
					"b":7
				}

		python 原始类型向json类型的转化对照表：

		python                        json

		dict                          object

		list,tuple                    array

		str,unicode                   string

		int long float                number

		True                          true

		Flase                         flase

		None                          null

	2、dump 必须传文件描述符，将序列化的str保存到文件中:

		语法：

			def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
				    allow_nan=True, cls=None, indent=None, separators=None,
					default=None, sort_keys=False, **kw):

			一个动作是将”obj“转换为JSON格式的字符串，还有一个动作是将字符串写入到文件中，
			也就是说文件描述符fp是必须要的参数

		实例：

			a = {"name":"Tom", "age":23}
				with open("test.json", "w", encoding='utf-8') as f:
				    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
				    f.write(json.dumps(a, indent=4))
					#json.dump(a,f,indent=4)   # 和上面的效果一样

		
	3、jsom.loads()         将已编码的JSON字符串解码为Python对象。

		语法：json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, 
						parse_constant[, object_pairs_hook[, **kw]]]]]]]])

		实例：
			
			jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

			print(json.loads(jsonData))
				{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

	4、load  只接收文件描述符，完成了读取文件和反序列化
		
		语法：

			def load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, 
					parse_constant=None, object_pairs_hook=None, **kw):
	
		实例：

			import json
			with open("test.json", "r", encoding='utf-8') as f:
			    aa = json.loads(f.read())
				f.seek(0)
				bb = json.load(f)    # 与 json.loads(f.read())
			print(aa)
			print(bb)


	5、使用第三方库：Demjson

		Demjson 是python第三方库，可用于编码和解码JSON数据，包含了JSONLint的格式化及校验功能。
	
		安装：
			pip install demjson
	
		JSON 函数：

			encode        将python对象编码成json字符串

				语法：demjson.encode(self,obj,nest_level=0)

				实例：	import demjson
						data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]
						json = demjson.encode(data)
						print(json)
							[{"a":1,"b":2,"c":3,"d":4,"e":5}]

			decode        将已编码的json字符串解码为python对象

				语法：	demjson.decode(self, txt)
				实例： import demjson
					   json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
					   print(demjson.decode(json))
	6、pickle 模块：

		json模块和pickle模块都有  dumps、dump、loads、load四种方法，而且用法一样。

		不用的是json模块序列化出来的是通用格式，其它编程语言都认识，就是普通的字符串，
		而picle模块序列化出来的只有python可以认识，其他编程语言不认识的，表现为乱码
		不过picle可以序列化函数，但是其他文件想用该函数，在该文件中需要有该文件的定义
		（定义和参数必须相同，内容可以不同）

		pickle模块能够让我们直接在文件中存储几乎任何python对象的高级工具，
		也并不要求我们把字符串转换来转换去。
		它就像是超级通用的数据格式化和解析工具。例如，想在文件中存储字典
		
		存:
			D = {'a':1,'b':2}
			F = open('/home/zhangkun/myfile.pkl','wb')
			import pickle
			pickle.dump(D,F)
			F.close()

		取：
			F = open('/home/zhangkun/myfile.pkl','rb')
			E = pickle.load(F)
				{'a': 1, 'b': 2}
	
	8、shelve

		pickle：任意python对象和字节串直接的序列化
		dbm:实现一个通过键访问的文件系统，存储字符串
		shelve:使用pickle，dbm按照键把python对象存储到文件中。
		pickle模块是一种非常通用的对象格式化和解格式化工具。
		shelve模块提供了一个额外的层结构，允许按照键来存储pickle处理处理后的对象。
	
		实际上，一个shelve提供了一个简单的数据库来按照键存储和获取本地的python对象，
		并由此使它们跨程序运行而保持持久化。它不支持SQL这样的查询语句，
		并缺乏在企业数据库中可用的某些高级功能(真正事务处理)
		但是，一旦使用键获取了存储在shelve中的本地python对象，
		就可以使用python语言的所有功能处理他。


		在shelve数据库中存储对象：
		
		一旦有了实例，将它们存储到shelve中简直是小菜一碟，直接导入shelve模块，
		用外一个文件打开一个新的shelve,
		把对象赋给shelve中的键，当我们操作完毕后关闭shelve，因为已经做过修改：

		from person import Person,Manager
		bob = Person('Bob Smith')
		sue = Person('Sue Jones',job = 'dev',pay = 100000)
		tom = Manager('Tom Jones',5000)
		
		import shelve
		db = shelve.open('persondb')
		for object in (bob,sue,tom):
			db[object.name] = object
		db.close()

		在shelve中，键可以是任何字符串，唯一的规则是必须唯一。文件的后缀是".db"

		这里交互的模式有效的成为一个数据库客户端：
		import shelve
		db = shelve.open('persondb')
		
		len(db)
			3
		list(db.keys())
			['Tom Jones','Sue Jones',"Bob Smith"]
		
		bob = db['Bob Smith']
		print(bob)
			[Person:job= None,name=Bob Smith,pay=0]
		
		for key in db:
			print(key,'=>',db[key])
			
		Tom Jones => [Manager:job=mgr,name=Tom Jones,pay=50000]
		Sue Jones => [Person: job=dev,name=Sue,pay=100000]
		Bob Smith => [Person: job=None,name=Bob Smith,apy=0]


"---------------------------------------------------------------------------------"

logging            记录日志，调试

简单配置

	1、日志级别：

		级别                  使用说明

		DEBUG                详细信息，典型地调试问题时会感兴趣

		INFO                 证明事情按预期工作

		WARNING              表明发生了一些意外，或者不久将来会发生的问题，软件还在正常工作

		ERROR                由于更严重的问题，软件不能执行一些功能

		CRITICAL             严重错误，表明软件已经不能继续运行了

	
	2、几个比较重要的概念：Logger、Handler、Formatter、Filter
		
	Logger 记录器，暴露了应用程序代码能直接使用的接口。
	
		Logger是一个树形层级结构，在使用接口debug,info,warn,error,critical之前必须创建Logger实例，
		即创建一个记录器，如果没有显示的进行创建，则默认创建一个root logger,并应用默认的日志级别
		（WARNING）,处理器Handler(StreamHandler,即将日志信息打印输出在标准输出上)
		和格式化Formatter(默认格式)

		创建方法：
			logger = logging.getLogger(logger_name)

		创建logger实例后，可以使用下面方法进行日志级别设置，增加处理器Handler.
		设置日志级别，只有日志级别大于等于ERROR的日志才会输出：
			logger.serLevel(logging.ERROR) 

		为Logger实例增加一个处理器：
			logger.addHandler(handler_name)

		为Logger实例删除一个处理器：
			logger.removeHandler(handler_name)


	Handler 处理器，将（记录生产的）日志记录发送至合适的目的地。
		
		Handler处理器类型有很多种，比较常用的有三个：StreamHandler,FileHandler,NullHandler.

		创建处理器的方法：

		StreamHandler:
			
			sh = logging.StreamHanler(stream=None)
	
		FileHandler:
			
			fh = logging.FileHandler(filename,mode='a',encoding=None,delay=False)

		NullHandler:

			NullHandler 类位于核心logging包，不做任何的格式化或者输出。
			本质上它是什么都不做的handler

		创建处理器之后，通过下面方法设置日志级别，设置格式化器Formatter，增加或删除过滤器Filter.

			设置日志级别：

				ch.setLevel(logging.WARN) 
			 
			设置一个格式化器:

				ch.setFormatter(formatter_name)
		
			增加一个过滤器：
				
				ch.addFilter(filter_name)

			删除一个过滤器：

				ch.removeFilter(filter_name)


	Filter 过滤器，提供了更好的粒度控制，它可以决定输出那些日志记录。
		
		Handlers 和Loggers 可以使用Filter来完成比较复杂的过滤。
		Filter基类只允许特定Logger层次一下的事件。

		创建方法：filter = logging.Filter(name='')

	
	Formatter 格式化器，指明了最终输出中日志记录的布局。
	
		使用Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为
		%Y-%m-%d %H:%M:%S。

		创建方法：

			formatter = logging.Formatter(fmt=None,datefmt=None)
		
		其中，fmt是消息的格式字符串，datefmt是日期字符串。如果不指名fmt，将使用"%(message)s".

	Logger是一个树形层级结构，Logger可以包含一个或多个Handler和Filter,即Logger与Handler或Filter
	是一对多的关系。

	
logging模块使用：


1、配置logging基本的设置，然后在控制台输出日志：

	import logging

	logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	函数basicConfig()函数直接进行配置，basicConfig关键字参数如下：

		关键字              描述
		filename        创建一个FileHandler，使用指定的文件名，而不是使用StreamHandler

		filemode		如果指明了文件名，指明文件的打开模式（如果没有指明filemode,默认为'a'）

		format          hanler使用指明的格式化字符串         

		datefmt         使用指明的日期/时间格式

		level           指明logger的级别

		stream  使用指明的流来初始化StreamHandler，该参数与filename不兼容，如果两者都有，'stream'被忽略


	有用的format格式：

			格式                   描述

		%(levelno)s              打印日志级别的数值

		%(levelname)s            打印日志级别名称
		
		%(pathname)s             打印当前执行程序的路径

		%(filename)s             打印当前执行程序的名称
		
		%(funcName)s             打印日志的当前函数
		
		%(lineno)d               打印日志的当前行号
		
		%(asctime)s              打印日志的世界
		
		%(thread)d               打印线程id
		
		%(threadName)s           打印线程名称

		%(process)d              打印进程ID

		%(message)s              打印日志信息

		
	logger = logging.getLogger(__name__)
	
	logger.info("Start print log")
	logger.debug("Do something")
	logger.warning("Something maybe fail.")
	logger.info("Finish")

		2018-08-20 15:04:44,557 - __main__ - INFO - Start print log
		2018-08-20 15:04:44,558 - __main__ - DEBUG - Do something
		2018-08-20 15:04:44,558 - __main__ - WARNING - Something maybe fail.
		2018-08-20 15:04:44,558 - __main__ - INFO - Finish
	
2、将日志写入到文件：

	设置logging,创建一个FileHandler,并对输出消息格式进行设置，
	将其添加到logger,然后将日志写入到指定的文件中。

	import logging

	logger = logging.getLogger(__name__)
	logger.setLevel(level = logging.INFO)

	handler = logging.FileHandler("log.txt")
	handler.setLevel(logging.INFO)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	logger.info("Start print log")
	logger.debug("Do something")
	logger.warning("Something maybe fail.")
	logger.info("Finish")

	在log.txt中日志数据为：

		2018-08-20 15:21:49,998 - __main__ - INFO - Start print log
		2018-08-20 15:21:49,998 - __main__ - WARNING - Something maybe fail.
		2018-08-20 15:21:49,998 - __main__ - INFO - Finish

3、将日志同时输出到屏幕和日志文件

	import logging

	logger = logging.getLogger(__name__)
	logger.setLevel(level=logging.INFO)

	handler = logging.FileHandler('log.txt')
	handler.setLevel(logging.INFO)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)

	console = logging.StreamHanler()
	console.setLevel(logging.INFO)

	logger.addHandler(handler)
	logger.addHandler(console)

	logger.info("Start print log")
	logger.debug("Do something")
	logger.warning("Something maybe fail.")
	logger.info("Finish")


4、可以发现，logging有一个日志处理的主对象，其他处理方式都是通过addHandler添加进去，
	
	logging中包含的handler主要有如下几种:

	handler 名称         位置         作用

	StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
	
	FileHandler：logging.FileHandler；日志输出到文件
	
	BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
	
	RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
	
	TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
	
	SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
	
	DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
	
	SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
	
	SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
	
	NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
	
	MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
	
	HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器


5、日志回滚

	import logging
	from logging.handlers import RotatingFileHandler
	logger = logging.getLogger(__name__)
	logger.setLevel(level = logging.INFO)
	#定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
	rHandler = RotatingFileHandler("log.txt",maxBytes = 1*1024,backupCount = 3)
	rHandler.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	rHandler.setFormatter(formatter)
	 
	console = logging.StreamHandler()
	console.setLevel(logging.INFO)
	console.setFormatter(formatter)
	 
	logger.addHandler(rHandler)
	logger.addHandler(console)
	 
	logger.info("Start print log")
	logger.debug("Do something")
	logger.warning("Something maybe fail.")
	logger.info("Finish")


"------------------------------------------------------------------------------"

multiprocessing	      多进程

os.fork:

	pid = os.fork()
	if pid<0:
		失败
	elif pid==0:
		子进程
	else:
		父进程

	os.getpid()   当前进程的进程号
	os.getppid()  父进程的进程号

multiprocessing:

	1、Pricess 类
	
		Process 类用来描述一个进程对象。创建子进程的时候，只需要传入一个执行函数和
		函数的参数即可完成Process实例的创建。

		Process语法结构如下:
		p = Process([group [, target [, name [, args [, kwargs]]]]])
		
			target：表示这个进程实例所调用对象；

			args：表示调用对象的位置参数元组；

			kwargs：表示调用对象的关键字参数字典；

			name：为当前进程实例的别名；

			group：大多数情况下用不到；


		Process类常用方法：
	
			p.is_alive()：判断进程实例是否还在执行；

			p.join([timeout])：是否等待进程实例执行结束，或等待多少秒；

			p.start()：启动进程实例（创建子进程）；

			p.run()：如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法；

			p.terminate()：不管任务是否完成，立即终止；

	2、Pool类

		常用函数解析：
		po = Pool(n)  #最大进程数为n

		po.apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func
			（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），
			args为传递给func的参数列表，kwds为传递给func的关键字参数列表；

		po.apply(func[, args[, kwds]])：使用阻塞方式调用func

		po.close()：关闭Pool，使其不再接受新的任务；

		po.terminate()：不管任务是否完成，立即终止；

		po.join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；


	3、Queue类

		q = Queue() #若括号中没有指定最大可接收的消息数量，
					或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；

		q.qsize() : 返回当前队列包含的消息数量

		q.empty() : 如果队列为空,返回True,反之返回False

		q.full()  : 如果队列满了，返回True,反之返回False

		q.get(block,timeout): 获取队列中的一条消息，然后将其从列中移除.
					如果block默认为True,直到从消息队列中读到消息为止，如果设置了timeout，则等待timeout秒
					若还没有读到任何消息，则抛出Queue.emoty异常
					如果block为False,消息队列为空，立刻抛Queue.Empty异常

		q.get_nowait():想当于q.get(false)

		q.put(item,block,timeout):将消息item写入到队列，block默认值为Ture
					如果block默认值为Ture,消息队列中如果已经没有空间可以写了，此时程序将被阻塞，直到
					从消息队列腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没有空间
					则抛Queue.Full异常。
					如果block默认值为False,消息队列如果没有空间可写，则会立刻抛出Queue.Full异常
		
		q.put_nowait(item): 相当于q.put(false)


	4、Manager类：

		如果使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue(),而不是Multiprocessing.Queue().
		否则报错：
			RuntimeError: Queue objects should only be shared between processes through inheritance.
	
		from multiprocessing import Manager,Pool

		q = Manager().Queue()
		
		po = Pool()

		po.apply(writer,(q,))
		po.apply(reater,(q,))


"-------------------------------------------------------------------------------"

threading	          多线程

1、Thread:

	创建线程实例，启动线程：
	t = threading.Thread(target=,args=(,))
	t.start()
	
	
	查看正在运行线程数量：
	threading.enumberate()

	返回当前线程变量：
	threading.currentThread()

2、Lock：

	创建锁：
	mutex = threading.Lock()

	锁定：
	mutexFlag = mutex.acquire([blocking])
	
	if mutexFlag:
		等待锁释放

	释放：
	mutex.release()

	其中acquire可以有一个blocking参数，
	如果设定blocking为true,则当前线程阻塞，知道获取这个锁为止。
	如果设定blocking为false,则当前线程不会阻塞。


	例子：

	mutex = Threading.Lock()
	def test1():
		global g_num
		for i in rang(10000):
			mutexFlag = mutex.acquire(True)
			if mutexFlag:   #得到锁
				g_num +=1
				mutex.release()  #释放


"-----------------------------------------------------------------------------"

copy	               拷贝

1、deepcopy()          深拷贝


2、copy()              拷贝


例子：

	a = [[1],[2],[3]]

	b = copy.copy(a)

		拷贝的只是引用。

	c = copy.deepcopy(a)
		
		拷贝了内存一块内存空间


	a[1].append(0)

	a
		[[1], [2, 0], [3]]
	b
		[[1], [2, 0], [3]]
	c
		[[1], [2], [3]]

"-------------------------------------------------------------------------------"

time	               时间

	1、time.tiem()				时间戳

	2、time.localtime()		    时间元组

	3、time.asctime()           格式化最简单的获取可读的时间模式的函数

	4、time.strftime(format[,t]) 格式化日期

	5、time.clock()              用以浮点数计算的秒数返回当前的CPU时间

	6、time.ctime([secs])        作用相当于asctime(localtime(secs))

	7、time.sleep(secs)          推迟调用线程的运行

	8、time.mktime(tupletime)    接受时间元组并返回时间戳

	9、time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')  根据fmt的格式把一个时间字符串解析为时间元组。

"-------------------------------------------------------------------------------"

datetime	        日期和时间

	datetime模块定义了5个类，分别是：
	
	1、datetime.date :表示日期的类
		
		静态方法和字段：
			date.max、date.min：date对象所能表示的最大、最小日期；
			date.resolution：date对象表示日期的最小单位。这里是天。
			date.today()：返回一个表示当前本地日期的date对象；
			date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；

			from datetime import *
			import time

			print   'date.max:', date.max
			print   'date.min:', date.min
			print   'date.today():', date.today()
			print   'date.fromtimestamp():', date.fromtimestamp(time.time())
																	  
			Output==============
			date.max: 9999-12-31
			date.min: 0001-01-01
			date.today(): 2016-10-26
			date.fromtimestamp(): 2016-10-26

		方法和属性：

			d1 = date(2011,06,03)#date对象
			d1.year、date.month、date.day：年、月、日；
			d1.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替
										  原有对象中的属性。（原有对象仍保持不变）
			d1.timetuple()：返回日期对应的time.struct_time对象；
			d1.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
			d1.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
			d1.isocalendar()：返回格式如(year，month，day)的元组；
			d1.isoformat()：返回格式如'YYYY-MM-DD’的字符串；
			d1.strftime(fmt)：和time模块format相同。'
	
	2、datetime.time:表示时间的类
		
		datetime.time(hour[,minute[,second[,microsecond[,tzinfo]]]]) 
		
		静态方法和字段：
			time.min、time.max：time类所能表示的最小、最大时间。
			其中，time.min = time(0, 0, 0, 0)， 
			time.max = time(23, 59, 59, 999999)；
			
			time.resolution：时间的最小单位，这里是1微秒；

		方法和属性：

			t1 = datetime.time(10,23,15)  #time对象
			t1.hour、t1.minute、t1.second、t1.microsecond：时、分、秒、微秒；
			t1.tzinfo：时区信息；
			t1.replace([ hour[,minute[,second[,microsecond[,tzinfo]]]]])：
					创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性
					（原有对象仍保持不变）；
			t1.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
			t1.strftime(fmt)：同time模块中的format。

	3、datetime.datetime:表示日期时间的类
		
		datetime相当于date和time结合起来。
		datetime.datetime (year, month, day[,hour[,minute[,second[,microsecond[,tzinfo]]]]])
		
		静态方法和字段:
			
			datetime.today()：返回一个表示当前本地时间的datetime对象；
			datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，
								则获取tz参数所指时区的本地时间；
			datetime.utcnow()：返回一个当前utc时间的datetime对象；#格林威治时间
			datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
			datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
			datetime.combine(date, time)：根据date和time，创建一个datetime对象；
			datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；
		
		方法和属性:

			dt=datetime.now()#datetime对象
			dt.year、month、day、hour、minute、second、microsecond、tzinfo：
			dt.date()：获取date对象；
			dt.time()：获取time对象；
			dt.replace([year[,month[,day[,hour[,minute[,second[,microsecond[,tzinfo]]]]]]]])：
			dt.timetuple ()
			dt.utctimetuple ()
			dt.toordinal ()
			dt.weekday ()
			dt.isocalendar ()
			dt.isoformat ([ sep] )
			dt.ctime ()：返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
			dt.strftime (format)


	4、datetime.timedelta:表示时间间隔，即两个时间点的间隔,时间加减
		
		dt = datetime.datetime.now()
		#日期减一天
		dt1 = dt + timedelta(days=-1)#昨天
		dt2 = dt - timedelta(days=1)#昨天
		dt3 = dt + timedelta(days=1)#明天
		delta_obj = dt3-dt


		dt = datetime.datetime.now()
			2018-08-21 18:15:38.331288
		dt1 = dt + datetime.timedelta(days=-1)
			2018-08-20 18:15:38.331288
		dt2 = dt - datetime.timedelta(days=1)
			2018-08-20 18:15:38.331288
		dt3 = dt + datetime.timedelta(days=1)
			2018-08-22 18:15:38.331288


	5、datetime.tzinfo:时区的相关信息
		
		tzinfo是关于时区信息的类
		tzinfo是一个抽象类，所以不能直接被实例化

"------------------------------------------------------------------------------"

calendar	           日历

	1、calendar.calendar(year,w=2,l=1,c=6)  
	
			返回一个多行字符串格式的year年年历
			3个月一行，间隔距离为c。每日宽度间隔为w字符。
			每行长度为21* W+18+2* C。l是每星期行数。
											
	2、calendar.month(year,month,w=2,l=1)  
	
			返回一个多行字符串格式的year年month月日历

	3、calendar.monthrange(year,month)  
			
			返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。
			日从0（星期一）到6（星期日）;月从1到12。
	
	4、calendar.isleap(year)
			
			是闰年返回True,否则返回False

	5、calendar.leapdays(y1,y2)

			当y1和y2两个年份之间闰年总数
		

"-----------------------------------------------------------------------------"

hashlib	            加密算法
	
	python 中的hashlib模块用来进行hash或者md5加密，这里的加密，其实并非我们通常
	所说的加密，简单的来说，这种加密一般是不可逆的，这种加密实际上是被称为"摘要算法"
	包括MD5、SHA1等等，MD5的全称是Message-Digest Algorithm 5(信息-摘要算法)
	SHA1是Secure Hash Algorithm(安全哈希算法)。SHA1基于MD5,加密后数据长度更长。

	那么什么是摘要算法呢？摘要算法又称哈希算法、散列算法。
	它通过一个函数，把任意长度的数据转换为一个长度固定的数据串(通常用16进制字符串表示)
	摘要算法就是通过摘要算法f(),对任意长度的数据data计算固定长度的摘要digest。摘要算法
	可以用来检验数据是否改变。

	摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)
	很容易，但是digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算
	出的摘要完全不同。

	hashlib是个摘要算法相关的操作，里面包括md5、sha1、sha224、sha226、sha384、sha512。
	代替了原来的md5和sha模块。

	hashlib是一个摘要算法库，不是加密，加密是可以解码的，摘要算法不可逆向，用于文件校验，密码转换等。
	SHA的用法比MD5一样，但是会比MD5更安全，但是效率也更低。


	1、方法：

		new(name,string='')    创建指定加密模式的hash对象
			
			d= hashlib.new('md5','ddd'.encode('utf-8'))
			print(d.hexdigest())

	2、update(arg)     更新哈希对象以字符串参数
			
			hash = haslib.md5()
			hash.update('admin'.encode('utf-8'))
			hash.hexdigest()

	3、digest()        返回摘要，作为二进制数据字符串


	4、hexdigest()     返回摘要，作为十六进制数据串
			
		
	5、密码验证，由于hashlib摘要加密不能反解，只能正解比较是否相等。

例子：

	1、md5 加密:

		hash = hashlib.md5()
		hash.update('admin'.encode('utf-8'))
		print(hash.hexdigest())
		21232f297a57a5a743894a0e4a801fc3

	2、sha1加密
		
		hash = hashlib.sha1()
		hash.update('admin'.encode('utf-8'))
		print(hash.hexdigest())
		d033e22ae348aeb5660fc2140aec35850c4da997

	3、sha256加密
		
		hash = hashlib.sha256()
		hash.update('admin'.encode('utf-8'))
		print(hash.hexdigest())
		8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918

	4、sha384加密
		
		hash = hashlib.sha384()
		hash.update('admin'.encode('utf-8'))
		print(hash.hexdigest())
		9ca694a90285c034432c9550421b7b9dbd5c0f4b6673f05f6dbce58052ba2
		0e4248041956ee8c9a2ec9f10290cdc0782

	5、sha512加密
		
		hash = hashlib.sha512()
		hash.update('admin'.encode('utf-8'))
		print(hash.hexdigest())
		c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd4726
		34dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec

加盐加密：

	上面的算法虽然很厉害，但是仍然有缺陷，通过装库可以反解，所以必须要对加密算法
	中添加自定义key再来做加密。

	md5加密:

		hash = hashlib.md5('python'.encode('utf-8'))
		hash.update('admin'.encode('utf-8'))
		print(hash.hexdigest())
			75b431c498b55557591f834af7856b9f
	
	hmac加密：不可逆键值对方式加密
		
		hmac内部对我们创建的key和内容进行处理后再加密

		import hmac

		h = hmac.new('python'.encode('utf-8'))
		h.update('helloworld'.encode('utf-8'))
		print(h.hexdigest())
			b3b867248bb4cace835b59562c39fd55


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

	1、表示字符 :

		.             匹配任意一个字符（除\n）

		[]            匹配[]中列举的字符

		\w            匹配单词字符，即a-z,A-Z,0-9   
		
		\W            匹配非单词

		\s            匹配空白，即空格、table键

		\S            匹配非空白
 
		\d            匹配数字，即0-9

		\D            匹配非数字，即不是数字


	2、数量

		*             匹配前一个字符出现0次或无数次

		+             匹配前一个字符至少出现一次

		?             匹配前一个字符出现1次或0次

		{m}           匹配前一个字符出现m次

		{m,n}         匹配前一个字符出现从m到n次

		{m,}          匹配前一个字符至少出现m次


	3、边界：

		^            匹配字符串开头

		$            匹配字符串结尾

		\b           匹配一个单词的边界

		\B           匹配非单词的边界

	4、匹配分组：

		|            匹配左右任意一个表达式

		(ab)         将括号中字符串作为一个分组

		\num         引用分组num匹配到的字符串

		(?p<name>)   分组起别名

		(?P=name)    引用别名为name分组匹配到的字符串


	5、python 交互

		import  re

		a、 ret=re.match(r'正则表达式'，'string')     从开头匹配
			ret.group()                               提取匹配到的内容          
		
		b、	ret=re.search(r'正则表达式','string')    全局匹配，只匹配一个
			ret.group()

		c、 ret=re.findall(r'正则表达式'，'string')   查找所有，返回一个列表
			pirnt(ret)

		d、	ret=re.findter(r'正则表达式'，'string')      查找所有，返回一个迭代器
			for i in ret:
		
		e、	re.sbu(r'正则表达式','替换内容'，'string')

			例1：ret = re.sbu(r"\d+",'998','python = 997')
				print(ret)
					python = 998

			例2：def add(temp):
					strNum = temp.group()
					num = int(strNum) + 1
					return str(num)

				ret = re.sub(r"\d+",add,"python = 997")
				print(ret)
					python = 998

		f、	re.split(r"","string")
			ret = re.split(r":| ","info:xiaoZhang 33 shandong")
			pirnt(ret)

				['info','xiaoZhang','33','shangdong']

	

"-----------------------------------------------------------------------------------------"

socket	        标准的 BSD Sockets API

from socket import *

UDP:

	1、客户端：

		udp = socket(AF_INET,SOCKET_DGRAM)

		udp.sendto(sendData,Addr)

		udp.recvfrom(1024)

		udp.close()

	2、服务器：

		udp = socket(AF_INEF,SOCKET_DGRAM)

		udp.bind(Addr)

		recvData = udp.recvfrom(1024)

		udp.sendto(recvData[0],recvData[1])    recvData[1] 客户端的ip和端口

		udp.close()

		
TCP:

	1、客户端

		tcp = socket(AF_INET,SOCKET_STREAM)
		
		tcp.connetc(Addr)

		tcp.send(sendData)

		tcp.recv(1024)

		tcp.close()


	2、服务器

		tcp = socket(AF_INET,SOCKET_STREAM)

		tcp.bind(Addr)

		tcp.listen(10)

			client,addr = tcp.accept()
			recvData = clent.recv(1024)
			clent.send(recvData)
			clent.close()
		tcp.close()


SELECT:
	
例1：

	tcp = socket(AF_INET,SOCKET_STREAM)
	tcp.bind(Addr)
	tcp.listen(10)

	imputs = [tcp,sys.stdin]

	running = True

	while True:

		调用select函数，阻塞等待
		readable,writeable,exceptional = select(inputs,[],[]) 

		数据抵达，循环
		for sock in readable:
			监听到有新的连接
			if sock == tcp:
				conn,addr = tcp.accept()
				inputs.append(conn)

			监听到有键盘输入
			elif sock == sys.stdin:
				cmd = sys.stdin.readline()
				running = False
				break

			有数据抵达
			else：
				data = sock.recv(1024)
				if data:
					sock.send(data)
				else:
					imputs.remove(sock)
					sock.close()
		
		if not running:
			break

	tcp.close()


例2：

	import Queue
	form select import select
	form socket import *

	保存客户端发送过来的消息，将消息存放到队列中
	
	message_queue = {}
	inputs = []
	outputs = []

	if __name__ == '__main__':

		tcp = socket(AF_INET,SOCK_STREAM)
		tcp.bind()
		tcp.listen(10)
		inputs.append(tcp)

		while True:
			readable,writeable,exceptional = select(inputs,outputs,[])
			
			for sock in readable:

				if sock == tcp:

					conn,addr = sock.accept()
					inputs.append(conn)
					message_queue[conn] = Queue.Queue()

				else:

					try:

						recvData = sock.recv(1024)
					
						if recvData:
							message_queue[sock].put(recvData)

							if sock not in outputs:
								outputs.append(sock)

					except ConnectionResetError:
						inputs.remove(sock)
						del message_queue[sock]

		for sock in outable:
			try:
				if not message_queue[sock].empty():
					send_data = message_queue[sock].get()
					sock.send(send_data)
				else:
					outputs.remove(sock)

			except ConnectionResetError:

				del message_queue[sock]
				outputs.remove(sock)

	
I/O多路复用：SELECT

	通过上面的，只是用到一个函数 select.select()
	while True:
		readable, writable, exceptional = select.select(inputs, outputs,inputs)
						
	对reable,writeable 列表循环,对应reable列表中的值有两种情况：
		for sock in reable:

			if sock == tcp:  
				这是一个新来的链接,需要接受链接，放到inputs列表中

			else:
				这是一个已经存在的类别，需要接受数据
				recvData = sock.recv(1024)
				
				if recvData:
					如果数据不为空，则存放到这个链接对应的队列中
					这个队列存放到outputs列表中
				else:
					如果这个接受到的数据为空，
					则删除这个链接对应在列表中的文件描述符。

		for sock in writeable:

			if 链接对应的队列中数据：
				存在，则得到数据，发送数据

			else:
				不存在数据，删除链接对应的输出列表中的文件描述符

EPOLL:

	import select
	from socket import *

	s = socket(AF_INET,SOCK_STREAM)
	s.bind()
	s.listen()

	创建一个epoll对象
	epoll = select.epoll()

	注册事件到epoll中
	epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

	connections={}
	addresses={}

	while True:

		epoll进行fd扫描
		epoll_list = epoll.poll()

		对事件进行判断
		for fd,event in epoll_list:
			
			如果fd是sock创建套接字
			if fd == s.fileno():
				conn,addr = s.accept()

				connections[conn.fileno()] =conn
				address[conn.fileno()] = addr

				向epoll中注册链接socket事件
				epoll.register(conn.fileno(),select.EPOLLIN|select.EPOLLET)

			elif events == select.EPOLLIN:
				
				recvData = connection[fd].recv(1024)

				if len(recvData) > 0:
					print(recvData)
				else:
					epoll.unregister(fd)
					
					connection[fd].close()



I/O多路EPOLL:

	import select
	1、创建一个epoll对象：

		epoll = select.epoll()
	
	2、注册事件到epoll中

		epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

	3、移除：
		
		epoll.unregister(fd)

	4、epoll进行fd扫描

		epoll_list = epoll.poll()

	5、事件进行判断

		for fd,event in epoll_list:

		if fd = s.fileno():	是一个新来的链接

		elif events == select.EPOLLIN:

			取得数据
			recvData = connection[fd].recv(1024)

	6、说明：

		EPOLLIN （可读）
		EPOLLOUT （可写）
		EPOLLET （ET模式）
		
		epoll对文件描述符的操作有两种模式：LT（level trigger）和ET（edge trigger）。
		LT模式是默认模式，LT模式与ET模式的区别如下：

		LT模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。
		下次调用epoll时，会再次响应应用程序并通知此事件。

		ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。
		如果不处理，下次调用epoll时，不会再次响应应用程序并通知此事件。


gevent	            基于协程的Python网络库

协程gevent:

	gevent的使用

	def f(n):
		for i in range(n):
			print gevent.getcurrent(), i

	g1 = gevent.spawn(f, 5)
	g2 = gevent.spawn(f, 5)
	g3 = gevent.spawn(f, 5)
	g1.join()
	g2.join()
	g3.join()

	

	tcp中使用：

	import sys
	import time
	import gevent

	from gevent import socket,monkey
	monkey.patch_all()

	def handle_request(conn):
		while True:
		data = conn.recv(1024)
		if not data:
			conn.close()
			break
		print("recv:", data)
		conn.send(data)


	def server(port):
		s = socket.socket()
		s.bind(('', port))
		s.listen(5)
		while True:
			cli, addr = s.accept()
			gevent.spawn(handle_request, cli)

	if __name__ == '__main__':
	server(7788)


	
异步socket处理器：asyncore:

	该模块提供了异步socket服务客户端和服务器的基本架构.
	
	只有两种方式让程序在单个处理器上同时做超过一件事情，多线程是最简单，最普遍的方式。
	但还有另一种非常不同的技术，可以让你具有多线程几乎所有的优点，实际上并没有使用多线程。
	如果您的程序主要受I/O限制，那么它真的很实用。如果您的程序受处理器限制，
	那么使用多线程可能就是您真正需要的。但是，网络服务器很少受处理器限制。

	如果您的操作系统支持I/O库的select()系统调用（一般都支持），那么你可以使用它
	同时处理多个通信信道做其他的工作的同时让I/O在后台执行，这比多线程更容易理解。

	该asyncore模块为您解决了许多难题，使得构建复杂的高性能网络服务器和客户端的任务变得轻而易举。
	对于“会话”应用程序和协议，配套asynchat 模块非常有用。
	asyncore和asynchat两个模块的基本思路是创建一个或多个网络通道，即asyncore.dispatcher
	和asynchat.async_chat的实例。然后添加到全局映射，如果你没有创建自己的映射，可以直接使用loop()函数。
	loop()激活所有通道服务，执行直到最后一个通道关闭。

	asyncore.loop([timeout[, use_poll[, map[, count]]]])
	
		进入轮询循环直到所有打开的通道已被关闭或计数通过。所有的参数都是可选的。
		
		count参数：默认为None,只有当所有通道都关闭时循环才终止。
		
		timeout参数：设置为select()或poll()调用超时时间，以秒为单位，默认30秒

		use_poll参数：如果为true,则表示poll()优先于select(),默认为false。

		map参数:监听的channel的字典，channcle关闭时会从map中删除，不知道map会使用全局map。


	类asyncore.dispatcher:

		dispatcher：是一个底层socket的轻便包装类，类中有几个方法处理异步循环调用的事件处理非常有用，
		另外，它可以被视为普通的非阻塞套接字对象。
		
		在某些时间或在某些连接状态下触发低级事件会告诉异步循环已发生某些更高级别的事件。
		例如，如果我们要求套接字连接到另一个主机，我们就知道当套接字第一次变为可写时已经建立了连接
		（此时你知道你可以写信给它，期望成功）。隐含的更高级别事件是：

			事件					描述
			handle_connect()	第一个读或写事件暗示
			handle_close()		由没有数据可用的读取事件隐含
			handle_accept()		隐藏在侦听套接字上的读取事件
	

		在异步处理，每个映射通道的readable()和writable()方法用于确定通道的
		socket是否应该被添加到select()或poll()通道的频道列表中以读写事件。
		因此通道事件比基本socket 事件要多。在子类中重写的方法如下：

		
			handle_read()：当异步循环检测到通道的read()将成功时调用。
			handle_write()：当异步循环检测到通道的write()将成功时调用。需要缓冲以提高性能
			handle_connect()：当活动socket实际创建连接时调用。可能发送“welcome” banner，
							  或与远程端点启动协议协商。				
			handle_close()：当关闭socket时调用。
			handle_error()：当异常引发又没有其他处理时调用。默认版本print压缩的traceback。
			handle_accept()：监听通道(被动开启) ，当本端通过connect()可以和
							 远端建立连接时在监听通道(被动开启)上调用。
			readable():每次异步循环时调用，以确定通道的socket是否应该被添加到产生读事件列表。
						默认的方法只返回True，表示在默认情况下，所有通道将拥有读取事件。
			writable()：每次异步循环时调用，以确定通道的socket是否应该被添加到产生写事件列表。
						默认的方法只返回True，表示在默认情况下，所有通道将拥有写事件。

	类asyncore.dispatcher_with_send:
		
		一个dispatcher子类，它添加了简单的缓冲输出功能，对简单客户端很有用。
		用于更复杂的使用 asynchat.async_chat。

	类asyncore.file_dispatcher:
		
		封装了文件描述符或文件对象及映射参数(可选)供poll()和loop()函数使用的文件分发器。
		它提供了文件对象或其他具备fileno()方法的对象，调用fileno()并传递到file_wrapper构造函数。可用于UNIX。

	class asyncore.file_wrapper：
		
		接收整数文件描述符并调用os.dup()复制句柄，这样原句柄可以关闭，
		而文件包装器不受影响。该类封装了大量方法以模拟socket给file_dispatcher类使用。可用于UNIX。
		

	客户端实例：

		这是一个非常基本的HTTP客户端，它使用dispatcher该类来实现其套接字处理：

		import asyncore, socket
		class HTTPClient(asyncore.dispatcher):
			
			def __init__(self, host, path):
				asyncore.dispatcher.__init__(self)
				self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
				self.connect( (host, 80) )
				self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path

			def handle_connect(self):
				pass

			def handle_close(self):
				self.close()

			def handle_read(self):
				print self.recv(8192)

			def writable(self):
				return (len(self.buffer) > 0)

			def handle_write(self):
				sent = self.send(self.buffer)
				self.buffer = self.buffer[sent:]

		client = HTTPClient('www.python.org', '/')
		asyncore.loop()
			

	echo server:

		import asyncore,socket
		import socket

		
		class EchoHandler(asyncore.dispatcher_with_send):
			def handle_read(self):
				data = self.recv(8192)
				if data:
					self.send(data)

		class EchoServer(asyncore.dispatcher):

			def __init__(self,host,port):
				asyncore.dispatcher.__init__(self)
				self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
				self.set_reuse_addr()
				self.bind((host, port))
				self.listen(5)

				def handler_accept(self):
					pair = self.accept()
					if pair is not None:
						sock, addr = pair
						print 'Incoming connection from %s' % repr(addr)
						handler = EchoHandler(sock)

		server = EchoServer('localhost',8080)
		asyncore.loop()



"-----------------------------------------------------------------------------------------"

shutil        主要作用与拷贝文件用的

	1、shutil.copyfileobj(fsrc,fdest)	将文件内容拷贝到另一个文件

		shutil.copyfileobj(open('old.xml','r'),open('new.xml','w'))

	2、shutil.copyfile(src, dst)　　（copyfile只拷贝文件内容）
		
		shutil.copyfile('f1.log','f2.log')

	3、shutil.copy(src,dst)   拷贝文件和权限

		shutil.copy('f1.log','f2.log')

	4、shutil.copy2(src,dst)  拷贝文件和状态信息

		shutil.copy2('fl.log','f2.log')

	5、shutil.copymode(src,dst) 拷贝权限，内容，组，用户均不变 （前提是dst文件存在，不然报错）
		
		shutil.copymode('f1.log','f2.log')

	6、shutil.copystat(src,dst) 
		仅拷贝状态信息，即文件属性，包括：mode bit,atime,mtime,flags

		shutil.copystat('f1.log','f2.log')

	7、shutil.ignore_patterns( *patterns) （忽视那个文件，有选择性的拷贝）
	   shutil.copytree(src,dst,symlinks=False,ignore=None)
		递归的去拷贝文件夹

		shutil.copytree('folder1','folder2',ignore=shutil.ignore_patterns('*.payc','tmp*'))

	8、shutil.rmtree(path,ignore_errors[,onerror])  递归的去删除文件

		shutil.rmtree('folder1')

	9、shutil.move('folder1','folder3')  递归的去移动文件，它类似mv命令，其实就是重命名。


	10、shutil.make_archive(base_name,format,...) 创建压缩包并返回文件路径，例如zip,tar

		base_name:压缩包的文件名，也可以是压缩包的路径，只是文件时，则保存至当前目录,否则保存到指定目录。

		format :压缩包种类，"zip","tar","bztar","gztar"

		root_dir:要压缩文件夹路径(默认当前目录)

		owner:用户，默认当前用户

		group:组，默认当前组

		logger:用户记录日志，通常是logging.Logger对象

		#将 /Users/wupeiqi/Downloads/test 下的文件打包放置当前程序目录
		ret = shutil.make_archive("www","gztar",root_dir='/Users/wupeiqi/Downloads/test')
		
		#将 /Users/wupeiqi/Downloads/test 下的文件打包放置 /Users/wupeiqi/目录.
		ret = shutil.make_archive("/Users/wupeiqi/www",'gztar',root_dir='/Users/wupeiqi/Downloads/test')
		


"----------------------------------------------------------------------------------------"

glob	       基于文件通配符搜索

	glob模块是用来查找文件目录和文件，常用的两个方法由glob.glob()和glob.iglob()
	可以用find功能进行类比，glob支持*?[]这三种通配符。

	1、glob.glob:

		import glob
		filelist = glob.glob(r'./*.py') 
	
			for file in filelist:
			返回的数据类型是list:
				./module-04.py
				./module-03.py
				./module-01.py
				./module-02.py

		filelist = glob.glob(r'*.py')
			for file in filelist:
				module-04.py
				module-03.py
				module-01.py
				module-02.py

	2、glob.iglob: 与glob类似，只是这里返回值为迭代器，对于大量文件是更省内存

		import glob

		f = glob.iglob(r'../*.py')
		
		for py in f:
			print(py)

"---------------------------------------------------------------------"

数据库：

redis:	                

python 库：redis

	import redis
	
	1、普通链接：
		try:
			r = redis.StrictRedis(host=ip,port)
		except Exception:
			print()
		
		r.set()
		r.get()

	2、连接池：
	
		
		pool = redis.ConnectionPool(host=ip,port)

		r = redis.StrictRedis(connection_pool=pool)

		r.set()

		r.get()


mysql:	    

python MySQLdb

	import MySQLdb 

	1、connection对象：
		
		conn = MySQLdb.connect(host,port,db,user,password,charset)

		方法：
		conn.cursor()
		conn.commit()
		conn.rollback()
		conn.close()

	2、Cursor对象：

		cursor = conn.cursor()

			cursor.close()
			cursor.execute()
			cursor.fetchone()
			cursor.fetchall()
			cursor.next()    执行查询语句时，获取当前行的下一行
			cursor.scroll(value,[,move])  将行指针移动到某个位置
				mode 表示移动的方式
				mode的默认值为reltive，表示基于当前行移动到value,value为正则向下移动，value为负则向上移动。
				mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0
				
mongodb:


import pymongo
from pymongo import MongoClient

	1、链接Mongodb库

		client = pymongo.MongoClient('localhost',27017)


	2、得到数据库

		db = client.数据库名

	3、得到集合

		collection = db.集合名

	4、添加数据

		s1 = {
			'name':'gj'
			"age":18}

		s1_id = collection.insert_one(s1).inserted_id

	5、查找一个文档

		s2 = collection.find_one()

	6、查找多个文档

		第一种方式：
			for cur in collection.find()
				print(cur)

		第二种方式：

			cur = collection.find()
			cur.next()
			cur.next()

	7、获取文档数

		print(collection.count())
			
"------------------------------------------------------------------------------------------"

traceback： 
	
	用于提取，格式化和打印Python程序的堆栈跟踪。
	它在打印堆栈跟踪时完全模仿了Python解释器的行为。当您想要在程序控制下打印堆栈跟踪时，
	这很有用，例如在解释器周围的“包装器”中。

	简单的异常处理可以帮助我们解决很多问题，但是随着逐渐深入，很多情况下，打印异常
	所提供的信息非常有限。

	例1：

		def func1():
			raise Exception("--func1 exception--")

		def main():

			try:
				func1()
			except Exception as e:
				print e
		if __name__=='__main__':
			main()

		结果如下：
			--func1 exception--
	
		打印的有用信息很少，如果打印更详细的信息

	第一种方式：sys.exc_info:
		
		import sys
		def func1():
			raise Exception("func1 exception")
				
		def main():
			try:
				func1()
			except Exception as e:					   
				exc_type,exc_value,exc_traceback_obj = sys.exc_info()
	
				print exc_type
			    print exc_value
				print exc_traceback_obj
							
		if __name__ == '__main__':
			main()

		结果如下：
			<type 'exceptions.Exception'>
			func1 exception
			<traceback object at 0x7fd2dadc4170>

	sys.exc_info()获取了当前处理的exception的相关信息，并返回一个元组，
	元组的第一个数据是异常的类型(示例是NameError类型)，第二个返回值是异常的value值，
	第三个就是我们要的traceback object.

	
	第二种方式：traceback object:

		Python的traceback module提供一整套接口用于提取，格式化和打印Python程序的stack traces信息，
		下面我们通过例子来详细了解下这些接口：

		1、traceback.print_tb(tb[, limit[, file]])
			
			tb:这个就是traceback object,通过sys.exc_info获取得到

			limit:这个是限制stack trace层级的，如果不设或为None,打印所有层stack trace

			file: 这个是设置打印的输出流的，可以为文件，也可以是stdout之类的file-like object。
				  如果不设或为None，则输出到sys.stderr。

			例子：
			import sys
			import traceback
			def func1():
				raise Exception("func1 exception")   
			def main():
				try:
					func1()
				except Exception as e:
					exc_type,exc_value,exc_traceback_obj = sys.exc_info)
					traceback.print_tb(exc_traceback_obj)
					traceback.print_exception(exc_type,exc_value,exc_traceback_obj,limit=2,file=sys.stdout)
	
			if __name__ == '__main__':
				main()
	
			结果：
				  File "traceback01.py", line 12, in main
				      func1()
				  File "traceback01.py", line 8, in func1
						 raise Exception("func1 exception")


		2、traceback.print_exception(etype,value,tb[,limit [file]])
			
			跟print_tb相比，多个两个参数etype和value,分别是exception type 和exception value
			加上tb(traceback object)，正好是sys.exc_info()返回的值

			另外，与print_tb相比，打印信息多了开头的"Traceback (most...)"信息以及最后一行的异常类型和value信息
			还有一个不同是当异常为SyntaxError时，会有"^"来指示语法错误的位置
		
		3、print_exc([limit[,file]])

			print_exc是简化版的print_exception, 
			由于exception type, value和traceback object都可以通过sys.exc_info()获取，
			因此print_exc()就自动执行exc_info()来帮助获取这三个参数了，
			也因此这个函数是我们的程序中最常用的，因为它足够简单

			import sys
			import traceback
			def func1():
				raise NameError("--func1 exception--")
			def func2():
				func1()
							
			def main():
				try:
					func2()
				except Exception as e:
					traceback.print_exc(limit=1, file=sys.stdout)
													   
			结果：

				Traceback (most recent call last):
					File "traceback01.py", line 12, in main
						func1()
					Exception: func1 exception


	异常由四个语句处理：

	1、try/except
		
		捕捉由python引起的异常

	2、try/finally

		无论异常是否发生，执行清理行为

	3、raise

		手动触发异常
		def func1():
			raise Exception("--func1 exception--")

	4、assert

		有条件在程序中触发异常
		def f(x):
			assert x < 0, 'x must be negative'
			return x ** 2''
			
	5、with /as

		实现环境管理器

		with open('hello.txt','r') as file

	异常对象:

	内置Exception类：

	python自身能够引发所有的内置异常，都是预定义的类对象。

	BaseException:
		异常的顶级根类。这个类不能由用户定义的类直接继承的。它提供了子类所继承的默认的打印和状态保存行为。
	
	Exception:
		这是BaseException的一个直接子类，并且是所有其他内置异常的超类，除了系统退出事件之外(SystemExit、
		KeyboardInterrupt和GeneratorExit)

	ArithmeticError
		所有数值错误的超类。

	OverflowError
		识别特定的数值错误的子类。

"--------------------------------------------------------------------------------"

itertools : 

	python的内建模块，用于高效循环创建迭代器函数

	无限的迭代器(Infinite iterators:)

		函数         参数            实例

	1、count()    start,[step]    start,start+step
		
		count(10)
			10 11 12 ...
		
	2、cycle()    p				p0,p1,..plast,p0,p1..	
	
		cycle('ABCD') 
			A B C D A B C D ...

	3、repeat()  elem [,n]      elem,elem..up to n times 
	
		repeat(10,3)
			10 10 10

	迭代器终止于最短的输入序列：

	Iterator		Arguments       Results                Example

	1、accumulate()	p[,func]      p0,p0+p1,p0+p1+p2,..  
		
		accumulate([1,2,3,4]) 
			1 3 6 10

	2、chain()         p,q,...       p0,p1..plast,q0,q1,.  
	
		chain('ABC','DEF') 
			A B C D E F

	3、compress()  data,selectors (d[0] is s[0],(d[1] if s[1])..) 
		
		compress('ABCD',[1,0,1,1])
			A C D

	4、islice()    seq,[start] stop[,step]    elem from seq[start:stop:step] 

			islice('ABCDEFG',2,None)
				C D E F G

	5、filterfalse() pred,seq    elements of seq  where pred(elem) is false

		filterfalse(lambda x: x%2,range(10))
			0 2 4 6 8


	6、groupby()   iterable[, key]   sub-iterators grouped by 
								  value of key(v)
		for key, group in itertools.groupby('AAABBBCCAAA'):
			print(key, list(group))
				A ['A', 'A', 'A']
				B ['B', 'B', 'B']
				C ['C', 'C']
				A ['A', 'A', 'A']
			

	组合迭代器：

	
	1、product()		p, q, … [repeat=1]		笛卡尔积，相当于一个嵌套的for循环

		product('ABCD', repeat=2)		
			AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
	
	2、permutations()		p[, r]  长度元组，所有可能的顺序，没有重复的元素
		
		permutations('ABCD', 2)		
			AB AC AD BA BC BD CA CB CD DA DB DC

	3、combinations()    p, r       长度为r的元组，按顺序排列，没有重复的元素
		
		combinations('ABCD', 2)		
			AB AC AD BC BD CD


"-----------------------------------------------------------------------------"

dis库：是python默认的CPython自带的一个库，可用来分析字节码
	
1、首先导入库
	import dis

2、dis函数

	def add(a, b = 0):
		return (a+b)

	dis.dis(add)

		2		0 LOAD_FAST                0 (a)
				2 LOAD_FAST                1 (b)
	            4 BINARY_ADD
				6 RETURN_VALUE


"----------------------------------------------------------------------------"


常用扩展库:

扩展库					说明

requests	    使用的是 urllib3，继承了urllib2的所有特性

urllib	           基于http的高层库

scrapy	                 爬虫

beautifulsoup4	   HTML/XML的解析器

django/tornado/flask	web框架

xmltodict	         xml 转 dict

celery	          分布式任务调度模块

Pillow(PIL)	          图像处理

xlsxwriter	      仅写excle功能,支持xlsx

xlwt	          仅写excle功能,支持xls ,2013或更早版office

xlrd				仅读excle功能

elasticsearch	    全文搜索引擎

matplotlib	             画图

numpy/scipy            科学计算

SimpleHTTPServer	简单地HTTP Server,不使用Web框架

fabric	               系统管理

pandas                数据处理库

scikit-learn	      机器学习库




"==================================================================="

psutil:

	1、psutil 是一个跨平台库，能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。
		它主要用来做系统监控，性能分析，进程管理。它实现了同等命令行工具提供的功能，
		如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、
		iotop、uptime、pidof、tty、taskset、pmap等。目前支持32位和64位的Linux、Windows、
		OS X、FreeBSD和Sun Solaris等操作系统.

	2、获取系统基本信息的使用：

		cup 信息:

			使用cpu_times方法获取cpu的完整信息：

				psutil.cpu_times()

			获取单个数据，如用户的cpu时或io等待时间，
		
				psutil.cpu_times().user

				psutil.cpu_times().iowait
	
			 获取cpu逻辑和物理个数，默认logical值为True
				
				#CPU逻辑个数
				psutil.cpu_count()

				#CPU物理个数
				psutil.cpu_count(logical=False)

		内存信息:

			内存信息的获取主要使用virtual_memory方法。swap使用就用swap_memory方法。

			>>>mem = psutil.virtual_memory()

			>>>svmem(total=4018601984, available=1066205184, percent=73.5, used=3904004096, free=114597888, 
					active=3302174720, inactive=426078208, buffers=156520448, cached=795086848)

			>>> mem.total
			4018601984
			>>> mem.used
			3904004096
			>>> mem.free
			114597888
			>>> print(mem.total/1024/1024)
			3832.4375

			其中percent表示实际已经使用的内存占比，即（1047543808-717537280）/1047543808*100% 。
			available表示还可以使用的内存。

		磁盘信息:

			磁盘信息主要有两部分，一个是磁盘的利用率，一个是io，
			他们分别可以通过disk_usage和disk_io_counters方法获取。

			如下先获取分区信息，然后看下根分区的使用情况:

				>>> psutil.disk_partitions()
				[sdiskpart(device='/dev/mapper/root', mountpoint='/', fstype='ext4', 
				opts='rw,errors=remount-ro'), sdiskpart(device='/dev/sda1', 
				mountpoint='/boot', fstype='ext2', opts='rw')]
		
				>>> psutil.disk_usage('/')
					sdiskusage(total=42273669120, used=17241096192, free=22885195776, percent=40.8)
			
			默认disk_io_counters方法获取的是硬盘总的io数和读写信息，
			如果需要获取单个分区的io和读写信息加上"perdisk=True"参数。
			
				>>> psutil.disk_io_counters()
					sdiskio(read_count=638190, write_count=77080153, read_bytes=16037795840, 
					write_bytes=1628871606272, read_time=2307367, write_time=1777841305)
				>>> psutil.disk_io_counters(perdisk=True)
					{'vdb1': sdiskio(read_count=312, write_count=0, read_bytes=1238016, write_bytes=0, 
							read_time=95, write_time=0), 'vda1': sdiskio(read_count=637878, 
								write_count=77080257, read_bytes=16036557824,
								write_bytes=1628873314304, read_time=2307272, write_time=1777841879)}
			
		网络信息：

			 网络io和磁盘io使用方法差不多，主要使用net_io_counters方法，如果需要获取单个网卡的io信息，
			 加上pernic=True参数。

			 #获取网络总的io情况
			 >>> psutil.net_io_counters()
				snetio(bytes_sent=525490132009, bytes_recv=409145642892, packets_sent=948527563, 
						packets_recv=778182181, errin=0, errout=0, dropin=0, dropout=0)
			
			#获取网卡的io情况
			>>> psutil.net_io_counters(pernic=True)
				{'lo': snetio(bytes_sent=56524704027, bytes_recv=56524704027, packets_sent=33602236,
				  packets_recv=33602236, errin=0, errout=0, dropin=0, dropout=0), 
				  'eth0': snetio(bytes_sent=468966480940, bytes_recv=352622081327, 
				  packets_sent=914930488, packets_recv=744583332, errin=0, errout=0, dropin=0, dropout=0)}
		
		其他系统信息：

			获取开机时间:

				##以linux时间格式返回，可以使用时间戳转换
				>>> psutil.boot_time()    
					1496647567.0

				#转换成自然时间格式
				>>> psutil.boot_time()
					1496647567.0
				>>> datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H: %M: %S")
					'2017-06-05 15: 26: 07'
			
			查看系统全部进程:

				psutil.pids()

			查看单个进程:

				p = psutil.Process(16031)
				p.name()      #进程名
				p.exe()         #进程的bin路径
				p.cwd()        #进程的工作目录绝对路径
				p.status()     #进程状态
				p.create_time()  #进程创建时间
				p.uids()      #进程uid信息
				p.gids()      #进程的gid信息
				p.cpu_times()    #进程的cpu时间信息,包括user,system两个cpu信息
				p.cpu_affinity()  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
				p.memory_percent()  #进程内存利用率
				p.memory_info()    #进程内存rss,vms信息
				p.io_counters()    #进程的IO信息,包括读写IO数字及参数
				p.connectios()    #返回进程列表
				p.num_threads()  #进程开启的线程数
				听过psutil的Popen方法启动应用程序，可以跟踪程序的相关信息
				from subprocess import PIPE
				p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"],stdout=PIPE)
				p.name()
				p.username()


"-------------------------------------------------------------------------"

monkey patch(猴子补丁):
	
	 定义:
	      
		猴子补丁（monkey patching）
	    在运行时动态修改模块、类或函数，通常是添加功能或修正缺陷。猴子补丁在代码运行时
		（内存中）发挥作用，不会修改源码，因此只对当前运行的程序实例有效。
		因为猴子补丁破坏了封装，而且容易导致程序与补丁代码的实现细节紧密耦合，
		所以被视为临时的变通方案，不是集成代码的推荐方式。
	
		猴子补丁的名声不太好。如果滥用，会导致系统难以理解和维护。补丁通常与目标紧密耦合，
		因此很脆弱。另一个问题是，打了猴子补丁的两个库可能相互牵绊，因为第二个库可能撤销
		了第一个库的补丁。不过猴子补丁也有它的作用，例如可以在运行时让类实现协议。
		适配器设计模式通过实现全新的类解决这种问题。为 Python 打猴子补丁不难，但是有些局限。
		与 Ruby 和 JavaScript 不同， Python 不允许为内置类型打猴子补丁。
		其实这是优点，因为这样可以确保 str 对象的方法始终是那些。
		这一局限能减少外部库打的补丁有冲突的概率。


		mokney patch 指的是在运行时动态的替换，一般是在startup的时候。

		用过gevent就会知道,会在最开头的地方gevent.monkey.patch_all();
		把标准库中的thread/socket等给替换掉.这样我们在后面使用socket的时候可以跟平常一样使用,
		无需修改任何代码,但是它变成非阻塞的了.
	
		很多地方用的import json,后来发现ujson比自带json快了N倍,于是问题来了,
		难道几十个文件要一个个把import json改成import ujson as json吗?
		其实只需要在进程startup的地方monkey patch就行了.是影响整个进程空间的.
		同一进程空间中一个module只会被运行一次.

		代码如下：

			main.py

				import json
				import ujson
				def monkey_patch_json():
					json.__name__ = 'ujson'
					json.dumps = ujson.dumps
					json.loads = ujson.loads

				monkey_patch_json()
				print 'main.py',json.__name__
				import sub

			sub.py
				import json
				print 'sub.py',json.__name__

		运行main.py,可以看到都是输出'ujson',说明后面的json被patch了的。

		最后,注意不能单纯的json = ujson来替换.

		执行main.py 的结果是：
	
			'main.py', 'ujson'
			'sub.py', 'ujson'
		很神奇，所有的json都变成了ujson.

"-----------------------------------------------------------------------"

autopep8:

	autopep8 会根据PEP 8样式文档来格式化Python代码。它使用pep8来决定代码
	的哪部分需要被格式化。autopep8可以修复pep8汇报的大部分格式问题。

	PEP8是Python Enhancement Proposal的缩写，翻译过来就是python增强建议书。
	是python 的一个官方样式指导，它规定了一些比较好的编码方式，比如用4个空格代替缩进等等。

	1、安装：from pip:

		$ pip insall --upgrade autopep8

	2、依赖：
		
		autopep8 requires pycodestyle.

	3、autopep8修复了pycodestyle报告的下列问题:

		E101  -  Reindent所有线路。
		E11  - 修复缩进。
		E121  - 将缩进修复为四的倍数。
		E122  - 为缺口缩进添加缺少的缩进。
		E123  - 对齐闭合支架以匹配开口支架。
		E124  - 对齐闭合支架以匹配视觉压痕。
		E125  - 缩进以区分线与下一逻辑线。
		E126  - 修复过度缩进的悬挂压痕。
		E127  - 修复视觉缩进。
		E128  - 修复视觉缩进。
		E129  - 修复视觉缩进。
		E131  - 修复未对齐延续线的悬挂缩进。
		E133  - 修复关闭括号的缺失缩进。
		E20  - 删除无关的空格。
		E211  - 删除无关的空格。
		E22  - 修复关键字周围的无关空白。
		E224  - 删除操作员周围的无关空格。
		E225  - 修复操作员周围缺少的空白。
		E226  - 修复算术运算符周围缺少的空格。
		E227  - 修复按位/移位运算符周围缺少的空格。
		E228  - 修复模运算符周围缺少的空格。
		E231  - 添加缺少的空格。
		E241  - 修复关键字周围的无关空白。
		E242  - 删除操作员周围的无关空格。
		E251  - 删除参数'='符号周围的空格。
		E252  - 参数等于缺少空格。
		E26  - 在内联注释的注释哈希后修复间距。
		E265  - 修复块注释的注释哈希后的间距。
		E266  - 为块注释修复了太多前导'＃'。
		E27  - 修复关键字周围的无关空白。
		E301  - 添加缺少的空白行。
		E302  - 添加缺少的2个空行。
		E303  - 删除多余的空白行。
		E304  - 删除功能装饰器后面的空白行。
		E305  - 功能或课程结束后预计有2个空白行。
		E306  - 嵌套定义之前预计有1个空行。
		E401  - 将进口分开。
		E402  - 修复模块级别导入不在文件顶部
		E501  - 尝试使线条适合--max-line-length字符。
		E502  - 删除换行符的无关逃逸。
		E701  - 将冒号分隔的复合语句放在单独的行上。
		E70  - 将分号分隔的复合语句放在单独的行上。
		E711  - 修复与无比较。
		E712  - 修复与布尔值的比较。
		E713  - 使用'not in'进行会员资格测试。
		E714  - 对对象标识使用'is not'测试。
		E721  - 使用“isinstance（）”而不是直接比较类型。
		E722  - 修复裸露除外。
		E731  - 使用时不使用def指定lambda表达式。
		W291  - 删除尾随空格。
		W292  - 在文件末尾添加一个换行符。
		W293  - 删除空白行上的尾随空格。
		W391  - 删除尾随空白行。
		W503  - 在二元运算符之前修复换行符。
		W504  - 修复二元运算符后的换行符。
		W601  - 使用“in”而不是“has_key（）”。
		W602  - 修复不推荐的提出异常的形式。
		W603  - 使用“！=”代替“<>”
		W604  - 使用“repr（）”而不是反引号。
		W605  - 修复无效的转义序列'x'。
		W690  - 修复各种已弃用的代码（通过lib2to3）。

	4、autopep8还修复了pycodestyle找不到的一些问题。

		更正已弃用或非惯用的Python代码（通过lib2to3）。使用它可以使Python 2.7代码与Python 3更兼容。
		（如果W690启用，则会触发此代码。）

		标准化具有混合行结尾的文件。
		在类docstring和它的第一个方法声明之间加一个空行。（启用E301。）
		删除函数声明及其docstring之间的空行。（启用E303。）

	5、具体用法：

		1、使用 autopep8 更改一个文件。

			假设文件名是 test.py,对之个文件执行autopep8命令：

			/usr/local/Python-2.7.14/bin/autopep8 --in-place --aggressive --aggressive test.py

			备注： 
				
				--in-place： 以更改后的文件直接替代源文件。
				--aggressive --aggressive : 以 aggressive 等级2 来更改源文件。

		2、aggressive 等级
			
			默认情况下，autopep8只修复空格问题，所以，默认情况下，autopep8不会修复 E711 和 E712 ，
			也不会修复弃用的代码 W6。
			为了应用这些更加 aggressive 的修复，使用 --aggressive 选项：

			autopep8 --aggressive test.py
			
			使用多个 --aggressive 可以增加 aggressiveness 等级。

			比如， E712 需要 aggressiveness 等级2.

			autopep8 --aggressive  --aggressive test.py


		3、选择修复部分规范

			只修复一部分规范，使用 --select 选项。

			比如，修复多种缩进问题：

			$ autopep8 --select=E1,W1 test.py

			仅仅修复弃用代码问题：

			$ autopep8 --aggressive --select=W6 test.py


		4、显示详细的过程信息

			$ autopep8 -v test.py


		5、以模块的方式使用
			
			>>> import autopep8
			>>> autopep8.fix_code('x=       123\n')
			'x = 123\n'

		6、以模块的方式使用，且带有条件

			>>> import autopep8
			>>> autopep8.fix_code('x.has_key(y)\n', options={'aggressive': 1})
			'y in x\n'
			>>> autopep8.fix_code('print( 123 )\n', options={'ignore': ['E']})
			'print( 123 )\n'


"-------------------------------------------------------------------------------"

Pylint:

	1、Pylint 是什么:

		Pylint 是一个Python代码分析工具，它分析Python代码中的错误，查找不符合代码
		风格标准(Pylint默认的代码风格是PEP8)和潜在的问题的代码。

		Pylint 是一个Python工具，除了平常代码分析工具的作用之外，它提供了
		更多的功能：如检查一行代码的长度，变量名是否符合命名标准，
		一个声明过的接口是否被真正的实现等等。

		Pylint 的一个很大的好处是它的高可配置性，高可定制性，并且可以很容易写小插件来添加功能。

		如果运行两次 Pylint，它会同时显示出当前和上次的运行结果，从而可以看出代码质量是否得到了改进。

		目前在 eclipse 的 pydev 插件中也集成了 Pylint。


	2、Pylint 具体介绍:


		Pylint 的安装:

			Pylint 可以用于所有高于或者等于 2.2 的 Python 版本。
			需要logilab-astng（version >= 0.14和logilab-common(version >= 0.13)的包

		Pylint 在 Linux 上的安装:

			Debian:	sudo apt-get install pylint 
			Ubuntu: sudo apt-get install pylint
			centos: sudo yum install pylint

			Pylint can be simply installed by running:

				pip install pylint

			If you are using Python 3.6+, upgrade to get full support for your version:

				pip install pylint --upgrade

	3、Pylint 的调用:

		Pylint 的调用命令:
			pylint [options] module_or_package

		使用 Pylint 对一个模块 module.py 进行代码检查：

			a. 进入这个模块所在的文件夹，运行 pylint [options] module.py
			   这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。

			b.  不进入模块所在的文件夹，运行 pylint [options] directory/module.py
				这种调用方式当如下条件满足的时候是可以工作的：directory 是个 Python 包 
				( 比如包含一个 __init__.py 文件 )，或者 directory 被加入了 Python 的路径中。

		使用 Pylint 对一个包 pakage 进行代码检查：

			a. 进入这个包所在文件夹，运行 pylint [options] pakage。
			   这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。

			b. 不进入包所在的文件夹，运行 pylint [options] directory/ pakage。
				这种情况下当如下条件满足的时候是可以工作的：directory 被加入了 Python 的路径中。
				比如在 Linux 上，export PYTHONPATH=$PYTHONPATH: directory。
		
		
	4、Pylint 的常用命令行参数:

		a. -h,--help:

			显示所有帮助信息。

		b. --generate-rcfile:

			可以使用 pylint --generate-rcfile 来生成一个配置文件示例。
			可以使用重定向把这个配置文件保存下来用做以后使用。也可以在前面加上其它选项，
			使这些选项的值被包含在这个产生的配置文件里。
			如：pylint --persistent=n --generate-rcfile > pylint.conf，
			查看 pylint.conf，可以看到 persistent=no，而不再是其默认值 yes。	
		
		c. --rcfile=<file> :
		
			指定一个配置文件。把使用的配置放在配置文件中，
			这样不仅规范了自己代码，也可以方便地和别人共享这些规范。

		d. -i <y_or_n>, --include-ids=<y_or_n> :

			在输出中包含 message 的 id, 然后通过 pylint --help-msg=<msg-id>
			来查看这个错误的详细信息，这样可以具体地定位错误。

		e. -r <y_or_n>, --reports=<y_or_n> :

			默认是 y, 表示 Pylint 的输出中除了包含源代码分析部分，也包含报告部分。

		f. --files-output=<y_or_n> :

			将每个 module /package 的 message 输出到一个以 pylint_module/package. [txt|html] 命名的文件中，
			如果有 report 的话，输出到名为 pylint_global.[txt|html] 的文件中。
			默认是输出到屏幕上不输出到文件里。

		g. -f <format>, --output-format=<format> :

			设置输出格式。可以选择的格式有 text, parseable, colorized, msvs (visual studio) 和 html, 
			默认的输出格式是 text。

		h. --disable-msg=<msg ids>
	
			禁止指定 id 的 message. 比如说输出中包含了 W0402 这个 warning 的 message,
			如果不希望它在输出中出现，可以使用 --disable-msg= W0402
	
	5、Pylint 的输出:

		Pylint的默认输出格式是原始文本（raw text）格式 ，
		可以通过 -f <format>，--output-format=<format> 来指定别的输出格式如html等等。
		在Pylint的输出中有如下两个部分：源代码分析部分和报告部分。

		源代码分析部分：

			对于每一个 Python 模块，Pylint 的结果中首先显示一些"*"字符 , 
			后面紧跟模块的名字，然后是一系列的 message, message 的格式如下：

			a. MESSAGE_TYPE: LINE_NUM:[OBJECT:] MESSAGE:
			
				MESSAGE_TYPE 有如下几种：

				(C) 惯例。违反了编码风格标准
				(R) 重构。写得非常糟糕的代码。
				(W) 警告。某些 Python 特定的问题。
				(E) 错误。很可能是代码中的错误。
				(F) 致命错误。阻止 Pylint 进一步运行的错误。

			b. Pylint 中的 utils 模块的输出结果:

				************* Module utils 
				C: 88:Message: Missing docstring 
				R: 88:Message: Too few public methods (0/2) 
				C:183:MessagesHandlerMixIn._cat_ids: Missing docstring 
				R:183:MessagesHandlerMixIn._cat_ids: Method could be a function 
				R:282:MessagesHandlerMixIn.list_messages: Too many branches (14/12)

		报告部分：

			在源代码分析结束后面，会有一系列的报告，每个报告关注于项目的某些方面，
			如每种类别的 message 的数目，模块的依赖关系等等。具体来说，报告中会包含如下的方面：


			检查的 module 的个数。
			
			对于每个 module, 错误和警告在其中所占的百分比。比如有两个 module A 和 B,
			如果一共检查出来 4 个错误，1 个错误是在 A 中，3 个错误是在 B 中，
			那么 A 的错误的百分比是 25%, B 的错误的百分比是 75%。
			
			错误，警告的总数量。
	
	6、使用 Pylint 分析 Python 代码的具体示例：

		[root@iz2ze0lvzs717097h32rpcz ~]# pylint binary_2ststem.py

		源码：

			1 #!/bin/python
			2 # _*_coding:UTF-8_*_
			3 
			4 
			5 def binary(n):
			6     if n == 0:
			7         return '0'
			8     else:
			9         return binary(n // 2) + str(n % 2)
			10 
			11 
			12 num = int(input("请输入一个十进制的数字:"))
			13 
			14 bin_num = binary(num)
			15 
			16 print(bin_num)


		 Pylint 的分析结果

			************* Module binary_2ststem
			 C: 16, 0: Unnecessary parens after u'print' keyword (superfluous-parens)
			 C:  1, 0: Missing module docstring (missing-docstring)
			 C:  5, 0: Invalid argument name "n" (invalid-name)
			 C:  5, 0: Missing function docstring (missing-docstring)
			 C: 12, 0: Invalid constant name "num" (invalid-name)
			 C: 14, 0: Invalid constant name "bin_num" (invalid-name)

		 Report 部分:

			Report
			======
			7 statements analysed.

			Statistics by type
			------------------

			+---------+-------+-----------+-----------+------------+---------+
			|type     |number |old number |difference |%documented |%badname |
			+=========+=======+===========+===========+============+=========+
			|module   |1      |NC         |NC         |0.00        |0.00     |
			+---------+-------+-----------+-----------+------------+---------+
			|class    |0      |NC         |NC         |0           |0        |
			+---------+-------+-----------+-----------+------------+---------+
			|method   |0      |NC         |NC         |0           |0        |
			+---------+-------+-----------+-----------+------------+---------+
			|function |1      |NC         |NC         |0.00        |0.00     |
			+---------+-------+-----------+-----------+------------+---------+


			Raw metrics
			-----------
			+----------+-------+------+---------+-----------+
			|type      |number |%     |previous |difference |
			+==========+=======+======+=========+===========+
			|code      |8      |47.06 |NC       |NC         |
			+----------+-------+------+---------+-----------+
			|docstring |0      |0.00  |NC       |NC         |
			+----------+-------+------+---------+-----------+
			|comment   |2      |11.76 |NC       |NC         |
			+----------+-------+------+---------+-----------+
			|empty     |7      |41.18 |NC       |NC         |
			+----------+-------+------+---------+-----------+

			Duplication
			-----------

			+-------------------------+------+---------+-----------+
			|                         |now   |previous |difference |
			+=========================+======+=========+===========+
			|nb duplicated lines      |0     |NC       |NC         |
			+-------------------------+------+---------+-----------+
			|percent duplicated lines |0.000 |NC       |NC         |
			+-------------------------+------+---------+-----------+

			Messages by category
			--------------------

			+-----------+-------+---------+-----------+
			|type       |number |previous |difference |
			+===========+=======+=========+===========+
			|convention |6      |NC       |NC         |
			+-----------+-------+---------+-----------+
			|refactor   |0      |NC       |NC         |
			+-----------+-------+---------+-----------+
			|warning    |0      |NC       |NC         |
			+-----------+-------+---------+-----------+
			|error      |0      |NC       |NC         |
			+-----------+-------+---------+-----------+

			Messages
			--------
			+-------------------+------------+
			|message id         |occurrences |
			+===================+============+
			|invalid-name       |3           |
			+-------------------+------------+
			|missing-docstring  |2           |
			+-------------------+------------+
			|superfluous-parens |1           |
			+-------------------+------------+

			Global evaluation
			-----------------
			Your code has been rated at 1.43/10


		b. 因为输出结果太长，所以先不让输出报告部分，先根据源代码分析部分来找出代码中的问题。
			使用选项"--reports=n"

			[root@iz2ze0lvzs717097h32rpcz ~]# pylint --reports=n binary_2ststem.py 
			No config file found, using default configuration
			************* Module binary_2ststem
			C: 16, 0: Unnecessary parens after u'print' keyword (superfluous-parens)
			C:  1, 0: Missing module docstring (missing-docstring)
			C:  5, 0: Invalid argument name "n" (invalid-name)
			C:  5, 0: Missing function docstring (missing-docstring)
			C: 12, 0: Invalid constant name "num" (invalid-name)
			C: 14, 0: Invalid constant name "bin_num" (invalid-name)
		
		c. 根据提示去修改源码中的错误：
			
"--------------------------------------------------------------------------------"

Python定时任务:

    1、第一种办法是最近简单有暴力，写一个死循环，使用 sleep() 函数
    
        import time

        from datetime import datetime
        
        def timedTask():
            while True:
                pass
                time.sleep(10)        
        
        if __name__ == '__main__':
            timedTask()

    2、Python 标准库 threading 中有一个 Timer 类。它会新启动
        一个线程来执行定时任务，所以它是非阻塞，如果需要关心线程安全
        可以选用threading.Timer 模块。
        
        from datetime import datetime
        from threading import Timer
        import time
       
        def timedTask():
            # 第一个参数：延迟多长时间执行任务（单位：秒）
            # 第二个参数：要执行的任务，即函数
            # 第三个参数：调用函数的参数（tuple）
            
            Timer(10, task(), ()).start()
        
        def task():
            
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        if __name__ == '__main__':
            timedTask()
            while True:
                print(time.time())
                time.sleep(4)
    
    3、 第三种方式是使用标准库中 sched 模块。 sched 是事件调度器，
        它通过 scheduler 类来调度事件，从而达到定时执行任务的效果。
        
        sched库使用起来也是非常简单。
 
        a. 首先构造一个sched.scheduler类:
            
           它接受两个参数：timefunc 和 delayfunc。
           timefunc 应该返回一个数字，代表当前时间，
           delayfunc 函数接受一个参数，用于暂停运行的时间单元。            
    
            一般使用默认参数就行，即传入这两个参数 time.time 和 time.sleep.
            当然，你也可以自己实现时间暂停的函数。
			
		b. 添加调度任务:
		
		   enter(delay, priority, action, argument=(), kwargs={}) 
		   
		   该函数可以延迟一定时间执行任务。
		   delay 表示延迟多长时间执行任务，单位是秒。
		   priority为优先级，越小优先级越大。
		   两个任务指定相同的延迟时间，优先级大的任务会向被执行。
		   action 即需要执行的函数，argument 和 kwargs 分别是函数的位置和关键字参数。
		   
		   
		   scheduler.enterabs(time, priority, action, argument=(), kwargs={})
           添加一项任务，但这个任务会在 time 这时刻执行。因此，time 是绝对时间.
           其他参数用法与 enter() 中的参数用法是一致。
		    
		c. 把任务执行起来
		    
		   调用 scheduler.run() 函数就完事了。
		   
		    
		d. 例子：
		    
		    from datetime import datetime
		    import sched
		    import time
		    
		    # 每个 10 秒打印当前时间。
		    def timedTask():
		        # 初始化 sched 模块的 scheduler 类 
		        sched.scheduler(time.time, time.sleep)
		        
		        #增加调度任务
		        scheduler.enter(10, 1 , task)
		    
		    # 定时任务
		    
		    def task():
		        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		           
		    if __name__ == '__main__':
		        timedTask()
		       
		 值得注意的是： scheduler 中的每个调度任务只会工作一次，
		 不会无限循环被调用。如果想重复执行同一任务， 需要重复添加调度任务即可。
	
    4、  我们了解到有三种办法能实现定时任务，但是都无法做到循环执行定时任务。
        因此，需要一个能够担当此重任的库。它就是APScheduler。
        
        a. 简介:
        
            APScheduler的全称是Advanced Python Scheduler。它是一个轻量级的 Python 定时任务调度框架。
            APScheduler 支持三种调度任务：固定时间间隔，固定时间点（日期）, Linux 下的 Crontab 命令。
            同时，它还支持异步执行、后台执行调度任务。

        b. 安装：
        
            使用 pip 包管理工具安装 APScheduler 是最方便快捷的。
            
            pip install APScheduler
            
        c. 使用步骤：
        
            APScheduler 使用起来还算是比较简单。运行一个调度任务只需要以下三部曲
            
                新建一个 schedulers (调度器)
                添加一个调度任务(job stores)
                运行调度任务
                
            下面是执行每 2 秒报时的简单示例代码：  
                 
                import datetime
                import time
                from apscheduler.schedulers.background import BackgroundScheduler
                
                def timedTask():
                    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
                
                if __name__ == '__main__':
                    # 创建后台执行的 schedulers
                    scheduler = BackgroundScheduler()  
                    # 添加调度任务
                    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
                    scheduler.add_job(timedTask, 'interval', seconds=2)
                    # 启动调度任务
                    scheduler.start()
                    
                    while True:
                        print(time.time())
                        time.sleep(5)
        d、基础组件:
        
            APScheduler 有四种组件，分别是：调度器(scheduler), 作业器(job store), 
            触发器（trigger）, 执行器（executor）
            
            scheduler: 属于控制器角色，它配置作业存储器和执行器可以在调度器中完成，例如添加、修改和移除作业。
                
                APScheduler 非常好用的原因。它提供 7 种调度器，能够满足我们各种场景的需要。
                例如：后台执行某个操作，异步执行操作等。调度器分别是：
                
                1、BlockingScheduler : 调度器在当前进程的主线程中运行，也就是会阻塞当前线程。
                2、BackgroundScheduler : 调度器在后台线程中运行，不会阻塞当前线程。
                3、AsyncIOScheduler : 结合 asyncio 模块（一个异步框架）一起使用。
                4、GeventScheduler : 程序中使用 gevent（高性能的Python并发框架）作为IO模型，和 GeventExecutor 配合使用。
                5、TornadoScheduler : 程序中使用 Tornado（一个web框架）的IO模型，用 ioloop.add_timeout 完成定时唤醒。
                6、TwistedScheduler : 配合 TwistedExecutor，用 reactor.callLater 完成定时唤醒。
                7、QtScheduler : 你的应用是一个 Qt 应用，需使用QTimer完成定时唤醒。
      
            triggers: 描述调度任务被触发的条件。不过触发器完全是无状态的。
                
                APScheduler 有三种内建的 trigger:
                
                1、date 触发器
                   date 是最基本的一种调度，作业任务只会执行一次。
                   它表示特定的时间点触发。它的参数如下：
                   
                    参数	                                 说明
                    run_date (datetime 或 str)	        作业的运行日期或时间
                    timezone (datetime.tzinfo 或 str)	指定时区
                   
                date 触发器使用示例如下：
                    from datetime import datetime
                    from datetime import date
                    from apscheduler.schedulers.background import BackgroundScheduler
                    
                    def job_func(text):
                        print(text)
                    
                    scheduler = BackgroundScheduler()
                    # 在 2017-12-13 时刻运行一次 job_func 方法
                    scheduler .add_job(job_func, 'date', run_date=date(2017, 12, 13), args=['text'])
                    # 在 2017-12-13 14:00:00 时刻运行一次 job_func 方法
                    scheduler .add_job(job_func, 'date', run_date=datetime(2017, 12, 13, 14, 0, 0), args=['text'])
                    # 在 2017-12-13 14:00:01 时刻运行一次 job_func 方法
                    scheduler .add_job(job_func, 'date', run_date='2017-12-13 14:00:01', args=['text'])
                    
                    scheduler.start()
                
                2、interval 触发器固定时间间隔触发。interval 间隔调度，
                    参数如下：
                   
                    参数                 说明

                    weeks (int)           间隔几周
                    days (int)            间隔几天
                    hours (int)           间隔几小时
                    minutes (int)         间隔几分钟
                    seconds (int)         间隔多少秒
                    start_date (datetime 或 str)  开始日期
                    end_date (datetime 或 str)    结束日期
                    timezone (datetime.tzinfo 或str) 区
		    
		    interval 触发器使用示例如下：
		    
		    	import datetime
			from apscheduler.schedulers.background import BackgroundScheduler

			def job_func(text):
			    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

			scheduler = BackgroundScheduler()
			# 每隔两分钟执行一次 job_func 方法
			scheduler .add_job(job_func, 'interval', minutes=2)
			# 在 2017-12-13 14:00:01 ~ 2017-12-13 14:00:10 之间, 每隔两分钟执行一次 job_func 方法
			scheduler .add_job(job_func, 'interval', minutes=2, start_date='2017-12-13 14:00:01' , 
					  end_date='2017-12-13 14:00:10') 

			scheduler.start()
			
		3、cron 触发器
		
			在特定时间周期性地触发，和Linux crontab格式兼容。它是功能最强大的触发器。
			我们先了解 cron 参数：
			
			参数说明

			year (int 或 str)年，4位数字
			month (int 或 str)月 (范围1-12)
			day (int 或 str)日 (范围1-31
			week (int 或 str)周 (范围1-53)
			day_of_week (int 或 str)周内第几天或者星期几 (范围0-6 或者 mon,tue,wed,thu,fri,sat,sun)
			hour (int 或 str)时 (范围0-23)
			minute (int 或 str)分 (范围0-59)
			second (int 或 str)秒 (范围0-59)
			start_date (datetime 或 str)最早开始日期(包含)
			end_date (datetime 或 str)最晚结束时间(包含)
			timezone (datetime.tzinfo 或str)指定时区

		    cron 触发器使用示例如下：
		    	
			import datetime
			from apscheduler.schedulers.background import BackgroundScheduler

			def job_func(text):
			    print("当前时间：", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

			scheduler = BackgroundScheduler()
			# 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 job_func 任务
			scheduler .add_job(job_func, 'cron', month='1-3,7-9',day='0, tue', hour='0-3')

			scheduler.start()
            
            job stores: 任务持久化仓库，默认保存任务在内存中，也可将任务保存都各种数据库中，
                        任务中的数据序列化后保存到持久化数据库，从数据库加载后又反序列化。
			
			该组件是对调度任务的管理。
			
			添加 job 
			
				两种添加方法，其中一种上述代码用到的 add_job()， 另一种则是scheduled_job()修饰器来修饰函数。
				这个两种办法的区别是：第一种方法返回一个 apscheduler.job.Job 的实例，可以用来改变或者移除 job。
				第二种方法只适用于应用运行期间不会改变的 job。
			
				第二种添加任务方式的例子：
			
				import datetime
				from apscheduler.schedulers.background import BackgroundScheduler

				@scheduler.scheduled_job(job_func, 'interval', minutes=2)
				def job_func(text):
				    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

				scheduler = BackgroundScheduler()
				scheduler.start()
			移除 job
			
				移除 job 也有两种方法：remove_job() 和 job.remove()。
				remove_job() 是根据 job 的 id 来移除，所以要在 job 创建的时候指定一个 id。
				job.remove() 则是对 job 执行 remove 方法即可
			
				scheduler.add_job(job_func, 'interval', minutes=2, id='job_one')
				scheduler.remove_job(job_one)

				job = add_job(job_func, 'interval', minutes=2, id='job_one')
				job.remvoe()
			
			获取 job 列表
			
				通过 scheduler.get_jobs() 方法能够获取当前调度器中的所有 job 的列表
			
			修改 job
				
				如果你因计划改变要对 job 进行修改，可以使用Job.modify() 或者 modify_job()方法来修改 job 的属性。
				但是值得注意的是，job 的 id 是无法被修改的。
			
				scheduler.add_job(job_func, 'interval', minutes=2, id='job_one')
				scheduler.start()
				# 将触发时间间隔修改成 5分钟
				scheduler.modify_job('job_one', minutes=5)

				job = scheduler.add_job(job_func, 'interval', minutes=2)
				# 将触发时间间隔修改成 5分钟
				job.modify(minutes=5)
			
			关闭 job
			
				默认情况下调度器会等待所有正在运行的作业完成后，关闭所有的调度器和作业存储。如果你不想等待，
				可以将 wait 选项设置为 False。
				
				scheduler.shutdown()
				scheduler.shutdown(wait=false)
			
            
            executors: 负责处理作业的运行，它们通常通过在作业中提交指定的可调用对象到一个线程或者进城池来进行。
                       当作业完成时，执行器将会通知调度器。
                
                    	执行器顾名思义是执行调度任务的模块。最常用的 executor 有两种：ProcessPoolExecutor 和 ThreadPoolExecutor
			
			下面是显式设置 job store(使用mongo存储)和 executor 的代码的示例。
				
				from pymongo import MongoClient
				from apscheduler.schedulers.blocking import BlockingScheduler
				from apscheduler.jobstores.mongodb import MongoDBJobStore
				from apscheduler.jobstores.memory import MemoryJobStore
				from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


				def my_job():
				    print 'hello world'
				host = '127.0.0.1'
				port = 27017
				client = MongoClient(host, port)

				jobstores = {
				    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
				    'default': MemoryJobStore()
				}
				executors = {
				    'default': ThreadPoolExecutor(10),
				    'processpool': ProcessPoolExecutor(3)
				}
				job_defaults = {
				    'coalesce': False,
				    'max_instances': 3
				}
				scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
				scheduler.add_job(my_job, 'interval', seconds=5)

				try:
				    scheduler.start()
				except SystemExit:
				    client.close()

          
"---------------------------------------------------------------------------"
            
           
