
"-----------------------------------------------------------------------------"
		
			     第 一 章  基础知识

"-----------------------------------------------------------------------------"

1、数据类型转换：
	
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


	hex(x)                                将一个整数转换为一个十六进制字符串

	oct(x)                                将一个整数转换为一个八进制字符串


2、列表取反

	a = '123456789'
	a[::-1]                               片将从右至左进行而不是从左到右
		'987654321'              

	a[-2] 
		8                                 读取列表中倒数第二个元素(从1开始说)

	a[5:1:-1]                             以反转的顺序取从2到5的元素,
		'6543'							  即先反转a的元素'987654321',再从右第2位(从0开始说)取到第5位



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


































