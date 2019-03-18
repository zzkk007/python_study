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
            
            假设我们用一组tuple表示学生名字和成绩：
            L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
            请用sorted()对上述列表分别按名字排序：
            
                def by_name(t):
                    return t[0]
                L2 = sorted(L, key=by_name)
                print(L2)
                
            再按成绩从高到低排序：
                
                def by_name(t):
                    return t[1]
                L2 = sorted(L, key=by_name)
                print(L2)    
            
            sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
        
    2、返回函数：
    
        高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
        
        def lazy_sum(*args):
            def sum():
                ax = 0
                for n in args:
                    ax = ax + n
                return ax
            return sum    
        
        >>> f = lazy_sum(1, 3, 5, 7, 9)
        >>> f
        <function lazy_sum.<locals>.sum at 0x101c6ed90>
        
        闭包：
            注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
            其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
            
            另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
            我们来看一个例子：
                
                def count():
                    fs = []
                    for i in range(1, 4):
                        def f():
                             return i*i
                        fs.append(f)
                    return fs
                
                f1, f2, f3 = count()
            
            在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
            你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
                >>> f1()
                9
                >>> f2()
                9
                >>> f3()
                9
        
            全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
            等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
            返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。    
                
            如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
            无论该循环变量后续如何更改，已绑定到函数参数的值不变：    
                
                def count():
                    def f(j):
                        def g():
                            return j*j
                        return g
                    fs = []
                    for i in range(1, 4):
                        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
                    return fs        
                          
                >>> f1, f2, f3 = count()
                >>> f1()
                1
                >>> f2()
                4
                >>> f3()
                9    
                
    3、匿名函数：
    
        关键字lambda表示匿名函数，冒号前面的x表示函数参数。
        匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
        用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
        此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

            >>> f = lambda x: x * x
            >>> f
            <function <lambda> at 0x101c6ef28>
            >>> f(5)
            25            
                        
    4、装饰器：
    
        在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
        OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
        直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

        decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。            
                                    
    5、偏函数：
        
        Python 的 functools 模块提供了很多有用的功能，其中一个就是偏函数(Partial function)
        这里的偏函数和数学意义上的偏函数不一样。
        
        在介绍函数参数的时候，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
        int() 函数可以把字符串换为整数，当仅传入字符串时，int() 函数默认十进制转换：
        >>> int('1234')
        1234
        
        但 int() 函数还提供额外的 base 参数，默认值为 10，如果传入 base 参数，就可以做 N 进制转换：
        >>> int('12345', base=8)
        5349
        
        假设要转换大量的二进制字符串，每次都要传入 int(x, base=2) 非常麻烦，于是，
        可以定义一个 int2()的函数，默认把 base=2 传进去：
            def int2(x, base=2):
                return int(x, base)
        这样，我们转换二进制就非常方便了：
            >>> int2('1000000')
            64
            >>> int2('1010101')
            85    
        
        functools.partial 就是帮助我们创建一个偏函数的，不需要自己定义int2()，
        可以直接使用下面的代码创建一个新的函数 int2:
            
            >>> import functools
            >>> int2 = functools.partial(int, base=2)
            >>> int2('1000000')
            64
        
        简单总结 functools.partial 的作用就是，把一个函数的某些参数给固定住(也就是设置默认值)
        返回一个新的函数，调用这个新的函数会更简单。
        
        注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，
        但也可以在函数调用时传入其他值：         
            
            >>> int2('1000000', base=10)
            1000000
            
        最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：        
            int2 = functools.partial(int, base=2)
        实际上固定了int()函数的关键字参数base，也就是：

            int2('10010')
            相当于：
            
            kw = { 'base': 2 }
            int('10010', **kw)
               
    
        max2 = functools.partial(max, 10)
        实际上会把10作为*args的一部分自动加到左边，也就是：
            max2(5, 6, 7)
        相当于：
            args = (10, 5, 6, 7)
        
            
"""05| 面向对象编程"""

    面向对象编程--Object Oriented Programming，简称 OOP,是一种程序设计思想。
    OOP 把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
    
    面向过程的设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
    为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割
    成小块函数来降低系统的复杂度。
    
    而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收
    其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一些列消息在各个
    对象之间传递。
    
    在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象
    数据类型就是面向对象中的类(class)的概念。
    
    我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处：
    假设我们要处理学生的成绩表，为了表示一个学生的成绩，
    面向过程的程序可以用一个dict表示：
        std1 = { 'name': 'Michael', 'score': 98 }
        std2 = { 'name': 'Bob', 'score': 81 }    
    而处理学生成绩可以通过函数实现，比如打印学生的成绩：
        def print_score(std):
            print('%s: %s' % (std['name'], std['score']))            
        
    如果采用面向对象的程序设计思想，我们首先考虑的不是程序的执行流程，
    而是  Student 这种数据类型应该被视为一个对象，这个对象拥有 name 和 score
    这两个属性(Property)。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象
    然后，给这个对象发一个 print_score 消息，让对象自己把自己的数据打印出来。
        class Student(object):
            def __init__(self, name, score):
                self.name = name
                self.score = score
                
            def print_score(self):
                print("%s:%s"%(self.name, self.score))
                 
    给对象发消息实际上就是调用对象对象的关联函数，我们称之为对象的方法(Method)
    面向对象的程序写出来像这样：
    
        bart = Student('Bart Simson', 60)
        bart.print_score()             
                
    面向对象的抽象程度比函数要高，因为一个 Class 即包含数据，又包含操作数据的方法。
              
    1、类和实例：
    
        面向对象最重要的概念就是类(Class)和实例(Instance)，必须牢记类是抽象的模板，
        比如 Student 类，而实例是根据类创建出来的一个个具体的“对象”，
        每个对象都拥有相同的方法，但各自的数据可能不同。
        
        在类中，如果有了__init__ 方法，在创建实例的时候，就不能传入空的参数了，
        必须传入与 __init__ 方法匹配的参数，但 self 不需要传，Python 解释器
        自己会把实例变量传进去：
        
        数据封装：
            
            面向对象编程的一个重要的特点就是数据封装。在 Student 类中，每个实例都拥有各自的
            name 和 score 数据，我们可以通过函数来访问这些数据。
                >>> def print_score(std):
                ...     print('%s: %s' % (std.name, std.score))
                ...
                >>> print_score(bart)
                Bart Simpson: 59
                
            但是，既然 Student 实例本身就拥有这些数据，要访问这些数据，
            就没有必要从外面的函数去访问，可以直接在 Student 类的内部
            定义访问数据的函数，这样，就把"数据"给封装起来了，这些封装
            的数据的函数是和 Student 类本身关联起来的，我们称之为类的方法。
            
                class Student(object):

                    def __init__(self, name, score):
                        self.name = name
                        self.score = score
                
                    def print_score(self):
                        print('%s: %s' % (self.name, self.score))      
            
            要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
            要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，
            其他参数正常传入：

                >>> bart.print_score()
                Bart Simpson: 59
                                
            这样一来，我们从外部看 Student 类，就需要知道，就只需要知道，
            创建实例需要给出name和score，而如何打印，都是在Student类的
            内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，
            但却不用知道内部实现的细节。
    
        类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
        方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
        通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。  
    
    
    2、访问限制：
        
        在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，
        这样，就隐藏了内部的复杂逻辑。
        
        但是，从前面定义的 Student 类的定义来看，外部代码还是可以自由地修改一个实例的 name，score 属性。
        
            >>> bart = Student('Bart Simpson', 59)
            >>> bart.score
            59
            >>> bart.score = 99
            >>> bart.score
            99
        
        如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
        在 Python 中，实例的变量名如果以__开头，就变成了一个私有变量(Prive)
        只要在内部可以使用，外部不能访问。
        
            class Student(object):

                def __init__(self, name, score):
                    self.__name = name
                    self.__score = score
            
                def print_score(self):
                    print('%s: %s' % (self.__name, self.__score))
        
        改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问
        实例变量.__name和实例变量.__score了：
    
            >>> bart = Student('Bart Simpson', 59)
            >>> bart.__name
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            AttributeError: 'Student' object has no attribute '__name'
    
        这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
        但是如果外部代码要获取name和score怎么办？
        可以给Student类增加get_name和get_score这样的方法：
            
            class Student(object):
                ...
            
                def get_name(self):
                    return self.__name
            
                def get_score(self):
                    return self.__score
                
                def set_score(self, score):
                    self.__score = score
         
        最后注意下面的这种错误写法：
        
            >>> bart = Student('Bart Simpson', 59)
            >>> bart.get_name()
            'Bart Simpson'
            >>> bart.__name = 'New Name' # 设置__name变量！
            >>> bart.__name
            'New Name'
    
        表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量
        和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器
        自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
        
            >>> bart.get_name() # get_name()内部返回self.__name
            'Bart Simpson'
    
    
    3、继承和多态：
    
        class Animal(object):
            def run(self):
                print('Animal is running...')
    
        class Dog(Animal):

            def run(self):
                print('Dog is running...')
        
        class Cat(Animal):
        
            def run(self):
                print('Cat is running...')
        
        当子类和父类都存在相同的 run() 方法时，我们说，子类的run()方法覆盖了父类的run()
        在代码运行的时候，总是调用子类的run()，这样，我们就获得了继承的另一个好处：多态。
        
        要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个 class 的时候，
        我们实际上是定义了一种数据类型。我们定的数据类型和python自带的数据类型，list、str没什么两样。
            
            a = list()
            b = Animal()
            c = Dog()
        
        判断一个变量是否是某个数据类型用 isinstance()判断：
        
            >>> isinstance(a, list)
            True
            >>> isinstance(b, Animal)
            True
            >>> isinstance(c, Dog)
            True   
            >>> isinstance(c, Animal)
            True 
                        
        看了 c 不仅仅是 Dog, C 还是 Animal!
        在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看作是父类。
        但是，反过来就不行：
            
            >>> b = Animal()
            >>> isinstance(b, Dog)
            False
        
        Dog可以看成Animal，但Animal不可以看成Dog。                 
        
        要理解多态的好处，我们需要再编写一个函数，这个函数接收一个 Animal 类型的变量：
        
            def run_twice(animal):
                animal.run()
                animal.run()
        当我们传入 Animal 的实例时，run_twice() 就打印出：
        
            >>> run_twice(Animal())
            Animal is running...
            Animal is running...        
                                       
        当我们传入 Dog 的实例时，run_twice() 就打印出：
        
            >>> run_twice(Dog()):
            Dog is running...
            Dog is running...
                    
            class Tortoise(Animal):
                def run(self):
                    print('Tortoise is running slowly...')        
                
            >>> run_twice(Tortoise())
            Tortoise is running slowly...
            Tortoise is running slowly...    
            
        你会发现，新增一个 Animal 的子类，函数 run_twice() 必须做任何修改，任何依赖 Animal
        作为参数的函数或者方法都可以不加修改的正常运行，原因就是多态。
        
        多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
        因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。    
            
        多态的意思就是对于一个变量，只需要知道他是 Animal 类型，无需确切的知道它的子类型，就可以
        放心地调用 run() 方法，而具体调用的run() 方法是作用在 Animal、Dog、Cat对象上，由运行时
        该对象的确切类型决定，这就是多态的真正威力：调用方只管调用，不管细节，当我们新增一种Animal
        的子类时，只要确保 run() 方法编写正确，不要管原来的代码是如何调用的。
        这就是著名的“开闭” 原则：
            对扩展开发：允许新增 Animal 子类
            对修改封闭：不需要修改依赖 Animal 类型的 run_twice() 等函数。
                
        静态语言 vs 动态语言：
        
            对于静态语言（java）来说，如果需要传入 Animal 类型，则传入的对象必须是 Animal 
            类型或者子类,否则，将无法调用 run() 方法。
            
            对于Python这样的动态语言来说，则不一定需要传入 Animal 类型，我们只需要保证传入
            的对象有一个 run() 方法就可以了:
            
                class Timer(object):
                    def run(self):
                        print('Start...')    
            
            这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
            一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。        
            
            Python的“file-like object“就是一种鸭子类型。
            对真正的文件对象，它有一个read()方法，返回其内容。
            但是，许多对象，只要有read()方法，都被视为“file-like object“。
            许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，
            完全可以传入任何实现了read()方法的对象。 
            
        class Animal(object):

            def run(self):
                print("Animal run ...")
        
        class Dog(Animal):
            def run(self):
                print("Dog run ...")
        
        class Cat(Animal):
            def run(self):
                print("Cat run ...")
        
        class duck(object):
            def run(self):
                print("duck run ...")
        
        
        def two_func(Animal):
            Animal.run()
            Animal.run()
        
        two_func(Animal())
        two_func(Dog())
        two_func(duck())    
            
        运行结果：    
            Animal run ...
            Animal run ...
            Dog run ...
            Dog run ...
            duck run ...
            duck run ...           
                    
    4、获取对象信息：
    
        当我们拿到一个对象的引用时，如何知道这个对象是什么类型，有哪些方法？
        
        使用 type():
           
            但是type()函数返回的是什么类型呢？它返回对应的Class类型。
            如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
            
            >>> type(123)==type(456)
            True
            >>> type(123)==int
            True
            >>> type('abc')==type('123')
            True
            >>> type('abc')==str
            True
            >>> type('abc')==type(123)
            False
                          
            判断基本数据类型可以直接写int，str等，
            但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：    
                
                >>> import types
                >>> def fn():
                ...     pass
                ...
                >>> type(fn)==types.FunctionType
                True
                >>> type(abs)==types.BuiltinFunctionType
                True
                >>> type(lambda x: x)==types.LambdaType
                True
                >>> type((x for x in range(10)))==types.GeneratorType
                True      
        
        使用 isinstance:
        
            >>> isinstance(a, list)
            True
            >>> isinstance(b, Animal)
            True
            >>> isinstance(c, Dog)
            True   
            >>> isinstance(c, Animal)
            True 
            
            >>> isinstance([1, 2, 3], (list, tuple))
            True
            >>> isinstance((1, 2, 3), (list, tuple))
            True            
            总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
        
        使用 dir():
        
            如果要获得一个对象的所有属性和方法，可以使用dir()函数。
            它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
            >>> dir('ABC')
            ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
            
            仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，
            我们可以直接操作一个对象的状态：
                
                >>> class MyObject(object):
                    def __init__(self):
                        self.x = 9
                    def power(self):
                        return self.x * self.x
            紧接着，可以测试该对象的属性：
            
                >>> hasattr(obj, 'x') # 有属性'x'吗？
                True
                >>> obj.x
                9
                >>> hasattr(obj, 'y') # 有属性'y'吗？
                False
                >>> setattr(obj, 'y', 19) # 设置一个属性'y'
                >>> hasattr(obj, 'y') # 有属性'y'吗？
                True
                >>> getattr(obj, 'y') # 获取属性'y'
                19
                >>> obj.y # 获取属性'y'
                19
            
            如果试图获取不存在的属性，会抛出AttributeError的错误：
                
                >>> getattr(obj, 'z') # 获取属性'z'
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                AttributeError: 'MyObject' object has no attribute 'z'       
                
        通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，
        只有在不知道对象信息的时候，我们才会去获取对象信息。
        如果可以直接写：
            sum = obj.x + obj.y
        就不要写：
            sum = getattr(obj, 'x') + getattr(obj, 'y')
                
        一个正确的用法的例子如下：
            
            def readImage(fp):
                if hasattr(fp, 'read'):
                    return readData(fp)
                return None        
            
            假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
            如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

            请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，
            不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
            但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。            
    
    5、实例属性和类属性：
    
        由于 Python 是动态语言，根据类创建的实例可以任意绑定属性。
        给实例绑定属性的方法是通过实例变量，或者通过 self 变量：
        
            class Student(object):
                def __init__(self, name):
                    self.name = name
            
            s = Student('Bob')
            s.score = 90
                
        但是，如果 Student 类本身需要绑定一个属性，可以直接在 Class 中定义属性
        这种属性是类属性，归 Student 类所有：
        
            class Student(object):
                name = 'Student'
                
            >>> class Student(object):
            ...     name = 'Student'
            ...
            >>> s = Student() # 创建实例s
            >>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
            Student
            >>> print(Student.name) # 打印类的name属性
            Student
            >>> s.name = 'Michael' # 给实例绑定name属性
            >>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
            Michael
            >>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
            Student
            >>> del s.name # 如果删除实例的name属性
            >>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
            Student
            
        在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
        因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，
        再使用相同的名称，访问到的将是类属性。
        
        实例属性属于各个实例所有，互不干扰；
        类属性属于类所有，所有实例共享一个属性；
        不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
        
        
"""06| 面向对象高级编程"""

    数据封装、继承和多态只是面向对象程序设计汇总最基本的三个概念。
    在 Python 中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
    多重继承、定制类、元类等概念。
    
    1、使用 __slots__:
        
        正常情况下，当我们定义一个 class, 创建了一个 class 的实例后，我们
        可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义 class:
        
            class Student(object):
                pass         
            
        然后，尝试给实例绑定一个属性：
            
            >>> s = Student()
            >>> s.name = 'Jack'
            >>> print(s.name)
            Jack
            >>> 
        
        还可以尝试给实例绑定一个方法：
            
            >>> def set_age(self, age):  #定义一个函数作为实例方法
            ...     self.age = age
            ... 
            >>> 
            >>> from types import MethodType
            >>> 
            >>> s.set_age = MethodType(set_age,s) # 给实例绑定一个方法
            >>> s.set_age(23)
            >>> s.age
            23
            >>>     
        
        但是，给一个实例绑定的方法，对另一个实例是不起作用的：
        
            >>> s2 = Student() # 创建新的实例
            >>> s2.set_age(25) # 尝试调用方法
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            AttributeError: 'Student' object has no attribute 'set_age'       

        为了给所有实例都绑定方法，可以给class 绑定方法：
        
            >>> def set_score(self, score):
                self.score = score
            >>> Student.set_score = set_score
            
        通常情况下，set_score 方法可以直接定义在 class中，但动态绑定允许我们在程序运行过程中
        动态的给 class 加上功能，这在静态语言中很难实现。
        
        使用__slots__:
        
            但是，如果我们想限制实例的属性，只允许对 Student 实例添加 name 和 age 属性。
            为了达到这个目的，Python 允许在定义 class 的时候，定义一个特殊的 __slots__ 变量，
            来限制该 class 实例能添加的属性。
    
            >>> class Student(object):
            ...     __slots__ = ('name','age') # 用 tuple 定义允许绑定的属性名称
            ... 
            >>> 
            >>> s = Student()
            >>> s.name = 'Jack'
            >>> s.age = 20
            >>> s.score = 99
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            AttributeError: 'Student' object has no attribute 'score'
            >>> 
            >>> class GraduateStudent(Student):
            ...     pass
            ... 
            >>> g = GraduateStudent()
            >>> g.score = 99
            >>> 
            >>> g.score
            99
            >>> 
            
        除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。    
            
    2、使用 @property:
    
        在绑定属性时，如果我们直接把属性暴露出去，虽然写起了很简单，但是，没办法检查参数，导致可以随意更改：
        
            s = Student()
            s.score = 999
        
        这显然不合逻辑，为了限制 score 的范围，可以通过一个 set_score() 方法来设置成绩，再通过一个 get_score()
        来获取成绩，这样，在 set_score() 方法里，就可以检查参数：
        
            class Student(object):
                def get_score(self):
                    return self._score
                
                def set_score(self, value):
                    if not isinstance(value, int):
                        raise ValuError('score must be an integer!')
                    
                    if value < 0 or value > 100:
                        raise ValueError('score must between 0~100!')
                    self._score = value
              
        但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
        有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
        Python 内置了 @property 装饰器就是负责把一个方法变成属性调用的：
        
            class Student(object):

                @property
                def score(self):
                    return self.__score
            
                @score.setter
                def score(self, value):
                    if not isinstance(value, int):
                        raise ValueError('score must bu integer')
            
                    if value < 0 or value > 100:
                        raise ValueError('score must between o ~ 100')
            
                    self.__score = value

        @property的实现比较复杂，我们先考察如何使用。
        把一个 getter 方法变成属性，只需要加上 @property 就可以了，此时，@property 本身又创建了另一个
        装饰器 @socre.setter, 负责把一个 setter 方法变成属性赋值，于是，我们就拥有了一个可控的属性操作：
        
            >>> s = Student()
            >>> s.score = 60 # OK，实际转化为s.set_score(60)
            >>> s.score # OK，实际转化为s.get_score()
            60
            >>> s.score = 9999
            Traceback (most recent call last):
              ...
            ValueError: score must between 0 ~ 100!   

        注意到这个神奇的 @property, 我们在对实例属性操作的时候，就知道这个属性不可能直接暴露的，
        而是通过 getter 和 setter 方法来来实现的。 
        
        还可以定义只读属性，只定义getter 方法，不定义 setter 方法就是一个只读属性：
            
            class Student(object):
                @property
                def birth(self):
                    return self._birth
                
                @birth.setter
                def bitrh(self, value):
                    self._bitrh = value
                
                @property
                def age(self):
                    return 2019 - self._birth
            
        上面的 birth 是可读写属性，而 age 就是一个只读属性。
        
        @property广泛应用在类的定义中，可以让调用者写出简短的代码，
        同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。    
        
    3、多重继承：
    
            class Animal(object):
                pass
            
            # 大类:
            class Mammal(Animal):
                pass
            
            class Bird(Animal):
                pass
            
            # 各种动物:
            class Dog(Mammal):
                pass
            
            class Bat(Mammal):
                pass
            
            class Parrot(Bird):
                pass
            
            class Ostrich(Bird):
                pass
        
        现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
        
            class Runnable(object):
                def run(self):
                    print('Running...')
                    
            class Flyable(object):
                def fly(self):
                    print('Flying...')        
        
       
        通过多重继承，一个子类就可以同时获得多个父类的所有功能。
        
        MinIn:
            
            在设计类的继承关系时，通常，主线都是单一继承下来的，例如 Ostrich 继承 Bird。
            但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如,让 Ostrich 除了继承 Bird 外
            再同时继承 Runnable。这种设计通常称为 MixIn。
            
            MixIn 的目的就是给一个类增加多个功能，这样，在设计类的时候，优先考虑通过多重继承来组合多个
            MixIn 的功能，而不是设计多层的复杂的继承关系。
            
            Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
            而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。
            通过组合，我们就可以创造出合适的服务来。             
                
            比如，编写一个多进程模式的TCP服务，定义如下：
                
                class MyTCPServer(TCPServer, ForkingMixIn):
                    pass
                
            编写一个多线程模式的UDP服务，定义如下：
                
                class MyUDPServer(UDPServer, ThreadingMixIn):
                    pass  
                     
                               
        由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
        只允许单一继承的语言（如Java）不能使用MixIn的设计。

    4、定制类：
        
        Python 的 class 中有许多特殊用途的函数，帮助我们定义类。
        
        __str__:
                
            我们先定义一个Student类，打印一个实例：
    
                >>> class Student(object):
                ...     def __init__(self, name):
                ...         self.name = name
                ...
                >>> print(Student('Michael'))
                <__main__.Student object at 0x109afb190>    
            
            怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
            
                >>> class Student(object):
                ...     def __init__(self, name):
                ...         self.name = name
                ...     def __str__(self):
                ...         return 'Student object (name: %s)' % self.name
                ...
                >>> print(Student('Michael'))
                Student object (name: Michael)           
               
            但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
                
                >>> s = Student('Michael')
                >>> s
                <__main__.Student object at 0x109afb310>   
                   
            这是因为直接显示变量调用的不是__str__(), 而是 __repr__(), 两者的区别是
            __str__() 返回用户看到的字符串，而__repr__() 返回程序开发者看到的字符串。
            也就是说，__repr__() 是为调试服务的。
            解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，
            所以，有个偷懒的写法：
                
                class Student(object):
                    def __init__(self, name):
                        self.name = name
                    def __str__(self):
                        return 'Student object (name=%s)' % self.name
                    __repr__ = __str__            
        
        __iter__:
        
            如果想一个类被用于 for..in 循环，类似list那样，就必须实现一个 __iter__()方法，
            该方法返回一个迭代对象，然后，Python 的 for 循环就会不断调用该迭代对象的__next__()
            方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环。
            
            我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
            
                class Fib(object):
                    def __init__(self):
                        self.a, self.b = 0, 1 # 初始化两个计数器a，b
                
                    def __iter__(self):
                        return self  #实例本身就是迭代对象，故返回自己
                
                    def __next__(self):
                        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
                        if self.a > 1000:
                            raise StopIteration()
                        return self.a
                
                
                for n in Fib():
                    print(n)        
                 
        __getitem__:
            
            Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，
            比如，取第5个元素：
            
                >>> Fib()[5]
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                TypeError: 'Fib' object does not support indexing   
            
            要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
            
                class Fib(object):
                    def __getitem__(self, n):
                        a, b = 1, 1
                        for x in range(n):
                            a, b = b, a + b
                        return a    
            现在，就可以按下标访问数列的任意一项了：
                
                >>> f = Fib()
                >>> f[0]
                1
                >>> f[1]
                1
                >>> f[2]
                2
                >>> f[3]    
            
            但是list有个神奇的切片方法：
            对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，
            也可能是一个切片对象slice，所以要做判断：
            
                class Fib(object):
                    def __getitem__(self, n):
                        if isinstance(n, int): # n是索引
                            a, b = 1, 1
                            for x in range(n):
                                a, b = b, a + b
                            return a
                        if isinstance(n, slice): # n是切片
                            start = n.start
                            stop = n.stop
                            if start is None:
                                start = 0
                            a, b = 1, 1
                            L = []
                            for x in range(stop):
                                if x >= start:
                                    L.append(a)
                                a, b = b, a + b
                            return L
            
            通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
            这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
            
        __getattr__:
        
            正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错，比如定义 Student 类：
            
                class Student(object):
                    def __init__(self):
                        self.name = 'Michael'
            
            调用 name 属性，没有问题，但是，调用不存在 score 属性，就出问题了：
            
                >>> s = Student()
                >>> print(s.name)
                Michael
                >>> print(s.score)
                Traceback (most recent call last):
                  ...
                AttributeError: 'Student' object has no attribute 'score'    
            
            错误信息很清楚地告诉我们，没有找到score这个attribute。
            要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
            那就是写一个__getattr__()方法，动态返回一个属性。修改如下：     
            
                class Student(object):

                    def __init__(self):
                        self.name = 'Michael'
                
                    def __getattr__(self, attr):
                        if attr=='score':
                            return 99    
            
            当调用不存在的属性时，比如 score, Python 解释器会试图去调用 __getattr__(slef,'score')
            来尝试获得属性，这样，我们就有机会返回 score 的值：
                
                >>> s = Student()
                >>> s.name
                'Michael'
                >>> s.score
                99
            
            返回函数也是完全可以的：    
            注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，
            比如name，不会在__getattr__中查找。    
            
            此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
            要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
               
                class Student(object): 
                    def __getattr__(self, attr):
                        if attr=='age':
                            return lambda: 25
                        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)   
            
            这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。            
            现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
                http://api.server/user/friends
                http://api.server/user/timeline/list
            如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
            
            利用完全动态的__getattr__，我们可以写出一个链式调用：    
            
                class Chain(object):

                    def __init__(self, path=''):
                        self._path = path
                
                    def __getattr__(self, path):
                        return Chain('%s/%s' % (self._path, path))
                
                    def __str__(self):
                        return self._path
                
                    __repr__ = __str__    
        
        __call__：
        
            一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用 instance.method()来调用。
            能不能直接在实例本身上调用呢？在Python 中，答案是肯定的。
            
            任何类，只需要定义一个 __call__() 方法，就可以直接对实例进行调用。
            
                class Student(object):
                    def __init__(self, name):
                        self.name = name
                    
                    def __call__(self):
                        print('My name is %s' % self.name)
                        
                >>> s = Student('Michael')
                >>> s() # self参数不要传入
                My name is Michael.       
                
            __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
            所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

            如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，
            因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

            那么，怎么判断一个变量是对象还是函数呢？
            其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
            比如函数和我们上面定义的带有__call__()的类实例：
            
                >>> callable(Student())
                True
                >>> callable(max)
                True
                >>> callable([1, 2, 3])
                False
                >>> callable(None)
                False
                >>> callable('str')
                False    
            
            通过 callable() 函数，我们就可以判断一个对象是否是“可调用”对象。
            
    5、使用枚举类：
        
        当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
            JAN = 1
            FEB = 2
            MAR = 3
            ...
            NOV = 11
            DEC = 12
        
        好处是简单，缺点是类型是 int, 并且仍然是变量。
        
        更好的办法是为这样的枚举类型定义一个 calss 类，然后，每个常量都是 class 的一个唯一实例。
        Python 提供了 Enum 类来实现这个功能：
        
            from enum import Enum
            Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))   
        
        这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：    
            
            for name, member in Month.__members__.items():
                print(name, '=>', member, ',', member.value)       
            
            结果：
                
                Jan => Month.Jan , 1
                Feb => Month.Feb , 2
                Mar => Month.Mar , 3
                Apr => Month.Apr , 4
                May => Month.May , 5
                Jun => Month.Jun , 6
                Jul => Month.Jul , 7
                Aug => Month.Aug , 8
                Sep => Month.Sep , 9
                Oct => Month.Oct , 10
                Nov => Month.Nov , 11
                Dec => Month.Dec , 12
        
        value属性则是自动赋给成员的int常量，默认从1开始计数。    
        
        如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
            
            from enum import Enum, unique
            @unique
            class Weekday(Enum):
                Sun = 0 # Sun的value被设定为0
                Mon = 1
                Tue = 2
                Wed = 3
                Thu = 4
                Fri = 5
                Sat = 6    
            
            print(Weekday.Sun)
            print(Weekday.Sun.value) 
            打印结果：
                Weekday.Sun
                0         
        
        访问这些枚举类型可以有若干种方法：
            
            >>> day1 = Weekday.Mon
            >>> print(day1)
            Weekday.Mon
            >>> print(Weekday.Tue)
            Weekday.Tue
            >>> print(Weekday['Tue'])
            Weekday.Tue
            >>> print(Weekday.Tue.value)
            2
            >>> print(day1 == Weekday.Mon)
            True
            >>> print(day1 == Weekday.Tue)
            False
            >>> print(Weekday(1))
            Weekday.Mon
            >>> print(day1 == Weekday(1))
            True
            >>> Weekday(7)
            Traceback (most recent call last):
              ...
            ValueError: 7 is not a valid Weekday
            >>> for name, member in Weekday.__members__.items():
            ...     print(name, '=>', member)
            ...
            Sun => Weekday.Sun
            Mon => Weekday.Mon
            Tue => Weekday.Tue
            Wed => Weekday.Wed
            Thu => Weekday.Thu
            Fri => Weekday.Fri
            Sat => Weekday.Sat    
                        
                            
    6、使用元类：
        
        动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行是动态创建的。
        比方说我们要定义一个Hello的class，就写一个hello.py模块：
            
            class Hello(object):
                def hello(self, name='world'):
                    print('Hello, %s.' % name)    
            
        当Python解释器载入hello模块时，就会依次执行该模块的所有语句，
        执行结果就是动态创建出一个Hello的class对象，测试如下：
            
            >>> from hello import Hello
            >>> h = Hello()
            >>> h.hello()
            Hello, world.
            >>> print(type(Hello))
            <class 'type'>
            >>> print(type(h))
            <class 'hello.Hello'>   
            
        type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，
        而h是一个实例，它的类型就是class Hello。        
        我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
        type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，
        而无需通过class Hello(object)...的定义：
            
            >>> def fn(self, name='world'): # 先定义函数
            ...     print('Hello, %s.' % name)
            ...
            >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
            >>> h = Hello()
            >>> h.hello()
            Hello, world.
            >>> print(type(Hello))
            <class 'type'>
            >>> print(type(h))
            <class '__main__.Hello'>   
        
        要创建一个class对象，type()函数依次传入3个参数：
            
            class的名称；
            继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
            class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
       
        通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
        仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。        
        
        
        metaclass：
            
            除了使用 type() 动态创建类以外，要控制类的创建行为，还可以是使用 metaclass。
                
            metaclass，直译为元类，简单的解释就是：
            当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。            
            但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。           
            连接起来就是：先定义metaclass，就可以创建类，最后创建实例。            
            所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

"""07| 错误、调试和测试"""
    
    在程序运行过程中，总会遇到各种各样的错误。
    
    有的问题是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常为 bug，bug必须修复。
    有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。
    还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，
    或者从网络抓取数据，网络突然断掉了。这类错误也称为异常，在程序中通常是必须处理的，
    否则，程序会因为各种问题终止并退出。
    
    Python内置了一套异常处理机制，来帮助我们进行错误处理。
    此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。
    
    此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。
    
    1、错误处理：
    
        try...except 捕获错误有一个巨大的好处，就是可以跨越多层调用，比如函数 main()调用 foo(),
        foo()调用 bar(), 结果 bar() 错误了，这时，只要在 main() 捕获到了，就可以处理。
        
            def foo(s):
                return 10 / int(s)
            
            def bar(s):
                return foo(s)*2
            
            if __name__ == '__main__':
                try:
                    bar('0')
                except Exception as e:
                    print("Error:", e)
            
                finally:
                    print('finally...')    
            
            执行结果：
                
                Error: division by zero
                finally... 
                
        也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
        这样一来，就大大减少了写try...except...finally的麻烦。
    
        调用栈：
        
            如果错误没有被捕获，它就会一直往上抛，最后被 Python 解释器捕获，打印一个错误，
            来看看err.py：
            
                # err.py:
                def foo(s):
                    return 10 / int(s)
                
                def bar(s):
                    return foo(s) * 2
                
                def main():
                    bar('0')
                
                main()
            
            执行，结果如下：
                
                $ python3 err.py
                Traceback (most recent call last):
                  File "err.py", line 11, in <module>
                    main()
                  File "err.py", line 9, in main
                    bar('0')
                  File "err.py", line 6, in bar
                    return foo(s) * 2
                  File "err.py", line 3, in foo
                    return 10 / int(s)
                ZeroDivisionError: division by zero    
    
            出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。
            我们从上往下可以看到整个错误的调用函数链：
            
            错误信息第一行：    
                Traceback(most recent call last):
            告诉我们这是错误的跟踪信息。
            第2~3行：
                File "err.py", line 11, in <module>
                main()   
            调用 main() 出错，在代码文件 err.py 的第 11 行，但原因是在第9行：
                File "err.py", line 9, in main
                bar('0')
            调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
                File "err.py", line 6, in bar
                return foo(s) * 2       
            原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：
                File "err.py", line 3, in foo
                return 10 / int(s)    
            原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
                ZeroDivisionError: integer division or modulo by zero
            根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，
            但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。 
            出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。    
                
    2、调试：
    
        (1) print()
        
        (2)断言:
            
            def foo(s):
                n = int(s)
                assert n!=0,'n is zero!'
                return 10/n
                
            def main():
                foo('0')
                
            assert 的意思是，表达式 n != 0 应该是 True, 否则，根据程序运行的逻辑，后面的代码肯定出错。
            程序中如果到处充斥着assert，和print()相比也好不到哪去。
            不过，启动Python解释器时可以用-O参数来关闭assert：
                $ python -O err.py
                Traceback (most recent call last):
                  ...
                ZeroDivisionError: division by zero   
            
            关闭后，你可以把所有的assert语句当成pass来看。                          
        
        (3)logging
        
        (4)pdb:
            
            是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
            我们先准备好程序：   
                # err.py
                s = '0'
                n = int(s)
                print(10 / n)   
            
            然后启动：
                
                $ python -m pdb err.py
                > /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
                -> s = '0'    
                        
            以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
                
                (Pdb) l
                  1     # err.py
                  2  -> s = '0'
                  3     n = int(s)
                  4     print(10 / n)    
            
            输入命令n可以单步执行代码：
                
                (Pdb) n
                > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
                -> n = int(s)
                (Pdb) n
                > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
                -> print(10 / n)   
                
            任何时候都可以输入命令p 变量名来查看变量：
                
                (Pdb) p s
                '0'
                (Pdb) p n
                0  
                    
            输入命令q结束调试，退出程序：
                (Pdb) q    
                    
            这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，
            如果有一千行代码，要运行到第999行得敲多少命令啊。    
                
        (5) pdb.set_trace():
            
            这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，
            然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：           
                # err.py
                import pdb
                
                s = '0'
                n = int(s)
                pdb.set_trace() # 运行到这里会自动暂停
                print(10 / n)    
            
            运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，
            可以用命令p查看变量，或者用命令c继续运行：    
               
                $ python err.py 
                > /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
                -> print(10 / n)
                (Pdb) p n
                0
                (Pdb) c
                Traceback (most recent call last):
                  File "err.py", line 7, in <module>
                    print(10 / n)
                ZeroDivisionError: division by zero   
                    
    3、单元测试：
        
        单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
    
        比如函数 abs()，我们可以编写出以下几个测试用例：
            
            a. 输入正数，比如 1、1.2、0.99, 期待返回值与输入相同。
            
            b. 输入负数，比如 -1、-1.2、-0.99，期待返回值与输入相反。
            
            c. 输入 0 ，期待返回 0；
            
            d. 输入非法值类型，比如 None、[]、{}，期待抛出 TypeError。
            
        把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
        如果单元测试通过，说明我们测试的这个函数能够正常工作，如果单元测试不通过，
        要么函数有bug，要么测试条件输入不正确，总之，需要修复单元测试能够通过。
        
        单元测试通过后有什么意义呢？如果我们对 abs() 函数代码做了修改，只需要
        再跑一遍单元测试，如果通过，说明我们的修改不会对 abs()函数原有的行为造成
        影响，如果测试不通过，说明我们的修改和原有行为不一致，要么修改代码，要么修改测试。
        
        我们来编写一个 Dict 类，这个类的行为和 dict 一致，但是可以通过属性来访问，
        用起来就像下面这样：
            >>> d = Dict(a=1, b=2)k
            >>> d['a']
            1
            >>> d.a
            1
        
        mydict.py 代码如下：
        
            class Dict(dict):
                
                def __init__(self, **kw):
                    super().__init__(**kw)
                    
                def __getattr__(self, key):
                    try:
                        retrun self[key]
                    except KeyError:
                        raise AttributeError("Dict object has no attribute %s" % key)
                
                def __setattr__(self, key, value):
                    self[key] = value
                            
        为了编写单元测试，我们需要引入 Python 自带的 unittest 模块，编写 mydict_test.py 如下：
        mydict_test.py:
             
            import unittest
            
            from mydict import  Dict
            
            class TestDict(unittest.TestCase):
            
                def test_init(self):
                    d = Dict(a=1, b='test')
                    self.assertEqual(d.a, 1)
                    self.assertEqual(d.b, 'test')
                    self.assertTrue(isinstance(d, dict))
            
                def test_key(self):
                    d = Dict()
                    d['key'] = 'value'
                    self.assertEqual(d.key,'value')
            
                def test_attr(self):
                    d = Dict()
                    d.key = 'value'
                    self.assertTrue('key' in d)
                    self.assertEqual(d['key'], 'value')
            
                def test_keyerror(self):
                    d = Dict()
                    with self.assertRaises(KeyError):
                        value = d['empty']
            
                def test_attrerror(self):
                    d = Dict()
                    with self.assertRaises(AttributeError):
                        value = d.empty
        
        编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
        以 test 开头的方法就是测试方法，不以 test 开头的方法不认为是测试方法，测试的时候不会被执行。
        
        对于每一个类测试都需要编写一个 test_xxx() 方法，由于 unittest.TestCase 提供了很多内置的条件判断，
        我们需要调用这些方法就可以断言输出是否是我们所期望的，最常用的断言是 assertEqual():
        
            self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
            
        另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，
        断言会抛出KeyError：
            
            with self.assertRaises(KeyError):
                value = d['empty']            
        
        而通过d.empty访问不存在的key时，我们期待抛出AttributeError：
            
            with self.assertRaises(AttributeError):
                value = d.empty       
        
        运行单元测试:
        
            一旦编写好单元测试，我们就可以运行单元测试。
            最简单的运行方式是在mydict_test.py的最后加上两行代码：     
            
            if __name__ == '__main__':
                unittest.main()
        
        另一种方法是在命令行通过参数-m unittest直接运行单元测试：
            
            $ python -m unittest mydict_test
            .....
            ----------------------------------------------------------------------
            Ran 5 tests in 0.000s
            
            OK     
        
        setUp与tearDown:
        
            可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
            这两个方法会分别在每调用一个测试方法的前后分别被执行。    
            
            setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，
            这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，
            这样，不必在每个测试方法中重复相同的代码：
            
            class TestDict(unittest.TestCase):
    
                def setUp(self):
                    print('setUp...')
            
                def tearDown(self):
                    print('tearDown...')    

            单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
            单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
            单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
            单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
    
    4、文档测试：
        当我们编写注释时，如果写上这样的注释：
            def abs(n):
                '''
                Function to get absolute value of number.
            
                Example:
            
                >>> abs(1)
                1
                >>> abs(-1)
                1
                >>> abs(0)
                0
                '''
                return n if n >= 0 else (-n)
        
        无疑更明确地告诉函数的调用者该函数的期望输入和输出。
        并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。   
        doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
        只有测试异常的时候，可以用...表示中间一大段烦人的输出。               
        
        让我们用doctest来测试上次编写的Dict类：     
            # mydict2.py
            class Dict(dict):
                '''
                Simple dict but also support access as x.y style.
            
                >>> d1 = Dict()
                >>> d1['x'] = 100
                >>> d1.x
                100
                >>> d1.y = 200
                >>> d1['y']
                200
                >>> d2 = Dict(a=1, b=2, c='3')
                >>> d2.c
                '3'
                >>> d2['empty']
                Traceback (most recent call last):
                    ...
                KeyError: 'empty'
                >>> d2.empty
                Traceback (most recent call last):
                    ...
                AttributeError: 'Dict' object has no attribute 'empty'
                '''
                def __init__(self, **kw):
                    super(Dict, self).__init__(**kw)
            
                def __getattr__(self, key):
                    try:
                        return self[key]
                    except KeyError:
                        raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
            
                def __setattr__(self, key, value):
                    self[key] = value
            
            if __name__=='__main__':
                import doctest
                doctest.testmod()       
        
        运行python mydict2.py：
        什么输出也没有。这说明我们编写的doctest运行都是正确的。
        如果程序有问题，比如把__getattr__()方法注释掉，再运行就会报错：
            $ python mydict2.py
            **********************************************************************
            File "/Users/michael/Github/learn-python3/samples/debug/mydict2.py", line 10, in __main__.Dict
            Failed example:
                d1.x
            Exception raised:
                Traceback (most recent call last):
                  ...
                AttributeError: 'Dict' object has no attribute 'x'
            **********************************************************************
            File "/Users/michael/Github/learn-python3/samples/debug/mydict2.py", line 16, in __main__.Dict
            Failed example:
                d2.c
            Exception raised:
                Traceback (most recent call last):
                  ...
                AttributeError: 'Dict' object has no attribute 'c'
            **********************************************************************
            1 items had failures:
               2 of   9 in __main__.Dict
            ***Test Failed*** 2 failures.

"""08| """
    
        
    
                       
                