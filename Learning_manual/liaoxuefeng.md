'-----------------------------------------------------------'

           本篇是学习廖雪峰Python教程学习笔记     

'-----------------------------------------------------------'

"""01: Python 基础 """

    1、字符串:
        
        字符串是以单引号' 或 双引号 " 括起来的任意文本，比如 'abc',"xyz"等等。
        请注意: ''或 "" 本身只是一种表示方式，不是字符串的一部分
        因此 字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，
        那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。 
        
        如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
        >>> print('I\'m \"OK\"!')
        I'm "OK"!
        
        如果字符串里面有很多字符都需要转义，就需要加很多\, 为了简化， 
        Python 允许用 r'' 表示 '' 内部的字符串默认不转义。
        >>> print(r'I\'m \"OK\"!')
        I\'m \"OK\"! 
            
    2、整型:
    
        注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，
        例如Java对32位整数的范围限制在-2147483648-2147483647。

        Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。        
    
    3、字符编码:
    
        字符串也是一种数据类型，但是，字符串比较特殊的就是还有一个编码问题。
        
        因为计算机只能处理数字，如果要处理文本，就必须把文本转换为数字才能处理。
        最早的计算机在设计时采用 8 个比特(bit)作为一个字节(byte)，所以，一个字节
        能表示的最大的整数就是 255 (二进制 11111111=十进制255)，如果要表示更大的
        整数，就必须采用更多字节。比如两个字节可以表示的最大值65535，
        4个字节可以表示的最大整数是4294967295。
        
        为了统一不同的语言转换造成的乱码问题，Unicode 应运而生，Unicode 把所有语言都统一到
        一套编码里，这样就不会再有乱码的问题。
        
        Unicode 标准也在不断发展，但最常用的是用两个字节表示一个字符，如果非常偏僻的字符需要四个字节。
        
        ASCII 编码和Unicode 编码的区别：ASCII 编码是 1 个字节，而 Unicode 编码通常是 2 个字节。
        
        字母A用ASCII编码是十进制的65，二进制的01000001；
        字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
        
        汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
        你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，
        因此，A的Unicode编码是00000000 01000001。 
        
        新的问题又出现了：如果统一成 Unicode 编码，乱码问题就消失了。但是如果你写的文本基本上趋势英文的话
        用 Unicode 编码比 ASCII 编码需要多一倍的存储空间，在存储和传输上就不划算。
        
        所以，本着节约的原则，又出现了把 Unicode 编码转化成 “可变长编码” 的 uft-8 编码。
        UTF-8 编码把一个 Unicode 字符根据不同数字大小编码成 1-6 个字节。
        常用的英文字母被编码成 1 个字节，汉字通常是 3 个字节，只有很生僻的字符才会编码成 4-6个字节。
        如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。
        
        UTF-8 编码还有一个额外的好处，就是 ASCII 编码实际上可以被看成是 UTF-8 的一部分。
        所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。
        
        搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：
        在计算机内存中，统一使用 Unicode 编码，当需要保持到磁盘或者需要传输的时候，就转换成 UTF-8 编码。
        
        用记事本编辑的时候，从文本读取的 UTF-8 字符被转换为 Unicode 编码到内存里。
        编辑完成后，保存的时候再把 Unicode 转换成 UTF-8 保存到文件。
        
        浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
        所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码。
        
    4、Python 的字符串：
    
        在最新的 Python 3 版本中，字符串是以 Unicode 编码的，也就是说，Python 字符串支持多语言：
            
            >>>print('包含中文的str')
            包含中文的str
        
        对于单个字符的编码，Python 提供了 ord() 函数获取字符的整数表示，chr()函数把编码转换成对于字符。
            >>> ord('中')    
            20013
            >>> 
            >>> ord('A')
            65
            >>> 
            >>> chr(66)
            'B'
            >>> chr(20014)
            '丮'
            >>>      
        
        如果知道字符的整数编码，还可以用十六进制这么写 str：
            >>> ord('中')    
            20013
            >>> 
            >>> chr(20013)
            '中'
            >>> 
            >>> hex(20013)
            '0x4e2d'
            >>> 
            >>> '\u4e2d'
            '中'
            >>> 
        两种写法完全等价。
        
        
        由于 Python 的字符串类型是 str, 在内存中以 Unicode 表示，一个字符串对应若干个字节。
        如果要在网络上传输，或者保存到磁盘上，就需要把 str 变成以字节为单位的 bytes。
        
        Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示：
            
            x = b'ABC'
        
        要注意区分 'ABC' 和 b'ABC'，前者是 str, 后者虽然内容显示和前者一样，
        但 bytes 的每个字符都只占用一个字节。
        
        以 Unicode 表示的 str 通过 encode() 方法可以编码为指定的 bytes, 例如：
        
            >>> 'ABC'.encode('ASCII')
            b'ABC'
            >>> 
            >>> 'ABC'.encode('utf-8')
            b'ABC'
            >>> 
            >>> 
            >>> '中文'.encode('utf-8')
            b'\xe4\xb8\xad\xe6\x96\x87'
            >>> 
            >>> '中文'.encode('ASCII')
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
            >>> 
                           
        纯英文的 str 可以用 ASCII 编码为 bytes, 内容是一样的，含有中文的 str 可以用 UTF-8 编码为 bytes。
        含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
        在bytes中，无法显示为ASCII字符的字节，用\x##显示。
        
        反过来，如果我们从网络或者磁盘上读取了字节流，那么读到的数据是 bytes。
        要把 bytes 变成 str，就需要用 decode() 方法。
            
            >>> b'ABC'.decode('ascii')
            'ABC'
            >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
            '中文'
        如果bytes中包含无法解码的字节，decode()方法会报错：

            >>> b'\xe4\xb8\xad\xff'.decode('utf-8')
            Traceback (most recent call last):
              ...
            UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte    
                     
        如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
            
            >>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
            '中'
        
        len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
            
            >>> len(b'ABC')
            3
            >>> len(b'\xe4\xb8\xad\xe6\x96\x87')
            6
            >>> len('中文'.encode('utf-8'))
            6   
        
        可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。            
        在操作字符串时，我们经常遇到 str 和 bytes 的互相转换，为了避免乱码问题，
        应当坚持使用 UTF-8 编码对 str 和 bytes 进行转换。
        
        由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，
        在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，
        为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：    
            #!/usr/bin/env python3
            # -*- coding: utf-8 -*-   
        
        第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
        第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，
        否则，你在源代码中写的中文输出可能会有乱码。    
         
    5、 list 和 tuple:
        
        list:
        
            如果一个 list 中一个元素也没有，就是一个空 list, 它的长度为 0：
            >>> L = []
            >>> len(L)
            >>> 0
            
        tuple:
            
            如果要定义一个空的tuple，可以写成()：
            >>> t = ()
            >>> t
            ()
            
            但是，要定义一个只有1个元素的tuple，如果你这么定义：
            >>> t = (1)
            >>> t
            >>> 1
            定义的不是 tuple ，这是一个数，这是因为括号()即可以表示 tuple，又可以表示数学公式
            中的小括号，这就产生了歧义，因此，Python 规定，这种情况下，按数学中小括号进行计算，
            所以计算结果自然是 1。
            
            所以，只有 1 个元素的 tuple 定义时必须加上一个逗号",",来消除歧义。
            >>> t = (1,)
            >>> t
            (1, )
            
        最后来看一个“可变的”tuple：     
            
            >>> t = ('a', 'b', ['A', 'B']) 
            >>> t[2][0] = 'X' 
            >>> t[2][1] = 'Y'
            >>> t
            ('a', 'b', ['X', 'Y'])
            >>>         
        
            这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。
            不是说tuple一旦定义后就不可变了吗？怎么后来又变了？           
            
            表面上，tuple 的元素确实变了，但其实变的不是 tuple 的元素，而是 list 的元素，
            tuple- 开始指向的 list 并没有改成变的 list。所以，tuple 所谓的“不变”是说，
            tuple 的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，
            就不能改成指向其他对象，但指向的这个list本身是可变的！ 
        
        理解了“指向不变”后，要创建一个内容也不变的 tuple 怎么做，那就是必须保证tuple中
        的每个元素本身也是不变的。
    
    6、条件判断：
    
        if 语句执行有一个特点，它是从上往下判断，如果在某个判断上是 True, 把该判断对应的
        语句执行后，就忽略掉剩下的 elif 和 else, 所以，为什么下面程序的打印结果是 teenager：
        
            >>> age = 20
            >>> if age>6:
            ...     print('teenager')
            ... elif age==20:
            ...     print('adult')
            ... else:
            ...     print('kid')
            ... 
            teenager
            >>>        
            
        if判断条件还可以简写，比如写：

            if x:    
                print('True')
                
        只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。        
                            
        input：  
            
            >>> birth = input('birth:')
            birth:200
            >>> if birth < 200:
            ...     print('00 before')
            ... else:
            ...     print('00 after')
            ... 
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: '<' not supported between instances of 'str' and 'int'
            
            这是因为 input() 返回的数据类型是str, str 不能直接和整数比较，
            必须先把 str 转换成整数，Python 提供了 int() 函数来完成这个事。
            
            s = input('birth: ')
            birth = int(s)
            if birth < 2000:
                print('00前')
            else:
                print('00后')     
                
            但是，如果输入abc呢？又会得到一个错误信息：
          >>> aa = int(input('birth:')) 
          birth:abc
          Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
          ValueError: invalid literal for int() with base 10: 'abc'
            
          因为int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了。    
    
    7、循环:
    
        Python的循环有两种:
           
            一种是for...in循环，依次把可迭代容器中的每个元素迭代出来，然后执行缩进块中的语句。
            第二种循环是 while 循环，只有条件满足就不断循环，条件不满足时退出循环。
            
        break语句可以在循环过程中直接退出循环，
        而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
        这两个语句通常都必须配合if语句使用。    
             
        要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
        大多数循环并不需要用到break和continue语句，可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
            
    8、使用 dict 和 set:
    
        dict:
            
            Python 内置了字典，dict 的支持，dict 全称是 dictionary,在其他语言中也称为 map,
            使用 （key-value）存储，具有极快的查找速度。
            
            为什么dict查找速度这么快：
                
                这种key-value 存储方式，在放进去的时候，必须根据key算出value的存放位置，
                这样取的时候才能根据 key 直接拿到 value。
                这个通过key计算位置的算法称为哈希算法（Hash）。
                
            如何避免key不存在错误：
            
                一个通过 in 判断 key 是否存在。
                二是通过dict 提供的get()方法，如果key 不存在，可以返回 None,或者自己指定的value。
                
                >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
                >>> d.get('ddd')
                >>> d.get('ddd',-1)
                -1
                >>>    
                
                注意：返回None的时候Python的交互环境不显示结果。     
                 
            和list比较，dict有以下几个特点：
            
                查找和插入的速度极快，不会随着key的增加而变慢；
                需要占用大量的内存，内存浪费多。     
            
            而list相反：

                查找和插入的时间随着元素的增加而增加；
                占用空间小，浪费内存很少。    
                
            所以，dict是用空间来换取时间的一种方法。
            
            dict可以用在需要高速查找的很多地方,在Python代码中几乎无处不在，正确使用dict非常重要，
            需要牢记的第一条就是dict的key必须是不可变对象        
                
        set:
            
            set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于key不能重复，
            所以，在set中，没有重复的key。
            
            要创建一个 set, 需要提供一个 list 作为输入集合：
            >>> s = set([1, 2, 3])
            >>> s
            {1, 2, 3}
            
            注意：传入的参数 [1, 2, 3]是一个 list, 而显示的 {1, 2, 3}只是告诉你这个 set 内部
            有 1, 2, 3 这 3 个元素，显示的顺序也不表示 set 是有序的。
            
            set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象。
       
            
"""02| 函数 """            
                    
    1、调用函数：
        函数就是最基本的一种代码抽象的方式。
        调用函数的时候，如果传入的参数数量不对，会报 TypeError 的错误，
        并且 Python 会明确的告诉你：abs() 有且只有 1 个参数，但给出了两个：
        >>> abs(1, 2)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: abs() takes exactly one argument (2 given)
        
        如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，
        并且给出错误信息：str是错误的参数类型：                         
        >>> abs('a')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: bad operand type for abs(): 'str'        
        
        数据类型转换：
        
            >>> bool(1)
            True
            >>> bool('')
            False            
                            
        函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，
        相当于给这个函数起一个“别名”
        >>> a = abs
        >>> a(-1)
        1
                
    2、定于函数：
        
        注意，函数体内部的语句在执行时，一旦执行到 return 时，函数就执行完毕，并将结果返回。
        因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
        
        如果没有 return 语句，函数执行完毕后也会返回结果，只是结果为 None, return None, 可以简写return。
        
        空函数：
            如果想定义一个什么事也不做的空函数，可以用 pass 语句：
            def nop():
                pass
                
            pass 语句什么都不做，那有什么用？实际上 pass 可以用来作为占位符，
            比如现在还没有想好怎么写函数的代码，可以先放一个 pass,让代码能运行
            起来，比如：
           
                if age >= 18:
                    pass
                
            缺少 pass, 代码运行就会出现语法错误。
            
            定义函数时，需要确定函数名和参数个数；

        如果有必要，可以先对参数的数据类型做检查；
        
            isinstance:
                def my_abs(x):
                    if not isinstance(x, (int, float)):
                        raise TypeError('bad operand type')
                    if x >= 0:
                        return x
                    else:
                        return -x
            type():
            
                ip_port = ['219.135.164.245', 3128]
                if type(ip_port) is list:
                    print('list数组')
                else:
                    print('其他类型')
            
            isinstance() 和 type() 的区别在于：
            type()不会认为子类是一种父类类型
            isinstance()会认为子类是一种父类类型       
            
            class A:
                pass
            
            class B(A):
                pass
            
            isinstance(A(), A)  # returns True
            type(A()) == A      # returns True
            isinstance(B(), A)    # returns True
            type(B()) == A        # returns False
            
        
        函数体内部可以用return随时返回函数结果；
        函数执行完毕也没有return语句时，自动return None。
        函数可以同时返回多个值，但其实就是一个tuple。      
    
    3、参数调用：                    
                
        函数如下：
            
            def add_end(L=[]):
                L.append('END')
                return L            
            
            >>> add_end()
            ['END', 'END']
            >>> add_end()
            ['END', 'END', 'END']        
                
        默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
        
        原因解释如下：
        
            Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
            因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
            则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。            
                
        定义默认参数要牢记一点：默认参数必须指向不变对象。
        要修改上面的例子，我们可以用None这个不变对象来实现：
            
            def add_end(L=None):
                if L is None:
                    L = []
                L.append('END')
                return L        
                
        Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

        默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
        要注意定义可变参数和关键字参数的语法：
        *args是可变参数，args接收的是一个tuple；
        **kw是关键字参数，kw接收的是一个dict。
        
        以及调用函数时如何传入可变参数和关键字参数的语法：
        可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
        关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
        使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
        命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
        定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。        
    
    4、递归函数：
    
        使用递归函数需要注意防止栈溢出。在计算机中，函数调用听过栈(stack)这种数据结构实现，
        每进入一个函数调用，栈就会加上一层栈帧，每当函数返回，栈就会减一层栈帧。
        由于栈的大小不是无限的，所以，递归函数调用次数过多，会导致栈溢出。
        
        解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，
        把循环看成是一种特殊的尾递归函数也是可以的。
        
        尾递归是指，在函数返回的时候，调用自身本身，并且，return 语句不包含表达式。
        这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
        都只占用一个栈帧，不会出现栈溢出的情况。
        
        举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
        fact(n)用递归的方式写出来就是：

            def fact(n):
                if n==1:
                    return 1
                return n * fact(n - 1)
            
        由于 fact(n) 函数由于 return n*fact(n - 1) 引入了乘法表达式，所以就不是尾递归。
        要改成尾递归方式，需要多一点代码，主要是把每一步的乘积传入到递归函数中：
        
            def fact(n):
                return fact_iter(n, 1)
            
            def fact_inter(num, product):
                if num == 1:
                    return product
                return fact_inter(n-1, num*product)
                 
        可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，
        num - 1和num * product在函数调用前就会被计算，不影响函数调用。    
        
        遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
        所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。    
       
            
"""03| 高级特性 """

    在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
    基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。
    请始终牢记，代码越少，开发效率越高。
                
    1、切片:
    
        经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，
        能大大简化这种操作。        
        有了切片操作，很多地方循环就不再需要了。Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作。    
            
    2、迭代：
    
        如果给定一个 list 或 tuple, 我们可以通过 for 循环来遍历这个 list 或 tuple, 这种遍历我们称为迭代(Iteration)。
        在 Python 中，迭代是通过 for ... in 来完成的，而很多语言比如C语言，迭代 list 。
        可以看出，Python 的 for 循环抽象程度要高于 C 的 for 循环，因为 Python 的 for 循环不仅可以用在 list 或tuple上，
        还可以作用在其他可迭代对象上。
        
        list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，
        无论有无下标，都可以迭代，比如dict就可以迭代：
            
            >>> d = {'a':1, 'b':2, 'c':3}
            >>> for key in d:
                    print(key)
            a
            b
            c
            
            因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
            默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
            如果要同时迭代key和value，可以用for k, v in d.items()。
            
            所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
            而我们不太关心该对象究竟是list还是其他数据类型。
        
            那么，如何判断>>> isinstance('abc', Iterable) # str是否可迭代
                True
                >>> isinstance([1,2,3], Iterable) # list是否可迭代
                True
                >>> isinstance(123, Iterable) # 整数是否可迭代
                False一个对象是可迭代对象呢？方法是通过 collections 模块的 iterable类型判断：
                >>> from collections import Iterable
                
        Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
            
            >>> for i, value in enumerate(['A', 'B', 'C']):
            ...     print(i, value)
            ...
            0 A
            1 B
            2 C
        
        
    3、列表生成式：    
        
        列表生成式即 List Comprehensions, 是 Python 内置非常简单却强大的可以用来创建 list 的生成式。
        运用列表生成式，可以写出非常简洁的代码。
        运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
        
    4、生成器：
    
        通过列表生成式，可以直接创建一个列表，但是由于内存容量限制，而且创建一个很大的列表，不仅仅
        占用很大存储空间，如果我们仅仅访问前面几个元素，那么后面大多数元素所占的空间就白白浪费。
        所以，如果列表元素可以按照某种算法推算出来，那么我们是否可以在循环的过程中不断推算出后续的元素呢？
        这样就不必完整的list,从而节省大量的空间，在Python 中，这种一边循环一边计算的机制，称为生成器：generator。
        
    5、迭代器：
    
        可以直接用于 for 循环的数据类型是可迭代对象有以下几种：
        一类是集合数据类型，如：list、tuple、dict、set、str等。
        一类是 generator，包括生成器和带 yield 的generator function。
        可以使用isinstance()判断一个对象是否是Iterable对象：  
            
            >>> from collections import Iterable
            >>> isinstance([], Iterable)
            True
            >>> isinstance({}, Iterable)
            True
            >>> isinstance('abc', Iterable)
            True
            >>> isinstance((x for x in range(10)), Iterable)
            True
            >>> isinstance(100, Iterable)
            False    
        
        而生成器不但可以作为 for 循环，还可以被 next() 函数不断调用
        并返回下一个值，直到最后抛出 StopIteration 错误表示无法继续
        返回下一个值了。
        
        可以被 next() 函数调用并不断返回下一个值的对象称为迭代器:Iterator。
        可以使用 isinstance() 判断一个对象是否是 Iterator 对象：
            
            >>> from collections import Iterator
            >>> isinstance((x for x in range(10)), Iterator)
            True
            >>> isinstance([], Iterator)
            False
            >>> isinstance({}, Iterator)
            False
            >>> isinstance('abc', Iterator)
            False
                    
        生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
        把list、dict、str等Iterable变成Iterator可以使用iter()函数：
            
            >>> isinstance(iter([]), Iterator)
            True
            >>> isinstance(iter('abc'), Iterator)
            True
              
        为什么list、dict、str等数据类型不是Iterator？
            因为 Python 的 Iterator 对象表示的是一个数据流，Iterator 对象
            可以被 next() 函数调用并不断返回下一个数据，直到没有数据时抛出
            StopIteration 错误。可以把这个数据流看作是一个有序序列，但我们
            不能提前知道序，列的长度，只能不断通过 next() 函数实现按需计算下一个
            数据，所以 Iterator 的计算是惰性的，只有在需要返回下一个数据时它才会计算。
            
            Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
            而使用list是永远不可能存储全体自然数的。


"""04| 函数式编程 """ 

    函数式编程--Functional Programming，虽然也可以归结到面向过程的程序设计，
    但其思想更接近数学计算。
    
    函数式编程是一种抽离程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量。
    
    函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
    Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。          
    
    1、 高阶函数:
    
        （1）变量可以指向函数：
            >>> abs(-10)
            10
            >>> abs
            <built-in function abs>
              
            可见，abs(-10)是函数调用，而abs是函数本身。
             
            >>> f = abs
            >>> f
            <built-in function abs>
        
            结论：函数本身也可以赋值给变量，即：变量可以指向函数。
        
        （2）函数名也是变量：
            
            那么函数名是什么呢？函数名其实就是指向函数的变量！对于 abs()这个函数
            完全可以把函数名 abs 看成变量，它指向一个计算绝对值的函数！
            
            >>> abs = 10
            >>> abs(-10)
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: 'int' object is not callable
            
            把abs指向10后，就无法通过abs(-10)调用该函数了！
            因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

            当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。
            要恢复abs函数，请重启Python交互环境。   
            
            注：由于abs函数实际上是定义在import builtins模块中的，
            所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。
        
        （3）传入函数：
        
            既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
            把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
        
        （4）map/reduct:
            
            map() 函数接收两个参数，一个是函数，一个是 Iterable，map 将传入的函数依次作用到序列的每个元素，
            并把结果作为新的 Iterator 返回。
            
            >>> def f(x):
            ...     return x * x
            ...
            >>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
            >>> list(r)
            [1, 4, 9, 16, 25, 36, 49, 64, 81]
            
            map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
            因此通过list()函数让它把整个序列都计算出来并返回一个list。
            
            >>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
            ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            
            reduce 把一个函数作用在一个序列[x1, x2, x3, x4, ...]上，这个函数必须接收两个参数，
            reduce 把结果继续和序列的下一个元素做累积计算，其效果就是：
            
                reduct(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
            
            比方说一个序列求和，就可以用 reduce 实现：
                
                >>> form functools import reduce
                >>> def add(x, y):
                ... return x + y
                ...
                >>> reduce(add, [1, 3, 5, 7, 9])
                25
            当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
               
            把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：    
                
                >>> from functools import reduce
                >>> def fn(x, y):
                ...     return x*10 + y
                
                >>>reduce(fn, [1, 3, 5, 7, 9])
                13579    
    
            对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
                
                from functools import reduce

                DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
                
                def str2int(s):
                    def fn(x, y):
                        return x * 10 + y
                    def char2num(s):
                        return DIGITS[s]
                    return reduce(fn, map(char2num, s))    
                            
            还可以用lambda函数进一步简化成：
                
                from functools import reduce
                DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
               
                def char2num(s):
                    return DIGITS[s]
                
                def str2int(s):
                    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
        
        (5) filter:
        
            和 map() 类似，filter() 也接收一个函数和一个序列，和 map() 不同的是
            filter() 把传入的函数依次作用每个元素，然后返回值是 True 还是 False
            决定保留还是丢弃该元素。
            
            在一个 list 中，删除偶数，只保留奇数，可以这么写：
                def is_odd(n):
                    return n%2 == 1:
                    
                list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
                结果是：[1, 5, 9, 15]
            
            把一个序列中的空字符串删掉，可以这么写：    
                
                def not_empty(s):
                    return s and s.strip()
                
                list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
                # 结果: ['A', 'B', 'C']
            可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
            注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
            所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
            
        (6) sorted:
        
            Python内置的sorted()函数就可以对list进行排序：
            >>> sorted([36, 5, -12, 9, -21])
            [-21, -12, 5, 9, 36]
            
            此外，sorted() 函数也是一个高级函数，它还可以接收一个 key 函数来实现
            自定义的排序，例如按绝对值大小排序：
            
            >>> sorted([36, 5, -12, 9, -21], key=abs)
            [5, 9, -12, -21, 36]   
            
            key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序。
            
            要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
            >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
            ['Zoo', 'Credit', 'bob', 'about']
            
            sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
        
        
        
        
        
        
        
        
        
        
        
        
                
                
                
                    
          
                
                
                
                
                
                
                
                
                
                
                
                
                