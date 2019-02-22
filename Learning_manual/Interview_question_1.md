
"""

    https://www.cnblogs.com/apollo1616/category/1285283.html
    
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

    >>> 1<(2==2)
    False
    >>> 
    >>> 1==(2==2)
    True
    >>> 
    >>> 1 < 2 == 2
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
    
31、
    
            
        
    







        