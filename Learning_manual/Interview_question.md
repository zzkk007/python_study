
1、简述函数式编程

	函数式编程（英语：functional programming）或称函数程序设计，又称泛函编程.
	有些人喜欢称为Pythonic，是一种编程典范，
	它将电脑运算视为数学上的函数计算，并且避免使用程序状态以及易变对象。
	函数编程语言最重要的基础是λ演算（lambda calculus）。
	而且λ演算的函数可以接受函数当作输入（引数）和输出（传出值）。

	比起指令式编程，函数式编程更加强调程序执行的结果而非执行的过程，
	倡导利用若干简单的执行单元让计算结果不断渐进，逐层推导复杂的运算，而不是设计一个复杂的执行过程。


	什么是函数式编程？
		
		函数式编程使用一系列的函数解决问题。函数仅接受输入并产生输出，不包含任何能影响产生输出的内部状态。
		任何情况下，使用相同的参数调用函数始终能产生同样的结果。

		在一个函数式的程序中，输入的数据“流过”一系列的函数，每一个函数根据它的输入产生输出。
		函数式风格避免编写有“边界效应”(side effects)的函数：修改内部状态，或者是其他无法反应在输出上的变化。
		完全没有边界效应的函数被称为“纯函数式的”(purely functional)。
		避免边界效应意味着不使用在程序运行时可变的数据结构，输出只依赖于输入。

	为什么使用函数式编程？
		
		模块化 
			函数式编程推崇简单原则，一个函数只做一件事情，将大的功能拆分成尽可能小的模块。
			小的函数更易于阅读和检查错误。
		
		组件化 	
			小的函数更容易加以组合形成新的功能。

		易于调试 
			细化的、定义清晰的函数使得调试更加简单。当程序不正常运行时，
			每一个函数都是检查数据是否正确的接口，能更快速地排除没有问题的代码，定位到出现问题的地方。
	
		易于测试
			不依赖于系统状态的函数无须在测试前构造测试桩，使得编写单元测试更加容易。

		更高的生产率 
			函数式编程产生的代码比其他技术更少（往往是其他技术的一半左右），并且更容易阅读和维护。

	
	在函数式编程中，函数是基本单位，变量只是一个名称，而不是一个存储单元。除了匿名函数外，
	Python还使用内建函数fliter(),map(),reduce(),zip()函数来支持函数式编程。
		
		reduce():函数会对参数序列中元素进行累积。
			
			函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
			用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
			得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

		reduce() 函数语法：
		
			reduce(function, iterable[, initializer])

				function -- 函数，有两个参数
				iterable -- 可迭代对象
				initializer -- 可选，初始参数

			返回函数计算结果。


			from functools import reduce

			def add(x, y) :            # 两数相加
				 return x + y
			
			reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
																					  
		    reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
				15

			reduce(lambda x, y: x+y, [1,2,3,4,5],100) 
				115


		fliter(): 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
			
			该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
			然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
		
		以下是 filter() 方法的语法:
				
				filter(function, iterable)
	
					function -- 判断函数。
					iterable -- 可迭代对象。
					返回列表。

			def is_odd(n):
			    return n % 2 == 1
				 
			newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			print(newlist)
		
			[1, 3, 5, 7, 9]


		map():会根据提供的函数对指定序列做映射。

			第一个参数 function 以参数序列中的每一个元素调用 function 函数，
			返回包含每次 function 函数返回值的新列表。

			map() 函数语法：

				map(function, iterable, ...)

					function -- 函数，有两个参数
					iterable -- 一个或多个序列

					返回值
						Python 2.x 返回列表。
						Python 3.x 返回迭代器。

			def square(x) :            # 计算平方数
				return x ** 2
																 
			map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
				[1, 4, 9, 16, 25]
			map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
				[1, 4, 9, 16, 25]
			
			提供了两个列表，对相同位置的列表数据进行相加			 
			
			map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
				[3, 7, 11, 15, 19]

		zip():函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
			  然后返回由这些元组组成的列表。
		
			  如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
			  利用 * 号操作符，可以将元组解压为列表。
		
			  zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，
			  zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
		
			  语法：
				zip([iterable, ...])
					iterabl -- 一个或多个迭代器;

		     >>>a = [1,2,3]
			 >>> b = [4,5,6]
			 >>> c = [4,5,6,7,8]
			 >>> zipped = zip(a,b)     # 打包为元组的列表
			 [(1, 4), (2, 5), (3, 6)]
			 >>> zip(a,c)              # 元素个数与最短的列表一致
			 [(1, 4), (2, 5), (3, 6)]
			 >>> zip( *zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
			 [(1, 2, 3), (4, 5, 6)]
					

2、什么是匿名函数，匿名函数有什么局限性？

	
	Lambda是一个表达式，也可以说它是一个匿名函数。通常用在函数体比较简单的函数上。
	匿名函数顾名思义就是函数没有名字，
	因此不用担心函数名冲突。不过Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。

	优点

		在普通代码里几行的代码，在Lambda中只需要一行就可以解决。所以代码比以前更简洁了
		可以在某一个方法内部定义，这样可以提高操作的便捷性
		
		def是一个语句，Lambda是一个表达式，可以用在def不能够使用的地方。

	缺点

		Lambda是一个匿名函数，因为是匿名，所以可读性变差了
		有时候有多个Lambda嵌套（就像实例中的第3点一样），让程序变得难以理解
		
    表达式和语句：
        Python 代码由表达式和语句组成，并由 Python 解释器负责执行。

        其中，“表达式”是一个值，它的结果一定是一个 Python 对象。    
        当 Python 解释器计算它时结果可以是任何对象。
        常见了 Python 表达式操作符有：
            算术运算符、比较运行符、逻辑运算符(or, and, not )、成员关系符(in, not in)、
            对象实例测试符(is, not is)、位运算符(&、|、^、<<、>>)
            
        结果不是对象的代码则称为“语句”。它们表示的是一个"动作"而不是生产或者返回一个值。
        常见的 Python 语句有：
            赋值语句（=）
            调用
            print;打印对象
            if/elif/else：条件判断
            for/else：序列迭代
            while/else：普通迭代
            pass: 占位符
            break
            continue
            def
            return
            yield
            global
            raise
            import
            from
            等等
            
3、如何捕获异常，常用的异常机制有哪些？

	如果我们没有对异常进行任何预防，那么在程序执行的过程中发生异常，就会中断程序，
	调用python默认的异常处理器，并在终端输出异常信息。

	try...except...finally语句:当try语句执行时发生异常，回到try语句层，寻找后面是否有except语句。
	找到except语句后，会调用这个自定义的异常处理器。except将异常处理完毕后，程序继续往下执行。
	finally语句表示，无论异常发生与否，finally中的语句都要执行。

	assert语句：判断assert后面紧跟的语句是True还是False，如果是True则继续执行print，
	如果是False则中断程序，调用默认的异常处理器，同时输出assert语句逗号后面的提示信息。

	with语句：如果with语句或语句块中发生异常，会调用默认的异常处理器处理，但文件还是会正常关闭。


4、copy()与deepcopy()的区别

	copy是浅拷贝，只拷贝可变对象的父级元素。 deepcopy是深拷贝，递归拷贝可变对象的所有元素。

5、函数装饰器有什么作用（常考）

	装饰器本质上是一个Python函数,它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
	装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，
	比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
	有了装饰器，就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。


6、简述Python的作用域以及Python搜索变量的顺序

	Python作用域简单说就是一个变量的命名空间。代码中变量被赋值的位置，
	就决定了哪些范围的对象可以访问这个变量，这个范围就是变量的作用域。
	
	在Python中，只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域。

	Python的变量名解析机制也称为 LEGB 法则：本地作用域（Local）→当前作用域被嵌入的本地作用域
	（Enclosing locals）→全局/模块作用域（Global）→内置作用域（Built-in）

	
7、新式类和旧式类的区别,如何确保使用的类是新式类

	为了统一类(class)和类型(type)，python在2.2版本引进来新式类。在2.1版本中，类和类型是不同的。
	在2.2之前，比如2.1版本中，类和类型是不同的，如a是ClassA的一个实例，那么a.__class__返回 
	‘class __main__.ClassA‘ ，type(a)返回总是<type 'instance'>。而引入新类后，比如ClassB是个新类，
	b是ClassB的实例，b.__class__和type(b)都是返回‘class '__main__.ClassB' ，这样就统一了。

	引入新类后，还有其他的好处，比如更多的内置属性将会引入，描述符的引入，属性可以来计算等等。

	为了确保使用的是新式类，有以下方法：

	放在类模块代码的最前面 __metaclass__ = type
	从内建类object直接或者间接地继承
	在python3版本中，默认所有的类都是新式类。



	1）首先，写法不一样：
	class A:
		pass

	class B(object):
		pass
	
	2）在多继承中，新式类采用广度优先搜索，而旧式类是采用深度优先搜索。
	3）新式类更符合OOP编程思想，统一了python中的类型机制。
	4) 新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中。
	5) 新式类增加了__getattribute__方法。
	
	Python 2.x中默认都是经典类，只有显式继承了object才是新式类
	Python 3.x中默认都是新式类，不必显式的继承object


8、简述__new__和__init__的区别：

	创建一个新实例时调用__new__,初始化一个实例时用__init__,这是它们最本质的区别。

	new方法会返回所构造的对象，init则不会.

	new函数必须以cls作为第一个参数，而init则以self作为其第一个参数.


9、Python垃圾回收机制(常考)


	python采用的是引用计数机制为主，标记-清除和分代收集两种机制为辅的策略
	Python GC主要使用引用计数（reference counting）来跟踪和回收垃圾。在引用计数的基础上，
	通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，
	通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。


	 1 引用计数:

		PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。
		当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，
		它的ob_refcnt就会减少.引用计数为0时，该对象生命就结束了。

		优点:简单 实时性 
		缺点:维护引用计数消耗资源 循环引用
	
	2 标记-清除机制

		
		Python的GC算法类似于Ruby所用的标记回收算法。周期性地从一个对象到另一个对象追踪引用
		以确定对象是否还是活跃的，正在被程序所使用的，这正类似于Ruby的标记过程。

		基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，
		遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，
		然后清扫一遍内存空间，把所有没标记的对象释放。


	3 分代技术
		
		Python使用一种不同的链表来持续追踪活跃的对象。而不将其称之为“活跃列表”，
		Python的内部C代码将其称为零代(Generation Zero)。每次当你创建一个对象或其他什么值的时候，
		Python会将其加入零代链表：请注意到这并不是一个真正的列表，并不能直接在你的代码中访问，
		事实上这个链表是一个完全内部的Python运行时。
		随后，Python会循环遍历零代列表上的每个对象，检查列表中每个互相引用的对象，
		根据规则减掉其引用计数。在这个过程中，Python会一个接一个的统计内部引用的数量以防过早地释放对象。
		通过识别内部引用，对于判断出零代中的引用为0，Python能够减少许多零代链表对象的引用计数。
		这意味着收集器可以释放它们并回收内存空间了。剩下的活跃的对象则被移动到一个新的链表：一代链表。
		Python的GC算法类似于Ruby所用的标记回收算法。周期性地从一个对象到另一个对象追踪
		引用以确定对象是否还是活跃的，正在被程序所使用的，这正类似于Ruby的标记过程。

		分代回收的整体思想是：将系统中的所有内存块根据其存活时间划分为不同的集合，
		每个集合就成为一个“代”，垃圾收集频率随着“代”的存活时间的增大而减小，
		存活时间通常利用经过几次垃圾回收来度量。

	Python默认定义了三代对象集合，索引数越大，对象存活时间越长。

	
	应用程序那颗跃动的心:

		GC系统所承担的工作远比"垃圾回收"多得多。实际上，它们负责三个重要任务。它们
	
			1 为新生成的对象分配内存
			2 识别那些垃圾对象，并且
			3 从垃圾对象那回收内存。

	Python中的GC阈值:

		Python什么时候进行标记-清除操作：即是GC阀值

		随着你的程序运行，Python解释器保持对新创建的对象，以及因为引用计数为零而被释放掉的对象的追踪。
		从理论上说，这两个值应该保持一致，因为程序新建的每个对象都应该最终被释放掉。

		当然，事实并非如此。因为循环引用的原因，并且因为你的程序使用了一些比其他对象存在
		时间更长的对象，从而被分配对象的计数值与被释放对象的计数值之间的差异在逐渐增长。
		一旦这个差异累计超过某个阈值，则Python的收集机制就启动了，并且触发上边所说到的零代算法，
		释放“浮动的垃圾”，并且将剩下的对象移动到一代列表。
	
		随着时间的推移，程序所使用的对象逐渐从零代列表移动到一代列表。
		而Python对于一代列表中对象的处理遵循同样的方法，一旦被分配计数值与被释放计数值累计到达一定阈值，
		Python会将剩下的活跃对象移动到二代列表。

		通过频繁的处理零代链表中的新对象，Python的垃圾收集器将把时间花在更有意义的地方：
		它处理那些很快就可能变成垃圾的新对象。同时只在很少的时候，当满足阈值的条件，
		收集器才回去处理那些老变量。

	1、导致引用计数+1的情况

	对象被创建，例如a=23
	对象被引用，例如b=a
	对象被作为参数，传入到一个函数中，例如func(a)
	对象作为一个元素，存储在容器中，例如list1=[a,a]
	
	2、导致引用计数-1的情况

	对象的别名被显式销毁，例如del a
	对象的别名被赋予新的对象，例如a=24
	一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
	对象所在的容器被销毁，或从容器中删除对象

	
10、Python中的@property有什么作用?如何实现成员变量的只读属性？

	@property装饰器就是负责把一个方法变成属性调用，通常用在属性的get方法和set方法，
	通过设置@property可以实现实例成员变量的直接访问，又保留了参数的检查。
	另外通过设置get方法而不定义set方法可以实现成员变量的只读属性



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




11、*args and **kwargs

	*args代表位置参数，它会接收任意多个参数并把这些参数作为元组传递给函数。
	**kwargs代表的关键字参数，允许你使用没有事先定义的参数名，另外，位置参数一定要放在关键字参数的前面。


12、有用过with statement吗？它的好处是什么？具体如何实现？

	with语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常
	都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。

	简而言之，with/as语句设计是为常见try/finally用法模式的替代方案。
	wit/as语句也是用于定义必须执行的终止或"清理"行为，无论处理步骤中是否发生异常。
	不过，和try/fianlly不同的是，with语句支持更丰富的基于对象的协议，可以为代码块定义
	支持进入和离开动作。


13、what will be the output of the code below? explain your answer

	
		def extend_list(val, list=[]):
			list.append(val)
				return list
		    
		list1 = extend_list(10)
		print(list1)
		    #list1 = [10]   
		list2 = extend_list(123, [])
		print(list2) 
		    # list2 = [123]  
		list3 = extend_list('a')
	    print(list3) 
	        # list3 = [10, 'a']
	    
		print(list1) 
			#list1 = [10, 'a']
		print(list2) 
			# list2 = [123]
		print(list3) 
			# list3 = [10, 'a']
	

		class Parent(object):
			x = 1

		class Child1(Parent):
			pass

		class Child2(Parent):
			pass

		print(Parent.x, Child1.x, Child2.x)  # [1,1,1]
		Child1.x = 2
		print(Parent.x, Child1.x, Child2.x)  # [1,2,1]
		Parent.x = 3
		print(Parent.x, Child1.x, Child2.x)  # [3,2,3]


14、在一个二维数组中，每一行都按照从左到右递增的顺序排序，
	每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
	判断数组中是否含有该整数。


	arr = [[1,4,7,10,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]

	def getNum(num, data=None):
		while data:
			if num > data[0][-1]:
				del data[0]
				print(data)
				getNum(num, data=None)
			elif num < data[0][-1]:
				data = list(zip( *data))
				del data[-1]
				data = list(zip( *data))
				print(data)
				getNum(num, data=None)
			else:
				return True
				data.clear()
		return False


	if __name__ == '__main__':
		print(getNum(18, arr))








15、获取最大公约数、最小公倍数

	a = 36
	b = 21
	 
	def maxCommon(a, b):
		while b: a,b = b, a%b
		return a
		
	# 最小公倍数 = 两者乘积 // 最大公约数		    	    
	def minCommon(a, b):
		c = a*b
		while b: a,b = b, a%b
		return c//a
							  
	if __name__ == '__main__':
		print(maxCommon(a,b))
	    print(minCommon(a,b))

16、获取中位数

	def median(data):
		data.sort()
		half = len(data) // 2
		return (data[half] + data[~half])/2
			    
	l = [1,3,4,53,2,46,8,42,82]
			    
	if __name__ == '__main__':
		print(median(l))


17、输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
    
    def getOnecount(num):
        if num > 0:
            b_num = bin(num)
            count = b_num.count('1')
            print(b_num)
            print(count)
            return count
    
        elif num < 0:
            b_num = bin(~num)
            count = 8 - b_num.count('1')
            print(b_num)
            print(count)
            return count
        else:
            return 8
    
    if __name__ == "__main__":
        print(getOnecount(21))
        print(getOnecount(0))


18、使用递归把一个十进制数转换成二进制数：

	def binary2(num):

		if num == 0:
			return '0'
		else:
	        # return binary(num >> 1) + str( num & 1)
			return binary(num//2) + str(num%2)
	
	if __name__ == "__main__":
		
		num = int(input("请输入一个十进制的数字:"))
		print(binary2(num))
		

19、使用递归把一个十进制数转换成64进制数：

	def binary64(num,base):
	
		Keycode = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$"

		if num == 0:
			return '0'
		else:
			m = num%base
			return binary64(num//base,base) + Keycode[m]
	
	if __name__ == "__main__":
		num = int(input("请输入一个十进制的数字:"))
		base = int(input("请输入一个base的数字:"))
		print(binary64(num,base))

20、使用递归计算阶乘N!=n*(n-1)*(n-2)...*1:

	def factorial(n):

		if n == 1:
			return 1
		else:
			return n*factorial(n-1)
	
	if __name__ == "__main__":
		num = int(input("请输入一个十进制的数字:"))
		print(factorial(num))

21、使用递归计算高斯求和n+(n-1)+(n-2)+...+1
	
	def gauss(num):
		if num == 1:
			return 1
		else:
			return num + gauss(num-1)

	if __name__ == "__main__":
		num = int(input("请输入一个十进制的数字:"))
		print(gauss(num))

22、使用递归求斐波纳契: 0、1、1、2、3、5、8、13:

	def Fibonacci_sequence(num):

		if num <= 1:
			return num
		else:
			return (Fibonacci_sequence(num-1) +  Fibonacci_sequence(num-2))

	if __name__ == "__main__":
		nterms = int(input("您要输出几项? "))
		list1 = []
		for i in range(nterms):
			list1.append(Fibonacci_sequence(i))
		print(list1)			

23、使用递归求两个数的最大公约数：
    
    a = 36
	b = 21 
	def maxCommon(a, b):
		while b: 
		    a,b = b, a%b
		return a   # 这里返回 a 的原因是，a 已经为 a%b 了。


	def gcd(n,m):
		if m > n:
			n,m = m,n

		if n % m == 0:
			return m
		else:
			return (gcd(m,n%m))

	if __name__ == '__main__':
		n = int(input("please large number:"))
		m = int(input("please litter number:"))

		print(gcd(n,m))
		print("-------------")
		print(gcd1(n,m))

24、求递归求两个数的最小公倍数：

	def lcm(n,m,c):
		if m > n:
			n,m = m,n
		
		if n*c %m == 0:
			return n*c
		else:
			return lcm(n,m,c+1)
	if __name__ == '__main__':
		n = int(input("please input a number:"))
		m = int(input("please input another number:"))
		print(lcm(n,m,1))

25、求递归求一个字符串是不是回文数：

	def huiwen(str):
		if len(str)<=1:
			return True
		elif str[0] != str[-1]:
			reutrn False
		else:
			return huiwen(str[1:-1])
			
	if __name__ == '__main__':
		str1 = input("please input a string:")
		print(huiwen(str1))

26、递归函数求汉若塔：

	def move(n,a,buffer,c):
		if(n == 1):
			print(a,"-->",c)
			return
		move(n-1,a,c,buffer)
		move(1,a,buffer,c)
		move(n-1,buffer,a,c)
	if __name__ == '__main__':
	  move(3,"a","b","c")

27、递归函数求杨辉三角(python3)：
	
	def yang(i,j):
		if j == 0 or j == i:
			return 1
		else:
			return yang(i-1,j) + yang(i-1,j-1)
	if __name__ == '__main__':
		for i in range(0,10):
			print()
			for n in range(0,10-i):
				print(" ",end="")
			for j in range(0,i):
				print(yang(i,j),"",end="")


"================================================================="

1、列表a = [1,2,3,4,5,6,7,8,9], a[5:0:-2]值是多少？
    
    a[5:0:-2]
	    [6,4,2]
    
    a[-5:0:-2]
        [5,3]
	从index=5 到index=0,每隔1位取一个值。
    这个要看a[m,n,k], 要看m,n的值是正还是负，正是从前数索引，负是从后数索引。k 的值是步调和方向。
    
2、存在数组a = [1,2,3,[4,5,6]]进行如下计算，a,b,c,d的值各是多少？

	b = a

	c = copy.copy(a)

	d = copy.deepcopy(a)

	a.append(5)

	a[3].append(7)


	
	a --> [1, 2, 3, [4, 5, 6, 7], 5]

	b --> [1, 2, 3, [4, 5, 6, 7], 5]

	c --> [1, 2, 3, [4, 5, 6, 7]]

	d --> [1, 2, 3, [4, 5, 6]]


3、1 and [""] or "False"

	['']

	and :逻辑与，只有当1 为真时，才是计算[""]

	or : 逻辑或，只有当[""]为假时，才会执行"False"
	
	[""] 的结果为真。

	python中，真和假的概念是每个对象的固有属性，
	每个对象不是真就是假：

		数字如果非零，则为真
		其他对象如果非空，则为真。

		对象       值

		""         False
		
		[]         False

		{}         False

		0.0        False

		None       False


		[""]       True


4、实现一个带参数的装饰器deco:
	
	@deco(debug = True)
	def func(a, b):
		pass

	
	def deco(debug):
		""""""
		def decorate(func):

			def wrapper(a, b):
				return func(a, b)

			return wrapper
		return decorate

	初看起来，这种实现看上去很复杂，但是核心思想很简单。 
	最外层的函数 deco() 接受参数并将它们作用在内部的装饰器函数上面。 
	内层的函数 decorate() 接受一个函数作为参数，然后在函数上面放置一个包装器。
	这里的关键点是包装器是可以使用传递给deco() 的参数的。


	例子:

		#!/bin/python
		#_*_coding:UTF-8_*_


		def deco(debug):

			def decorator(func):

				def wrapper(a, b):
					print("%d---->%d")%(a, b)
					return func(a, b)	
				return wrapper							
			return decorator
												
		@deco(debug = True)
		def func(a, b):
			print("a + b = %d")%(a + b)
			
			
		if __name__ == '__main__':
				
			func(1, 2)
	
5、使用上下文管理器实现open 函数

	with open('some_file', 'w') as opened_file:
		opened_file.write('Hola!')

6、定义一个自己的dict类Storage,使其元素支持属性(点)访问

	class Storage(dict):
		
		"""
		A Storage object is like a dictionary except 'obj.foo' can be used
		in addition to 'obj['foo']'

		>>> o = storage(a=1)
		>>> o.a
			1
		>>> o['a']
			1
		>>> o.a = 2
		>>> o['a']
			2
		>>> del o.a
		>>> o.a
		Traceback (most recent call last):
			...
		AttributeError: 'a'

		"""
		
		def __getattr__(self,key):
			try:
				return self[key]
			except KeyError, k:
				raise AttributeError, k
		
		def __setattr__(self,key,value):
			self[key] = value

		def __delattr__(self,key):
			try:
				del self[key]
			except KeyError, k:
				raise AttributeError, k

		def __repr__(self):
			return '<Storage ' + dict.__repr__(self) + '>'


7、请写出常见的python的web应用部署方式，格式：webContainer + appContainer + app

	
	准备知识:

		python 与世界上大多数的事情不同，当涉及到选择生产服务器堆栈来部署应用程序时，
		并没有一个明显的选择，在衡量你的需求和要求后，才能决定使用哪个服务器。

		我们首先关注的是该web服务器的人气，稳定性和突出特点。
		要注意的是：警惕有偏见和欺骗性的基准，这些基准往往不能反映真实生产环境的条件。

		
	a. Python Web Server Gateway Interface v1.0 (WSGI)

		问题：在上个世纪，开发人员并不能轻松的切换web服务器，选择了一个web应用程序框架
		往往也意味着决定了相应的web服务器。这是由于缺乏普遍的接口规范：应用程序（框架）
		和web 服务器都应该适配的用于互相通信的规则（允许在不改变代码下的互换性）

		标准的诞生：

			在本世纪初，Python社区提出PEP-333来解决这个问题：

			这个新标准意味着保障Web服务器和Python Web应用程序之间的可移植性。
			该标准的强大特性和广泛采用形成了今天的局面：
			存在着许多(也许是太多)愿意为你工作的web服务器。


	b. Python Web 服务器(按字母排序):

		CherryPy WSGI服务器

			CherryPy实际上是一个Web框架。然而，它是一个完全独立的 - 意味着它可以独立运行，
			包括在生产场景中而不需要额外的软件。这要归功于它自己的WSGI，符合HTTP / 1.1标准的Web服务器。
			CherryPy项目将其描述为“高速，生产就绪，线程池，通用HTTP服务器”。
			由于它是一个WSGI服务器，它也可以用于任何其他WSGI Python应用程序，
			而不受CherryPy的应用程序开发框架的约束。

			
			你为什么要考虑使用它？

				它结构紧凑，简单。
				它可以为在WSGI上运行的任何Python Web应用程序提供服务。
				它可以处理静态文件，它只能用于单独提供文件和文件夹。
				它是线程池。
				它支持SSL。
				它是一种易于使用，易于使用的纯Python替代品，坚固可靠。

		Gunicorn:

			Gunicorn是一个独立的Web服务器，以非常易于操作的方式提供相当多的功能。
			它使用预分叉模型 - 意味着中央主进程（Gunicorn）的任务是管理启动的工作进程（不同类型），
			然后直接处理和处理请求。所有这些都可以根据您的需求和不同的生产场景进行配置和调整。

			你为什么要考虑使用它？

				它支持WSGI，可以与任何运行Python应用程序和框架的WSGI一起使用。
				它也可以用作Paster（例如：Pyramid），Django的开发服务器，web2py等的替代品。
				提供各种工人类型/配置和自动工人流程管理的选择。
				通过同步和异步工作程序支持HTTP / 1.0和HTTP / 1.1（Keep-Alive）。
				附带SSL支持
				可伸缩的钩子。
				它是透明的，具有清晰的架构。
				支持Python版本2.6,2.7,3,3.2,3.3

		Tornado (HTTP Server via wsgi.WSGIContainer):

			Tornado是一个应用程序开发框架和一个用于处理异步操作的网络库，
			允许服务器维护大量开放连接。它还附带了一个WSGI服务器，
			其他WSGI Python应用程序（和框架）可以使用它来运行。

			你为什么要考虑使用它？

				如果您正在构建顶级Tornado框架; 要么您的应用需要异步功能。

				虽然在这些情况下您可能想为您的项目选择Tornado的WSGI服务器，
				但您也可以选择将Gunicorn与Tornado [Asynchronous]工作者一起使用。

		Twisted Web：
			
			Twisted Web 是一款带有网络库的web server,
			虽然Twisted本身是“一个事件驱动的网络引擎”，
			但Twisted Web服务器在WSGI上运行，它能够为其他Python Web应用程序提供动力。
	
			你为什么要考虑使用它？

				它是一种易于使用，稳定和成熟的产品。
				它将运行WSGI Python应用程序。
				它可以像Python Web服务器框架一样，允许您使用语言对其进行编程，以实现自定义HTTP服务。
				它提供简单快速的原型设计功能，通过Python Scrips (.rpy)该功能在HTTP请求时执行。
				它具有代理和反向代理功能。
				它支持虚拟主机。
				它甚至可以通过twisted.web.twcgi API为Perl，PHP等提供服务。

		uWSGI:

			尽管它的命名约定非常混乱，但uWSGI本身是一个包含许多组件的庞大项目，
			旨在提供一个full [software] stackfor building hosting services。
			其中一个组件是uWSGI服务器，它运行Python WSGI应用程序。

			它能够使用各种协议，包括它自己的uwsgi线协议，它与SCGI准几何相同。
			为了满足在应用服务器前使用独立HTTP服务器的（可理解的）需求，
			NGINX和Cherokee Web服务器进行了模块化，以支持uWSGI（性能最佳）的uwsgi协议，以直接控制其进程。
			
			你为什么要考虑使用它？

				uWSGI附带一个WSGI适配器，它完全支持在WSGI上运行的Python应用程序。
				它与libpython链接。它在启动时加载应用程序代码，就像Python解释器一样。它解析传入的请求并调用Python可调用。
				它直接支持流行的NGINX Web服务器（以及Cherokee *和lighttpd）。
				它是用C写的。
				它的各种组件可以比运行应用程序做得更多，这可能对扩展很方便。
				目前（截至2013年底），它正在积极开发并具有快速发布周期。
				它有各种用于运行应用程序的引擎（异步和同步）。
				它可能意味着运行内存占用更少。


8、考虑下面情况，将得到什么结果？并解释为什么？

	print "hello! %s" % u"中国"
		
	print "hello ! %s" % "中国"

	print u"hello ! %s" % "中国"

9、用正则匹配一下ip地址:

	localhost is 127.0.0.1



10、一个列表中的元素有正有负，在该数组中找出一个连续的子数组，要求该连续子数组
	中各元素的和最大，这个连续子数组便被称作最大连续子数组，然后返回该和值即可。
	比如，数组[2, 4, -7, 5, 2, -4, 3] 的最大连续子数组为[5, 2, -1, 2],最大连续
	子数组的和是5 + 2 - 1 + 2 = 8



"---------------------------------------------------------------------------"

    1、为什么使用装饰器函数，举出一例
    
        装饰器是一个本质上是一个可调用的 python 对象，用作修改或扩展函数或类定义。
        装饰器的优点之一是，单个装饰器定义可以应用于多个函数(或类)。
        因此可以用装饰器完成很多工作，否则将需要大量样板代码(甚至更糟糕的是，冗余代码!)
        
        例如：Flask, 使用装饰器作为向web应用程序添加新端点的机制。
        一些更常见的装饰器使用示例包括向类或函数添加同步、类型强制、日志记录或前/后条件。 
    
    2、 什么是 lambda 表达式、列表解析、生成器表达式？每种方法的优点和适当用途是什么？
    
        Lambda表达式： 是创建单行匿名函数的一种简写技术。
        它们简单、内联的特性通常(尽管不总是)比正式函数声明的替代方法更容易读和更简洁的代码。
        另一方面，根据定义，它们简洁的内联特性在很大程度上限制了它们的功能和适用性。
        由于是匿名和内联的，在代码中的多个位置使用相同lambda函数的惟一方法是冗余地指定它。
        
        列表解析：列表解析为创建列表提供了一种简洁的语法
        列表理解通常用于创建列表，其中每个元素是应用于另一个序列或可迭代的每个成员的某个操作的结果。
        它们还可以用来创建元素的子序列，这些元素的成员满足某个条件。
        在Python中，列表解析提供了使用内置map()和filter()函数的替代方法。
        
        由于lambda表达式和列表理解的应用用法可能会重叠，因此对于何时何地使用其中一个表达式和另一个表达式的意见大相径庭。
        但是需要记住的一点是，与使用map和lambda的类似解决方案相比，
        列表理解的执行速度要快一些(一些快速测试产生了大约10%的性能差异)。
        这是因为调用lambda函数会创建一个新的堆栈框架，而对列表理解中的表达式进行求值时不会这样做。
        
        生成器表达式在语法和功能上类似于列表理解，
        但是它们的操作方式和应该使用它们的时间之间有一些相当显著的差异。       
        
        简而言之，迭代生成器表达式或列表理解本质上是做同样的事情，
        但是列表理解将首先在内存中创建整个列表，而生成器表达式将根据需要动态创建项目。
        
        因此，生成器表达式可以用于非常大(甚至无限)的序列及其惰性，即生成值可以提高性能和降低内存使用。
        标准Python列表方法可以用于列表理解的结果，但不能直接用于生成器表达式。
        
    3、 考虑以下两种初始化数组的方法以及将产生的数组。
        得到的数组有何不同?为什么要使用一种初始化方法而不是另一种?   
            
            
            
            >>> # INITIALIZING AN ARRAY -- METHOD 1
            ...
            >>> x = [[1, 2, 3, 4]] * 3
            >>> x
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]       
            
            >>> x = [1, 2, 3, 4] * 3
            [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
            
            
            >>> # INITIALIZING AN ARRAY -- METHOD 2
            ...
            # 这里for 循环里的 _ 是省略，代表什么也不做，可以是"_", 也可以是"__"。
            >>> y = [[1, 2, 3, 4] for _ in range(3)]
            >>> y
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]] 
            
            虽然这两种方法乍一看似乎产生了相同的结果，但它们之间存在着极为显著的差异。
            如您所料，方法2生成一个包含3个元素的数组，每个元素本身就是一个独立的4个元素数组。
            然而，在方法1中，数组的成员都指向同一个对象。这可能导致最可能的意外和不希望的行为，
            如下所示:
            
            >>> x = [[1,2,3,4]] * 3
            >>> x
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
            >>> 
            >>> 
            >>> x[0][3] = 99
            >>> x
            [[1, 2, 3, 99], [1, 2, 3, 99], [1, 2, 3, 99]]
            
            >>> y[0][3] = 99
            >>> y
            [[1, 2, 3, 99], [1, 2, 3, 4], [1, 2, 3, 4]]
    
    4、Python2 和 Python3 有什么不同：
    
        虽然目前Python 2被正式认为是遗留下来的，但是它的使用仍然非常广泛，
        对于开发人员来说，识别Python 2和Python 3之间的差异非常重要。   
        
        以下是开发人员应该注意的一些关键区别:
            a.  文本和数据，而不是Unicode和8位字符串。
                Python 3.0使用了文本和(二进制)数据的概念，而不是Unicode字符串和8位字符串。
                这样做的最大后果是，任何在Python 3.0中混合文本和数据的尝试都会引发类型错误
                (为了安全地将两者结合，您必须解码字节或编码Unicode，但是您需要知道正确的编码，例如UTF-8)   
                
                这解决了天真的Python程序员长期存在的问题。
                在Python 2中，如果字符串碰巧只包含7位(ASCII)字节，那么混合使用Unicode和8位数据是可行的，
                但是如果字符串包含非ASCII值，则会得到UnicodeDecodeError。
                此外，异常将发生在组合点，而不是将非ascii字符放入str对象的点。
                对于初学Python的程序员来说，这种行为是混淆和惊慌的常见来源。
            
            b.  打印功能。print语句已替换为print()函数
            
            c.  xrange——buh-bye。xrange()不再存在(range()现在的行为与以前的xrange()类似，
                只不过它可以处理任意大小的值)
            
            d.  API的变化:
                zip()、map()和filter()现在都返回迭代器，而不是列表
                keys()、dic .items()和dic .values()现在返回“视图”，而不是列表
                iterkeys()、dic .iteritems()和dic .itervalues()不再受支持
            
            e.  比较运算符。排序比较操作符(<，<=，>=，>)现在在操作数没有有意义的自然排序时引发类型错误异常。
                这方面的一些后果包括:
                            表达式1 < "，0 > None或len <= len不再有效
                            None < None现在会引发一个类型错误，而不是返回False
                            对异构列表进行排序不再有意义——所有元素必须相互比较。
       
    5、 python 是解释器还是编译器
        
        坦率地说，这是一个棘手的问题，因为它是畸形的。
        Python本身只不过是一个接口定义（对于任何语言规范都是如此），其中有多个实现。
        因此，解释或编译“Python”的问题不适用于Python语言本身;
         相反，它适用于Python规范的每个特定实现。

        这个问题的答案进一步复杂化的是，在CPython（最常见的Python实现）的情况下，
        答案实际上是“两者兼而有之”。
        具体来说，使用CPython，首先编译代码然后进行解释。
        更准确地说，它不是预编译为本机机器代码，而是预编译为字节码。
        虽然机器代码肯定更快，但字节码更加便携和安全。
        然后在CPython的情况下解释字节码（或者在PyPy的情况下，在运行时解释和编译为优化的机器代码）。
     
    6、 CPython有哪些替代实现？您何时以及为何使用它们？
    
        其中一个更突出的替代实现是Jython，一个用Java编写的Python实现，它使用Java虚拟机（JVM）。
        当CPython生成在CPython VM上运行的字节码时，Jython会生成Java字节码以在JVM上运行。
        
        另一个是IronPython，用C＃编写并以.NET堆栈为目标。IronPython运行在Microsoft的公共语言运行时（CLR）上。

        同样在为什么有这么多python？，完全有可能在没有接触过Python的非CPython实现的情况下生存，
        但是切换有很多好处，其中大部分依赖于你的技术堆栈。
        
        另一个值得注意的替代实现是PyPy，其主要功能包括：
        
            速度。 由于它的Just-in-Time（JIT）编译器，Python程序通常在PyPy上运行得更快。
            内存使用情况。 与CPython相比，使用PyPy占用大量内存的Python程序可能会占用更少的空间。
            兼容性。 PyPy与现有的python代码高度兼容。它支持cffi，可以运行像Twisted和Django这样的流行Python库。
            沙箱。 PyPy提供了以完全安全的方式运行不受信任的代码的能力。
            无堆叠模式。 PyPy默认支持无堆栈模式，为大规模并发提供微线程。     
    
    7、 你在Python中进行单元测试的方法是什么？
        
        对这个问题的最根本的答案主要围绕Python的单元测试的测试框架。
        基本上，如果候选人在回答这个问题时没有提及unittest，那应该是一个巨大的危险信号。
        
        unittest支持测试自动化，共享测试的设置和关闭代码，将测试聚合到集合中，以及测试与报告框架的独立性。
        unittest模块提供的类可以轻松地为一组测试支持这些质量。  
        
        假设候选人确实提到了单元测试（如果他们不这样做，你可能只想在那时和那里结束面试！），
        你也应该让他们描述单元测试框架的关键元素; 即测试夹具，测试用例，测试套件和测试运行器。
         
        单元测试框架的最新成员是mock。mock允许您使用模拟对象替换测试中的系统部分，并对如何使用它们进行断言。
        mock现在是Python标准库的一部分，在Python 3.3及更高版本中以unittest.mock的形式提供。
        
    8、 在Python与Java编码时，要记住哪些关键区别？
    
        动态与静态类型。 两种语言之间最大的区别之一是Java仅限于静态类型，而Python支持动态类型化变量。
        
        静态与类方法。 Java中的静态方法不会转换为Python类方法。
            在Python中，调用类方法涉及调用静态方法或函数的额外内存分配。
            在Java中，编译器会查找虚线名称（例如，foo.bar.method），因此在运行时，它们中有多少并不重要。但是，在Python中，查找在运行时发生，因此“每个点计数”。
        
        方法重载。 虽然Java要求使用不同签名显式指定多个同名函数，但在Python中使用单个函数可以实现相同的功能，如果未由调用者指定，则该函数包含具有默认值的可选参数。
        
        单引号与双引号。 虽然单引号与双引号的使用在Java中具有重要意义，但它们可以在Python中互换使用（但不是，它不允许使用双引号开始使用相同的字符串并尝试使用单引号结束它，或者反之亦然！）。
        
        Python中的getter和setter是多余的; 相反，你应该使用内置的'property'（这就是它的用途！）。在Python中，getter和setter浪费了CPU和程序员的时间。
        
        类是可选的。 Java要求在封闭类定义的上下文中定义每个函数，而Python没有这样的要求。
        
        缩进很重要...... 在Python中。这咬了许多新手Python程序员。    

    9、 Python特别适用于什么？何时使用Python是项目的"正确选择"
    
        由于Python语法的灵活性，易于使用和易于重构，这使其特别适用于快速原型设计。
        
        更复杂的代码，再次感谢Python的语法，以及丰富的功能丰富的Python库（随大多数Python语言实现自由分发）。
        
        一种动态类型和强类型语言，提供罕见的代码灵活性组合，同时避免讨厌的隐式类型转换错误。
        
        它是免费和开源的！ 需要我们说更多？
    
    10、Python语言有哪些缺点？
        
        GIL 锁：不是完全线程安全的。为了支持多线程Python程序，CPython提供了一个全局锁，
            必须由当前线程保存才能安全地访问Python对象。
            因此，无论存在多少线程或处理器，在任何给定时间只执行一个线程。
            相比之下，值得注意的是，本文前面讨论的PyPy实现提供了无堆栈模式，支持用于大规模并发的微线程。
           
        执行速度。 Python可能比编译语言慢，因为它被解释。

"-------------------------------------------------------------"














