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


"""08| IO编程 """

    IO 在计算机中指 Input/Output, 也就是输入和输出。
    由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，
    通常是磁盘、网络等，就需要IO接口。           
        
    由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。
    举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，
    可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：       
    
    第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，
    再接着往下执行，这种模式称为同步IO；

    另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，
    于是，后续代码可以立刻接着执行，这种模式称为异步IO。
    
    同步和异步的区别就在于是否等待IO执行的结果。好比你去麦当劳点餐，你说“来个汉堡”，
    服务员告诉你，对不起，汉堡要现做，需要等5分钟，于是你站在收银台前面等了5分钟，
    拿到汉堡再去逛商场，这是同步IO。

    你说“来个汉堡”，服务员告诉你，汉堡需要等5分钟，你可以先去逛商场，等做好了，我们再通知你，
    这样你可以立刻去干别的事情（逛商场），这是异步IO。

    很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。
    想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。
    如果是服务员跑过来找到你，这是回调模式，
    如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。
    总之，异步IO的复杂度远远高于同步IO。
    
    1、文件读写：
        
        读写文件是最常见的 IO 操作。
        
        在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
        所以，读写文件就是请求操作系统打开一个文件对象(通常称为文件描述符)，然后，通过操作系统
        提供的接口从这个文件对象中读取数据(读文件)，或者把数据写入这个文件对象(写文件)。
        
        调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
        所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
        另外，调用readline()可以每次读取一行内容，
        调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
        
        字符编码：
            要读取非 UTF-8 编码的文本文件，需要给 open() 函数传入 encoding参数：
            >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
            >>> f.read()
            '测试'
              
            遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
            因为在文本文件中可能夹杂了一些非法编码的字符。
            遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
            最简单的方式是直接忽略：    
            >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
            
    2、StringIo 和 BytesIO
        
        StringIO:
            
            很多时候，数据读写不一定是文件，也可以在内存中读写。
            StringIO顾名思义就是在内存中读写str。
            要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：   
            
                >>> from io import StringIO
                >>> f = StringIO()
                >>> f.write('hello')
                5
                >>> f.write(' ')
                1
                >>> f.write('world!')
                6
                >>> print(f.getvalue())
                hello world!
            
            getvalue()方法用于获得写入后的str。
            要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
                           
                >>> from io import StringIO
                >>> f = StringIO('Hello!\nHi!\nGoodbye!')
                >>> while True:
                ...     s = f.readline()
                ...     if s == '':
                ...         break
                ...     print(s.strip())
                ...
                Hello!
                Hi!
                Goodbye!    
                
        BytesIO:
        
            StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
            BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
            
                >>> from io import BytesIO
                >>> f = BytesIO()
                >>> f.write('中文'.encode('utf-8'))
                6
                >>> print(f.getvalue())
                b'\xe4\xb8\xad\xe6\x96\x87'    
                
            请注意：写入的不是 str,而是经过 UTF-8 编码的 bytes。
            和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
                
                >>> from io import BytesIO
                >>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
                >>> f.read()
                b'\xe4\xb8\xad\xe6\x96\x87'    
                
    3、操作文件和目录:
        
        Python内置的os模块也可以直接调用操作系统提供的接口函数。
        
        >>> import os
        >>> os.name # 操作系统类型
        'posix'
        >>> os.uname() # 获取详细的系统信息
        posix.uname_result(sysname='Linux', nodename='debian', release='3.2.0-4-amd64', 
        version='#1 SMP Debian 3.2.54-2', machine='x86_64')
        
        >>> os.environ # 操作系统中定义的环境变量
        >>> os.environ.get('PATH') # 要获取某个环境变量的值  
        
        看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录:
        >>> [x for x in os.listdir('.') if os.path.isdir(x)]
        要列出所有的.py文件，也只需一行代码：
        >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.split(x)[1]=='.py']
        
        但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
        幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，
        它们可以看做是os模块的补充。
        
        Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
        
    4、序列化:
        
        在程序运行过程中，所有的变量都是在内存中，比如：定义一个dict:
        d = dict(name='Bob',age=20,score=80)
        可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
        如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
        
        我们把变量从内存中变成可存储或传输的过程称之为序列化, 在 Python 中叫 pickling,
        在其他语言中称之为 serialization、marshalling、flattening等。
        
        序列化后，就可以把序列化的内容写入磁盘，或者通过网络传输到别的机器上。
        反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
        
        Python提供了pickle模块来实现序列化。
            
            >>> import pickle
            >>> d = dict(name='Bob', age=20, score=88)
            >>> pickle.dumps(d)
            b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\
            x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'        
            
        pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
        或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
           
            >>> f = open('dump.txt', 'wb')
            >>> pickle.dump(d, f)
            >>> f.close()        
            
        当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化
        出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
        我们打开另一个Python命令行来反序列化刚才保存的对象：    
            
            >>> f = open('dump.txt', 'rb')
            >>> d = pickle.load(f)
            >>> f.close()
            >>> d
            {'age': 20, 'score': 88, 'name': 'Bob'}        
            
            
        JSON:
            
            如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
            比如XML，但更好的方法是序列化为JSON，因为 JSON 表示出来就是一个字符串，
            可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
            JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。     
                
            
            Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
            我们先看看如何把Python对象变成一个JSON：    
                
                >>> import json
                >>> d = dict(name='Bob', age=20, score=88)
                >>> json.dumps(d)
                '{"age": 20, "score": 88, "name": "Bob"}'    
            
            dumps()方法返回一个str，内容就是标准的JSON。
            类似的，dump()方法可以直接把JSON写入一个file-like Object。
            要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
            前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
                
                >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
                >>> json.loads(json_str)
                {'age': 20, 'score': 88, 'name': 'Bob'}    
            
        JSON进阶：
        
            Python 的 dict 对象可以直接序列化为 JSON 的{}，不过，很多时候，
            我们更喜欢 class 表示对象，比如定义 Student 类，然后序列化：
            
                import json

                class Student(object):
                    def __init__(self, name, age, score):
                        self.name = name
                        self.age = age
                        self.score = score
                
                s = Student('Bob', 20, 88)
                print(json.dumps(s))       
           
            运行代码，毫不留情地得到一个TypeError：
                Traceback (most recent call last):
                  ...
                TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable   
            
            错误的原因是 class 不是一个可序列化为JSON的对象。
            如果连class的实例对象都无法序列化为JSON，这肯定不合理！
            我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，
            dumps()方法还提供了一大堆的可选参数：   
            这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，
            是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
            
            可选参数 default 就是把任意一个对象变成一个可序列化为 JSON 的对象
            我们只需要为Student专门写一个转换函数，再把函数传进去即可：
            
                def student2dict(std):
                return {
                    'name': std.name,
                    'age': std.age,
                    'score': std.score
                }    
                
            这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
                import json
                def student2dict(std):
                    return {
                        'name':std.name,
                        'age':std.age,
                        'score':std.score,
                    }
                
                class Student(object):
                    def __init__(self, name, age, score):
                        self.name = name
                        self.age = age
                        self.score = score
                
                s = Student('Bob', 20, 88)
                print(json.dumps(s, default=student2dict))
            
            结果为：
                {"name": "Bob", "age": 20, "score": 88}
                
            不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。
            我们可以偷个懒，把任意class的实例变为dict：    
                print(json.dumps(s, default=lambda obj: obj.__dict__))
            
            同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
            然后，我们传入的object_hook函数负责把dict转换为Student实例：
                def dict2student(d):
                    return Student(d['name'], d['age'], d['score'])
                
                >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
                >>> print(json.loads(json_str, object_hook=dict2student))
                <__main__.Student object at 0x10cd3c190> 
                
                

"""09| 进程和线程"""
    
    1、多进程：
    
        子进程永远返回 0, 而父进程返回子进程的 ID.
        这样做的理由是，一个父进程可以 Fork出很多子进程，所以，父进程要记下每个子进程的ID,
        而子进程只需要调用 getppid() 就可以拿到父进程的ID.
        
    
    2、多线程：
        
        因为Python的线程虽然是真正的线程，但解释器执行代码时，
        有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
        然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
        这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
        即使100个线程跑在100核CPU上，也只能用到1个核。
        
        不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
        多个Python进程有各自独立的GIL锁，互不影响。
    
    3、ThreadLocal：
        
        在多进程环境下，每个线程都有自己的数据，一个线程使用自己的局部变量比使用全局变量好，
        因为局部变量只有线程自己能看见，不会影响到其他线程，而全局变量的修改必须加锁。
        
        但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
            
            def process_student(name):
                std = Student(name)
                # std是局部变量，但是每个函数都要用它，因此必须传进去：
                do_task_1(std)
                do_task_2(std)
            
            def do_task_1(std):
                do_subtask_1(std)
                do_subtask_2(std)
            
            def do_task_2(std):
                do_subtask_2(std)
                do_subtask_2(std)   
        
        每个函数一层一层调用都这么传参数那还得了？
        用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。
            
        如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
            
            global_dict = {}

                def std_thread(name):
                    std = Student(name)
                    # 把std放到全局变量global_dict中：
                    global_dict[threading.current_thread()] = std
                    do_task_1()
                    do_task_2()
                
                def do_task_1():
                    # 不传入std，而是根据当前线程查找：
                    std = global_dict[threading.current_thread()]
                    ...
                
                def do_task_2():
                    # 任何函数都可以查找出当前线程的std变量：
                    std = global_dict[threading.current_thread()]
                    ...
        
        这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，
        但是，每个函数获取std的代码有点丑。                       
        有没有更简单的方式？
        
        ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
        
            import threading

            # 创建全局ThreadLocal对象:
            local_school = threading.local()
            
            def process_student():
                # 获取当前线程关联的student:
                std = local_school.student
                print('Hello, %s (in %s)' % (std, threading.current_thread().name))
            
            def process_thread(name):
                # 绑定ThreadLocal的student:
                local_school.student = name
                process_student()
            
            t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
            t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        
        全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
        你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
        可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。 
        
        可以理解为全局变量local_school是一个dict，不但可以用local_school.student，
        还可以绑定其他变量，如local_school.teacher等等。
        
        ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
        这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
        
        一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
        ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
           
  
    4、进程 VS 线程：
        
        首先，要实现多任务，通常设计 Master-Worker 模式，Master 负责分配任务，Worker负责执行任务。
        因此，多任务环境下，通常是一个 Master, 多个 Worker。
        
        如果用多进程实现 Master-Worker,主进程就是 Master,其他进程就是Worker
        如果用多线程实现 Master-Worker,主线程就是 Master,其他线程就是Worker
        
        多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。
       （当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）
        著名的Apache最早就是采用多进程模式。
        
        多进程模式的缺点是创建进程的代价大，在Unix/Linux 系统下，用 fork 调用还行，
        在Windows 下创建进程开销巨大。另外操作系统能够运行的进程数有限，在内存和CPU
        的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。
        
        多线程模式通过比进程快一点，但是也快不到那里去，而且多线程致命的缺点就是任何一个
        线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。
        在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示
        “该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。
        
        线程切换：
        
            无论是多进程还是多线程，只有数量一多，效率肯定上不去。
            因为，操作系统在切换进程或者线程需要消耗时间，
            它需要先保存当前执行的现场环境(CPU寄存状态，内存页等)，然后，把新任务的执行环境
            准备好(恢复上次的寄存器状态、内存页等)，才开始执行。这个切换过程很快，但是也要耗费时间
            如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有时间执行任务了，
            这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。
            所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。
            
        计算密集型 VS I/O 密集型：
        
            是否采用多任务的第二个考虑是任务的类型，我们可以把任务分为计算密集型和IO密集型。
            
            计算密集型任务的特点是要进行大量的计算，消耗 CPU 资源，比如计算圆周率，对视频进行高清解码等
            这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间久越多，
            CPU 执行任务的效率就越低，所以，要有效的利用CPU,计算密集型任务同时进行的数量应等于
            CPU 的核心数。
            
            计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。
            Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。
                    
            第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是 CPU 消耗少，
            任务大部分时间都在等待IO操作完成。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。
            常见的大部分任务都是IO密集型，比如 web 应用。
            
            IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，
            因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。
            对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。
        
        异步IO:
        
            考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，
            单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型
            来支持多任务并发执行。

            现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。
            如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，
            这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，
            它在单核CPU上采用单进程模型就可以高效地支持多任务。
            在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。
            由于系统总的进程数量十分有限，因此操作系统调度非常高效。
            用异步IO编程模型来实现多任务是一个主要的趋势。
            
            对应到 Python 语言，但线程的异步编程模型称为协程，有了协程的支持，
            就可以基于事件的驱动编写高效的多任务程序。
            
    
    5、分布式进程：
        
        在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，
        而Thread最多只能分布到同一台机器的多个CPU上。
        
        Python 的 multiprocessing 模块不但支持多进程，其中 managers 子模块还支持把多进程分布到多台机器上，
        一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信，由于managers模块封装很好，
        不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
        
        举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，
        现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。
        怎么用分布式进程实现？
        
        原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，
        就可以让其他机器的进程访问Queue了。

        我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
        
        
                    
            
"""10| 正则表达式"""

    字符串是编程时涉及到最多的一种数据结构，对字符串进程操作的需求几乎无处不在。
    
    正则表达式是一种用来匹配字符串的强有力的武器，它的设计思想是用一种描述性的语言来
    给字符串定义一个规则，凡是符合规则的字符串，我们就认为它匹配了，否则，该字符串就不合法的。
    
    分组：
     
        ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
                
        >>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
        >>> m
        <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
        >>> m.group(0)
        '010-12345'
        >>> m.group(1)
        '010'
        >>> m.group(2)
        '12345'        
        
        注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
        
        
"""11| 常用内建模块"""                
    
    Python 之所以自称为“batteries include”,就是因为内置了许多非常有用的模块，
    无需额外配置，即可直接使用。    
    
    1、datetiem:
    
        datetime 是 python 处理日期和时间的标准库。
        
        获取当前日期和时间：
        
            >>> from datetime import datetime
            >>> now = datetime.now() # 获取当前datetime
            >>> print(now)
            2015-05-18 16:28:07.198690
            >>> print(type(now))
            <class 'datetime.datetime'>      
        
            注意到 datetime 是模块，datetime 模块还包含一个 datetime 类，
            通过 from datetime import datetime 导入的才是 datetime 这个类。
            如果仅导入import datetime，则必须引用全名datetime.datetime。
            datetime.now()返回当前日期和时间，其类型是datetime。
    
        获取指定日期和时间：
            
            要指定某个日期和时间，我们直接用参数构造一个 datetime:
            
            >>> from datetime import datetime
            >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
            >>> print(dt)
            2015-04-19 12:20:00
            
        datetime 转换为 timestamp:
            
            在计算机中，时间实际上是用数字表示的，我们把1970年1月1日 00:00:00 UTC+00:00
            时区的时刻称为 epoch time, 记为 0，1970年以前的时候为负数，当前时间就是相当于
            epoch time 的秒数，称为 timestamp。
            
            你可以认为：
                
                timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
            
            对应的北京时间是：
                
                timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
                
            可见timestamp的值与时区毫无关系，因为timestamp一旦确定，
            其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
            这就是为什么计算机存储的当前时间是以timestamp表示的，
            因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。                
            
            把一个datetime 类型转换为 timestamp 只需要简单调用 timestamp() 方法：
            
                >>> from datetime import datetime
                >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
                >>> dt.timestamp() # 把datetime转换为timestamp
                1429417200.0
                        
            注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
            某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，
            这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
                
        timestamp 转换为 datetime：
        
            要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
            
            >>> from datetime import datetime
            >>> t = 1429417200.0
            >>> print(datetime.fromtimestamp(t))
            2015-04-19 12:20:00
        
            注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
            上述转换是在timestamp和本地时间做转换。                
            本地时间是指当前操作系统设定的时区。
            
            timestamp也可以直接被转换到UTC标准时区的时间：
            >>> from datetime import datetime
            >>> t = 1429417200.0
            >>> print(datetime.fromtimestamp(t)) # 本地时间
            2015-04-19 12:20:00
            >>> print(datetime.utcfromtimestamp(t)) # UTC时间
            2015-04-19 04:20:00 
            
        str 转换为 datetime:
        
            很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
            转换方法是通过 datetime.strptime() 实现，需要一个日期和时间格式化字符串：
            
            >>> from datetime import datetime
            >>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
            >>> print(cday)
            2015-06-01 18:19:59    
            
        datetime转换为str:
        
            如果已经有了datetime对象，要把它格式化为字符串显示给用户，
            就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式       
            
            >>> from datetime import datetime
            >>> now = datetime.now()
            >>> print(now.strftime('%a, %b %d %H:%M'))
            Mon, May 05 16:28
                        
        datetime加减:
        
            对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
            加减可以直接用+和-运算符，不过需要导入timedelta这个类：        
            
            >>> from datetime import datetime, timedelta
            >>> now = datetime.now()
            >>> now
            datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
            >>> now + timedelta(hours=10)
            datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
            >>> now - timedelta(days=1)
            datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
            >>> now + timedelta(days=2, hours=12)
            datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
            
    
    2、collections：
        
        collections 是 python 内建的一个集合模块，提供了许多有用的集合类。
        
        a、namedtuple:
            
            我们知道 tuple 可以表示不变集合，例如，一个点的二维坐标可以表示成：
            >>> p = (1, 2)
            但是，看到 (1, 2)， 很难看出这个tuple 是用来表示一个坐标的。
            定义一个类又小题大做了，这时，namedtuple 就派上用场了：
            
                >>> from collections import namedtuple
                >>> Point = namedtuple('Point', ['x', 'y'])
                >>> p = Point(1, 2)
                >>> p.x
                1
                >>> p.y
                2    
                
            namedtuple 是一个函数，它用来创建一个自定义的 tuple 对象，并规定了 tuple 元素的个数。
            并可以用属性而不是用索引来引用 tuple 的某个元素。
            这样一来，我们用 namedtuple 可以很方便地定义一种数据类型，它具备 tuple 的不变性，
            又可以根据属性来引用，使用十分方便。
            可以验证创建的Point对象是tuple的一种子类：
                
                >>> isinstance(p, Point)
                True
                >>> isinstance(p, tuple)
                True    
            
            类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：                    
                
                circle = namedtuple('Circle', ['x', 'y', 'r'])
                
        b、deque:
        
            使用 list 存储数据时，按索引访问元素很快，但是插入和删除元素就很慢，
            因为 list 是线性存储，数据量很大时，插入和删除效率很低。
            
            deque 是为了高效实现插入和删除操作的双向列表，适用于队列和栈。
            
                >>> from collections import deque
                >>> q = deque(['a', 'b', 'c'])
                >>> q.append('x')
                >>> q.appendleft('y')
                >>> q
                deque(['y', 'a', 'b', 'c', 'x'])
        
            deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
            这样就可以非常高效地往头部添加或删除元素。
        
        c、defaultdict:
        
            使用 dict 时，如果引用的 key 不存在，就会抛 KeyError。
            如果希望 key 不存时，返回一个默认值，就可以用 defaultdict：
                
                >>> from collections import defaultdict
                >>> dd = defaultdict(lambda: 'N/A')
                >>> dd['key1'] = 'abc'
                >>> dd['key1'] # key1存在
                'abc'
                >>> dd['key2'] # key2不存在，返回默认值
                'N/A'
            
            注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
            除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
            
        d、OrderedDict:
        
            使用 dict 时， Key 是无效的，在对 dict 做迭代时，我们无法确定 Key 的顺序。
            
            如果要保持 Key 的顺序，可以收 OrderedDit。
                
                >>> from collections import OrderedDict
                >>> d = dict([('a', 1), ('b', 2), ('c', 3)])
                >>> d # dict的Key是无序的
                {'a': 1, 'c': 3, 'b': 2}
                >>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
                >>> od # OrderedDict的Key是有序的
                OrderedDict([('a', 1), ('b', 2), ('c', 3)])    
            
            注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
            
                >>> od = OrderedDict()
                >>> od['z'] = 1
                >>> od['y'] = 2
                >>> od['x'] = 3
                >>> list(od.keys()) # 按照插入的Key的顺序返回
                ['z', 'y', 'x']   
                            
            
            OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，
            先删除最早添加的Key：
            
                from collections import OrderedDict
                
                class LastUpdatedOrderedDict(OrderedDict):
               
                    def __init__(self, capacity):
                        super(LastUpdatedOrderedDict, self).__init__()
                        self._capacity = capacity
                
                    def __setitem__(self, key, value):
                        containsKey = 1 if key in self else 0
                        if len(self) - containsKey >= self._capacity:
                            last = self.popitem(last=False)
                            print('remove:', last)
                        if containsKey:
                            del self[key]
                            print('set:', (key, value))
                        else:
                            print('add:', (key, value))
                        OrderedDict.__setitem__(self, key, value)     
            
        e、ChainMap:
            
            ChainMap可以把一组dict串起来并组成一个逻辑上的dict。
            ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。    
            
            什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，
            可以通过环境变量传入，还可以有默认参数。
            我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，
            再查环境变量，如果没有，就使用默认参数。
            
            下面的代码演示了如何查找user和color这两个参数：
            
                from collections import ChainMap
                import os, argparse
                
                # 构造缺省参数:
                defaults = {
                    'color': 'red',
                    'user': 'guest'
                }
                
                # 构造命令行参数:
                parser = argparse.ArgumentParser()
                parser.add_argument('-u', '--user')
                parser.add_argument('-c', '--color')
                namespace = parser.parse_args()
                command_line_args = { k: v for k, v in vars(namespace).items() if v }
                
                # 组合成ChainMap:
                combined = ChainMap(command_line_args, os.environ, defaults)
                
                # 打印参数:
                print('color=%s' % combined['color'])
                print('user=%s' % combined['user'])        
            
            没有任何参数时，打印出默认参数：

                $ python3 use_chainmap.py 
                color=red
                user=guest
             
            当传入命令行参数时，优先使用命令行参数：
                
                $ python3 use_chainmap.py -u bob
                color=red
                user=bob
            
            同时传入命令行参数和环境变量，命令行参数的优先级较高：

                $ user=admin color=green python3 use_chainmap.py -u bob
                color=green
                user=bob
            
        f、Counter：
        
            Counter 是一个简单的计数器，例如。统计字符出现的个数：
            
                >>> from collections import Counter
                >>> c = Counter()
                >>> for ch in 'programming':
                ...     c[ch] = c[ch] + 1
                ...
                >>> c
                Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})    
            
            Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，
            其他字符各出现了一次。            
            
    3、 base64:
        
        base64 是一种用 64 个字符表示任意二进制数据的方法。
        
        用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，
        因为二进制文件包含很多无法显示和打印的字符，所以，
        如果要让记事本这样的文本处理软件能处理二进制数据，
        就需要一个二进制到字符串的转换方法。
        
        Base64 是一种罪常见的二进制编码方法。
        
        Base64 的原理很简单，首先，准备一个包含 64 个字符的数组。
        ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
        
        然后，对二进制数据进行处理，每3个字节一组，一共是 3x8=24 bit，划为4组，
        每组正好 6 个bit。这样我们就得到 4 个数字作为索引，然后查表，获得对应的4个字符，
        就是编码后的字符串。
        
        所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，
        好处是编码后的文本数据可以在邮件正文、网页等直接显示。
        
        如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
        Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，
        表示补了多少字节，解码的时候，会自动去掉。
        
        Python内置的base64可以直接进行base64的编解码：
            
            >>> import base64
            >>> base64.b64encode(b'binary\x00string')
            b'YmluYXJ5AHN0cmluZw=='
            >>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
            b'binary\x00string'   
                            
            
        由于标准的 Base64 编码后可能出现 + 和 /，在 URL 中就不能直接作为参数，
        所以又有一种“url safe” 的base64 编码，其实就是把字符 + 和 / 分别变成了 - 和 _。
        
            >>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
            b'abcd++//'
            >>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
            b'abcd--__'
            >>> base64.urlsafe_b64decode('abcd--__')
            b'i\xb7\x1d\xfb\xef\xff'                
               
        Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
        Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
        
    4、struct:
    
        准确地将，Python 没有专门处理字节的数据类型，但由于 b'str'可以表示字节，
        所以，字节数组=二进制str。而在 c 语言中，我们可以很方便地用 struct、union
        来处理字节，以及字节和 int, float的转换。
        
        在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，
        你得配合位运算符这么写：
           
            >>> n = 10240099
            >>> b1 = (n & 0xff000000) >> 24
            >>> b2 = (n & 0xff0000) >> 16
            >>> b3 = (n & 0xff00) >> 8
            >>> b4 = n & 0xff
            >>> bs = bytes([b1, b2, b3, b4])
            >>> bs
            b'\x00\x9c@c'    
            
        非常麻烦。如果换成浮点数就无能为力了。
        
        好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
        struct的pack函数把任意数据类型变成bytes：
                
            >>> import struct
            >>> struct.pack('>I', 10240099)
            b'\x00\x9c@c'
        
        pack的第一个参数是处理指令，'>I'的意思是：
        >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
                
        unpack把bytes变成相应的数据类型：
            
            >>> struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
            (4042322160, 32896)    
        
        根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
        
    5、hashlib:
        
        摘要算法简介：
            摘要算法又称哈希算法，散列算法。它通过一个函数，把任意长度的数据转换为一个
            长度固定的字符串。
            
            摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，
            目的是为了发现原始数据是否被人篡改过。
            
            摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，
            计算f(data)很容易，但通过digest反推data却非常困难。
            而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
        
        我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
        
            import hashlib

            md5 = hashlib.md5()
            md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
            print(md5.hexdigest())    
        
        计算结果如下：
            d26a53750bc40b38b65a520292f69306
        
        如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
            import hashlib

            md5 = hashlib.md5()
            md5.update('how to use md5 in '.encode('utf-8'))
            md5.update('python hashlib?'.encode('utf-8'))
            print(md5.hexdigest())
            
        MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
        
    6、hmac:
    
        通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值。
        例如，判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)的结果，
        如果一致，用户输入的口令就是正确的。    
        
        为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，
        需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。

        如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。
        但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，
        根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。
        
        这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。
        它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
        
        和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。
        采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
        
        Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希。
        我们首先需要准备待计算的原始消息message，
        随机key，哈希算法，这里采用MD5，使用hmac的代码如下：
            
            >>> import hmac
            >>> message = b'Hello, world!'
            >>> key = b'secret'
            >>> h = hmac.new(key, message, digestmod='MD5')
            >>> # 如果消息很长，可以多次调用h.update(msg)
            >>> h.hexdigest()
            'fa4ee7d173f2d97ee79022d1a7355bcf'    
        
        可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。
        需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
        
    7、itertools:
    
        Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
        首先，我们看看itertools提供的几个“无限”迭代器：
        
        
        count():
        
            >>> import itertools
            >>> natuals = itertools.count(1)
            >>> for n in natuals:
            ...     print(n)
            ...
            1
            2
            3
            ...        
        
            因为count()会创建一个无限的迭代器，
            所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。    
        
        cycle():
        
            cycle() 会把传入的一个序列无限重复下去：
            
            >>> import itertools
            >>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
            >>> for c in cs:
            ...     print(c)
            ...
            'A'
            'B'
            'C'
            'A'
            'B'
            'C'
            ...
            同样停不下来。        
                
            
        repeat():
            
            repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
            
            >>> ns = itertools.repeat('A', 3)
            >>> for n in ns:
            ...     print(n)
            ...
            A
            A
            A        
            
        无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
        它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。        
            
        无限序列虽然可以无限迭代下去，
        但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：                 
            
            >>> natuals = itertools.count(1)
            >>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
            >>> list(ns)
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                     
            
        itertools提供的几个迭代器操作函数更加有用：
        
        chain():
        
            chain() 可以把一组可迭代对象串联起来，形成一个更大的迭代器：
            
            >>> for c in itertools.chain('ABC', 'XYZ'):
            ...     print(c)
            # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
            
        groupby():
            
            groupby() 把迭代器中相邻的重复元素挑出来放在一起：
            
            >>> for key, group in itertools.groupby('AAABBBCCAAA'):
            ...     print(key, list(group))
            ...
            A ['A', 'A', 'A']
            B ['B', 'B', 'B']
            C ['C', 'C']
            A ['A', 'A', 'A']
    
        itertools模块提供的全部是处理迭代功能的函数，
        它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。        
    
    8、contextlib:
        
        在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。
        正确关闭文件资源的一个方法是使用try...finally：  
        
            try:
                f = open('/path/to/file', 'r')
                f.read()
            finally:
                if f:
                    f.close()     
        
        写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，
        而不必担心资源没有关闭，所以上面的代码可以简化为：
            
            with open('/path/to/file', 'r') as f:
                f.read()                   
            
        并不是只有 open() 函数返回的 fp 对象才能使用 with 语句，实际上，
        只有正确实现了上下文管理，就可以用 with 语句。
        
        实现上下文管理是通过 __enter__ 和 __exit__ 这两个方法实现的。
            
            class Query(object):

                def __init__(self, name):
                    self.name = name
            
                def __enter__(self):
                    print('Begin')
                    return self
            
                def __exit__(self, exc_type, exc_value, traceback):
                    if exc_type:
                        print('Error')
                    else:
                        print('End')
            
                def query(self):
                    print('Query info about %s...' % self.name)        
        
        这样我们就可以把自己写的资源对象用于 with 语句：
            
            with Query('Bob') as q:
                q.query()
                
        @contextmanager:
            
            编写__enter__和__exit__仍然很繁琐，因此Python的
            标准库contextlib提供了更简单的写法，上面的代码可以改写如下：    
            
                from contextlib import contextmanager
    
                class Query(object):
                
                    def __init__(self, name):
                        self.name = name
                
                    def query(self):
                        print('Query info about %s...' % self.name)
                
                @contextmanager
                def create_query(name):
                    print('Begin')
                    q = Query(name)
                    yield q
                    print('End')
                
            @contextmanager这个decorator接受一个generator，
            用yield语句把with ... as var把变量输出出去，
            然后，with语句就可以正常地工作了：
                
                with create_query('Bob') as q:
                    q.query()    
                    
            很多时候，我们希望在某段代码执行前后自动执行特定代码，
            也可以用@contextmanager实现。例如：
            
                @contextmanager
                def tag(name):
                    print("<%s>" % name)
                    yield
                    print("</%s>" % name)
                
                with tag("h1"):
                    print("hello")
                    print("world")  
                    
            上述代码执行结果为：

                <h1>
                hello
                world
                </h1> 
                
            代码的执行顺序是：

                with语句首先执行yield之前的语句，因此打印出<h1>；
                yield调用会执行with语句内部的所有语句，因此打印出hello和world；
                最后执行yield之后的语句，打印出</h1>。
                因此，@contextmanager让我们通过编写generator来简化上下文管理。     
                
        @closing:
        
            如果一个对象没有实现上下文，我们就不能把它用于with语句。
            这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：    
            
                from contextlib import closing
                from urllib.request import urlopen
                
                with closing(urlopen('https://www.python.org')) as page:
                    for line in page:
                        print(line)    
            
            closing也是一个经过@contextmanager装饰的generator，
            这个generator编写起来其实非常简单：
            
                @contextmanager
                def closing(thing):
                    try:
                        yield thing
                    finally:
                        thing.close()
                        
            它的作用就是把任意对象变为上下文对象，并支持with语句。 
                
"""12| 第三方模块"""

    1、Pillow:
        
        PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。
        PIL功能非常强大，但API却非常简单易用。                   
        
        由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上
        创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，
        因此，我们可以直接安装使用Pillow。
        
        安装Pillow:
            
            如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：
            $ pip install pillow
        
        操作图像:
        
            from PIL import Image

            # 打开一个jpg图像文件，注意是当前路径:
            im = Image.open('test.jpg')
            # 获得图像尺寸:
            w, h = im.size
            print('Original image size: %sx%s' % (w, h))
            # 缩放到50%:
            im.thumbnail((w//2, h//2))
            print('Resize image to: %sx%s' % (w//2, h//2))
            # 把缩放后的图像用jpeg格式保存:
            im.save('thumbnail.jpg', 'jpeg')        
                            
        其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
        
        PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
        
            from PIL import Image, ImageDraw, ImageFont, ImageFilter

                import random
                
                # 随机字母:
                def rndChar():
                    return chr(random.randint(65, 90))
                
                # 随机颜色1:
                def rndColor():
                    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
                
                # 随机颜色2:
                def rndColor2():
                    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
                
                # 240 x 60:
                width = 60 * 4
                height = 60
                image = Image.new('RGB', (width, height), (255, 255, 255))
                # 创建Font对象:
                font = ImageFont.truetype('Arial.ttf', 36)
                # 创建Draw对象:
                draw = ImageDraw.Draw(image)
                # 填充每个像素:
                for x in range(width):
                    for y in range(height):
                        draw.point((x, y), fill=rndColor())
                # 输出文字:
                for t in range(4):
                    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
                # 模糊:
                image = image.filter(ImageFilter.BLUR)
                image.save('code.jpg', 'jpeg')        
        
        如果运行的时候报错：

            IOError: cannot open resource
        这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：
        
            '/Library/Fonts/Arial.ttf'
            
        要详细了解PIL的强大功能，请请参考Pillow官方文档：

            https://pillow.readthedocs.org/  
            
            
    2、chardet：
        
        字符串编码一直是令人非常头疼的问题，尤其是处理不规范的第三方网页的时候，
        虽然 Python 提供了 Unicode 表示的 str 和 bytes 两种数据类型，并且
        可以通过 encode() 和 decode() 方法转换，但是，在不知道编码的情况下
        对 bytes 做 decode() 不好做。
        
        对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。
        猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。
        
        当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。
        chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。
        
        安装chardet：

            如果安装了Anaconda，chardet就已经可用了。否则，需要在命令行下通过pip安装：
            $ pip install chardet
            
        使用chardet：
        
            当我们拿到一个 bytes 时，就可以对其检测编码，用 chardet 检测编码，只需要一行代码：
            
            >>> chardet.detect(b'Hello, world!')
            {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
            检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。 
        
        我们来试试检测GBK编码的中文：
            
            >>> data = '离离原上草，一岁一枯荣'.encode('gbk')
            >>> chardet.detect(data)
            {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
        
        检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码，
        检测正确的概率是74%，language字段指出的语言是'Chinese'。
        
    3、psutil：
    
        用Python来编写脚本简化日常的运维工作是Python的一个重要用途。
        在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，
        如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。
        但这样做显得很麻烦，尤其是要写很多解析代码。    
        
        在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
        顾名思义，psutil = process and system utilities，
        它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，
        支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
            
        安装psutil

            如果安装了Anaconda，psutil就已经可用了。否则，需要在命令行下通过pip安装：
            $ pip install psutil
            
        获取CPU信息：
            
            >>> import psutil
            >>> psutil.cpu_count() # CPU逻辑数量
            4
            >>> psutil.cpu_count(logical=False) # CPU物理核心
            2
            # 2说明是双核超线程, 4则是4核非超线程    
        
        统计CPU的用户／系统／空闲时间：
        
            >>> psutil.cpu_times()
            scputimes(user=10963.31, nice=0.0, system=5138.67, idle=356102.45)  
            
        再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
            
            >>> for x in range(10):
            ...     psutil.cpu_percent(interval=1, percpu=True)
            ... 
            [14.0, 4.0, 4.0, 4.0]
            [12.0, 3.0, 4.0, 3.0]
            [8.0, 4.0, 3.0, 4.0]
            [12.0, 3.0, 3.0, 3.0]
            [18.8, 5.1, 5.9, 5.0]
            [10.9, 5.0, 4.0, 3.0]
            [12.0, 5.0, 4.0, 5.0]
            [15.0, 5.0, 4.0, 4.0]
            [19.0, 5.0, 5.0, 4.0]
            [9.0, 3.0, 2.0, 3.0]
        
        获取内存信息：
            >>> psutil.virtual_memory()
            >>> psutil.swap_memory() 
        
        获取磁盘信息：
            
            >>> psutil.disk_partitions() # 磁盘分区信息
            >>> psutil.disk_usage('/') # 磁盘使用情况
            >>> psutil.disk_io_counters() # 磁盘IO
            
        获取网络信息：
        
            >>> psutil.net_io_counters() # 获取网络读写字节／包的个数
            >>> psutil.net_if_addrs() # 获取网络接口信息
            >>> psutil.net_if_stats() # 获取网络接口状态
                   
        获取进程信息：
        
            >>> psutil.pids() # 所有进程ID
            [3865, 3864, 3863, 3856, 3855, 3853, 3776, ..., 45, 44, 1, 0]
            >>> p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
            >>> p.name() # 进程名称
            'python3.6'
            >>> p.exe() # 进程exe路径
            '/Users/michael/anaconda3/bin/python3.6'
            >>> p.cwd() # 进程工作目录
            '/Users/michael'
            >>> p.cmdline() # 进程启动的命令行
            ['python3']
            >>> p.ppid() # 父进程ID
            3765
            >>> p.parent() # 父进程
            <psutil.Process(pid=3765, name='bash') at 4503144040>
            >>> p.children() # 子进程列表
            []
            >>> p.status() # 进程状态
            'running'
            >>> p.username() # 进程用户名
            'michael'
            >>> p.create_time() # 进程创建时间
            1511052731.120333
            >>> p.terminal() # 进程终端
            '/dev/ttys002'
            >>> p.cpu_times() # 进程使用的CPU时间
            pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
            >>> p.memory_info() # 进程使用的内存
            pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
            >>> p.open_files() # 进程打开的文件
            []
            >>> p.connections() # 进程相关网络连接
            []
            >>> p.num_threads() # 进程的线程数量
            1
            >>> p.threads() # 所有线程信息
            [pthread(id=1, user_time=0.090318, system_time=0.062736)]
            >>> p.environ() # 进程环境变量
            {'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
            >>> p.terminate() # 结束进程
            Terminated: 15 <-- 自己把自己结束了           
                            
            
        psutil使得Python程序获取系统信息变得易如反掌。

        psutil还可以获取用户信息、Windows服务等很多有用的系统信息，
        具体请参考psutil的官网：https://github.com/giampaolo/psutil    
      
    4、virtualenv:
              
        在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。
        所有第三方的包都会被pip安装到Python3的site-packages目录下。          
        
        如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，
        就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？        
        
        这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。
        virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。        
        
        首先，我们用pip安装virtualenv：
            
            $ pip3 install virtualenv
            
        然后，假定我们要开发一个新的项目，需要一套独立的Python运行环境，可以这么做：
        第一步，创建目录：
            
            Mac:~ michael$ mkdir myproject
            Mac:~ michael$ cd myproject/
            Mac:myproject michael$   
            
        第二步，创建一个独立的Python运行环境，命名为venv：
        
            Mac:myproject michael$ virtualenv --no-site-packages venv
            Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
            New python executable in venv/bin/python3.4
            Also creating executable in venv/bin/python
            Installing setuptools, pip, wheel...done.         
                
            命令virtualenv就可以创建一个独立的Python运行环境，
            我们还加上了参数--no-site-packages，这样，
            已经安装到系统Python环境中的所有第三方包都不会复制过来，
            这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。    
        
        新建的Python环境被放到当前目录下的venv目录。
        有了venv这个Python环境，可以用source进入该环境：            
            
            Mac:myproject michael$ source venv/bin/activate
            (venv)Mac:myproject michael$             
                

"""13| 图形界面"""

    Python支持多种图形界面的第三方库，包括：
        
        Tk、wxWidgets、Qt、GTK         
                    
    但是Python自带的库是支持Tk的Tkinter,使用Tkinter，无需安装任何包，就可以直接使用。
    
    Tkinter:

        我们来梳理一下概念：
        
        我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
        Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
        Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
        所以，我们的代码只需要调用Tkinter提供的接口就可以了。       
        
        Python内置的Tkinter可以满足基本的GUI程序的要求.
        如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。
    
    turtle:
        
        在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，
        它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。

        海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，
        Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。
       
        
"""14 | 网络编程"""
    
    自从互联网诞生以来，现在基本上所有的程序都是网络程序。
    网络编程就是如何在程序中实现两台计算机的通信。
    网络通信时两台计算机上的两个进程之间的通信。
    用Python进行网络编程，就是在Python程序本身这个进程内，连接别的服务器进程的通信端口进行通信。
    
    1、TCP/IP简介：
        
        TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，
        保证数据包按顺序到达。TCP协议会通过握手建立连接，然后，对每个IP包编号，
        确保对方按顺序收到，如果包丢掉了，就自动重发。
        
        许多常用的更高级的协议都是建立在TCP协议基础上的，
        比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。   
        
        一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
        
        在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。
        一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。
        每个网络程序都向操作系统申请唯一的端口号，
        这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。
        
    2、TCP编程:
        
        Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
        而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
        
        
"""15| 数据库 """

    1、SQLite:
        
        SQLite是一种嵌入式数据库，它的数据库就是一个文件。
        由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中。
        
        Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
        在使用SQLite前，我们先要搞清楚几个概念：
            
            表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，
            比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
            要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
            连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
            Python定义了一套操作数据库的API接口，任何数据库要连接到Python，
            只需要提供符合Python标准的数据库驱动即可。
            由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。    
            
        我们在Python交互式命令行实践一下：
        
            # 导入SQLite驱动:
            >>> import sqlite3
            # 连接到SQLite数据库
            # 数据库文件是test.db
            # 如果文件不存在，会自动在当前目录创建:
            >>> conn = sqlite3.connect('test.db')
            # 创建一个Cursor:
            >>> cursor = conn.cursor()
            # 执行一条SQL语句，创建user表:
            >>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
            <sqlite3.Cursor object at 0x10f8aa260>
            # 继续执行一条SQL语句，插入一条记录:
            >>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
            <sqlite3.Cursor object at 0x10f8aa260>
            # 通过rowcount获得插入的行数:
            >>> cursor.rowcount
            1
            # 关闭Cursor:
            >>> cursor.close()
            # 提交事务:
            >>> conn.commit()
            # 关闭Connection:
            >>> conn.close()       
            
        我们再试试查询记录：
        
            >>> conn = sqlite3.connect('test.db')
            >>> cursor = conn.cursor()
            # 执行查询语句:
            >>> cursor.execute('select * from user where id=?', ('1',))
            <sqlite3.Cursor object at 0x10f8aa340>
            # 获得查询结果集:
            >>> values = cursor.fetchall()
            >>> values
            [('1', 'Michael')]
            >>> cursor.close()
            >>> conn.close()   
        
        使用Python的DB-API时，只要搞清楚Connection和Cursor对象，
        打开后一定记得关闭，就可以放心地使用。
        
        使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，
        就可以拿到执行结果。
        
        使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。
        结果集是一个list，每个元素都是一个tuple，对应一行记录。
        
        如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，
        有几个?占位符就必须对应几个参数，例如：     
        
            cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
            
        在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
        要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
        如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？
        请回忆try:...except:...finally:...的用法。
        
    2、使用MySQL：
        
        MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、
        可嵌入，但不能承受高并发访问，适合桌面和移动应用。
        而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
        
        执行INSERT等操作后要调用commit()提交事务；
        MySQL的SQL占位符是%s。    
        
    3、使用SQLAlchemy:
    
        数据库表示一个二维表，包含多行多列。把一个表的内容用 Python 的数据库结构表示出来的话，
        可以用一个 list 表示多行，list 的每一个元素是 tuple,表示一行记录。
        比如，包含 id 和 name 的 user 表：
        
            [
            ('1','Michael'),
            ('2','Bob'),
            ('3','Adam')
            ]
            
        Python的DB-API 返回的数据结构就是像上面这样表示的。
        但是用 tuple 表示一行很难看出表的结构，如果把一个 tuple 用 class 实例来表示，
        就可以更容易地看出表的结构来：
        
            class User(object):
                def __init__(self, id, name):
                    self.id = id
                    self.name = name
            
            [
                User('1', 'Michael'),
                User('2', 'Bob'),
                User('3', 'Adam')
            ]    
        
        这就是传说中的 ORM 技术：Object-Relation Mapping, 把关系数据库的表结构映射到对象上。
        但是有谁来做这个转换呢？所以 ORM 框架应运而生。
        
        在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。
        
        首先通过 pip 安装 SQLAlchemy:
        
            $pip install sqlachemy
        
        然后，利用上次我们在MySQL的test数据库中创建的user表，用SQLAlchemy来试试：
        第一步，导入SQLAlchemy, 并初始化 DBSession：
        
            # 导入:
            from sqlalchemy import Column, String, create_engine
            from sqlalchemy.orm import sessionmaker
            from sqlalchemy.ext.declarative import declarative_base
            
            # 创建对象的基类:
            Base = declarative_base()
            
            # 定义User对象:
            class User(Base):
                # 表的名字:
                __tablename__ = 'user'
            
                # 表的结构:
                id = Column(String(20), primary_key=True)
                name = Column(String(20))
            
            # 初始化数据库连接:
            engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
            # 创建DBSession类型:
            DBSession = sessionmaker(bind=engine)     
            
        以上代码完成SQLAlchemy的初始化和具体每个表的class定义。
        如果有多个表，就继续定义其他class，例如School：
            
            class School(Base):
                __tablename__ = 'school'
                id = ...
                name = ...    
        
        create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
            '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
            
        你只需要根据需要替换掉用户名、口令等信息即可。
        下面，我们看看如何向数据库表中添加一行记录。
        由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
            
            # 创建session对象:
            session = DBSession()
            # 创建新User对象:
            new_user = User(id='5', name='Bob')
            # 添加到session:
            session.add(new_user)
            # 提交即保存到数据库:
            session.commit()
            # 关闭session:
            session.close()   
               
        可见，关键是获取session，然后把对象添加到session，最后提交并关闭。
        DBSession对象可视为当前数据库连接。
        
        如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，
        而是User对象。SQLAlchemy提供的查询接口如下：    
            
            # 创建Session:
            session = DBSession()
            # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
            user = session.query(User).filter(User.id=='5').one()
            # 打印类型和对象的name属性:
            print('type:', type(user))
            print('name:', user.name)
            # 关闭Session:
            session.close()    
        
        运行结果如下：

            type: <class '__main__.User'>
            name: Bob
        
        可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
        
        由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，
        相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。

        例如，如果一个User拥有多个Book，就可以定义一对多关系如下：   
            
            class User(Base):
                __tablename__ = 'user'
            
                id = Column(String(20), primary_key=True)
                name = Column(String(20))
                # 一对多:
                books = relationship('Book')
            
            class Book(Base):
                __tablename__ = 'book'
            
                id = Column(String(20), primary_key=True)
                name = Column(String(20))
                # “多”的一方的book表是通过外键关联到user表的:
                user_id = Column(String(20), ForeignKey('user.id'))
                    
        当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。
        
        ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

        正确使用ORM的前提是了解关系数据库的原理。
        
        
"""16| Web 开发 """

    最早的软件都是运行在大型机上的，后来随着PC机的兴起，软件开始主要运行在桌面上，
    而数据库这样的软件运行在服务器端，这种Client/Server模式简称CS架构。   
    
    随着互联网的兴起，人们发现，CS架构不适合Web，最大的原因是Web应用程序的修改和升级非常迅速，
    而CS架构需要每个客户端逐个升级桌面App，因此，Browser/Server模式开始流行，简称BS架构。

    在BS架构下，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。
    浏览器只需要请求服务器，获取Web页面，并把Web页面展示给用户即可。
        
    当然，Web页面也具有极强的交互性。由于Web页面是用HTML编写的，而HTML具备超强的表现力，
    并且，服务器端升级后，客户端无需任何部署就可以使用到新的版本，因此，BS架构迅速流行起来。    
           
    Web应用开发可以说是目前软件开发中最重要的部分。Web开发也经历了好几个阶段：
    
        (1)静态 Web 页面: 
            由文本编译器直接编译并生产静态的 HTML 页面，如果要修改 Web 页面的内容
            就需要再次编译 HTML 源文件，早期的互联网 Web 页面都是静态的。
        
        (2)CGI: 
            由于静态 Web 页面无法与用户交互，比如用户填写一个注册表单，静态 Web 页面就无法处理，
            要处理用户发送动态数据，就出现了 Common Gateway Interface，简称 CGI,用 C/C++ 编写。
         
        (3)ASP/JSP/PHP:
            由于Web应用特点是修改频繁，用C/C++这样的低级语言非常不适合Web开发，而脚本语言由于开发效率高，
            与HTML结合紧密，因此，迅速取代了CGI模式。ASP是微软推出的用VBScript脚本编程的Web开发技术，
            而JSP用Java来编写脚本，PHP本身则是开源的脚本语言。   
            
        (4)MVC:
            为了解决直接用脚本语言嵌入HTML导致的可维护性差的问题，
            Web应用也引入了Model-View-Controller的模式，来简化Web开发。
            ASP发展为ASP.Net，JSP和PHP也有一大堆MVC框架。   
        
    目前，Web开发技术仍在快速发展中，异步开发、新的MVVM前端技术层出不穷。
    Python的诞生历史比Web还要早，由于Python是一种解释型的脚本语言，开发效率高，所以非常适合用来做Web开发。
    Python有上百种Web开发框架，有很多成熟的模板技术，选择Python开发Web应用，不但开发效率高，而且运行速度快。 
    
    1、 HTTP协议简介:
    
        在 Web 应用中，服务器把网页传给浏览器，实际上就是把网页的 HTML 代码发送给浏览器，让浏览器显示出来，
        而浏览器和服务器之间的传输协议是 HTTP,所以：
            HTML 是一种用来定义网页的文本，会HTML,就可以编写网页。
            HTTP 是在网络上传输 HTML 的协议，用于浏览器和服务器的通信。

    2、 HTML 简介：
        
        HTML 文档是一系列的 Tag 组成，最外层的 Tag 是<html>。
        规范的HTML也包含<head>...</head>和<body>...</body>
        由于HTML是富文档模型，所以，还有一系列的Tag用来表示链接、图片、表格、表单等等。
        
        CSS是Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现。
        
        JavaScript是为了让HTML具有交互性而作为脚本语言添加的，
        JavaScript既可以内嵌到HTML中，也可以从外部链接到HTML中。
               
        如果要学习Web开发，首先要对HTML、CSS和JavaScript作一定的了解。HTML定义了页面的内容，CSS来控制页面元素的样式，而JavaScript负责页面的交互逻辑。

        讲解HTML、CSS和JavaScript就可以写3本书，对于优秀的Web开发人员来说，
        精通HTML、CSS和JavaScript是必须的，这里推荐一个在线学习网站w3schools：

        http://www.w3schools.com/
        以及一个对应的中文版本：
        http://www.w3school.com.cn/

        当我们用Python或者其他语言开发Web应用时，我们就是要在服务器端动态创建出HTML，
        这样，浏览器就会向不同的用户显示出不同的Web页面。
        
    3、 WSGI 接口：
        
        了解了 HTTP 协议和 HTML 文档，我们其实就明白了一个 Web 应用的本质就是：
            a. 浏览器发送一个 HTTP 请求
            b. 服务器接收到请求，生产一个 HTML 文档
            c. 服务器把 HTML 文档作为 HTTP 响应的 Body 发送给浏览器
            d. 浏览器收到 HTTP 响应，从 HTTP Body 取出 HTML 文档并显示。
        
        所以，最简单的 Web 应用就是把 HTML 用文件保存好，用一个现成的 HTTP 服务器软件
        接收用户请求，从文件中读取 HTML, 返回，Apache, Nginx, Lighttpd 等这些常见
        的静态服务器都是干这件事情的。
        
        如果要动态生成 HTML, 就需要把上述步骤自己来实现，不过，接收 HTTP 请求，
        解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，
        还没开始写动态HTML呢，就得花个把月去读HTTP规范。      
        
        正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。
        因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，
        让我们专心用Python编写Web业务。
        
        这个接口就是WSGI： Web Server Gateway Interface。
        
        WSGI 接口定义非常简单，它只要求 Web 开发者实现一个函数，就可以响应 HTTP 请求，
        
            def application(environ, start_response):
                start_response("200 OK", [('Content-Type', 'text/htm;')])
                return [b'<h1>Hello , web</h1>']
            
        上面的 application() 函数就符合 WSGI 标准的一个 HTTP 处理函数，它接收两个参数：
            environ: 一个包含所有 HTTP 请求信息的 dict 对象
            start_response: 一个发送 HTTP 响应的函数。
            
        在application()函数中，调用：
            
            start_response('200 OK', [('Content-Type', 'text/html')])
            
        就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。
        start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，
        每个Header用一个包含两个str的tuple表示。    
                    
        通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。
        然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。    
        
        有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，
        通过start_response()发送Header，最后返回Body。

        整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，
        我们只负责在更高层次上考虑如何响应请求就可以了。
        
        不过，等等，这个application()函数怎么调用？如果我们自己调用，
        两个参数environ和start_response我们没法提供，返回的bytes也没法发给浏览器。
        
        所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，
        Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
        所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
             
        运行WSGI服务:

            我们先编写hello.py，实现Web应用程序的WSGI处理函数：
            
                # hello.py
                
                def application(environ, start_response):
                    start_response('200 OK', [('Content-Type', 'text/html')])
                    return [b'<h1>Hello, web!</h1>']
            
            然后，再编写一个server.py，负责启动WSGI服务器，加载application()函数：
                
                # server.py
                # 从wsgiref模块导入:
                from wsgiref.simple_server import make_server
                # 导入我们自己编写的application函数:
                from hello import application
                
                # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
                httpd = make_server('', 8000, application)
                print('Serving HTTP on port 8000...')
                # 开始监听HTTP请求:
                httpd.serve_forever()
        
        无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
        HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以
        通过start_response()加上函数返回值作为Body。

        复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，
        我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。    
        
    4、 使用Web框架:
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    5、 使用模板：
    
   
"""17| 异步 IO"""

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                    
    、