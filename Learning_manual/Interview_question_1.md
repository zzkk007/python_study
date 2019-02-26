
"""

    https://www.cnblogs.com/apollo1616/category/1285283.html
    https://www.cnblogs.com/lmx123/p/9212079.html
    
"""

1、 如何实现对 Python 列表去除并保持原先顺序？
        
    >>> l = ['cc', 'bbbb', 'afa', 'sss', 'bbbb', 'cc', 'shafa']
    >>>  
    >>> l = ['cc', 'bbbb', 'afa', 'sss', 'cc','bbbb', 'cc', 'shafa']
    >>> add_to = list(set(l))
    >>> add_to
    ['bbbb', 'sss', 'afa', 'shafa', 'cc']
    >>> 
    >>> add_to.sort(key=l.index)
    >>> add_to
    ['cc', 'bbbb', 'afa', 'sss', 'shafa']
    >>>
    
    List sort()方法:
        描述:
            sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
        
        语法:
            sort()方法语法：
            list.sort( key=None, reverse=False)    
          
        参数:       
            key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
            指定可迭代对象中的一个元素来进行排序。
            
            reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
            
        返回值：
            
            该方法没有返回值，但是会对列表的对象进行排序。
            
2、现有两元组(('a'),('b')),(('c'),('d')),请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
    
    >>> t1 = (('a'),('b'))
    >>> 
    >>> t2 = (('c'),('d'))
    >>> 
    >>> list(zip(t1,t2))
    [('a', 'c'), ('b', 'd')]
    >>> 
    >>> list(map(lambda t:{t[0]:t[1]},zip(t1,t2)))
    [{'a': 'c'}, {'b': 'd'}]


3、在 Python 字符串格式化中，% 和 .format 的主要区别是什么？

    %：
        Python 中内置的 % 操作符可以用于格式化字符串操作
        控制字符串的呈现格式，% 操作符的使用是最方面的。
        
    .format:
        
        字符串的format()函数，该方法收集位置参数和关键字参数的任意集合，
        并使用它们的值来替换字符串中的占位符。
        
4.*args 和 kwargs 在什么情况下会使用到?请给出使用kwargs的示例代码      

    *args: 表示将实参中按照位置传参，把多出了的值给 args, 且以元组的方式呈现。
        
        >>> def foo(x, *args):
        ...    print(x)
        ...    print(args)
        ... 
        >>> foo(1,2,3,4,5)
        1
        (2, 3, 4, 5)
    
    *kwargs: 表示形参中按照关键字传参，把多余的传值以字典的方式呈现：
    
        >>> def soo(x, **kwargs):
        ...     print(x)
        ...     print(kwargs)
        ... 
        >>> soo(1, a = 1, b = 2, c = 3)
        1
        {'a': 1, 'b': 2, 'c': 3}        
        
5、字符串 x = "foo", 整数 y = 2, 那么 x*y = ?
    
    >>> x = "foo"
    >>> y = 2
    >>> x * y
    'foofoo'

6、赋值：

    >>> kvps = {'1':1,'2':2}
    >>> theCopy = kvps
    >>> kvps['1'] = 5
    >>> sum = kvps['1'] + tehCopy['1']
    >>> print(sum)
    10

7、添加一个新的python模块的搜素路径

    >>> import sys
    >>> print(sys.path)
    ['', '/usr/local/Python-3.6.4/lib/python36.zip', '/usr/local/Python-3.6.4/lib/python3.6',
    '/usr/local/Python-3.6.4/lib/python3.6/lib-dynload', 
    '/usr/local/Python-3.6.4/lib/python3.6/site-packages']
    
    sys.path.append('/root/mods')
    
8、列表：

    >>> country_counter = {}
    >>> def addone(country):
    ...     if country in country_counter:
    ...             country_counter[country] += 1
    ...     else:
    ...             country_counter[country] = 1
    ... 
    >>> addone('China')
    >>> country_counter 
    {'China': 1}
    >>> 
    >>> addone('Japan')
    >>> country_counter
    {'China': 1, 'Japan': 1}
    >>> 
    >>> addone('China')
    >>> country_counter
    {'China': 2, 'Japan': 1}
    >>> 
    >>> len(country_counter)
    2

9、赋值和[:] 不是一回事：

    >>> name1 = ['Amir','Barry','Chales','Dao']
    >>> name2 = name1
    >>> name3 = name1[:]
    >>> 
    >>> name2[0] = 'Alice'
    >>> name3[1] = 'Bob'
    >>> name2
    ['Alice', 'Barry', 'Chales', 'Dao']
    >>> name1
    ['Alice', 'Barry', 'Chales', 'Dao']
    >>> name3
    ['Amir', 'Bob', 'Chales', 'Dao']    
    
    >>> sum = 0
    >>> for ls in (names1,names2,names3):
    ...    if ls[0] == 'Alice':
    ...        sum += 1
    ...    if ls[1] == 'Bob':
    ...        sum += 10
    >>> print(sum)       
    >>> 12
    
10、变量：
    
    >>> d = lambda p : p * 2
    >>> t = lambda p : p * 3
    >>> x = 2
    >>> x = d(x)
    >>> x = t(x)
    >>> x = d(x)
    >>> print(x)
    24

11、优先级not > and > or:        

    >>> x = True
    >>> y = False
    >>> z = False
    >>> 
    >>> if x or y and z:
    ...     print('yes')
    ... else:
    ...     print('no')
    ... 
    yes
    >>> 
    
12、Python 里面如何实现 tuple 和 list 的转换：

    temp_list = [1,2,4,3,5]
    s=tuple(temp_list)
    print(type(s))   #<class 'tuple'>
     
    temp_tupe = (1,2,3)
    l = list(temp_tupe)
    print(type(l))   #<class 'list'>   

13、如何得到列表list的交集与差集：

    >>> a = [2,3,4,5]
    >>> b = [2,5,8]
    >>> 
    >>> list(set(a).intersection(set(b)))  # 交集 
    [2, 5]
    >>> 
    >>> list(set(a).union(set(b)))  # 并集
    [2, 3, 4, 5, 8]
    >>> 
    >>> 
    >>> list(set(b).difference(set(a))) # 差集
    [8]
    >>> 
    >>> list(set(a).difference(set(b)))
    [3, 4]   


14、Python中定义函数时如何书写可变参数和关键字参数？    
    
    *args是可变参数,args接收的是一个tuple,
    **kwargs是关键字参数,kw接收的是一个dict.
    以及调用函数时如何传入可变参数和关键字参数的语法：
    可变参数既可以直接传入:func(1, 2, 3),
    又可以先组装list或tuple,再通过*args传入:func(*(1, 2, 3)).
    关键字参数既可以直接传入:func(a=1, b=2),
    又可以先组装dict,再通过**kw传入:func(**{'a': 1, 'b': 2}).    
    
15、什么是 lambda 表达式：

    匿名函数，也就是 lambda 函数，通常用在函数体比较简单的函数上，
    匿名函数顾名思义就是函数没有名字，因此不用担心函数名冲突

16、re的match()和search()有什么区别？ 

    match() 函数只检测re是不是在string 的开始位置匹配，
    search() 会扫描整个 string 查找匹配。
    也就是说match()只有在0位置匹配成功的话才有返回,
    如果不是开始位置匹配成功的话,match()就返回None.      
    
17、1 or 2 和 1 and 2 输出是什么，为什么？

    >>> 1 or 2
    1
    >>> 1 and 2
    2
    >>> 

18、1<(2==2) 和 1<2 == 2结果分别是什么？为什么？

    >>> 1<(2==2)  # False 因为2==2为True,而True表示为1，False表示为0，所以1<1，结果为False
    False
    >>> 
    >>> 1==(2==2)
    True
    >>> 
    >>> 1 < 2 == 2 # python是允许连续比较1<2==2意思是1<2且2==2
    True
    >>> 1 < 2
    True

19、[i%2 for i in range(10)] 和 (i % 2 for i in range(10)) 输出结果分别是什么？

    >>> [i%2 for i in range(10)]
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    >>> 
    >>> 
    >>> (i % 2 for i in range(10))
    <generator object <genexpr> at 0x7f3db2cf3200>


20、请描述unicode,utf-8,gbk等编码之间的关系        
    
    unicode --> encode --> utf-8
    utf-8 --> decode(gbk) --> unicode
    
    ascii 是最早美国用的标准信息交换码，把所有的字母的大小写，各种符号用 二进制来表示，共有256中，
    加入些拉丁文等字符，1bytes代表一个字符，

    Unicode是为了统一世界各国语言的不用，统一用2个bytes代表一个字符，可以表达2**16=65556个，
    称为万国语言，特点：速度快，但浪费空间，

    可以用在内存处理中，兼容了utf-8，gbk，ASCII，
    
    utf-8 为了改变Unicode的这种缺点，规定1个英文字符用1个字节表示，1个中文字符用3个字节表示，
    特点；节省空间，速度慢，用在硬盘数据传输，网络数据传输，相比硬盘和网络速度，体现不出来的，
    
    gbk  是中文的字符编码，用2个字节代表一个字符，
     
    简单来说，unicode，gbk和大五码就是编码的值，而utf-8,uft-16之类就是这个值的表现形式．
    而前面那三种编码是一兼容的，同一个汉字，那三个码值是完全不一样的．
    如＂汉＂的uncode值与gbk就是不一样的，假设uncode为a040，gbk为b030，
    而uft-8码，就是把那个值表现的形式．utf-8码完全只针对uncode来组织的，
    如果GBK要转UTF－8必须先转uncode码，再转utf-8就OK了．    
    
21、python中如果判断一个对象是否可调用对象?那些对象可以是可调用对象?
    
    1、使用内置的callable函数：
    callable(func)
    用于检查对象是否可调用，返回True也可能调用失败，但是返回False一定不可调用
    
    2、判断对象类型是否是FunctionType
    type(func) is FunctionType
    # 或者
    isinstance(func, FunctionType)
    
    3、判断对象是否实现__call__方法：
    hasattr(func, '__call__')

22、如何定义一个类,使其对象本身就是可调用对象?
    
    如果一个类实现了__call__方法,那么其实例也会成为一个可调用对象.
        
23、什么是装饰器?写一个装饰器,可以打印输出方法执行时长的信息.

    装饰器本身是一个python函数,它可以让其他函数在不需要做任何变动的前提下增加额外功能.
    import time
    def timer(func):
        def decor(*args):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            d_time = end_time - start_time
            print("run the func use:%s" % d_time)
        return decor
        
    @timer
    def func(str, count)
        for i in range(count):
            print("%d hello,%s!"%(i,str))
    
    func("world", 100)
    
24、哪些情况下，y! = x - (x-y)会成立？
    
    x, y是两个不相等的非空集合
    
    >>> x = set([1,2,3,4])
    >>> y = set([3,4,5,6])
    >>> 
    >>> x - y
    {1, 2}
    >>> 
    >>> x - (x-y)
    {3, 4}
    >>> y
    {3, 4, 5, 6}
    >>> 

25、用python实现"九九乘法表"，用两种不同的方式实现：

    >>> [('{}*{}={}'.format(i,j,i*j) for i in range(1, j+1)) for j in range(1,10)] 
    [<generator object <listcomp>.<genexpr> at 0x7f3db2cf33b8>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2cf3200>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2cf3258>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2cf31a8>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2a27e60>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2a47ca8>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2a47d00>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2a47d58>, 
    <generator object <listcomp>.<genexpr> at 0x7f3db2a47db0>]
    
    >>> [(['{}*{}={}'.format(i,j,i*j) for i in range(1, j+1)]) for j in range(1,10)]
    [['1*1=1'], ['1*2=2', '2*2=4'], ['1*3=3', '2*3=6', '3*3=9'], ['1*4=4', '2*4=8', '3*4=12', '4*4=16'],
     ['1*5=5', '2*5=10', '3*5=15', '4*5=20', '5*5=25'], 
     ['1*6=6', '2*6=12', '3*6=18', '4*6=24', '5*6=30', '6*6=36'], 
     ['1*7=7', '2*7=14', '3*7=21', '4*7=28', '5*7=35', '6*7=42', '7*7=49'], 
     ['1*8=8', '2*8=16', '3*8=24', '4*8=32', '5*8=40', '6*8=48', '7*8=56', '8*8=64'], 
     ['1*9=9', '2*9=18', '3*9=27', '4*9=36', '5*9=45', '6*9=54', '7*9=63', '8*9=72', '9*9=81']]
    
    
    >>> print('\n'.join('  '.join( ['{}*{}={}'.format(i,j,i*j) for i in range(1,j+1)] ) for j in range(1,10) ))
    1*1=1
    1*2=2  2*2=4
    1*3=3  2*3=6  3*3=9
    1*4=4  2*4=8  3*4=12  4*4=16
    1*5=5  2*5=10  3*5=15  4*5=20  5*5=25
    1*6=6  2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
    1*7=7  2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
    1*8=8  2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
    1*9=9  2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81               
    
    另一种方式：
        
    for j in range(1, 10):
        for i in range(1,j+1):
            print(('{}*{}={}'.format(i, j, i * j)),end='')
        print('')
    
    1*1=1 
    1*2=2 2*2=4 
    1*3=3 2*3=6 3*3=9 
    1*4=4 2*4=8 3*4=12 4*4=16 
    1*5=5 2*5=10 3*5=15 4*5=20 5*5=25 
    1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36 
    1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49 
    1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64 
    1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81  


26、如何在Python中拷贝一个对象?并说明它们之间的区别：           

    -深拷贝：完全拷贝一个副本，容器内部的元素地址都不一样
    -浅拷贝：仅仅复制了容器中元素的地址 
    
27、获取list的元素个数,和向末尾追加元素所用的方法分别是：

    cout() 和 append()
    
28、如何判断一个变量是不是字符串：
    
    用 type 查看它的类型
    用 isinstance 函数，来判断该对象是不是已知类型，这样讲返回 True 或 False
    
29、xrange 和 range 有什么不同：

    python2:
        xrange 用法和range 完全相同，所不同的是生产的不是一个 list 对象，而是一个生成器。    
    
    python3:
        xrange 已经取消，直接用range, range 生产的是一个生成器，一般与for结合使用。
        
30、is 和 == 的区别：

    == 是判断两者的内容是否相同。
    is 是判断两者是不是同一个对象。
    
31、如何生成[1,4,9,16,25,36,49,64,81,100]?尽量用一行实现
    
    [x * x for x in range(1, 11)]
    
32、生成器是什么?有什么作用?请写一个生成器：
    
    本质：迭代器（所以自带了 __iter__ 方法和__next__方法，不需要我们去实现）
    特点：惰性运算，开发者自定义
    
    Python中提供的生成器：
    - 生成器函数:
        一个包含 yield 关键字的函数就是生成器函数
        yield 可以为我们从函数中返回值，但是 yield 又不同于 return, return 的执行意味着程序的结束。
        调用生产器函数不会得到返回在具体值，而是得到一个可迭代的对象。
        每一次获取这个可迭代对象的值，就能推动函数的执行，获取新的返回值，知道函数执行结束。
        
        def genrator_func1():
            a = 1
            print('现在定义了a变量')
            yield a
            b = 2
            print('现在又定义了b变量')
            yield b   
        
        g1 = genrator_fun1()
        #打印g1可以发现g1就是一个生成器
        print('g1 : ',g1)
        print(next(g1))
        print(next(g1))

        g1 :  <generator object genrator_fun1 at 0x0000000004DCA2B0>
        现在定义了a变量
        1
        现在又定义了b变量
        2
  
    - 生成器表达式(几乎不占内存)
        sum(i for i in range(100))
    
33、map(str,[1,2,3,4,5,6,7,8,9])输出什么?

    >>> map(str,[1,2,3,4,5,6,7,8])      
    <map object at 0x7f3db29e3f98>
    >>> 
    >>> 
    >>> list(map(str,[1,2,3,4,5,6,7,8]))
    ['1', '2', '3', '4', '5', '6', '7', '8']
    >>>     
            
34、请写出一段Python代码实现删除一个list里面的重复元素：

    list1 = [11,3, 4, 5, 2, 3, 4]
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
    
        
35、如何用 Python 删除一个文件

    # 直接从系统里面删除文件,不经过回收站
    os.remove('文件')
   
    # 直接从系统里面删除空文件夹,不经过回收站
    os.rmdir('文件夹')

36、Python 里面如何生成随机数：

    import random
    print(random.random())
    # 0.44142579456844966
    print(random.uniform(10,20))
    # 11.171021064685485
    print(random.randint(12, 20))
    # 16
    
37、介绍一下except的用法和作用：
    
    Python 的 except 用来捕获所有异常，因为 python 里面的每次错误都会抛出一个异常
    所以每个程序的错误都被当作一个运行时错误。
    
        try:
            pass
        except BaseException as e:
            print(e)
        finally:
            pass

38、输入一个字符串，返回倒序排列的结果：
    
    如:'abcdef',返回'fedcba'
    l='abcdef'
    print(l[::-1])
    
39、Python中元组和列表的主要区别是？      

    - 元组是不可变的,列表是可变的
    - 元组是可以嵌套的
    - 元组---(),列表---[]        
 
40、Cookie和Session有什么区别?

    cookie数据存放在客户端的,而session则是存放在服务端的.
    
41、 HTTP协议是有状态协议还是无状态协议,如何从两次请求中判断是同一用户.

    HTTP是无状态协议.
    -比如用登录淘宝来举例,客户端访问淘宝,淘宝的服务端会返回给客户端一个“随机字符串”类型的键值对.
    当下一次再访问的时候,客户端会带着上次的“随机字符串”来和服务器进行验证,如果匹配,则登录成功.       

42、一行print出1-100偶数的列表:

    [n for n in range(1,101) if n%2 == 0]

43、写出五中HTTP请求的方法
    
    GET\POST\HEAD\PUT\DELETE\CONNECT\OPTIONS\TRACE
    GET:请求指定的页面信息，并返回实体主体
    HEAD:类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
    POST：向指定资源提交数据进行处理请求(例如提交表单或者上传文件)，数据被包含在请求体中。
    PUT:从客户端向服务器传送的数据取代指定的文档的内容
    DELETE:请求服务器删除指定的页面
    CONNECT:HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器
    OPTIONS:允许客户端查看服务器的性能
    TRACE:回显服务器收到的请求，主要用于测试或诊断
    
44、描述多进程开发中join与daemon的区别?：

    p.join([timeout]):
    主线程等待p终止
    强调:是主线程处于等的状态,而p是处于运行的状态.
    timeout是可选的超时时间,需要强调的是,
    p.join只能join住start开启的进程,而不能join住run开启的进程 .
    
    p.daemon:默认值为False,
    如果设为True,代表p为后台运行的守护进程,
    当p的父进程终止时,p也随之终止,并且设定为True后,
    p不能创建自己的新进程,必须在p.start()之前设置.            
    
45、斐波契纳数列 1,2,3,5,8,13,21......根据这样的规律,编程求出400万以内最大的斐波契纳数,
    并求出他是第几个斐波契纳数.    
    
    li = [1,2]
    while li[-1] < 4000000:
        li.append(li[-1] + li[-2])
    del li[-1]
    print(li[-1])
    print(len(li))
    
46、Python主要的内置数据类型都有哪些?哪些是可变的?哪些是不可变的?可变类型与不可变类型有什么区别？

    数字、字符串、列表、元组、字典、布尔型
    
    可变:列表,字典
    不可变:数字,字符串，布尔、元组
    可变数据类型:在id不变的情况下,数据类型的内部可以改变
    不可变数据类型:value值改变,id也跟着改变    

47、Python是如何进行内存管理的?python的程序会内存泄漏吗?说说有没有什么方面防止或检测内存泄漏?

    语言的内存管理是语言设计的一个重要方面.
    它是决定语言性能的重要因素.
    无论是C语言的手工管理,还是Java的垃圾回收,都成为语言最重要的特征.
    这里以Python语言为例子,说明一门动态类型的面向对象的语言的内存管理方式.
    项目中两种情况导致对象没有被正确回收:
    - 被退出才回收的对象引用
    - 交叉引用        
        
48、关于python程序的运行性能方面,有什么手段能提升性能?

    -让关键代码依赖外部包
    -排序时使用键(key)
    -优化代码中的循环
    -使用较新版本的python        

49、判断python对象是否为可调用的函数?

    -方法1:
    使用内置的callable函数,用于检查对象是否可调用.
    如果返回True也可能调用失败,但是返回False一定不可调用.
    callable(func)
    
    -方法2:判断对象类型是否是FunctionType
    type(func) is FunctionType
    # 或者
    isinstance(func, FunctionType)
    
    -方法3:判断对象是否实现__call__方法,
    如果定义一个类的话,里面只要定义了__call__方法,对象就可以被调用了.
    hasattr(func, '__call__')
       
43、编程实现以下功能：
    
    dicta = {'a':1,'b':2,'c':3,'d':4,'f':'hello'}
    dictb = {'b':3,'d':5,'e':7,'m':9,'k':'world'}
    要求写一段代码,实现两个字典的相加,不同的key对应的值保留,
    相同的key对应的值相加后保留,如果是字符串就拼接,最终得到如下结果：    
    dictc = {'a':1,'b':5,'c':3,'d':9,'e':7,'m':9,'f':'hello','k':'world'}
    
    
    dicta = {'a':1,'b':2,'c':3,'d':4,'f':'hello'}
    dictb = {'b':3,'d':5,'e':7,'m':9,'k':'world'}
    
    dic = {}
    for key1 in dicta:
        for key2 in dictb:
            if key1 == key2:
                dic[key1] = dicta[key1] + dictb[key2]
    
    for a in dicta:
        if a not in dic:
            dic[a] = dicta[a]
    
    for b in dictb:
        if b not in dic:
            dic[b] = dictb[b]
    print(dic)
    # dictc = {'a':1,'b':5,'c':3,'d':9,'e':7,'m':9,'f':'hello','k':'world'}
    
 44、递归求反转字符串：

    lst = []
    def output(str, length):
        if length == 0:
            return lst
        lst.append(str[length - 1])
        output(str, length - 1)
   
    str = input('请输入一个字符串:')
    output(str, len(str))
    print('反转序列：',lst)
 
 45、已知有五位朋友在一起。第五位朋友他说自己比第4个人大2岁；
    问第4个人岁数，他说比第3个人大2岁；
    问第三个人，又说比第2人大两岁；
    问第2个人，说比第一个人大两岁；
    最后问第一个人，他说是10岁。
    要求：求第5个人的年龄是多少。
    
    def age(n):
        if n==1:
            return 10
        else:
            return age(n-1)+2
        print(age(5))
 

46、python 闭包 closure 总结：
    
    1. 内嵌函数的非本地变量：
        在另一个函数里面定义的函数，被称为内嵌函数，内嵌函数可以访问闭合范围(就是外部函数范围)的变量，
        这些变量被称为非本地变量（nonllocal variable）
        默认情况下，非本地变量是只读的，为了可以修改非本地变量，需要将它们声明为 nonlocal,如下列所示：
        
        def print_msg(msg):
            """This is the outer enclosing function"""
            def printer():
                """This is the nested function"""
                print(msg)
            printer()
            
        print_msg("Hello")
        Hello 
    
        可以看到，内嵌函数是printer()，可以访问非本地变量msg，msg定义在外部函数print_msg()里面。
        
    2. 定义一个闭包函数：
        在上面的例子中，如果print_msg()返回print()函数，而不是调用它，会发生什么？这要求函数被这样定义
        
        def print_msg(msg):
            """This is the outer enclosing function"""
 
            def printer():
                """This is the nested function"""
                print(msg)
 
            return printer # this got changed
 
        # Now let's try calling this function.
        # Output: Hello
        another = print_msg("Hello")
        another()    
        
        和非同寻常。
        print_msg() 函数被通过传入 "Hello" 所调用，返回的函数被绑定为 another。
        在调用 another() 的时候，我们对 print_msg() 函数已经完成调用了，但是“Hello”仍然被记住了。
        这种将一些数据("Hello")附加到代码的技术，被称为 Python 里面的 closure.
        闭合范围内的数据(非本地变量)能够一直被记住，即便它们已经脱离了闭合范围或者外部函数已经被从命名空间删除.
        在python shell里面继续运行下面的代码，看看会发生什么.
        
        >>> del print_msg
        >>> another()
        Hello
        >>> print_msg("Hello")
        Traceback (most recent call last):
        ...
        NameError: name 'print_msg' is not defined
        
    3.怎样得到一个闭包函数：
    
        从上面的例子可以看出，当我们让内嵌函数引用一个非本地变量，就得到了一个python closure.
        python closure必须满足以下三点标准：
        1)必须有一个内嵌函数(函数里定义的函数）
        2)内嵌函数必须引用一个定义在闭合范围内(外部函数里)的变量
        3)外部函数必须返回内嵌函数            
        
    4. 什么时候使用closure：
    
        closure适合做什么？
        closure可以减少使用全局变量和提供一定程度的数据隐藏. 
        当一个类只有很少的方法(通常是一个)，closure可以提供一种更优雅的替代方案。
        但如果类的属性或者方法开始增多，最好还是实现一个类。
        下面是一个closure也许比类更好的一个例子。当然，到底哪个更好最终还是取决与你。    
        
        def make_multiplier_of(n):
            def multiplier(x):
                return x * n
            return multiplier
         
        # Multiplier of 3
        times3 = make_multiplier_of(3)
         
        # Multiplier of 5
        times5 = make_multiplier_of(5)
         
        # Output: 27
        print(times3(9))
         
        # Output: 15
        print(times5(3))
         
        # Output: 30
        print(times5(times3(2)))
        
        python的装饰器可以扩展closure的功能
    
    5. 获取闭合数值：
        
        最后还有一个友情提示，所有在外部函数定义的非本地变量，都可以被获取到。
        所有的函数对象都有一个__closure__属性，如果它是一个闭包函数，那么它包含一个cell objects元组。
        就上面的例子，我们知道time3和times5是闭包函数
        
        >>> make_multiplier_of.__closure__
        >>> times3.__closure__
        (<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)
        
        
        cell object有cell_contents属性，保存了闭合数值
            >>> times3.__closure__[0].cell_contents
            3
            >>> times5.__closure__[0].cell_contents
            5

47、“猴子补丁” ( monkey patching) 指的是什么？这种做法好吗？：

    “猴子补丁” 就是指，在函数或对象已经定义之后，再去改变它们的行为。
    
    举个例子：

    import datetime
    datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)
    大部分情况下，这是种很不好的做法 - 因为函数在代码库中的行为最好是都保持一致。
    打“猴子补丁”的原因可能是为了测试。mock包对实现这个目的很有帮助。

    为什么提这个问题？

    答对这个问题说明你对单元测试的方法有一定了解。你如果提到要避免“猴子补丁”，
    可以说明你不是那种喜欢花里胡哨代码的程序员（公司里就有这种人，跟他们共事真是糟糕透了），
    而是更注重可维护性。还记得KISS原则码？答对这个问题还说明你明白一些Python底层运作的方式，
    函数实际是如何存储、调用等等。

    另外：如果你没读过mock模块的话，真的值得花时间读一读。这个模块非常有用。
            

48、什么是 Python：

    （1）Python 是一种解释型语言，python代码在运行之前不需要编译，之后再翻译成机器码再执行。
    
    （2）Python 是动态类型语言，在声明变量时，不需要说明变量的类型。
    
    （3）Python 适合面向对象的编程，因为它支持通过组合与继承的方式定义类。
    
    （4）在 Python 语言中，函数是第一个类对象。
    
    （5）Python代码编写快，但是运行速度比编译语言通常要慢。
    
    （6）Python用途广泛，程序员可以专注于算法和数据结构的设计，而不用处理底层的细节。
    
    
49、什么是 pickling 和 unpickling?:
    
    在文件中，字符串可以很方便的读取写入，数字可能稍微麻烦一下，因为read()方法只返回字符串，
    我们还需要将其传给 int() 这样的函数，使其将如"1994"的字符串转为数字1945.
    但是，如果要半寸更复杂的数据类型，如列表，字典，或者类的实例，那么就会更复杂了。
    为了让用户在平常的编程和测试时保存复杂的数据类型，python提供了标准模块，
    称为pickle.这个模块可以将几乎任何的python对象(甚至是python的代码)，转换为字符串表示，
    这个过程称为pickling.而要从里面重新构造回原来的对象，
    则称为unpickling.在pickling和unpicking之间，表示这些对象的字符串表示，
    可以存于一个文件，也可以通过网络远程机器间传输。
    
    如果你有一个对象friend,和一个已经打开并用于写的文件对象f,pickle这个对象最简单的方式就是使用： 
    pickle.dunmp(friend,f)
    # Pickle模块读入任何Python对象，将它们转换成字符串，然后使用dump函数将其转储到一个文件中——这个过程叫做pickling。

50、Python是怎么管理内存的？

    Python 的内存管理是由私有的 heap 空间管理的，所有的 python 对象和数据结构都在一个私有的 heap 中。
    程序员没有访问操作改 heap 的权限，只有解释器才能对它进行操作。
    
    为 Python 的 heap 空间分配内存是由 python 内存管理模块进行的，其核心 API 会提供一下访问该模块方法供程序员使用。
    
    Python 有自带的垃圾回收机制，它回收并释放没有被使用的内存，让它们能够被其他程序使用。             


51、有没有一个工具可以帮助查找python的bug和进行静态的代码分析？
    
    PyChecker是一个静态分析工具，它不仅能报告源代码中的错误，并且会报告错误类型和复杂度。
    Pylint是检验模块是否达到代码标准的另一个工具。   
    
            
52、什么是Python的命名空间？
    
    在 python 中，所有的名字都存在一个空间中，它们在该空间中存在和被操作--这就是命名空间。
    它就像一个盒子，每一个变量名字都对应装着一个对象。当查询变量的时候，会从该盒子里面找到相应的对象。
    
    定义：
        
        名称到对象的映射。命名空间是一个字典的实现，键为变量名，值是变量对应的值。
        各个命名空间是独立没有关系的，一个命名空间中不能有重名，
        但是不同的命名空间可以重名而没有任何影响。
        
    分类：
    
        Python 命名空间：
        LOCAL: 局部命名空间，每个函数所拥有的命名空间，记录了函数中定义的所有变量，包括函数的入参、内部定义的局部变量。
        
        ENCOBEL:上一层结构中的def或lambda的本地作用域（E） 
        
        GLOBAL: 全局命名空间，每个模块加载执行时创建的，记录了模块中定义的变量，
                包括模块中定义的函数、类、其他导入的模块、模块级的变量与常量。
        
        Built-in: python自带的内建命名空间，任何模块均可以访问，放着内置的函数和异常。
    
    生命周期：
        
        Local（局部命名空间）在函数被调用时才被创建，但函数返回结果或抛出异常时被删除。（每一个递归函数都拥有自己的命名空间）。
        Global（全局命名空间）在模块被加载时创建，通常一直保留直到python解释器退出。
        Built-in（内建命名空间）在python解释器启动时创建，一直保留直到解释器退出。

        各命名空间创建顺序：
        python解释器启动 ->创建内建命名空间 -> 加载模块 -> 创建全局命名空间 ->函数被调用 ->创建局部命名空间
        
        各命名空间销毁顺序：
        函数调用结束 -> 销毁函数对应的局部命名空间 -> python虚拟机（解释器）退出 ->销毁全局命名空间 ->销毁内建命名空间
        
        python解释器加载阶段会创建出内建命名空间、模块的全局命名空间，
        局部命名空间是在运行阶段函数被调用时动态创建出来的，函数调用结束动态的销毁的。         
                 

53、参数按值传递和引用传递是怎么实现的：

    Python 中的一切都是类，所有的变量都是一个对象的引用，引用的值是由函数确定的，因此无法改变。
    
    传值：
        
        简单来说，你在内存中有一个地址，我也有一个地址，我把我的地址里面的内容复制给你，
        以后你做什么就跟我没关系，不会改变原来的参数的内容。
    
    传引用：
        
        所谓传引用是有一个参数在内存有个地址，地址里面放了一堆东西，在调用函数时，
        把实际参数的地址传递到函数中，那么在函数中对参数所进行的修改，将影响到实际参数。
        也就是说最后函数运行完之后会改变原来参数的内容。
    
54、Python 中 pass 是什么？

    pass 是一个在 Python 中不会执行的语句，在复杂语句中，如果一个地方需要暂时被留白，它常常被用于占位符。                    
        
55、构造器是什么？

    构造器是实现迭代的一种机制。它功能的实现依赖于yield表达式，除此之外它跟普通的函数没有什么两样。
    
56、在Python中什么是slicing?

    Slicing是一种在有序的对象类型中(数组，元组，字符串)节选某一段的语法。
    
57、如何在Python中拷贝对象？   
    
    如果在python中拷贝对象，大多数时候你可以用copy.copy()或者copy.deepcopy()。但是并不是所有的对象都可以被拷贝。   
    
58、doc string是什么？
    
    Python中文档字符串被称为docstring,它在Python中的作用是为函数、模块和类注释生成文档。
    
59、Python中如何将一个数字转换成一个字符串？

    可以使用自带函数str()将一个数字转换成字符串。
    如果想要八进制或十六进制数或二进制，可以使用oct()或hex()或bin()。    

60、Python中模块和包是什么？

    在 Python 中，模块是搭建程序的一种方式。每一个 Python 代码文件都是一个模块，并可引用其他的模块，比如对象和属性。
    一个包包含许多Python代码的文件夹是一个包。一个包可以包含模块和子文件夹。                          
    
61、什么是协程？

    简单点说协程是进程和线程的升级版，进程和线程都面临着内核态和用户态的切换问题而耗费许多切换时间，
    而协程就是用户自己控制切换的时机，不需要再陷入系统的内核态。    


62、1,2,3,4,5能组成多少个互不相同且无重复数字的三位数(程序实现)
    
     
63、请用自己的算法,按升序合并如下两个list,并去除重复的元素.     


"=========================================================================================="

1、Python解释器种类以及特点？

    CPython：这个解释器是用C语言开发的，所以叫CPython，在命名行下运行python，就是启动CPython解释器，CPython是使用最广的Python解释器。       
    
    Jython：Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
    
    IPython：IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，
    但是执行Python代码的功能和CPython是完全一样的，好比很多国产浏览器虽然外观不同，但内核其实是调用了IE。


2、什么是PEP8？
    
    PEP8 是一个编程规范，内容是一些关于如何让你的程序更具有可读性建议。
    其中主要内容包括：代码编排、文档编排、空格的使用、注释、文档描述、命名规范、编码建议等。
    
    请至少列举5个 PEP8 规范（越多越好）：
    
        a. 缩进，4个空格的缩进，不使用 Tap, 更不能混合使用 Tap 和 空格。
        
        b. 每行最大长度 79， 换行可以使用反斜杠，最好使用圆括号。
        
        c. 类和top-level函数定义之间空两行；
           类中的方法定义之间空一行；
           函数内逻辑无关段落之间空一行；
           其他地方尽量不要再空行。     
        
        d. 块注释，在一段代码前增加的注释，在“#”后增加一空格。
        
        e. 各种右括号请不要加空格。
        
        f. 逗号、冒号、分号前不用加空格。
        
        g. 函数的左括号前不要加空格。
        
        h. 序列的左括号前不要加空格。
        
        i. 操作符左右各加一个空格，不要为了对齐增加空格。
        
        j. 函数默认参数使用的赋值符左右省略空格。
        
        k. 不要将多句语句写在同一行，尽管使用‘；’允许。
        
        l. if/for/while语句中，即使执行语句只有一句，也必须另起一行。
        
        m. 类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。
        
        
3、通过代码实现如下转换：
    
    二进制转换成十进制：v = “0b1111011” 
        
        #先将其转换为字符串，再使用int函数，指定进制转换为十进制。
        
        >>> int("0b1111011",2)      
        123
      
    十进制转换成二进制：v = 18
        
        使用 bin 函数，将10进制转换成2进制。
        >>> bin(18)
        '0b10010'
    
    八进制转换成十进制：v = “011”  
        
        print(int("011",8))
        #9
        
    十进制转换成八进制：v = 30
        
        print("转换为八进制为：", oct(30))
        #转换为八进制为： 0o36
          
    十六进制转换成十进制：v = “0x12”
        
        print(int("0x12",16))
        #18    
      
    十进制转换成十六进制：v = 87      
        
        print("转换为十六进制为：", hex(87))
        转换为十六进制为： 0x57         
               
    如何实现['1', '2', '3']变成[1,2,3]
    
        a=['1','2','3']
        b=[int(i) for i in a]
        print(b)     
        
4、python递归的最大层数？     
    
    
    def fab(n):
        if n == 1:
            return 1
        else:
            return fab(n-1) + n

    
    print (fab(998))
    498501
    print (fab(999))
    RecursionError: maximum recursion depth exceeded in comparison
    #得到的最大数为998，以后就是报错了。     
    
    import sys
    sys.setrecursionlimit(100000)

    def foo(n):
        print(n)
        n += 1
        foo(n)
        
    if __name__ == '__main__':
    foo(1)

    #得到的最大数字在3922-3929之间浮动，这个是和计算机有关系的，
    将数字调到足够大了，已经大于系统堆栈，python已经无法支撑到太大的递归崩了。

5、计算题：

    >>> v = dict.fromkeys(['k1','k2'],[])
    >>> v
    {'k1': [], 'k2': []}
    >>> 
    >>> v['k1'].append(666)
    >>> v
    {'k1': [666], 'k2': [666]}
    >>> 
    >>> v['k1'] = 777
    >>> v
    {'k1': 777, 'k2': [666]}
    >>> 
    >>> 
    >>> v = dict.fromkeys(['k1','k2'],[1])
    >>> v
    {'k1': [1], 'k2': [1]}
    >>> v['k1'].append(622)
    >>> v
    {'k1': [1, 622], 'k2': [1, 622]}
    >>> v['k2'].append(63) 
    >>> v
    {'k1': [1, 622, 63], 'k2': [1, 622, 63]}
    >>> 
    >>> v['k2'] = 777
    >>> v
    {'k1': [1, 622, 63], 'k2': 777} 

6、求结果, 不明白

    def num():
        return [lambda x:i*x for i in range(4)]
    print(m(2) for m in num())
    # <generator object <genexpr> at 0x0000000000B2FA40> 为元祖
    print(list(m(2) for m in num()))     
    # [6, 6, 6, 6] 
    
7、求结果：

    >>> 1 or 3
    1
    >>> 
    >>> 1 and 3
    3
    >>> 
    >>> 0 and 2 and 1
    0
    >>> 
    >>> 0 and 2 or 1
    1
    >>> 
    >>> 0 and 2 or 1 or 4
    1
    >>>
    >>> 0 or False and 1     
    False     
 
8、字节码和机器码的区别：

    字节码：
    
        字节码是一种中间码
        字节码通常指的是已经经过编译，但与特定机器码无关，需要直译器转译后才能成为机器码的中间代码。
        字节码通常不像源码一样可以让人阅读，而是编码后的数值常量、引用、指令等构成的序列。
        字节码主要为了实现特定软件运行环境和软件环境、硬件环境无关。
        字节码的实现方式是通过编译器和虚拟机器。
        编译器将源码编译成字节码，特定平台上的虚拟机器将字节码转译为可以直接执行的指令。
        总结：字节码是一种中间状态（中间码）的二进制代码（文件）。需要直译器转译后才能成为机器码。
        
    机器码：
    
        机器码就是计算机可以直接执行，并且执行速度最快的代码。
        机器码是电脑CPU直接读取运行的机器指令，运行速度最快             
     
    
9、三元运算规则以及应用场景：

     三元运算符的功能与“if...else”流程语句一致，它在一行中书写，代码非常精练、执行效率更高。
     
    (expr1) ? (expr2) : (expr3);
    
        解释：如果条件“expr1”成立，则执行语句“expr2”，否则执行“expr3”。
    
    实现同样的功能，若使用条件流程语句，就需要书写多行代码： 
    
        if(expr1) {
            expr2;
        } else {
            expr3;
        }    

10、Python自省：

    自省就是面向对象的语言所写的程序在运行时,所能知道对象的类型。
    简单一句就是运行时能够获得对象的类型.比如type(),dir(),getattr(),hasattr(),isinstance().        


11、列举 Python2和Python3的区别？：
    
    (1). Print:
    
       在 Python 2 中， print 被视为一个语句而不是一个函数。
       在使用 Python 3 时，print（）会被显式地视为一个函数。
       
    （2）整数的除法：
    
        debian:~$ python
        Python 2.7.14 (default, May  2 2018, 15:37:08) 
        [GCC 4.7.2] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 
        >>> 
        >>> 5 / 2
        2
        >>> 
        >>> 
        debian:~$ python3
        Python 3.6.4 (default, May  2 2018, 15:27:32) 
        [GCC 4.7.2] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 
        >>> 5/2
        2.5
        >>>     
       
    （3）支持 Unicode：
    
        Python 2 默认使用 ASCII 字母表，因此当您输入“Hello，Sammy！”时， Python 2 将以 ASCII 格式处理字符串。
        Python 3 默认使用 Unicode，这节省了程序员多余的开发时间，并且您可以轻松地在程序中直接键入和显示更多的字符。   
            
    （4）后续发展：
        
         Python 3 和 Python 2 之间的最大区别不是语法上的，而是事实上 Python 2.7 将在 2020 年失去后续的支持，
         Python 3 将继续开发更多的功能和修复更多的错误。
        
    （5）：
    
        long整数类型被Python3废弃，统一使用int
        xrange()函数被 pytho3 废弃
        raw_input()函数被 pytho3 废弃

    
12、文件操作时：xreadlines和readlines的区别？：

    二者使用时相同，但返回类型不同，xreadlines返回的是一个生成器，readlines返回的是list
    
13、什么是正则的贪婪匹配？：

    贪婪匹配：总是尝试匹配尽可能多的字符。
    非贪婪匹配：是尝试匹配尽可能少的字符。
    
    贪婪格式：xx.*xx
    非贪婪格式：xx.*?xx
    区别重点在：.* 和 .*？
    
    
14、如何实现 “1,2,3” 变成 [‘1’,’2’,’3’] ?

    >>> "1,2,3".split(',')
    ['1', '2', '3']    
                       
    如何实现[‘1’,’2’,’3’]变成[1,2,3] ?
    >>> a=['1','2','3']
    >>> b=[int(i) for i in a]
    >>> b
    [1, 2, 3]
    >>> 
    

15、比较： a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 b = [(1,),(2,),(3,) ] 的区别 ?:

    >>> a = [1,2,3]
    >>> 
    >>> b = [(1),(2),(3)] 
    >>> 
    >>> c = [(1,),(2,),(3,)]  
    >>> 
    >>> a == b
    True
    >>>
    >>> b
    [1, 2, 3]
    >>> 
    >>> a is b
    False
    >>> 
    >>> a == c
    False
    >>>     

16、常用字符串格式化哪几种？：

    Python的字符串格式化常用的有三种：
    第一种：最方便的
    缺点：需一个个的格式化 
        print('hello %s and %s'%('df','another df'))
    
    第二种：最好用的
    优点：不需要一个个的格式化，可以利用字典的方式，缩短时间
        print('hello %(first)s and %(second)s'%{'first':'df' , 'second':'another df'})
    
    第三种：最先进的
    优点：可读性强
        print('hello {first} and {second}'.format(first='df',second='another df'))    


17、谈谈你对闭包的理解？：
    
    再说说闭包之前，先说一说什么是外函数，什么是内函数？
        
        外函数：函数A的内部定义了函数B，那么函数A就叫做外函数
        内函数：函数B就叫做内函数        

    什么是闭包？
    
        在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，
        并且外函数的返回值是内函数的引用。这样就构成了一个闭包。
        
    一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。
    但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
    就把这个临时变量绑定给了内部函数，然后自己再结束。   

        def outer(a):
            b = 10
            def inner():
                print(a+b)
            return inner
        
        if __name__ == '__main__':
            demo = outer(5)
            demo()
            demo2 = outer(7)
            demo2()


18、os和sys模块的作用：
    
    sys模块主要是用于提供对python解释器相关的操作:
    函数：
        
        sys.argv #命令行参数List，第一个元素是程序本身路径   
        sys.path #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
        sys.modules.keys() #返回所有已经导入的模块列表
        sys.exc_info() #获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
        sys.exit(n) #退出程序，正常退出时exit(0)
        sys.version #获取Python解释程序的版本信息
        sys.platform #返回操作系统平台名称
        sys.stdout #标准输出
        sys.stdin #标准输入
        
    常用功能:
    
        sys.arg 获取位置参数
        print(sys.argv)
        
        执行该脚本，加参数的打印结果
        python3 m_sys.py  1 2 3 4 5
        
        ['m_sys.py', '1', '2', '3', '4', '5']
        可以发现 sys.arg返回的是整个位置参数，类似于shell的$0 $1...
        sys.exit(n) 程序退出，n是退出是返回的对象
        sys.version 获取python版本
        >>> sys.version
        '3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) \n[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]'
        
        sys.path 返回模块的搜索路径列表,可通过添加自定义路径，来添加自定义模块
        >>> sys.path
        ['', '/Library/Frameworks/Python.framework/Versions/3.5/lib/python35.zip', 
        '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5', 
        '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin', 
        '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload', 
        '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages']
        
        sys.platform 返回当前系统平台 linux平台返回linux，windows平台返回win32，MAC返回darwin
        >>> sys.platform
        'darwin
        
        sys.stdout.write() 输出内容
        >>> sys.stdout.write('asd')
        asd3
        >>> sys.stdout.write('asd')
        asd3
        >>> sys.stdout.write('as')
        as2   

    
    os模块:
        
        OS模块是Python标准库中的一个用于访问操作系统功能的模块，
        使用OS模块中提供的接口，可以实现跨平台访问用于提供系统级别的操作.
        
        os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
        os.chdir(dirname) 改变当前脚本工作目录；相当于shell下cd
        os.curdir 返回当前目录: ('.')
        os.makedirs('dir1/dir2') 可生成多层递归目录
        os.removedirs('dirname1') 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
        os.mkdir('dirname') 生成单级目录；相当于shell中mkdir dirname
        os.rmdir('dirname') 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
        os.listdir('dirname') 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
        os.remove() 删除一个文件
        os.rename(oldname,new) 重命名文件/目录
        os.stat('path/filename') 获取文件/目录信息
        os.sep 操作系统特定的路径分隔符，win下为\,Linux下为/
        os.linesep 当前平台使用的行终止符，win下为\t\n,Linux下为\n
        os.pathsep 用于分割文件路径的字符串
        os.name 字符串指示当前使用平台。win->'nt'; Linux->'posix'
        os.system(bash command) 运行shell命令，直接显示
        os.environ 获取系统环境变量
        
        os.path.abspath(path) 返回path规范化的绝对路径
        os.path.split(path) 将path分割成目录和文件名二元组返回
        os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
        os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
        os.path.exists(path) 如果path存在，返回True；如果path不存在，返回False
        os.path.lexists  #路径存在则返回True,路径损坏也返回True
        os.path.isabs(path) 如果path是绝对路径，返回True
        os.path.isfile(path) 如果path是一个存在的文件，返回True。否则返回False
        os.path.isdir(path) 如果path是一个存在的目录，则返回True。否则返回False
        os.path.join(path1[, path2[, ...]]) 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
        os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间
        os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间
        os.path.commonprefix(list) #返回list(多个路径)中，所有path共有的最长的路径。
        os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
        os.path.expandvars(path)  #根据环境变量的值替换path中包含的”$name”和”${name}”
        
        os.access('pathfile',os.W_OK) 检验文件权限模式，输出True，False
        os.chmod('pathfile',os.W_OK) 改变文件权限模式


19、谈谈你对面向对象的理解？
    
    什么是封装？
        
        所谓的面向对象就是将我们的程序模块化，对象化，把具体事物的特性属性和通过这些属性来
        实现一些动作的具体方法放到一个类里面，这就是封装。
        封装是我们所说的面向对象编程的特征之一。    
          
    什么是继承？
    
        继承有点类似我们生物学上的遗传，就是子类的一些特征是来源于父类的，
        面向对象里的继承也就是父类的相关的属性，可以被子类重复使用，子类
        不必再自己的类里面重新定义一回，父类里面有的我们直接拿过来用就好了。
        而对于自己类里面需要用到的新的属性和方法，子类就可以自己来扩展了。
 
    什么是多态？     

        多态就是我们要把父类中定义的方法在子类里面重新实现一遍，多态包含了重载和重写。
        
    什么是重写？
        
        重写很简单就是把子类从父亲类里继承下来的方法重新写一遍，这样，父类里相同的方法就被覆盖了。
        
    什么是重载？
        
        重载就是类里面相同方法名，不同形参的情况，可以是形参类型不同或者形参个数不同，或者形参顺序不同，
        但是不能使返回值类型不同。
            
        












    













           

        