
"-----------------------------------------------------------------------------"
		
			     第 一 章  基础知识

"-----------------------------------------------------------------------------"

python Number:

	1、Number 类型转换:

		int(x [,base ])         将x转换为一个整数  
		long(x [,base ])        将x转换为一个长整数  
		float(x )               将x转换到一个浮点数  
		complex(real [,imag ])  创建一个复数  
		str(x )                 将对象 x 转换为字符串  
		repr(x )                将对象 x 转换为表达式字符串  
		eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
		tuple(s )               将序列 s 转换为一个元组  
		list(s )                将序列 s 转换为一个列表  
		chr(x )                 将一个整数转换为一个字符  
		unichr(x )              将一个整数转换为Unicode字符  
		ord(x )                 将一个字符转换为它的整数值  
		hex(x )                 将一个整数转换为一个十六进制字符串  
		oct(x )                 将一个整数转换为一个八进制字符串  

		函数                                  说明
		complex(real,[,imag])               创建一个复数

			complex(1,2) 
					(1+2j)
		repr(x)                             将对象 x 转换为字符串

			repr(1)
				'1'
			repr('1')
				"'1'"

		eval(str)                           用来计算字符串中有了python表达式，返回一个对象

			eval('pow(2,2)')
				4

			eval('2 + 2')
				4
	2、Python math 模块、cmath 模块：
	
		Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
		Python math 模块提供了许多对浮点数的数学运算函数。
		Python cmath 模块包含了一些用于复数运算的函数。
		cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
		要使用 math 或 cmath 函数必须先导入：
		
		>>> import math
		>>> dir(math)
		['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 
		'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1',
		'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite',
		'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians',
		'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

		>>> import cmath
		>>> dir(cmath)  
		['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 
		'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj', 'isclose', 'isfinite', 'isinf', 'isnan', 'log', 
		'log10', 'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau']		
	
	3、Python数学函数：
	

		函数	       返回值 ( 描述 )
		abs(x)	     	返回数字的绝对值，如abs(-10) 返回 10
		ceil(x)	     	返回数字的上入整数，如math.ceil(4.1) 返回 5
		cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
		exp(x)		返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
		fabs(x)		返回数字的绝对值，如math.fabs(-10) 返回10.0
		floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
		log(x)		如math.log(math.e)返回1.0,math.log(100,10)返回2.0
		log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
		max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
		min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
		modf(x)		返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
		pow(x, y)	x**y 运算后的值。
		round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
		sqrt(x)		返回数字x的平方根
	
	4、Python随机数函数：
	
		随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
		Python包含以下常用随机数函数：
		函数	 	描述
		choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
		randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
		random()	随机生成下一个实数，它在[0,1)范围内。
		seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
		shuffle(lst)	将序列的所有元素随机排序
		uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

	5、Python三角函数
		Python包括以下三角函数：
		
		函数		描述
		acos(x)		返回x的反余弦弧度值。
		asin(x)		返回x的反正弦弧度值。
		atan(x)		返回x的反正切弧度值。
		atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
		cos(x)		返回x的弧度的余弦值。
		hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
		sin(x)		返回的x弧度的正弦值。
		tan(x)		返回x弧度的正切值。
		degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
		radians(x)	将角度转换为弧度

	6、Python数学常量
		常量	描述
		pi	数学常量 pi（圆周率，一般以π来表示）
		e	数学常量 e，e即自然常数（自然常数）。	
		



2、列表取反

	a = '123456789'
	a[::-1]                               片将从右至左进行而不是从左到右
		'987654321'              

	a[-2] 
		8                                 读取列表中倒数第二个元素(从1开始说)

	a[5:1:-1]                             以反转的顺序取从2到5的元素,
		'6543'			      即先反转a的元素'987654321',再从右第2位(从0开始说)取到第5位



3、字符串常见操作：

	find：检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1

		mystr.find(str, start=0, end=len(mystr))

		a.find('345')
			2
		a.find('345',5)
			-1

	index:跟find()方法一样，只不过如果str不在 mystr中会报一个异常.

		mystr.index(str, start=0, end=len(mystr))

		a.index('345',1)
			2
		a.index('345',3)
			ValueError: substring not found


	count:返回 str在start和end之间 在 mystr里面出现的次数。
	
		mystr.count(str, start=0, end=len(mystr))

		a.count('1')
			1

		a.count('123')
			1

		a.count('123A')
			0


	replace:把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

		mystr.replace(str1, str2,  mystr.count(str1))

		a.replace('1234','abcd')
			'abcd56789'


	split:以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

		name = 'i love the world'
		name.split(' ',2)
			['i', 'love', 'the world']

	capitalize:把字符串的第一个字符大写

		mystr = 'hello world itcast and itcastcpp'
		mystr.capitalize()
			Hello world itcast and itcastcpp

	title:把字符串的每个单词首字母大写

		a = "hello itcast"
		a.title()
			'Hello Itcast'


	startswith:检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False

		mystr.startswith(obj)

		mystr = 'hello world itcast and itcastcpp'
		mystr.startswith('hello')
			True
		mystr.startswith('Hello')
			False

	endswith:检查字符串是否以obj结束，如果是返回True,否则返回 False.

		mystr.endswith(obj)


	lower:转换 mystr 中所有大写字符为小写


	upper:转换 mystr 中的小写字母为大写

	ljust:返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
		mythr = "hello"
		mythr.ljust(10)
			'hello     '

	rjust:返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

		mystr.rjust(width)

	center : 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
		
		mystr.center(width) 

	lstrip : 删除 mystr 左边的空白字符

		mythr = "    hello"
		mythr.lstrip()
			'hello'

	rstrip:删除 mystr 字符串末尾的空白字符

		mystr.rstrip()

	strip :删除mystr字符串两端的空白字符

		a = "\n\t itcast \t\n"
		a.strip()
			'itcast'

	partition:把mystr以str分割成三部分,str前，str和str后

		mystr.partition(str)

		name = 'i love the world'
		name.partition('the')
			('i love ', 'the', ' world')


	splitlines:按照行分隔，返回一个包含各行作为元素的列表

		mystr.splitlines()  

		name = 'hello\nworld'
		name.splitlines()
			['hello', 'world']

	isalpha:如果 mystr 所有字符都是字母 则返回 True,否则返回 False
		mystr.isalpha() 


	isdigit:如果 mystr 只包含数字则返回 True 否则返回 False.
		mystr.isdigit() 


	isalnum:如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
		mystr.isalnum() 
		
	
	isspace:如果 mystr 中只包含空格，则返回 True，否则返回 False.
		mystr.isspace()  

	join:mystr 中每个字符后面插入str,构造出一个新的字符串
		mystr.join(str)


4、 字典的常见操作

	dict = {"name":'zhangsan','sex':'m'}
	
	dir(dict)
		['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

	在我们不确定字典中是否存在某个键而又想获取其值时，可以使用get方法，还可以设置默认值：
	
	name = dict.get('name')
		'name'键不存在，所以name为None

	删除元素:
		
		del dict['name']  删除指定的元素

		dict.clear()   清空
	
	更新合并

		dict.update(dict2)   把字典dict2的键/值对更新到dict里
		

	len():测量字典中，键值对的个数
	len(dict)
		2


	keys():返回一个包含字典所有KEY的列表
	dict.keys()
		dict_keys(['name', 'sex'])

	
	values():返回一个包含字典所有value的列表
	dict.values()
		dict_values(['zhangsan', 'm'])


	items():返回一个包含所有（键，值）元祖的列表
	dict.items()
		dict_items([('name', 'zhangsan'), ('sex', 'm')])

	

5、全局变量和局部变量名字相同问题：

	例子1：
	 a = 100
	 def test1():
		 a = 200
		 print(a)

	test1()
		200


	例子2：

	a = 100 
	def test1():
		print(a)
		a = 200
		print(a)

	test1()
		Traceback (most recent call last):
			UnboundLocalError: local variable 'a' referenced before assignment

	这种就相当于全局变量和局部变量冲突，你有想让当全局有想让做局部，是矛盾的
	解决矛盾的方式，使用global 当做全局变量。

	例子3：

	a = 100 
	def test1():
		global a
		print(a)
		a = 200
		print(a)

	test1()
		100
		200



6、对象的属性

	python中没有像C++中public和private这些关键字区别公有属性和私有属性。
	它是以属性名方式来区分，如果在属性前面加上两个下划线'__',则表明该属性为私有属性（伪私有）。
	
	如下例：
		
		class Animal(object):
			def __init__(self, name='动物', color='白色'):
				self.__name = name
				self.color = color

			def __test(self):
				print(self.__name)
				print(self.color)

			def test(self):
				print(self.__name)
				print(self.color)



		class Dog(Animal):
			def dogTest1(self):
				#print(self.__name) #不能访问到父类的私有属性
			print(self.color)


			def dogTest2(self):
				#self.__test() #不能访问父类中的私有方法
				self.test()


		A = Animal()
		#print(A.__name) #程序出现异常，不能访问私有属性
		print(A._Animal__name)
			'animal'
		print(A.color)
		#A.__test() #程序出现异常，不能访问私有方法
		A.test()

		print("------分割线-----")

		D = Dog(name = "小花狗", color = "黄色")
		D.dogTest1()
		D.dogTest2()

	例如:dir(A)
		
		['_Animal__name', '_Animal__test', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'test']
			
	注意：像Spam类内__X这样的变量名会自动变成_Spam__X,再外面依然可以调用。


7、del 删除属性：

	当有1个变量保存了对象的引用时，此对象的引用计数就会加1
	当使用del删除变量指向的对象时，如果对象的引用计数不是1，比如3，那么此时只会让引用的
	计数减1，变位2，当再次调用del时，变位1，如果再次调用del，此时真的把对象进行删除。

	import sys
	sys.getrefcount(1)  #查看引用个数


8、静态方法和类方法:

	类方法：

		是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，
		对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数。
	
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
		print p.getCountry()         #可以用过实例对象引用
		print People.getCountry()    #可以通过类对象引用
	
		p.setCountry('japan')        #通过类方法修改类属性
	
		print p.getCountry()   
		print People.getCountry()


	静态方法：

		需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数

		class People(object):
			country = 'china'
				
			@staticmethod
			#静态方法
			def getCountry():
				return People.country
									
		print People.getCountry()

	
	  从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，
	  那么通过cls引用的必定是类对象的属性和方法；而实例方法的第一个参数是实例对象self，
	  那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），
	  不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
	  静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。
	
	
9、	__new__方法：

	__new__和__init__的作用：

		class A(object):
			
			def __init__(self):
				print("这是 init 方法")
							
			def __new__(cls):
				print("这是 new 方法")
				return object.__new__(cls)
												  
		A()
			这是 new 方法
			这是 init 方法
			<__main__.A object at 0x7fc993e9f518>
		
	__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
	__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
	可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

	__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以
	完成一些其它初始化的动作，__init__不需要返回值

	我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是
	在有原材料的基础上，加工，初始化商品环节

		
	

10、单例模式:

	单例是什么：

		确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，
		单例模式是一种对象创建型模式。	


	创建单例-保证只有1个对象:

		# 实例化一个单例
		class Singleton(object):
		    __instance = None

			def __new__(cls, age, name):
				
				#如果类数字能够__instance没有或者没有赋值
				#那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
				#能够知道之前已经创建过对象了，这样就保证了只有1个对象
				
				if not cls.__instance:
						cls.__instance = object.__new__(cls)
				
				return cls.__instance


		a = Singleton(18, "dongGe")
		b = Singleton(8, "dongGe")

		id(a)
			140298627282200
		id(b)
			140298627282200

		a.age = 19
		print(b.age)
			19



	创建单例时，只执行1次__init__方法:

		# 实例化一个单例
		class Singleton(object):	
			__instance = None
			__first_init = False
			
			def __new__(cls, age, name):
				if not cls.__instance:
					cls.__instance = object.__new__(cls)
				return cls.__instance

			def __init__(self, age, name):
				if not self.__first_init:
					self.age = age
					self.name = name
					Singleton.__first_init = True

		a = Singleton(18, "dongGe")
		b = Singleton(8, "dongGe")

		print(id(a))
			140298627282200
		print(id(b))
			140298627282200


		print(a.age)
			18
		print(b.age)
			18

		a.age = 19
		print(b.age)
			19

	想创建单例必须使用__new__，代表要实例化的类。__init__只能保证一个实例参数一致，并不能保证一个实例。
	

11、   set 、list 、tuple之间可以相互转换。

		b = [1,2,3,4,5,6,7,8,9]
		set(b)
			{1, 2, 3, 4, 5, 6, 7, 8, 9}

		list(b)
			[1, 2, 3, 4, 5, 6, 7, 8, 9]

		tuple(b)
			(1, 2, 3, 4, 5, 6, 7, 8, 9)


12、python标准一些内建函数：

	abs(x)                       返回x的绝对值
	bin(x)                       将一个整数x转换为二进制字符串
	chr(i)                       返回i对应的ASCII字符
	complex([real[, imag]])      返回一个复数 read+imag1j*，或者将一个字符串或数转换为复数。
	dict()                       返回一个字典。
	dir([object])                无参数时，返回当前局部作用域中的属性；有参数时，返回参数对象的有效属性
	enumerate(sequence，start=0) 返回可迭代对象sequence的（count，value）元组序列，其中count从start开始递增。
	filter(function，iterable)   对可迭代对象iterable中的每个元素调用function函数，返回结果序列。
	float([x])                   返回x对应的浮点数。
	frozenset([iterable])        返回一个不可变的集合对象。
	globals()                    返回全局符号表字典。
	help([object])               返回帮助信息。
	hash(object)                 返回对象object的哈希值。
	id(object)                   返回对象object的唯一标识，通常是object在内存中的地址。
	input([prompt])              读取输入值。
	isinstance(object，classinfo)判断object是否是classinfo的一个实例，或者是其子类的实例
	len(s)                       返回s的长度。
	map(function，iterable，...) 应用function到每一个元素上，返回结果列表。
	max()                        返回最大值。
	min()                        返回最小值。
	next(iterable[,default])     返回迭代器的下一个元素。
	open(name[, mode[, buffering]]) 打开一个文件，返回文件对象。
	pow(x, y[, z])               如果z存在，返回x^y % z，否则返回x^y。
	print()                      输出
	range(stop)                  返回从0到stop-1的列表。
	reload(module)               重新导入模块module。
	type(object)                 返回object对象的类型。

12、请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
	
	list = []
	for i in range(101):
		list.append(i)
	b = []
	for i in range(0,len(list),3):
		b.append(list[i:i+3])
	print(b)
	
	这里面涉及到了几个点：
	1、range()
		range(start, stop[, step])
			start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
			stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
			step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
				
	2、列表在增加元素：
	
		列表不是C语言的数组，不能够使用 list[i]=i
		extend: 通过extend可以将另一个集合中的元素逐一添加到列表中
		  >>> a = [1, 2]
			>>> b = [3, 4]
			>>> a.append(b)
			>>> a
					[1, 2, [3, 4]]
			>>> a.extend(b)
			>>> a
					[1, 2, [3, 4], 3, 4]
					
			append:通过append可以向列表添加元素,这个元素可以是列表、集合、元组，任何对象。
			
				b.append(set(list[i:i+3]))
				b.append(tuple(list[i:i+3]))
				
			insert:insert(index, object) 在指定位置index前插入元素object
				
				>>> a = [0, 1, 2]
				>>> a.insert(1, 3)
				>>> a
						[0, 3, 1, 2]
			
13:请写出一段 Python 代码实现删除一个 list 里面的重复元素

		第一种方法：
			a = [1,2,3,3,4,4,5,6]
			b = dict.fromkeys(a)
			a = list(b)
			print(a)
				
		这里使用了字典的生成方法fromkeys()函数用于创建一个新字典
			
			dict.fromkeys(seq[, value])
				seq -- 字典键值列表。
				value -- 可选参数, 设置键序列（seq）的值。
						
			seq = ('Google', 'Runoob', 'Taobao')
			dict = dict.fromkeys(seq)
				{'Google': None, 'Taobao': None, 'Runoob': None}
			dict = dict.fromkeys(seq, 10)
				{'Google': 10, 'Taobao': 10, 'Runoob': 10}
						
		第二种方法：
			
			使用set,set是非重复的，无序集合。
			可以用list来的排队对set进行排序，list()转换为列表，a.sort来排序
    			a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
    			a=list(set(a)) 
			print(a)
					
							
14、python设计实现遍历目录与子目录,抓取.py文件

	import os
	def getFiles(dir, suffix):
  	res = []
    	for root, dirs, files in os.walk(dir):
      		for filename in files:
        		name, suf = os.path.splitext(filename)
          	  	if suf == suffix:
            	    		res.append(os.path.join(root, filename))
   	print(res)  
	getFiles("./", '.py')						
						
	os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
	os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
	在Unix，Windows中有效。
	
	os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
		
	top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
		root 所指的是当前正在遍历的这个文件夹的本身的地址
		dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
		files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
		
	os模块概述
	1、os.name
		输出字符串指示正在使用的平台。如果是window 则用’nt’表示，对于Linux/Unix用户，它是’posix’。
	2、os.getcwd()
		函数得到当前工作目录，即当前Python脚本工作的目录路径。
	3、os.listdir()
		返回指定目录下的所有文件和目录名。
	4、os.remove()
		删除一个文件。
	5、os.system()
		运行shell命令。
	6、os.path.split()
		函数返回一个路径的目录名和文件名
		os.path.split(‘C:\Python25\abc.txt’) 
		(‘C:\Python25’, ‘abc.txt’)

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
		
	10、os.path.normpath(path):规范path字符串形式
		
	11、os.path.getsize(name):获得文件大小，如果name是目录返回0L

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

			
15、写出一个函数,给定参数 n,生成含有n个元素值为1~n的数组,元素顺序随机,但值不重复

	import random
	def random_list(n):
    		list =random.sample(range(1,n+1),n)
    		return list

	print(random_list(6))			
			
	random.seed(a=None, version=2)  # 初始化伪随机数生成器。如果未提供a或者a=None，则使用系统时间为种子。如果a是一个整数，则作为种子。
 	random.getstate()  # 返回一个当前生成器的内部状态的对象
 	random.setstate(state)  # 传入一个先前利用getstate方法获得的状态对象，使得生成器恢复到这个状态。
 	random.getrandbits(k)  # 返回range(0,2**k)之间的一个整数，相当于randrange(0,2**k)
 	random.randrange(stop)  # 返回range(0,stop)之间的一个整数
 	random.randrange(start, stop[, step])  # 返回range[start,stop)之间的一个整数，可加step，跟range(0,10,2)类似
 	random.randint(a, b)  # 返回range[a,b]之间的一个整数，等价于然的range(a,b+1)
 	random.choice(seq)  # 从非空序列seq中随机选取一个元素。如果seq为空则弹出 IndexError异常。
	random.choices(population, weights=None, *, cum_weights=None, k=1)  # 3.6版本新增。从population集群中随机抽取K个元素（可重复）。
				weights是相对权重列表，cum_weights是累计权重，两个参数不能同时存在。
 	random.shuffle(x[, random])  # 随机打乱序列x内元素的排列顺序。只能针对可变的序列，对于不可变序列，请使用下面的sample()方法。
 	random.sample(population, k)  # 从population样本或集合中随机抽取K个不重复的元素形成新的序列。
		常用于不重复的随机抽样。返回的是一个新的序列，不会破坏原有序列。要从一个整数区间随机抽取一定数量的整数，
		请使用sample(range(10000000), k=60)类似的方法，这非常有效和节省空间。如果k大于population的长度，则弹出ValueError异常。
 	random.random()  # 返回一个介于左闭右开[0.0, 1.0)区间的浮点数
 	random.uniform(a, b)  # 返回一个介于a和b之间的浮点数。如果a>b，则是b到a之间的浮点数。这里的a和b都有可能出现在结果中。
 
 
16：说明os,sys模块不同，并列举常用的模块方法？

	os：  提供一种方便的使用操作系统函数的方法。 
	sys： 提供访问由解释器使用或维护的变量和在与解释器交互使用到的函数		
		
	os 常用方法

		方法	使用
		os.remove()	删除文件
		os.rename()	重命名文件
		os.walk()	生成目录树下的所有文件名
		os.chdir()	改变目录
		os.mkdir/makedirs	创建目录/多层目录
		os.rmdir/removedirs	删除目录/多层目录
		os.listdir()	列出指定目录的文件
		os.getcwd()	取得当前工作目录
		os.chmod()	改变目录权限
		os.path.basename()	去掉目录路径，返回文件名
		os.path.dirname()	去掉文件名，返回目录路径
		os.path.join()	将分离的各部分组合成一个路径名
		os.path.split()	返回（dirname(),basename())元组
		os.path.splitext()	(返回filename,extension)元组
		os.path.getatime\ctime\mtime	分别返回最近访问、创建、修改时间
		os.path.getsize()	返回文件大小
		os.path.exists()	是否存在
		os.path.isabs()	是否为绝对路径
		os.path.isdir()	是否为目录
		os.path.isfile()	是否为文件
			
			
	sys 常用方法
		方法	使用
		sys.argv()	命令行参数List，第一个元素是程序本身路径
		sys.modules.keys()	返回所有已经导入的模块列表
		sys.exc_info()	获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
		sys.exit(n)	退出程序，正常退出时exit(0)
		sys.hexversion	获取Python解释程序的版本值，16进制格式如：0x020403F0
		sys.version	获取Python解释程序的版本信息
		sys.maxint	最大的Int值
		sys.maxunicode	最大的Unicode值
		sys.modules	返回系统导入的模块字段，key是模块名，value是模块
		sys.path	返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
		sys.platform	返回操作系统平台名称
		sys.stdout	标准输出
		sys.stdin	标准输入
		sys.stderr	错误输出
		sys.exc_clear()	用来清除当前线程所出现的当前的或最近的错误信息
		sys.exec_prefix	返回平台独立的python文件安装的位置
		sys.byteorder	本地字节规则的指示器，big-endian平台的值是’big’,little-endian平台的值是’little’
		sys.copyright	记录python版权相关的东西
		sys.api_version	解释器的C的API版本
		sys.getdefaultencoding()	返回当前你所用的默认的字符编码格式
		sys.getfilesystemencoding()	返回将Unicode文件名转换成系统文件名的编码的名字
		sys.setdefaultencoding(name)	用来设置当前默认的字符编码，如果name和任何一个可用的编码都不匹配，
						抛出 LookupError，这个函数只会被site模块的sitecustomize
		sys.builtin_module_names	Python解释器导入的模块列表
		sys.executable	Python解释程序路径
		sys.getwindowsversion()	获取Windows的版本
		sys.stdin.readline()	从标准输入读一行，sys.stdout.write(“a”) 屏幕输出a
					
					
					
"------------------------------------------------------------------------------------"
	
				第二部分      Python 高级

"------------------------------------------------------------------------------------"

元类：
	
	1、元类
	
		在大多数编程语言中，类就是一组用来描述如何生成一个对象的代码段。在Python中这一点仍然成立：
		但是，Python中的类还远不止如此。类同样也是一种对象。是的，没错，就是对象。
		只要你使用关键字class，Python解释器在执行的时候就会创建一个对象。
			
		下面的代码段：
			>>> class ObjectCreator(object):
		       		pass
		将在内存中创建一个对象，名字就是ObjectCreator。
		这个对象（类对象ObjectCreator）拥有创建对象（实例对象）的能力。
		但是，它的本质仍然是一个对象，于是乎你可以对它做如下的操作：
	
			你可以将它赋值给一个变量
			你可以拷贝它
			你可以为它增加属性
			你可以将它作为函数参数进行传递		
					
		print ObjectCreator     # 你可以打印一个类，因为它其实也是一个对象
		echo(ObjectCreator)                 # 你可以将类做为参数传给函数
		ObjectCreator.new_attribute = 'foo' #  你可以为类增加属性
		ObjectCreatorMirror = ObjectCreator # 你可以将类赋值给一个变量		
					
	2、使用type创建类：
	
		当你使用class关键字时，Python解释器自动创建这个对象。
		还记得内建函数type吗？这个古老但强大的函数能够让你知道一个对象的类型是什么，就像这样：
		
			>>> print type(1) #数值的类型
				<class 'int'>
			>>> print type("1") #字符串的类型
				<class 'str'>
			>>> print type(ObjectCreator) #类的类型
				<class 'type'>
						
		type还有一种完全不同的功能，动态的创建类。
		type可以接受一个类的描述作为参数，然后返回一个类。
		（要知道，根据传入参数的不同，同一个函数拥有两种完全不同的用法是一件很傻的事情，但这在Python中是为了保持向后兼容性）
			
		type可以像这样工作：
			type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)			
				
		比如下面的代码：	
			class Test: #定义了一个Test类
	   	   		pass
	   	
			Test() #创建了一个Test类的实例对象
				<__main__.Test at 0x10d3f8438>
			
		可以手动像这样创建：		
		 	Test2 = type("Test2",(),{}) #定了一个Test2类
	   			
			Test2() #创建了一个Test2类的实例对象
		 		<__main__.Test2 at 0x10d406b38>	
					
	3. 使用type创建带有属性的类				
					
		type 接受一个字典来为类定义属性，因此			
		Foo = type('Foo', (), {'bar':True})
			
		可以翻译为：
		class Foo(object):
	      		bar = True
					
		当然，你可以向这个类继承，所以，如下的代码：
		class FooChild(Foo):
			pass		
			
		就可以写成：
		FooChild = type('FooChild', (Foo,),{})
			print FooChild
				<class '__main__.FooChild'>
		print FooChild.bar   # bar属性是由Foo继承而来
			True		
					
		注意：
			type的第2个参数，元组中是父类的名字，而不是字符串添加的属性是类属性，并不是实例属性
	
	4、使用type创建带有方法的类
	
		最终你会希望为你的类增加方法。只需要定义一个有着恰当签名的函数并将其作为属性赋值就可以了。
		
		添加实例方法：
		def echo_bar(self): #定义了一个普通的函数
	    		print(self.bar)
			
		FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
				 #让FooChild类中的echo_bar属性，指向了上面定义的函数
	
		添加静态方法：
		 @staticmethod
	     	 def testStatic():
	     		print("static method ....")
	     		
	 	Foochild = type('Foochild', (Foo,), {"echo_bar":echo_bar, "testStatic":testStatic})
	 		
	 	添加类方法：
	 	@classmethod
	    	def testClass(cls):
	    		print(cls.bar)
	    				
	    	Foochild = type('Foochild', (Foo,), {"echo_bar":echo_bar, "testStatic":testStatic, "testClass":testClass})
	    
	   你可以看到，在Python中，类也是对象，你可以动态的创建类。
	   这就是当你使用关键字class时Python在幕后做的事情，而这就是通过元类来实现的。 
	   
	   
	5、到底什么是元类
		
		元类就是用来创建类的“东西”。你创建类就是为了创建类的实例对象，不是吗？
		但是我们已经学习到了Python中的类也是对象。
		
		元类就是用来创建这些类（对象）的，元类就是类的类，你可以这样理解为：
		MyClass = MetaClass() #使用元类创建出一个对象，这个对象称为“类”
		MyObject = MyClass() #使用“类”来创建出实例对象
		
		你已经看到了type可以让你像这样做：
		MyClass = type('MyClass', (), {})
		
		这是因为函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类。
		现在你想知道那为什么type会全部采用小写形式而不是Type呢？
		好吧，我猜这是为了和str保持一致性，str是用来创建字符串对象的类，
		而int是用来创建整数对象的类。
		type就是创建类对象的类。
		你可以通过检查__class__属性来看到这一点。
		Python中所有的东西，注意，我是指所有的东西——都是对象。
		这包括整数、字符串、函数以及类。
		它们全部都是对象，而且它们都是从一个类创建而来，这个类就是type。
	 
	 
	6、__metaclass__属性：
	
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
		现在的问题就是，你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？
		type，或者任何使用到type或者子类化type的东东都可以。   
	  
	7、自定义元类 
	
		元类的主要目的就是为了当创建类时能够自动地改变类。
		通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类。 
	    
	  	假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。
	  	有好几种方法可以办到，但其中一种就是通过在模块级别设定__metaclass__。
	  	采用这种方法，这个模块中的所有类都会通过这个元类来创建，
	  	我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。
	
		幸运的是，__metaclass__实际上可以被任意调用，它并不需要是一个正式的类。
		所以，我们这里就先以一个简单的函数作为例子开始。  
	  
		python2中：
			#-*- coding:utf-8 -*-
			def upper_attr(future_class_name, future_class_parents, future_class_attr):
			#遍历属性字典，把不是__开头的属性名字变为大写
				newAttr = {}
			    	for name,value in future_class_attr.items():
			      		if not name.startswith("__"):
			        		newAttr[name.upper()] = value
			
			   		 #调用type来创建一个类
			    	return type(future_class_name, future_class_parents, newAttr)
			
				
			class Foo(object):
				
				__metaclass__ = upper_attr #设置Foo类的元类为upper_attr
			    	bar = 'bip'
				print(hasattr(Foo, 'bar'))
				print(hasattr(Foo, 'BAR'))
			
			f = Foo()
				print(f.BAR)
			    
		python3中：
			#-*- coding:utf-8 -*-
			def upper_attr(future_class_name, future_class_parents, future_class_attr):
			
				#遍历属性字典，把不是__开头的属性名字变为大写
				newAttr = {}
			    	for name,value in future_class_attr.items():
			        	if not name.startswith("__"):
			            		newAttr[name.upper()] = value
			
			    	#调用type来创建一个类
				return type(future_class_name, future_class_parents, newAttr)
			
			class Foo(object, metaclass=upper_attr):
				bar = 'bip'
				print(hasattr(Foo, 'bar'))
				print(hasattr(Foo, 'BAR'))
			
			f = Foo()
			print(f.BAR)	    
			    
	  现在让我们再做一次，这一次用一个真正的class来当做元类。  
	  #coding=utf-8
	
		class UpperAttrMetaClass(type):
	    		# __new__ 是在__init__之前被调用的特殊方法
	    		# __new__是用来创建对象并返回之的方法
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
				#bar = 'bip'
				
				print(hasattr(Foo, 'bar'))
				# 输出: False
				print(hasattr(Foo, 'BAR'))
				# 输出:True
				
				f = Foo()
				print(f.BAR)
				# 输出:'bip'  
	 
		就是这样，除此之外，关于元类真的没有别的可说的了。但就元类本身而言，它们其实是很简单的：
	
			1、拦截类的创建
			2、修改类
			3、返回修改之后的类   
	    

python是动态语言：

1、动态语言的定义：

		动态编程语言 是 高级程序设计语言 的一个类别，在计算机科学领域已被广泛应用。
		它是一类 在运行时可以改变其结构的语言 ：例如新的函数、对象、甚至代码可以被引进，
		已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力。
		例如JavaScript便是一个动态语言，除此之外如 PHP 、 Ruby 、 Python 等也都属于动态语言，
		而 C 、 C++ 等语言则不属于动态语言。----来自 维基百科    

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
		>>>
		
		注意:
		使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
 		
 		class Test(Person):
         pass
    
		t = Test()
		t.score = 100
    
    
生成器：

	1、什么是生成器：
	通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
	而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
	那后面绝大多数元素占用的空间都白白浪费了。所以，如果列表元素可以按照某种算法推算出来，
	那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
	从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
  
  	2、创建生成器方法1 
 	
	要创建一个生成器，有很多种方法。第一种方法很简单，只要把一个列表生成式的 [ ] 改成 ( )
	
	L = [ x*2 for x in range(5)]
	G = ( x*2 for x in range(5))
	
	创建 L 和 G 的区别仅在于最外层的 [ ] 和 ( ) ， L 是一个列表，而 G 是一个生成器。
	我们可以直接打印出L的每一个元素，但我们怎么打印出G的每一个元素呢？
	如果要一个一个打印出来，可以通过 next() 函数获得生成器的下一个返回值。

  	生成器保存的是算法，每次调用 next(G) ，就计算出 G 的下一个元素的值，
  	直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的异常。
  	当然，这种不断调用 next() 实在是太变态了，正确的方法是使用 for 循环，
  	因为生成器也是可迭代对象。所以，我们创建了一个生成器后，基本上永远不会调用 next() ，
  	而是通过 for 循环来迭代它，并且不需要关心 StopIteration 异常。	 
    
    3. 创建生成器方法2：
  
  	generator非常强大。如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，
	还可以用函数来实现，包含yield语句的函数。
  
  	总结：
  
		生成器是这样一个函数，它记住上一次返回时在函数体中的位置。
		对生成器函数的第二次（或第 n 次）调用跳转至该函数中间，而上次调用的所有局部变量都保持不变。
		生成器不仅“记住”了它数据状态；生成器还“记住”了它在流控制构造（在命令式编程中，这种构造不只是数据值）中的位置。

	
	生成器的特点：
		节约内存
		迭代到下一次的调用时，所使用的参数都是第一次所保留下的，即是说，在整个所有函数调用的参数都是第一次所调用时保留的，而不是新创建的
    
    
迭代器：

	迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
	迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。    
    
    1. 可迭代对象
  
  	以直接作用于 for 循环的数据类型有以下几种：

		一类是集合数据类型，如 list 、 tuple 、 dict 、 set 、 str 等；
		一类是 generator ，包括生成器和带 yield 的generator function。
		这些可以直接作用于 for 循环的对象统称为可迭代对象： Iterable 。  
    
    2. 判断是否可以迭代
  
  	可以使用 isinstance() 判断一个对象是否是 Iterable 对象：
  	 from collections import Iterable
			
			isinstance([], Iterable)
				True
			
			isinstance({}, Iterable)
			 	True
				
			isinstance('abc', Iterable)
				True
			
			isinstance((x for x in range(10)), Iterable)
				True
			
			isinstance(100, Iterable)
				False
		
		而生成器不但可以作用于 for 循环，还可以被 next() 函数不断调用并返回下一个值，
		直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。  
			    
	3.迭代器：
	
		可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
		可以使用 isinstance() 判断一个对象是否是 Iterator 对象：
	
		from collections import Iterator

		isinstance((x for x in range(10)), Iterator)
			True
		
		isinstance([], Iterator)
			False
		
		isinstance({}, Iterator)
			False
		
		isinstance('abc', Iterator)
			False
		
		isinstance(100, Iterator)
			False

	4.iter()函数：
	
		生成器都是 Iterator 对象，但 list 、 dict 、 str 虽然是 Iterable ，却不是 Iterator 。
		把 list 、 dict 、 str 等 Iterable 变成 Iterator 可以使用 iter() 函数：
		
		from collections import Iterator
		isinstance(iter([]), Iterator)
 			True

		isinstance(iter('abc'), Iterator)
			True
			    
    总结：
   
		凡是可作用于 for 循环的对象都是 Iterable 类型；
		凡是可作用于 next() 函数的对象都是 Iterator 类型
		集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，
		不过可以通过 iter() 函数获得一个 Iterator 对象。
		
		
闭包：

	1、什么是闭包？
	
	在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
	
	闭包涉及到数据函数里面属性使用的问题，想要改变外面函数的变量，必须使用nonlocal或者global

	def test(number):

		def test_in(numer_in):
			print("in test_in 函数，number_in is %d" % number_in)
			return number+number_in

		return test_in

	

	给test函数赋值，这个20就是给参数number
	ret = test(20)

	#注意这里的100其实给参数number_in
	print(ret(100))

	
	2、闭包再理解

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

	3、 看一个闭包的实际例子：

	def line_conf(a, b):
		def line(x):
			return a*x + b
		return line

		
	line1 = line_conf(1, 1)
	line2 = line_conf(4, 5)
	print(line1(5))
	print(line2(5))

	这个例子中，函数line与变量a,b构成闭包。在创建闭包的时候，
	我们通过line_conf的参数a,b说明了这两个变量的取值，
	这样，我们就确定了函数的最终形式(y = x + 1和y = 4x + 5)。
	我们只需要变换参数a,b，就可以获得不同的直线表达函数。
	由此，我们可以看到，闭包也具有提高代码可复用性的作用。


	闭包思考：

		1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
		2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存


装饰器：

	1、装饰器(decorator)功能
		
		引入日志
		函数执行时间统计
		执行函数前预备理
		执行函数后清理功能
		权限校验等场景
		缓存


	2、无参数的函数

	from time import ctime,sleep

	def timefunc(func):

		def wrappedfunc():
			print("%s called at %s"%(func.__name__,ctime()))
			func()
		return wrappedfunc

	@timefunc
	def foo():
		print('I am foo')

	foo()
	sleep(2)
	foo()

	上面代码理解装饰器执行行为可理解成
	foo = timefun(foo)
	foo先作为参数赋值给func后,foo接收指向timefun返回的wrappedfunc
	foo()
	调用foo(),即等价调用wrappedfunc()
	内部函数wrappedfunc被引用，所以外部函数的func变量(自由变量)并没有释放
	func里保存的是原foo函数对象


	3、被装饰的函数有参数
	
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


	foo(3,5,7)


	4、被装饰的函数有不定长参数：

	from time import ctime, sleep

	def timefun(func):
		def wrappedfunc( *args, **kwargs):
			print("%s called at %s"%(func.__name__, ctime()))
			func( *args, **kwargs)
		return wrappedfunc

	@timefun
	def foo(a, b, c):
		print(a+b+c)

	foo(3,5,7)


	
	5、类装饰器

	装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。
	在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了 __call__() 方法，
	那么这个对象就是callable的。

		class Test():
			def __call__(self):
				print('call me!')
							
		t = Test()
		t()  # call me'')


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

	4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就
	  需要一个实例属性来保存这个函数体的引用 所以才有了self.__func = func这句代码，
	  从而在调用__call__方法中能够调用到test之前的函数体
			
	@Test
	def test():
		print("----test---")
	test()
	showpy()     #如果把这句话注释，重新运行程序，依然会看到"--初始化--"

	
	运行结果如下：
		---初始化---
		func name is test
		---装饰器中的功能---
		----test---
	


作用域:

	LEGB 规则:
	Python 使用 LEGB 的顺序来查找一个符号对应的对象
	locals -> enclosing function -> globals -> builtins

	locals，当前所在命名空间（如函数、模块），函数的参数也属于命名空间内的变量
	enclosing，外部嵌套函数的命名空间（闭包中常见）
	globals，全局变量，函数定义所在模块的命名空间
	builtins，内建模块的命名空间。

		Python 在启动的时候会自动为我们载入很多内建的函数、类，
		比如 dict，list，type，print，这些都位于 __builtin__ 模块中，
		可以使用 dir(__builtin__) 来查看。
		这也是为什么我们在没有 import任何模块的情况下，
		就能使用这么多丰富的函数和功能了。

		在Python中，有一个内建模块，该模块中有一些常用函数;在Python启动后，
		且没有执行程序员所写的任何代码前，Python会首先加载该内建函数到内存。
		另外，该内建模块中的功能可以直接使用，不用在其前添加内建模块前缀，
		其原因是对函数、变量、类等标识符的查找是按LEGB法则，其中B即代表内建模块
		比如：内建模块中有一个abs()函数，其功能求绝对值，如abs(-20)将返回20。



==、is:

	a = [11,22,33]
	b = a

	a == b
		True
	
	a is b
		True

	c = copy.deepcopy(a)

	a == c 
		True

	a is c
		False


	is 是比较两个引用是否指向了同一个对象（引用比较）。
	== 是比较两个对象是否相等。


深拷贝、浅拷贝：

	1、浅拷贝:
		
		浅拷贝是对于一个对象的顶层拷贝
		通俗的理解是：拷贝了引用，并没有拷贝内容

		a = [11,22,33]
		b = a

		id(a)
			139862797085256
		id(b)
			139862797085256

		a.append(44)
			[11, 22, 33, 44]
		b
			[11, 22, 33, 44]

		id(a)
			139862797085256
		id(b)
			139862797085256


	2、深拷贝:

		深拷贝是对于一个对象所有层次的拷贝(递归)

		import copy

		a = [11,22,33]

		b = copy.deepcopy(b)
		
		id(a)
			139862797085256
		id(b)
			139862797151560

		a.append(55)
			[11, 22, 33, 44]
		b
			[11,22,33]

	3、浅拷贝对不可变类型和可变类型的copy不同:

		a = [11,22,33]
		b = copy.copy(a)
		
		a.append(44)
			[11, 22, 33, 44]
		b
			[11, 22, 33]


		分片表达式可以赋值一个序列:
			a = "abc"
			b = a[:]

		字典的copy方法可以拷贝一个字典
		
			d = dict(name="zhangsan", age=27)	
			co = d.copy()
			修改字典 d['age'] = 23


		有些内置函数可以生成拷贝(list):
			a = list(range(10))
			b = list(a)

		
		copy模块中的copy函数:

			import copy
			a = (1,2,3)

			b = copy.copy(a)

		

进制、位运算:

	1、进制间转换

	#10进制转为2进制
	>>> bin(10)
	'0b1010'
	
	#2进制转为10进制
	>>> int("1001",2)
	9
	
	
	#10进制转为16进制
	>>> hex(10)
	'0xa'
	
	#16进制到10进制
	>>> int('ff', 16)
	255
	
	>>> int('0xab', 16)
	171
	
	#16进制到2进制
	>>> bin(0xa)
	'0b1010'

	#10进制到8进制
	>>> oct(8)
	'010'
	
	
	#2进制到16进制
	>>> hex(0b1001)
	'0x9'


	2、位运算

		& 按位与
		| 按位或
		^ 按位异或
		~ 按位取反
		<< 按位左移
		>> 按位右移

		用途: 直接操作二进制,省内存,效率高

		1）<< 按位左移
			各二进位全部左移n位,高位丢弃,低位补0
			左移1位相当于 乘以2
			用途:快速计算一个数乘以2的n次方 (8<<3 等同于8*2^3)
		
		2)>> 右移

			各二进位全部右移n位,保持符号位不变
			右移1位相当于 除以2
			x 右移 n 位就相当于除以2的n次方 用途:快速计算一个数除以2的n次方 (8>>3 等同于8/2^3)

		3)& 按位与
			
			全1才1否则0 :只有对应的两个二进位均为1时,结果位才为1,否则为0

		4) | 按位或

			有1就1 只要对应的二个二进位有一个为1时,结果位就为1,否则为0

		5) ^ 按位异或

			不同为1 当对应的二进位相异(不相同)时,结果为1,否则为0


私有化：
	
	xx: 公有变量
	_x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
	__xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
	__xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字
	xx_:单后置下划线,用于避免与Python关键词的冲突

	__xx通过name mangling（名字重整(目的就是以防子类意外重写基类的方法或者属性)
	如：_Class__object）机制就可以访问private了。
	


垃圾回收：

	Python的垃圾回收机制是：
		python采用的是引用计数机制为主，标记-清除和分代收集两种机制为辅的策略
	
	引用计数机制：
	
		python里每一个东西都是对象，它们的核心就是一个结构体：PyObject

		typedef struct_object {

			int ob_refcnt;
			struct_typeobject *ob_type;
		} PyObject;

	
		PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。
		当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少。

	引用计数机制的优点：
		
		简单
		实时性：一旦没有引用，内存就直接释放了。不用像其他机制等到特定时机。
		实时性还带来一个好处：处理回收内存的时间分摊到了平时。

	
	引用计数机制的缺点：

		维护引用计数消耗资源
		循环引用

			list1 = []
			list2 = []
			list1.append(list2)
			list2.append(list1)

		list1与list2相互引用，如果不存在其他对象对它们的引用，list1与list2的引用计数也仍然为1，
		所占用的内存永远无法被回收，这将是致命的。 对于如今的强大硬件，缺点1尚可接受，
		但是循环引用导致内存泄露，注定python还将引入新的回收机制。(标记清除和分代收集)

	
	有三种情况会触发垃圾回收：

		1、调用gc.collect(),
		2、当gc模块的计数器达到阀值的时候。
		3、程序退出的时候

	

gc模块常用功能解析：

	gc模块提供一个接口给开发者设置垃圾回收的选项。
	采用引用计数的方法管理内存的一个缺陷是循环引用，而gc模块的一个主要功能就是解决循环引用的问题。

	1、常用函数：

		gc.set_debug(flags) 设置gc的debug日志，一般设置为gc.DEBUG_LEAK
		gc.collect([generation]) 显式进行垃圾回收，可以输入参数，0代表只检查第一代的对象，
				1代表检查一，二代的对象，2代表检查一，二，三代的对象，如果不传参数，
				执行一个full collection，也就是等于传2。 返回不可达（unreachable objects）对象的数目
		
		gc.get_threshold() 获取的gc模块中自动执行垃圾回收的频率。
		gc.set_threshold(threshold0[, threshold1[, threshold2]) 设置自动执行垃圾回收的频率。
		gc.get_count() 获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表


模块进阶:

	常用标准库:

	标准库	             说明
	builtins	    内建函数默认加载
	os	              操作系统接口
	sys	            Python自身的运行环境
	functools	       常用的工具
	json	        编码和解码 JSON 对象
	logging            记录日志，调试
	multiprocessing	      多进程
	threading	          多线程
	copy	               拷贝
	time	               时间
	datetime	        日期和时间
	calendar	           日历
	hashlib	            加密算法
	random	           生成随机数
	re	             字符串正则匹配
	socket	        标准的 BSD Sockets API
	shutil	         文件和目录管理
	glob	       基于文件通配符搜索



	常用扩展库:

	扩展库               	说明
	requests	    使用的是 urllib3，继承了urllib2的所有特性
	urllib	           基于http的高层库
	scrapy	                 爬虫
	beautifulsoup4	   HTML/XML的解析器
	celery	          分布式任务调度模块
	redis	                 缓存
	Pillow(PIL)	          图像处理
	xlsxwriter	      仅写excle功能,支持xlsx
	xlwt	          仅写excle功能,支持xls ,2013或更早版office
	xlrd              	仅读excle功能
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



调试:

	pdb 
	pdb是基于命令行的调试工具，非常类似gnu的gdb（调试c/c++）。

		命令      	简写命令	       作用
		break	        b	         设置断点
		continue	    c	         继续执行程序
		list	        l          	 查看当前行的代码段
		step	        s	         进入函数
		return	        r	         执行代码直到从当前函数返回
		quit	        q	         中止并退出
		next	        n	         执行下一行
		print	        p	         打印变量的值
		help	        h            帮助
		args	        a	         查看传入参数
		回车	                     重复上一条命令
		break	        b          	 显示所有断点
		break lineno	b lineno	在指定行设置断点
		break file:lineno	b file:lineno	在指定文件的行设置断点
		clear num		            删除指定断点
		bt		                    查看函数调用栈帧


	
		执行时调试：

			程序启动，停止在第一行等待单步调试。
	
			python -m pdb some.py


		pdb 调试有个明显的缺陷就是对于多线程，远程调试等支持得不够好，
		同时没有较为直观的界面显示，不太适合大型的 python 项目。
		而在较大的 python 项目中，这些调试需求比较常见，因此需要使用更为高级的调试工具。
	
	日志调试:

		print大法

	

