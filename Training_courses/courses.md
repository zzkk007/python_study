
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























































			



			

































