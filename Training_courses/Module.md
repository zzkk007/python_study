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

traceback : 用于提取，格式化和打印Python程序的堆栈跟踪。
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

"-------------------------------------------------------------------------------"

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


"-------------------------------------------------------------------------------"

python 类:


1、类和实例的关系

	python oop的本质是:在已连接的命名空间内寻找属性而已。

	类对象和实例对象是两个不同的命名空间，
	类对象是由class()执行语句创建类对象，并赋值绑定到类名。
	实例对象是由调用类名是创建。

	类对象和实例对象是类树通过继承搜索相连的命名空间，继承
	是在属性点号运算符时发送的，而且只查找相连对象内的命名空间。
	搜索方式是通过字典类型来实现的。

2、运算符重载

	a、基础知识：
		
		运算符重载让类拦截常规的python运算

		类可重载所有的python表达式运算符

		类也可重载打印、函数调用、属性点号等内置运算

		重载使类实例的行为像内置类型

		重载是通过提供特殊名称的类方法来实现的。

	b、例子，__sub__()方法

		class Number:
			def __init__(self,start):
				self.data = start

			def __sub__(self,other):
				return Number(self.data - other)

		x = Number(5)
		
		y = x - 2  // x - 2 执行的是__sub__(self,other), y = Number(5-2)

		y.data
			3

	c、常见的运算符重载方法：

		方法             重载                 调用

		__new__          创建                在__init__之前创建对象

		__init__         构造函数            实例对象建立：x = Class(args)

		__del__          析构函数            x 对象回收

		__add__          运算符 +            如果没有__iadd__, x+y, x+=y

		__sub__          运算符 -            x - y ,x -= y

		__or__           运算符 |            如果没有__ior__, X|Y, X|=y



		__repr__,__str__ 打印，转换          print(x),repr(x),str(x)

		__call__         函数调用            x( *args,**kargs)


		
		__getattr__      点号运算            x.undefined

		__setattr__      属性赋值运算        x.any = value

		__delattr__      属性删除            del  x.any

		__getattribute__ 属性获取            x.any
 		
		__get__,__set__,__delete__  属性描述 x.attr,x.arrt= value,del x.attr

	

		__getitem__      索引运算           x[key],x[i:j],没有__iter__时的for循环和其他迭代器

		__setitem__      索引赋值运算       x[key] = value,x[i:j] = sequence

		__delitem__      索引和分片删除     del x[key],del x[i:j]



		__len__          长度               len(x),如果没有__bool__

		__bool__         布尔测试           bool(x) 真值测试


		__lt__           小于               x < y   less than
 
		__gt__           大于               x > y   greater than

		__le__           小于等于           x <= y  less equal

		__ge__           大于等于           x >= y  greater equal

		__eq__           等于               x == y  equal

		__ne__           不等于             x != y  not equal


		__iter__,__next__ 迭代环境          I = iter(x),next(x)

		__contains__     成员关系测试       item in x 

		__index__        整数值             hex(x),bin(x),oct(x)

		__enter__,__exit__ 环境管理         with obj as var

	
3、模块和类

	模块是一个文件
	类是一个语句

	模块：
		
		是数据/逻辑包
		通过编写python文件或C扩展来创建
		通过导入来使用

	类：
		
		实现新的对象
		由class语句创建
		通过调用使用
		总是在一个模块中

	类支持：运算符重载、多实例生成、继承。


python常用的OOP设计模式：继承、组合、委托和工厂。

4、继承：

		继承是基于python中属性查找的(在X.name表达式中)
		继承："是一个" 关系(is-a)。
	
	多态：

		在X.method方法中，method的意义取决于X的类型(类)
		因为python没有类型声明，属性总是在运行期解析，实现相同接口的对象是可互相交换的，
		所有客户端不需要知道实现它们调用方法是对象种类。

	封装：

		方法和运算符实现行为，数据隐藏默认是一种惯例。
		封装指的是在pyhon中打包，也就是把实现的细节隐藏在对象接口之后，
		封装可让对象接口的实现出现变动时，
		不影响对象的用户。

5、组合:

	OOP和组合："有一个" 关系(has-a)。
	组合就是指内嵌对象集合体。组合类一般都提供自己的接口，并通过内嵌的对象来实现接口。

	from employees import PizzaRobot,Server

	class Customer:

		def __init__(self,name):
			self.name = name
		def order(self,server):
			print(self.name,"Orders from",server)
		def pay(self,server):
			print(self.name,"pays for item to",server)

	class Over:
		def break(self):
			print("oven bakes")

	class PizzaShop:
		def __init__(self):
			self.server = Seerver('Pat')
			self.chef = PizzaRobot('Bob')
			sefl.oven = Oven()

		def order(self,name):
			customer = Customer(name)
			customer.order(self.server)
			self.chef.work()
			self.oven.bake()
			customber.pay(self.server)

	if __name__ == "__main__":
		scene = PizzaShop()
		scene.order('Homer')
		print('...')
		scene.order('Shaggy')

	PizzaShop类是容器和控制器，其构造函数会创建员工类实例并将其嵌入。


6、委托:

	面向对象程序员时常谈到所谓的委托，通常就会指控制器对象内嵌其他对象，
	而把运算请求传给那些对象。控制器负责管理工作，例如，记录存取等。
	在python中，委托通常以__getattr__(点号运算)钩子方法实现。

	class wrapper:
		
		def __init__(self,object):
			self.wrappend = object
		def __getattr__(self,attrname):
			print('Trace:',attrname)
			return getattr(self.wrapped,attrname) //执行点号运行

	你可以使用这个模块包装类的做法，管理任何带有属性的对象的存取：列表，字典，甚至是类和实例。
	在这里，wrapper类只是在每个属性读取时打印跟踪消息，并把属性请求委托给嵌入的wrapped对象。

	from trace import wrapper

	x = wrapper([1,2,3])

	x.append(4)
		Trace:wrappend

	x.wrappend
		[1,2,3,4]

	x = wrapper({"a":1,"b":2})
	x.keys()
		Trace: keys
		dict_keys(['a', 'b'])

7、工厂:

	类是对象，很容易传递，保存在数据结构中，也可以把类传给任意种类对象的函数，
	这类函数在OOP设计领域汇总偶尔称为工厂。

	def factory(aClass, *args):
		return aClass( *args)

	class Spam:
		def doit(self,message):
			print(message)

	class Person:
		def __init__(self,name,job):
			self.name = name
				self.job = job

	object1 = factory(Spam)
	object2 = factory(Person,"Guido","guru")
	
	我们定义了一个对象生成器函数，称为factory。它传入类对象。




8、抽象超类:

	抽象类是会调用方法的类，但没有继承或定义该方法，而是期待改方法由子类填补。

	class Super:
		def method(self):
			print('in Super.mothod')
		def delegate(self):
			self.action()

	class Provider(Super):
		def action(self):
			print('in Provider.action')


	if __name__ == '__main__':
	x = Provider()
	x.delegate()

	当通过Provider实例调用delegate方法时，有两个独立的搜索会发生：

	1、在最初x.delegate的调用中，Python会搜索Provider实例和它上层的对象，
	直到在Super中找到delegate的方法。实例x会像往常一样传递给这个方法的self参数。

	2、在Super.delegate方法中，self.action会对self以及它上层的对象启动新的独立继承搜索。
	因为self指的是Provider实例，在Provider子类中就会找到action方法。

	从delegate方法角度来看，超类有时也称作抽象超类--也就是类的部分默认是其子类所提供的。
	如果预期的方法子类没有定义，python会引发未定义变量名异常。

9、静态方法:

	需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数

	class People(object):
		country = 'china'
			
		#静态方法
		@staticmethod
		def getCountry():
			return People.country

	print People.getCountry()
	

10、类方法:


	是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，
	对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
	（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'
	作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。


	class People(object):
		country = 'china'
			
		#类方法，用classmethod来进行修饰
		@classmethod
		def getCountry(cls):
			return cls.country
								
	p = People()
	print p.getCountry()    #可以用过实例对象引用
	print People.getCountry()    #可以通过类对象引用


	类方法还有一个用途就是可以对类属性进行修改：

	class People(object):
		country = 'china'
			
		#类方法，用classmethod来进行修饰
		@classmethod
		def getCountry(cls):
			return cls.country
								
		@classmethod
		def setCountry(cls,country):
			cls.country = country
													
													
	p = People()
	print p.getCountry()    #可以用过实例对象引用
	print People.getCountry()    #可以通过类对象引用
	
	p.setCountry('japan')   
	
	print p.getCountry()   
	print People.getCountry()

	从类方法和实例方法以及静态方法的定义形式就可以看出来，
	类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；
	而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、
	也有可能是实例属性（这个需要具体分析），
	不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
	静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用.

11、管理属性:

	先来谈一下类属性和实例属性

	类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，
	在内存中只存在一个副本，这个和C++中类的静态成员变量有点类似。
	对于公有的类属性，在类外可以通过类对象和实例对象访问.

	类属性:

		class People(object):
			name = 'Tom'  #公有的类属性
			__age = 12     #私有的类属性
			   
		p = People()
	
		print(p.name)           #正确
		print(People.name)      #正确
		print(p.__age)            #错误，不能在类外通过实例对象访问私有的类属性
		print(People.__age)        #错误，不能在类外通过类对象访问私有的类属性''

	
	实例属性(对象属性):

		class People(object):
			address = '山东' #类属性
			
			def __init__(self):
				self.name = 'xiaowang' #实例属性
				self.age = 20 #实例属性
									  
		p = People()
		p.age =12 #实例属性
		print(p.address) #正确
		print(p.name)    #正确
		print(p.age)     #正确
	
		print(People.address) #正确
		print(People.name)    #错误
		print(People.age)     #错误


	如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。
	如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，
	不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，
	实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。


12、装饰器:

	1、装饰器用法：

		代码要遵循开放封闭原则，虽然在这个原则是用的面向对象开发，但是也适用于函数式编程，
		简单来说，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：
		封闭：已实现的功能代码块
		开放：对扩展开发

		
		def w1(func):
			def inner():
				# 验证1
				# 验证2
				# 验证3
				func()
			return inner
		@w1
		def f1():
			print('f1')


		python解释器就会从上到下解释代码，步骤如下：

		a、	def w1(func): ==>将w1函数加载到内存
		b、	@w1
		
		没错， 从表面上看解释器仅仅会解释这两句代码，因为函数在 没有被调用之前其内部代码不会被执行。

		从表面上看解释器着实会执行这两句，但是 @w1 这一句代码里却有大文章，@函数名 是python的一种语法糖。

		@w1内部会执行一下操作：
			
			执行w1函数 ，并将 @w1下面的函数作为w1函数的参数，
			即：@w1 等价于 w1(f1) 所以，内部就会去执行：
			
			def inner(): 
				#验证 1
				#验证 2
				#验证 3
				f1()     # func是参数，此时 func 等于 f1 
			return inner
			返回的 inner，inner代表的是函数，非执行函数 ,其实就是将原来的f1函数塞进另外一个函数中。
		
		w1的返回值：

			将执行完的w1函数返回值赋值给@w1下面的函数名f1，即将w1的返回值再重新赋值给f1，即：

			新f1 = def inner():
						#验证 1
				        #验证 2
				        #验证 3
				        原来f1()
					return inner
		
			所以，以后业务部门想要执行 f1 函数时，
			就会执行 新f1 函数，在新f1 函数内部先执行验证，
			再执行原来的f1函数，然后将原来f1 函数的返回值返回给了业务调用者。
			
	2、装饰器的作用：

		a、引入日志
		b、函数执行时间统计
		c、执行函数前预备处理
		d、执行函数后清理功能
		e、权限校验等场景
		f、缓存
		
	3、例1:无参数的函数

		from time import ctime, sleep

		def timefun(func):
			def wrappedfunc():
				print("%s called at %s"%(func.__name__, ctime()))
				func()
				return wrappedfunc
									 
		@timefunc
		def foo():
			print("I am foo")
											 
		
		foo()
		sleep(2)
		foo()

		上面代码理解装饰器执行行为可理解成:

			foo = timefun(foo)
			#foo先作为参数赋值给func后,foo接收指向timefun返回的wrappedfunc
			foo()
			#调用foo(),即等价调用wrappedfunc()
			#内部函数wrappedfunc被引用，所以外部函数的func变量(自由变量)并没有释放
			#func里保存的是原foo函数对象

	4、被装饰的函数有参数

		from time import ctime, sleep

		def timefun(func):
			def wrappedfunc(a, b):
				print("%s called at %s"%(func.__name__, ctime()))
				print(a, b)
				func(a, b)
			return wrappedfunc
										
		@timefun
		def foo(a, b):
		print(a+b)
												
		
		foo(3,5)
		sleep(2)
		foo(2,4)

	5、类装饰器（扩展，非重点）

		装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。

		在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了 __call__() 方法，
		那么这个对象就是callable的。
		
			class Test():
				def __call__(self):
					print('call me!')
							
			t = Test()
			t()  # call me

		类装饰器demo:

		class Test(object):
			def __init__(self, func):
				print("---初始化---")
				print("func name is %s"%func.__name__)
				self.__func = func
			def __call__(self):
				print("---装饰器中的功能---")
				self.__func()

		说明：
		1. 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
		   并且会把test这个函数名当做参数传递到__init__方法中
		   即在__init__方法中的func变量指向了test函数体
		
		2. test函数相当于指向了用Test创建出来的实例对象

		3. 当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法

		4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中
		   就需要一个实例属性来保存这个函数体的引用所以才有了self.__func = func这句代码，
		   从而在调用__call__方法中能够调用到test之前的函数体
		
		@Test
		def test():
			print("----test---")
		
		test()
		showpy()#如果把这句话注释，重新运行程序，依然会看到"--初始化--"

		运行结果如下：

			---初始化---
			func name is test
			---装饰器中的功能---
			----test---
		
13、元类：

	1. 类也是对象

		在大多数编程语言中，类就是一组用来描述如何生成一个对象的代码段。
		在Python中这一点仍然成立：但是，Python中的类还远不止如此。
		类同样也是一种对象。是的，没错，就是对象。
		只要你使用关键字class，Python解释器在执行的时候就会创建一个对象。

		class ObjectCreator(object):
			pass

		将在内存中创建一个对象，名字就是ObjectCreator。
		这个对象（类对象ObjectCreator）拥有创建对象（实例对象）的能力。
		但是，它的本质仍然是一个对象，于是乎你可以对它做如下的操作：

			你可以将它赋值给一个变量
			你可以拷贝它
			你可以为它增加属性
			你可以将它作为函数参数进行传递
		
	2. 到底什么是元类

		元类就是用来创建类的“东西”。
		元类就是用来创建这些类（对象）的，元类就是类的类，你可以这样理解为：

		MyClass = MetaClass() #使用元类创建出一个对象，这个对象称为“类”
		MyObject = MyClass() #使用“类”来创建出实例对象

		函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类。

	3. 使用type创建类

		type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

		Test2 = type("Test2",(),{}) #定了一个Test2类
		
	4. 使用type创建带有属性的类

		Foo = type('Foo', (), {'bar':True})

	5. __metaclass__属性

		你可以在定义一个类的时候为其添加__metaclass__属性。

		class Foo(object):
			__metaclass__ = something…
			...省略...
	
		如果你这么做了，Python就会用元类来创建类Foo。小心点，这里面有些技巧。
		你首先写下class Foo(object)，但是类Foo还没有在内存中创建。
		Python会在类的定义中寻找__metaclass__属性，如果找到了，Python就会用它来创建类Foo，
		如果没有找到，就会用内建的type来创建这个类。把下面这段话反复读几次。当你写如下代码时 :

		class Foo(Bar):
			    pass
		
		Python做了如下的操作：

		Foo中有__metaclass__这个属性吗？如果是，Python会通过__metaclass__创建一个名字为Foo的类(对象)
		如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
		如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
		如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
		现在的问题就是，你可以在__metaclass__中放置些什么代码呢？
		答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？
		type，或者任何使用到type或者子类化type的东东都可以。
	
	6. 自定义元类

		元类的主要目的就是为了当创建类时能够自动地改变类。
		通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类。

		假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。
		有好几种方法可以办到，但其中一种就是通过在模块级别设定__metaclass__。
		采用这种方法，这个模块中的所有类都会通过这个元类来创建，
		我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。

		幸运的是，__metaclass__实际上可以被任意调用，它并不需要是一个正式的类。
		所以，我们这里就先以一个简单的函数作为例子开始。

		
		class UpperAttrMetaClass(type):
			# __new__ 是在__init__之前被调用的特殊方法
			# __new__是用来创建对象并返回的方法
			# 而__init__只是用来将传入的参数初始化给对象
			# 你很少用到__new__，除非你希望能够控制对象的创建
			# 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
			# 如果你希望的话，你也可以在__init__中做些事情
			# 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
			
			def __new__(cls, future_class_name, future_class_parents, future_class_attr):
				#遍历属性字典，把不是__开头的属性名字变为大写
				newAttr = {}
				for name,value in future_class_attr.items():
					if not name.startswith("__"):
						newAttr[name.upper()] = value

				# 方法1：通过'type'来做类对象的创建
				# return type(future_class_name, future_class_parents, newAttr)

				# 方法2：复用type.__new__方法
				# 这就是基本的OOP编程，没什么魔法
				# return type.__new__(cls, future_class_name, future_class_parents, newAttr)

				# 方法3：使用super方法
				return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, newAttr)

			#python2的用法
			class Foo(object):
				__metaclass__ = UpperAttrMetaClass
				bar = 'bip'

			# python3的用法
			# class Foo(object, metaclass = UpperAttrMetaClass):
			#     bar = 'bip'

		print(hasattr(Foo, 'bar'))
		# 输出: False
		print(hasattr(Foo, 'BAR'))
		# 输出:True

		f = Foo()
		print(f.BAR)
		# 输出:'bip'

14、闭包：

	在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
	那么将这个函数以及用到的一些变量称之为闭包
		
	定义一个函数
	def test(number):
		def test_in(number_in):
			print("in test_in 函数, number_in is %d"%number_in)
			return number+number_in
			#其实这里返回的就是闭包的结果
		return test_in
								  
								  
	#给test函数赋值，这个20就是给参数number
	ret = test(20)
	
	#注意这里的100其实给参数number_in
	print(ret(100))
	
	#注意这里的200其实给参数number_in
	print(ret(200))


	内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。
	def counter(start=0):
		count=[start]
		def incr():
			count[0] += 1
			return count[0]
		return incr


	nonlocal访问外部函数的局部变量(python3)
		
	def counter(start=0):
		def incr():
			nonlocal start
			start += 1
			return start
		return incr

	闭包思考：

	1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
	2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存


15、私有化:

	xx: 公有变量
	_x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
	__xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
	__xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字
	xx_:单后置下划线,用于避免与Python关键词的冲突

	父类中属性名为__名字的，子类不继承，子类不能访问
	如果在子类中向__名字赋值，那么会在子类中定义的一个与父类相同名字的属性
	_名的变量、函数、类在使用from xxx import *时都不会被导入


16、__slots__:

	python是动态语言,动态编程语言 是 高级程序设计语言 的一个类别，在计算机科学领域已被广泛应用。
	它是一类 在运行时可以改变其结构的语言 ：例如新的函数、对象、甚至代码可以被引进，
	已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力。

	1. 运行的过程中给对象绑定(添加)属性

		>>> class Person(object):
				def __init__(self, name = None, age = None):
					self.name = name
					self.age = age

		>>> P = Person("小明", "24")
		
		在这里，我们定义了1个类Person，在这个类里，定义了两个初始属性name和age，
		但是人还有性别啊！如果这个类不是你写的是不是你会尝试访问性别这个属性呢？

		>>> P.sex = "male"
		>>> P.sex
			'male'
	
		这时候就发现问题了，我们定义的类里面没有sex这个属性啊！怎么回事呢？ 
		这就是动态语言的魅力和坑！ 这里 实际上就是 动态给实例绑定属性！

	
	2. 运行的过程中给类绑定(添加)方法

		既然给类添加方法，是使用类名.方法名 = xxxx，
		那么给对象添加一个方法也是类似的对象.方法名 = xxxx
		
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

		#定义一个类方法
		@classmethod
		def testClass(cls):
			cls.num = 100

		#定义一个静态方法
		@staticmethod
		def testStatic():
			print("---static method----")

		#创建一个实例对象
		P = Person("老王", 24)
		#调用在class中的方法
		P.eat()

		#给这个对象添加实例方法
		P.run = types.MethodType(run, P)
		#调用实例方法
		P.run(180)

		#给Person类绑定类方法
		Person.testClass = testClass
		
		#调用类方法
		print(Person.num)
		Person.testClass()
		print(Person.num)

		#给Person类绑定静态方法
		Person.testStatic = testStatic
		#调用静态方法
		Person.testStatic()

	3. 运行的过程中删除属性、方法

		a、del 对象.属性名
		b、delattr(对象, "属性名")
		通过以上例子可以得出一个结论：相对于动态语言，静态语言具有严谨性！
		所以，玩动态语言的时候，小心动态的坑！
		
		那么怎么避免这种情况呢？ 请使用__slots__，

	4、__slots__：

		动态语言：可以在运行的过程中，修改代码
		静态语言：编译时已经确定好代码，运行过程中不能修改

		如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加name和age属性。
		为了达到限制的目的，Python允许在定义class的时候，
		定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

		
		>>> class Person(object):
			    __slots__ = ("name", "age")		
		>>> P = Person()
		>>> P.name = "老王"
		>>> P.age = 20
		>>> P.score = 100
		Traceback (most recent call last):
		  File "<pyshell#3>", line 1, in <module>
		  AttributeError: Person instance has no attribute 'score'
		
		
		注意:

		使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，
		对继承的子类是不起作用的
		
		class Test(Person):
			pass
		t = Test()
		t.score = 100


17、属性property：

	1. 私有属性添加getter和setter方法

		class Money(object):
			def __init__(self):
				self.__money = 0

			def getMoney(self):
				return self.__money

			def setMoney(self, value):
				if isinstance(value, int):
					self.__money = value
				else:
					print("error:不是整型数字")

	2.使用property升级getter和setter方法

		class Money(object):
			def __init__(self):
				self.__money = 0

			def getMoney(self):
				return self.__money

			def setMoney(self, value):
				if isinstance(value, int):
					self.__money = value
				else:
					print("error:不是整型数字")

			money = property(getMoney, setMoney)

		运行结果:

			from get_set import Money
			a = Money()
			a.money = 100
			a.getMoney()
				100

	3.使用property取代getter和setter方法
		
		@property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小，
		主要有2个作用:

			将方法转换为只读
			重新实现一个属性的设置和读取方法,可做边界判定

		class Money(object):
			def __init__(self):
				self.__money = 0

			@property
			def money(self):
				return self.__money

			 @money.setter
			def money(self, value):
				if isinstance(value, int):
					self.__money = value
				else:
					print("error:不是整型数字")


"--------------------------------------------------------------------------------"

itertools : python的内建模块，用于高效循环创建迭代器函数

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
			

3、组合迭代器：

	
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





