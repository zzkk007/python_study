
学习手册

"---------------------------------------------------------------------------------------------------------"  
					第四章   python 对象类型  
"----------------------------------------------------------------------------------------------------------"

1、import 和 from 

import 语句将模块作为一个整体载入，并使用模块名后跟一个属性名来获取使用。
内置的dir函数，可以使用它获得模块内部的可用的变量名列表。

from 和import 很相似，只不过增加了对载入组件的变量名的额外的赋值，从技术上讲，from复制了模块的属性，以便属性能够成为接收者的直接变量。

from语句从某种意义上来说战胜了模块的名称空间分隔的目的，以为from把变量从一个文件复制到另一个文件，这可能导致在导入的文件中相同名称的变量被覆盖（不会警告）。这根本上回导致名称空间重叠在一起，至少会在复制变量上回重叠。



2、核心类型

python内置对象：数字、字符串、列表、字典、元组、文件、集合。

其他类型(类型、None、布尔型)、编程单元类型(函数、模块、类)、与现实相关的类型（编译的代码堆栈跟踪）

核心类型中，数字、字符串和元组是不可变的，列表和字典可以自由改变，字符串，列表、元组是序列，字典是映射。

集合:集合是最近增添到python语言中的类型，它不是映射也不是序列，相反他是唯一的不可变的无序集合，集合可以通过内置对象set函数而创建或使用python3中集合常量和表达式创建，集合更像是一个无值的字典的键。


字典：字典不是队列，而是一种映射。映射是一个其他对象的集合，但是他们是通过键而不是相对位置来存储的。
	  字典是python核心对象中唯一的一种映射类型，也具有可变性。

文件：文件对象是python代码对电脑上外部文件的主要接口。虽然文件是核心类型，但是它有些特殊：没有特定的常量语法创建文件。要创建一个文件对象，需要调用内置的open函数一字符串的形式传递给它一个外部的文件名以及一个处理模式的字符串。

Python还有额外的类文件工具:管道、先进先出队列（FIFO）、套接字、通过键访问文件、对象持久、基于描述符的文件、关系数据库和面向对象数据库接口等。例如，描述符文件支持文件锁定和其他的底层工具，问套接字提供网络和进程间通信接口。


Python3中类型已经和类结合起来了。

python中允许编写代码来检验它所处理的对象的类型，python中至少有三种方法可以做到:

1:
		if type(L) == type([]):   
			print('yes')

2:       
		if type(L) == list:  
			print('yes')

3:
		if isinstance(L,list):  
			print('yes')

核心python概念(可能是唯一一个)：在代码中检验了特定的类型，实际上是破坏了它的灵活性，即限制它使用一种类型工作。没有这样的检测，代码也许能使用整个范围的类型工作。

这与多太思想有些关联，它是由Python没有类型声明而发展出来的。在python中，我们编写对象接口而不是类型。不关注于特定的类型意味着代码会自动地适应它们中的很多类型：任何具有兼容接口的对象均能够工作,而不管它是什么对象类型。尽管支持类型检测（极少情况下，是必要的），但是它并不是一个“python式”的思维方法。事实上，多态也是使用Python的一个关键思想。

"多态"意味着一个操作符的意义取决于被操作的对象。这将变成使用好Python的关键思想之一：不要把代码限制在特定的类型上，使代码自动适应多种类型。


我们学的这些数字、字符串、列表、字典、集合类型，是对象仅是对象而已，并不一定是面向对象。面向对象是一种往往要求有继承和python类声明的概念。


"----------------------------------------------------------------------------------------------------------"  
						第五章  数字    
"----------------------------------------------------------------------------------------------------------"

在python中数字并不是一个真正的对象类型，而是一组类似类型的分类。

yield x                    生成器函数发送协议

lambda args:expression     生产匿名函数

x if y else z              三元选择表达式

x or y                     逻辑或（只有x 为假，才会计算y）

x and y                    逻辑与（只有x 为真，才会计算y）

not x                      逻辑非

x in y , x not in y        成员关系（可迭代对象、集合）

x is y , x is not y        对象实体测试

x | y                      位或

x ^ y                      位异或

x // y                     真除法

x[i:j:k]                   分片

x(...)                     调用（函数、方法、类及其他调用）

(...)                      元组、表达式、生成器表达式

[...]                      列表、列表解析

{...}                      字典、集合、集合和字典解析


列表解析：
	
	根据已有的列表，高效创建新列表的方式。列表解析是python迭代机制的一种应用。
	
	语法：
	
	[expression for iter_val in interable]
	
	[expression for iter_val in interable if cond_expr]

	例如：
	L = [ i**2 for i in range(1,11) if i >= 4 ]
	
	print L
	
	[16,25,36,49,64,81,100]



协程：

协程是一种用户级的轻量级线程。协程拥有自己的寄存器上下文和栈。

协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。

因此：协程能保留上一次调用时的状态（即所有局部状态的一个特定组合），每次过程重入时，

就相当于进入上一次调用的状态，换种说法：进入上一次离开时所处逻辑流的位置。

在并发编程中，协程与线程类似，每个协程表示一个执行单元，有自己的本地数据，与其它协程共享全局数据和其它资源。

目前主流语言基本上都选择了多线程作为并发设施，与线程相关的概念是抢占式多任务（Preemptive multitasking），

而与协程相关的是协作式多任务。



yield与send实现协程操作:

在函数内部含有yield语句即称为生成器。

def foo():

	while True:
	
		x = yield
			
		print("value:",x)

g = foo()        #g 是一个生产器

next(g)          #程序运行到yield就停住了，等待下一个next

g.send(1)        #我们给yield 发送值1，然后这个值就被赋值给了x,并且打印出来，然后继续下一次循环停在yield处

g.send(2)        #同上

next(g)          #没有给赋值，执行print语句，打印None,继续循环停在yield处


我们都知道，程序一旦执行到yield就会停在该处,并且将其返回值进行返回.上面的例子中，我们并没有设置返回值，

所有默认程序返回的是None。我们通过打印语句来查看一下第一次next的返回值：

print(next(g))

####输出结果#####
	
	None

正如我们所说的，程序返回None。接着程序往下执行，但是并没有看到next()方法。

为什么还会继续执行yield语句后面的代码呢？这是因为，send()方法具有两种功能：

第一，传值，send()方法，将其携带的值传递给yield，注意，是传递给yield，而不是x,然后再将其赋值给x；

第二，send()方法具有和next()方法一样的功能，也就是说，传值完毕后，会接着上次执行的结果继续执行，

知道遇到yield停止。这也就为什么在调用g.send()方法后，还会打印出x的数值。

有了上述的分析，我们可以总结出send()的两个功能：1.传值；2.next()。

既然send()方法有和next一样的作用，那么我们可不可以这样做：

def foo():
	    
	while True:
		        
		x = yield
		
		print("value:",x)
		   
g = foo()
	
g.send(1) #执行给yield传值,这样行不行呢?

执行结果：TypeError: can not send non-None value to a just-started generator

错误提示:不能传递一个非空值给一个未启动的生成器。

也就是说，在一个生成器函数未启动之前，是不能传递数值进去。必须先传递一个None进去或者调用一次next(g)方法，

才能进行传值操作。至于为什么要先传递一个None进去，可以看一下官方说法。

Because generator-iterators begin execution at the top of the
generator function body, there is no yield expression to receive
a value when the generator has just been created.  Therefore,
calling send() with a non-None argument is prohibited when the
generator iterator has just started, and a TypeError is raised if
this occurs (presumably due to a logic error of some kind).  Thus,
before you can communicate with a coroutine you must first call
next() or send(None) to advance its execution to the first yield
expression.

问题就来，既然在给yield传值过程中，会调用next()方法，那么是不是在调用一次函数的时候，

是不是每次都要给它传递一个空值？有没有什么简便方法来解决這个问题呢？答案，装饰器！！看下面代码:

def deco(func):  # 装饰器:用来开启协程
	
	def wrapper():

		res = func()

		next(res)

		return res    #返回一个已经执行了next的函数对象

	return wrapper

@deco

def foo():

	food_list = []

	while True:
		
		food = yield food_list    #返回添加food的列表

		food_list.append(food)

		print("elements in foodlist are:",food)

g = foo()

print(g.send('苹果'))

print(g.send('香蕉'))

print(g.send('菠萝'))

###########输出结果为######

elements in foodlist are: 苹果

['苹果']

elements in foodlist are: 香蕉

['苹果', '香蕉']

elements in foodlist are: 菠萝

['苹果', '香蕉', '菠萝']


这里我们要明确一点，yield的返回值和传给yield的值是两码事！！

yield的返回值就相当于return的返回值，这个值是要被传递出去的,而send()传递的值，是要被yield接受，

供函数内部使用的的，明确这一点很重要的。那么上面的打印，就应该打印出yield的返回值，

而传递进去的值则本保存在一个列表中。






装饰器：


装饰器本质上是一个Python函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下增加额外的功能，

装饰器的返回值也是一个函数或类对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、

缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计。

有了装饰器，我们可以抽离大量与函数功能本身无关的雷同代码到装饰器中并继续使用。概括的将，装饰器的作用

就是为已经存在的对象添加额外的功能。


例子： 定义一个函数专门处理日志，日志处理完之后执行代码

def use_logging(func):
	
	logging.warn("%s is running"% func.__name__)
	
	func()

def foo():

	print('i am foo')

use_logging(foo)


这样做的逻辑没有问题，功能实现了，但是我们调用的时候不再试调用真正的业务逻辑函数foo，而是变成了use_logging函数

破坏了原有的代码结构， 现在我们不得不每次都要把原来的那个 foo 函数作为参数传递给 use_logging 函数，

那么有没有更好的方式的呢？当然有，答案就是装饰器。


def use_logging(func):

	def wrapper():

		logging.warn("%s is running"% func.__name__)

		return func()

	return wrapper

def foo():
	print('i am foo')


foo = use_logging(foo) #因为装饰器use_logging(foo)返回的函数对象wrapper,这条语句相当于foo = wrapper

foo()                  # 执行foo()就相当于执行 wrapper()


@语法糖

@ 符号就是装饰器的语法糖，它放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作。

def use_logging(func):

	def wrapper():
	
		logging.warn("%s is running" % func.__name__)
		
		return func()
	return wrapper
							 

@use_logging

def foo():
	
	print("i am foo")
									 
foo()

如上所示，有了@，我们就可以省去foo = use_logging(foo)这一句了，直接调用 foo() 即可得到想要的结果。

装饰器在 Python 使用如此方便都要归因于 Python 的函数能像普通的对象一样能作为参数传递给其他函数，

可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。



*args、**kwargs:

可能有人问，如果我的业务逻辑函数 foo 需要参数怎么办？比如：

def foo(name):
	
	print("i am %s" % name)

我们可以在定义 wrapper 函数的时候指定参数：

def wrapper(name):
	        
		logging.warn("%s is running" % func.__name__)
			    
		return func(name)

	return wrapper


这样 foo 函数定义的参数就可以定义在 wrapper 函数中。这时，又有人要问了，如果 foo 函数接收两个参数呢？

三个参数呢？更有甚者，我可能传很多个。当装饰器不知道 foo 到底有多少个参数时，我们可以用 *args 来代替：

def wrapper(*args):
	
		logging.warn("%s is running" % func.__name__)
			        
		return func(*args)

	return wrapper





类装饰器：

没错，装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。

使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。


class Foo(object):
	
	def __init__(self, func):
		
		self._func = func

		def __call__(self):
			
				print ('class decorator runing')
									        
				self._func()
				
				print ('class decorator ending')
											 
@Foo

def bar():
	
	print ('bar')
													 
bar()



