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
        
        要注意区分 'ABC' 和 b'ABC'，前者是 str, 后者虽然内容显示和前者一样，但 bytes 的每个字符都只占用一个字节。
        
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
        第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。    
         
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
        
                    
                
                
                