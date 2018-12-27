
"--------------------------------------------------------------------"

                本文档是学习 Fluent Python 的学习笔记

"--------------------------------------------------------------------"
                     
                     第一部分  序幕
    
    第一个部分只有单独一章，讲解 Python 的数据模型（data model）,以及
    如何为了保持一致性而使用的特殊方法，毕竟 Python 的一致性是出了名的。 
    其实整本书几乎都是在讲解 Python 的数据模型， 第 1 章算是一个概览。
    
                     
                     
                     第一章   Python 数据模型
    1、pythonic:
       
       我们通常所说的"Python 风格"（Pythonic）其背后代表这它的庞大的设计思想。
       这种设计思想完全体现在 Python 的数据模型上，而数据模型所描述的 API，
       为使用最地道的语言特性来构建自己的对象提供了工具。
    
    2、数据模型：
    
        数据模型其实就是对 Python 框架的描述，它规范了这们语言自身构建模块的接口，
        这些模块包括但不限于序列、迭代器、函数、类和上下文管理器。
    
    3、特殊方法（魔方方法，特殊方法的昵称）：
    
        不管在那种框架下写程序，都会花费大量时间去实现那些会被框架本身调用的方法，
        Python 也不例外，Python 解释器碰到特殊的语法时，会使用特殊方法去激活一些
        基本的对象操作，这些特殊方法的名字以两个下划线开头，以两个下划线结尾。（例如 __getitem__）
        比如 obj[key] 的背后就是__getitem__ 方法，为了能求得 my_collection[key] 的值，
        解释器实际上会调用 my_collection.__getitem__(key)。
        
        这些特殊方法名能让你自己的对象实现和支持一下的语言框架，并与之交互：
            迭代、集合类、属性访问、运算符重载、函数和方法的调用、对象的创建和销毁
            字符串表示形式和格式化、管理上下文（即 with 块）
    
    1.1、一摞 Python 风格的纸牌
    
        import collections
        Card = collections.namedtuple('Card',['rank', 'suit'])
        class FrenchDeck:
            ranks = [str(n) for n in range(2, 11)] + list('JQKA')
            suits = 'spades diamonds clubs hearts'.split()
            def __init__(self):
                self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
            def __len__(self):
                return len(self._cards)
            def __getitem__(self, position):
                return self._cards[position]
        
        # {'hearts': 2, 'clubs': 0, 'spades': 3, 'diamonds': 1}
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


        def spades_high(card):
            rank_value = FrenchDeck.ranks.index(card.rank)
            print("rank_value[%d]" % rank_value)
            return rank_value * len(suit_values) + suit_values[card.suit]
        
        if __name__ == "__main__":
        
            deck = FrenchDeck()
            # 1 一叠牌有多少张
            print(len(deck))
      
            # 2、3 随机抽取一张，python 内置了一个序列中随机挑出一个元素的函数 random.choice,
            print(choice(deck))
        
            # 4 可迭代
            for card in deck:
                print(card)
        
            # 反向迭代也没有关系
            for card in reversed(deck):
                print(card)
        
            # 5 in 操作
        
            print(Card('Q', 'hearts') in deck)
            print(Card('7', 'beasts') in deck)
            
            # 6 排序：
            for card in sorted(deck, key=spades_high):
                print(card)
  
    
            
        内置函数sorted 
         
            sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
             list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值。
             而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
             
             sorted 语法
             sorted(iterable[, cmp[, key[, reverse]]])
             参数说明：
                iterable -- 可迭代对象
                cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，
                       此函数必须遵守的规则为 大于则返回 1，小于则返回 -1，等于则返回 0
                key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的
                       参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
                reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
                
                >>>a = [5,7,6,3,4,1,2]
                >>> b = sorted(a) # 保留原列表
                >>> a
                   [5, 7, 6, 3, 4, 1, 2]
                >>> b
                   [1, 2, 3, 4, 5, 6, 7]
                >>> L=[('b',2),('a',1),('c',3),('d',4)]
                >>> sorted(L, cmp=lambda x,y:cmp(x[1],y[1])) # 利用cmp函数
                    [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
                >>> sorted(L, key=lambda x:x[1]) # 利用key
                     [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
                >>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
                >>> sorted(students, key=lambda s: s[2]) # 按年龄排序
                    [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
                >>> sorted(students, key=lambda s: s[2], reverse=True) # 按降序
                     [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
        
        内置函数 reversed   
        
            描述：reversed 函数返回一个反转的迭代器。
            语法：reversed(seq)
            
            参数：seq -- 要转换的序列，可以是 tuple, string, list 或 range
            返回值: 返回一个反转的迭代器。 
    
            # 字符串
            >>> seqString = 'Runoob'
            >>> print(list(reversed(seqString)))
            ['b', 'o', 'o', 'n', 'u', 'R']
            >>> print((reversed(seqString)))    
            <reversed object at 0x7fc0c94d33d0>
      
            # 元组
            >>> seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
            >>> print(list(reversed(seqTuple)))
            ['b', 'o', 'o', 'n', 'u', 'R']
            >>> 
            
            # range
            >>> seqRange = range(5, 9)
            >>> print(list(reversed(seqRange)))
            [8, 7, 6, 5]
            >>> 
            
            # 列表
            >>> seqList = [1, 2, 4, 3, 5]
            >>> print(list(reversed(seqList)))
            [5, 3, 4, 2, 1]
            
            # 字典
            >>> seqDict = dict(a = 1, b = 2, c = 3, d= 4)
            >>> seqDict
            {'a': 1, 'c': 3, 'b': 2, 'd': 4}
            >>> reversed(seqDict)
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: argument to reversed() must be a sequence
            
            >>> print(list(reversed(list[seqDict])))
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: 'type' object has no attribute '__getitem__'
        
        random 生成随机数：
            
            # 返回range(0,stop)之间的一个整数
            random.randrange(stop)	 
            
            # 返回range[start,stop)之间的一个整数，可加step，跟range(0,10,2)类似
            random.randrange(start, stop[, step])  
            
            # 返回range[a,b]之间的一个整数，等价于然的range(a,b+1)
            random.randint(a, b)
            
            # 从非空序列seq中随机选取一个元素。如果seq为空则弹出 IndexError异常。
            random.choice(seq)	
            
            # 3.6版本新增。从population集群中随机抽取K个元素（可重复）。
            # weights是相对权重列表，cum_weights是累计权重，两个参数不能同时存在。
            random.choices(population, weights=None, *, cum_weights=None, k=1)  
             
            # 从population样本或集合中随机抽取K个不重复的元素形成新的序列。
            random.sample(population, k)   
            
            # 返回一个介于左闭右开[0.0, 1.0)区间的浮点数
            random.random()                  
            
            # 返回一个介于a和b之间的浮点数。如果a>b，则是b到a之间的浮点数。这里的a和b都有可能出现在结果中。
            random.uniform(a, b)  
            
        collections 模块
        
            自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型
            分别是：
            
                OrderedDict类：排序字典，是字典的子类。引入自2.7。
                namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
                Counter类：为hashable对象计数，是字典的子类。引入自2.7。
                deque：双向队列。引入自2.4。
                defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。
    
    1.2  如何使用特殊方法:
    
        首先明确一点，特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它们。
        也就是说没有 my_object.__len__() 这种写法，而应该用 len(my_object)。 在执行
        len(my_object) 的时候，如果 my_object 是一个自定义类的对象，那么 python 会自己
        去调用其中由你实现的 __len__ 方法。
        
        然而如果是 Python 内置的类型，比如列表（list）、字符串（str）、字节序列（bytearray）等
        那么 CPython 会炒个近路， __len__ 实际上会直接返回 PyVarObject 里的 ob_size 属性。
        PyVarObject 是表示内存中长度可变的内置对象的 C 语言结构体。 直接读取这个值比调用一个方法
        要快很多。
        
        通常你的代码无需直接使用特殊方法。除非有大量的元编程存在，直接调用特殊方法的频率应该
        远远低于你去实现它们的次数。唯一例外的是 __init__() 方法。你的代码里可能经常用到它。
        目的是在你自己的子类的__init__() 方法中调用超类的构造器。
        
        通过内置函数（例如 len、iter、str 等等）来使用特殊方法是最好的选择，这些内置函数不仅仅
        会调用特殊方法，通常还提供额外的好处，而且对于内置的类来书，它们的速度更快。
        
        不要想当然的随便添加特殊方法，比如 __foo__ 之类，因为虽然现在这个名字没有被 python 内部使用
        以后就不一定了。
        
    1.2.1 模拟数值类型:
    
        利用特殊方法，可以让自定义对象通过加号 "+"（或者别的运算符）进行计算。
        
            from math import hypot

            class Vector(object):
            
                def __init__(self, x = 0, y = 0):
                    self.x = x
                    self.y = y
            
                def __repr__(self):
                    return 'Vector(%r, %r)' % (self.x, self.y)
            
                def __abs__(self):
                    return hypot(self.x, self.y)
            
            
                def __bool__(self):
                    return bool(abs(self))
            
                def __add__(self, other):
                    x = self.x + other.x
                    y = self.y + other.y
                    return Vector(x, y)
            
                def __mul__(self, scalar):
                    return Vector(self.x * scalar, self.y * scalar)
                    
            v1 = Vector(2, 4)
            v2 = Vector(2, 1)
            print(v1 + v2)
            print(abs(v2))
        
        math.hypot 函数：    
            
            hypot() 返回欧几里德范数 sqrt(x*x + y*y)。
                      
            >>> math.hypot(4, 3) 
            5.0
            >>> math.hypot(1, 1) 
            1.4142135623730951
            >>> 
            >>> 
            >>> math.hypot(2, 2) 
            2.8284271247461903
            
    1.2.2  字符串表示形式：
    
        Python 中有一个内置函数叫 repr, 它能把一个对象用字符串的形式表达出来以便辨认。
        这就是"字符串表还是形式"。 repr 就是通过 __repr__ 这个特殊方法来得到一个对象
        的字符串表示形式的。当我们在控制台里打印一个向量的实例时，得到的字符串可能会
        是<Vector object at 0x10e100070>
        
        在 __repr__ 的实现中，我们用到了 %r 来获取对象的各个属性的标准字符串表示形式
        --- 这是一个好习惯，它暗示了一个关键： Vector(1, 2) 和 Vector('1', '2')
        是不一样的。如下面的例子：
        
            class Test(object):
                def __init__(self, value):
                    self.data = value
            
            class TestRepr(Test):
                def __repr__(self):
                    return 'Value(%r)' % self.data
            
            class TestStr(Test):
                def __str__(self):
                    return '(Value(%s)' % self.data
            
            tr = TestRepr(1)
            print(tr)   # 返回结果 Value(1)
            
            tr1 = TestRepr('1')
            print(tr1)  # 返回结果 Value('1')
            
            ts = TestStr(1)
            print(ts)   # 返回结果 Value(1)
            ts1 = TestStr('1')
            print(ts1)  # 返回结果 Value(1)
        
         __repr__ 所返回的字符串应该准确、无歧义，并且尽可以表达出
         如何使用代码创建出整个被打印的对象。
         
         __repr__ 和 __str__ 的区别在于，后者是在 str() 函数中被使用。
         或者在用 print 函数打印一个对象时候才被调用，并且返回的字符串
         对终端用户更友好。
         如果一个对象没有 __str__ 函数，而python 又需要调用它的时候，解释器
         会用 __repr__ 作为替代。
    
    1.2.4 自定义的布尔值：
    
        尽管 Python 里有 bool 类型，但实际上任何对象都可以用于需要布尔值的上下文中
        （比如 if 或 while 语句，或者 and、or 或 not 运算），为了判断一个值 x 为真
        还是为假，Python 会调用 bool(x), 这个函数只能返回 True 或 False.
        bool(x) 的背后是调用x.__bool__() 的结果； 如果不存在 __bool__ 方法， 
        那么 bool(x) 会尝试调用 x.__len__()。 若返回 0， 则 bool 会返回 False； 
        否则返回True。
    
    1.3 特殊方法一览：
        
                类别                           方法名
        
        跟运算符无关的特殊方法:
        
        字符串/字节序列表示形式         __repr__、__str__、__format__、__bytes__
        
        数值转换      __abs__、__bool__、__complex__、__int__、__float__、__hash__、__index__
        
        集合模拟      __len__、__getitem__、__setitem__、__delitem__、__contains__
        
        迭代枚举      __iter__、__reversed__、__next__
        
        可调用模拟    __call__
        
        上下文管理    __enter__、__exit__
        
        实例创建与销毁 __new__ 、__init__、__del__
        
        属性管理     __getattr__、__getattribute__、__setattr__、__delattr__、__dir__
        
        属性描述符   __get__、__set__、__delete__
        
        跟类相关的服务 __prepare__、__instancecheck__、__subclasscheck__
        
        跟运算符相关的特殊方法:
        
          类别                    方法名和对应运算符
        
        一元运算符    __neg__ - 、  __pos__ +、__abs__ abs()
    
        比较运算符    __lt__ < 、__le__<=、__eq__ ==、__ne__ !=、__gt__ >、__ge__ >=
        
        算术运算符    __add__ +、__sub__ -、__mul__ *、__truediv__ /、__floordiv__ //、
                     __mod__ %、__divmod__ dovmod()、__pow__ **或 pow()、__round__ round()
                     
        反向算术运算符 __radd__、__rsub__、__rmul__、__rfloordiv__、__rmod__、__rdivmod__
        
        增量赋值算术运算符 __iadd__、__isub__、 __imul__、 __itruediv__、 __ifloordiv__、 __imod__、 __ipow__
        
        位运算符  __invert__ ~、 __lshift__ <<、__rshift__ >>、__and__ &、__or__ |、 __xor__ ^
        
        反向位运算符  __rlshift__、 __rrshift__、 __rand__、 __rxor__、 __ror__
    
    1.4 为什么 len 不是普通的方法：
    
        如果 x 是一个内置类型的实例， 那么 len(x) 的速度会非常快。 
        背后的原因是 CPython 会直接从一个 C 结构体里读取对象的长度， 
        完全不会调用任何方法。 获取一个集合中元素的数量是一个很常见的操作，
        在str、 list、 memoryview 等类型上， 这个操作必须高效。
        
        换句话说，len 之所以不是一个普通的方法，是为了让 python 自带的数据结构走后门abs 也是同理。
    
    1.5 本章小结：
    
        通过实现特殊方法，自定义数据类型可以表现的跟内置类型一样，从而让我们写出更具有表达力的代码
        --或者说，更具有 Python 风格的代码。
        
        Python 对象的一个基本要求就是它得有合理的字符串表示形式， 我们可
        以通过 __repr__ 和 __str__ 来满足这个要求。 前者方便我们调试和
        记录日志， 后者则是给终端用户看的。 这就是数据模型中存在特殊方法
        __repr__ 和 __str__ 的原因。    

                    
"---------------------------------------------------------------------"
                     
                     第二部分 数据结构
                     
    第二部分 包含各种集合类型: 序列(sequence)、映射(mapping)、集合(set)、字符串(str)、字节序列（bytes）
    
                     
                     第二章   序列构成的数组
                     
    你可能注意到了，之前提到的几个操作可以无差别的应用于文本、列表和表格上。我们把文本、
    列表和表格叫做数据火车...FOR 命令通常能作用于数据火车上。
    
    在创造 Python 以前， Guido 曾为 ABC 语言贡献过代码。 
    ABC 语言是一个致力于为初学者设计编程环境的长达 10 年的研究项目，
    其中很多点子在现在看来都很有 Python 风格：序列的泛型操作、 内置的元组和映射类型、
    用缩进来架构的源码、 无需变量声明的强类型， 等等。Python 对开发者如此友好， 根源就在这里。
    
    Python 也从 ABC 那里继承了用统一的风格去处理序列数据这一特点。
    不管是哪种数据结构， 字符串、 列表、 字节序列、 数组、 XML元素，
    抑或是数据库查询结果， 它们都共用一套丰富的操作： 迭代、 切片、 排
    序， 还有拼接。

"""2.1 内置序列类型概览 """

    Python 标准库用 C 实现了丰富的类型序列。
    
    容器序列： 
        list、 tuple 和 collections.deque 这些序列能存放不同类型的数据。
    
    扁平序列： 
        str、bytes、bytearray、memoryview 和 array.array 这类序列只能容纳一种类型。
    
    容器序列存放的是它们所包含的任意类型的对象的引用
    扁平序列存放的是是值而不是引用。换句话说。扁平序列其实是一段连续的内存空间。
    由此可见扁平序列其实更加紧凑，但是它里面只能存放诸如字符、字节和数值这种基础类型。
    
    序列的类型还能按照能否被修改来分类：
    
        可变序列：
        
            list、 bytearray、array.array、collections.deque 和 memoryview。
            
        不可变序列：
        
            tuple、str 和 bytes
            
"""2.2 列表推导和生成器表达式"""
    
    列表推导是构建列表(list) 的快捷方式，而生成器表达式则可以用来创建其他任何类型的序列。
    
    很多 python 程序员把列表推导 （list comprehension）简称为 listcomps,
    生成式表达器 （generator expression） 则称为 genexps。
    
    python 会忽略代码里 [] 、{} 和 () 中换行，因此如果你的代码里有很多行的列表、
    列表推导、生成器表达式、字典这一类的，可以省略不太好看的续行符 \。
    
    2.2.1 列表推导不会再有变量泄露的问题
    
        Python 2.x 中，在 列表推导中 for 关键词之后的赋值操作可能会影响列表推导
        上下文中的同名变量。下下面这个Python 2.7 控制台对话：
        
            Python 2.7.6 (default, Mar 22 2014, 22:59:38)
            [GCC 4.8.2] on linux2
            Type "help", "copyright", "credits" or "license" for more information.
            >>> x = 'my precious'
            >>> dummy = [x for x in 'ABC']
            >>> x
            'C'   
        
        如你所见， x 原本的值被取代了，但是这种情况在 python3 中是不会出现的。
        列表推导、生产器表达式，以及同他们很相似的集合（set）推导，字典(dict)推导。
        在python 3中都有了自己的局部作用域，就像函数似的。表达式内部的变量和赋值只在
        局部其作用，表达式的上下文里的同名变量还可以被正常引用，局部变量并不会影响到他们。
        
        这是python3 中代码：
        
            >>> x = 'ABC'
            >>> dummy = [ord(x) for x in x]
            >>> x
            'ABC'
            >>> dummy
            [65, 66, 67]
            >>> 
        
            x 的值被保留了
            列表推导也创建了正确的列表。
        
        列表推导可以帮助我们把一个序列或是其他可迭代类型中的元素过滤或
        是加工， 然后再新建一个列表。 Python 内置的 filter 和 map 函数组合
        起来也能达到这一效果， 但是可读性上打了不小的折扣。        
                   
    2.2.2 列表推导同 filter 和 map 的比较：
        
        filter 和 map 合起来能做的事情， 列表推导也可以做， 而且还不需要
        借助难以理解和阅读的 lambda 表达式。  
                
            >>> symbols = '$¢£¥€¤'
            >>> beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
            >>> beyond_ascii
            [162, 163, 165, 8364, 164]
            >>> beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
            >>> beyond_ascii
            [162, 163, 165, 8364, 164]        
        
    2.2.3 笛卡尔积：
    
        用列表推导可以生产两个或以上的可迭代类型的笛卡尔积。
        笛卡尔积是一个列表，列表里的元素是由输入的可迭代类型的元素对构成的元组。
        因此笛卡尔积列表的长度等于输入变量的长度的乘积。
        
            >>> colors = ['black', 'white']
            >>> sizes = ['S', 'M', 'L']
            >>> tshirts = [(color, size) for color in colors for size in sizes] (1)
            >>> tshirts
            [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
            ('white', 'M'), ('white', 'L')]
            >>> for color in colors: (2)
            ... for size in sizes:
            ... print((color, size))
            ...
            ('black', 'S')
            ('black', 'M')
            ('black', 'L')
            ('white', 'S')
            ('white', 'M')
            ('white', 'L')
            >>> tshirts = [(color, size) for size in sizes (3)
            ... for color in colors]
            >>> tshirts
            [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'),
            ('black', 'L'), ('white', 'L')]    
        
        (1) 这里得到的结果是先以颜色排序，再以尺码排序
        
        (2) 注意， 这里两个循环的嵌套关系和上面列表推导中 for 从句的先后顺序一样。
        
        (3) 如果想依照先尺码后颜色的顺序来排列， 只需要调整从句的顺序。
            我在这里插入了一个换行符， 这样顺序安排就更明显了。
        
        列表推导的作用只有一个： 生成列表。 如果想生成其他类型的序列， 生成器表达式就派上了用场。 
    
    
    2.2.4  生成器表达式:
        
        虽然也可以用列表推导来初始化元组、 数组或其他序列类型， 但是生成
        器表达式是更好的选择。 这是因为生成器表达式背后遵守了迭代器协
        议， 可以逐个地产出元素， 而不是先建立一个完整的列表， 然后再把这
        个列表传递到某个构造函数里。 前面那种方式显然能够节省内存。
        
        >>> symbols = '$¢£¥€¤'
        >>> tuple(ord(symbol) for symbol in symbols) (1)
        (36, 162, 163, 165, 8364, 164)
        >>> import array
        >>> array.array('I', (ord(symbol) for symbol in symbols)) (2) 
        array('I', [36, 162, 163, 165, 8364, 164])   
        
        (1) 如果生成器表达式是一个函数调用过程中的唯一参数， 
            那么不需要额外再用括号把它围起来。
        
        (2) array 的构造方法需要两个参数， 因此括号是必需的。 
            array 构造方法的第一个参数指定了数组中数字的存储方式。
    
    
"""2.3 元组不仅仅是不可变的列表"""   
    
    除了用作不可变的列表， 它还可以用于没有字段名的记录。         
    
    2.3.1 元组和记录:
    
        元组其实是对数据的记录：元组中的每个元素都存放了记录中一个字段的数据，
        外加这个字段的位置。这是这个位置信息给数据赋予了意义。
        
        如果只把元组理解为不可变的列表， 那其他信息——它所含有的元素的
        总数和它们的位置——似乎就变得可有可无。 但是如果把元组当作一些
        字段的集合， 那么数量和位置信息就变得非常重要了。

        示例 2-7 中的元组就被当作记录加以利用。 如果在任何的表达式里我们
        在元组内对元素排序， 这些元素所携带的信息就会丢失， 因为这些信息
        是跟它们的位置有关的。
        
        示例 2-7 把元组用作记录:
        
        
        
        
        


"---------------------------------------------------------------------"
    
                     第三章   字典和集合
    
"---------------------------------------------------------------------"

                     第四章   文本和字节序列    
"---------------------------------------------------------------------"

                     第三部分  把函数视作对象
                     
    第三部分 如何把函数最为一等对象（first-order object）来使用。
    第三部分首先会解释前面这句话是什么意思， 然后话题延伸到这个概念对那些被广
    泛使用的设计模型的影响， 最后读者会看到如何利用闭包（closure） 的
    概念来实现函数装饰器（function decorator）。 这一部分的话题还包括
    Python 的这些基本概念： 可调用（callable）、 函数属性（function
    attribute）、 内省（introspection）、 参数注解（parameter annotation）和
    Python 3 里新出现的 nonlocal 声明。

                     第五章   一等函数
    
"---------------------------------------------------------------------"

                     第六章   使用一等函数实现设计模式

"---------------------------------------------------------------------"

                     第七章   函数装饰器和闭包

"---------------------------------------------------------------------"

                     第四部分 面向对象惯用法
                     
    第四部分：重点转移到了类的构建上面，和任何面向对象语言一样， 
    Python 还有些自己的特性， 这些特性可能并不会出现在你我学习基于类的编程的语言中。
    这一部分的章节解释了引用（reference） 的原理、 “可变性”的概念、 实例的生命周期、
    如何构建自定义的集合类型和 ABC、 多重继承该怎么理顺、 什么时候
    应该使用操作符重载及其方法。
        

                     第八章   对象引用、可变性和垃圾回收 
"---------------------------------------------------------------------"

                     第九章   符合 python 风格的对象

"---------------------------------------------------------------------"

                     第十章   序列的修改、散列和切片

"---------------------------------------------------------------------"

                     第十一章  接口: 从协议到抽象基类

"---------------------------------------------------------------------"

                     第十二章  继承的优缺点
                     
"---------------------------------------------------------------------"

                     第十三章  正确重载运算符
                     
"---------------------------------------------------------------------"
                        
                        第五部分  控制流
    
    Python 中有些结构和库不再满足于诸如条件判断、循环和子程序（subroutine）之类的顺序控制流程，
    第五部分的笔墨会集中在这些构造和库上。我们会从生成器（generator）起步，
    然后话题会转移到上下文管理器（context manager） 和协程（coroutine） ， 
    其中会涵盖新增的功能强大但又不容易理解的 yield from 语法。 
    这一部分以并发性和面向事件的 I/O 来结尾， 其中跟并发性相关的是 collections.futures 这个
    很新的包，它借助 futures 包把线程和进程的概念给封装了起来； 
    而跟面向事件 I/O 相关的则是 asyncio，它的背后是基于协程和 yieldfrom 的 futures 包。   

                     第十四章  可迭代对象、迭代器和生成器

"---------------------------------------------------------------------"

                     第十五章  上下文管理器和 else 块
                     
"---------------------------------------------------------------------"
                     
                     第十六章   协程

"---------------------------------------------------------------------"

                     第十七章   使用期物处理并发
                     
"---------------------------------------------------------------------"

                     第十八章    使用 asynicio 包处理并发
                     
"---------------------------------------------------------------------"
                    
                     第六部分  元编程
    
    第六部分的开头会讲到如何动态创建带属性的类， 用以处理诸如
    JSON 这类半结构化的数据。 然后会从大家已经熟悉的特性（property）
    机制入手， 用描述符从底层来解释 Python 对象属性的存取。 同时， 函
    数、 方法和描述符的关系也会被梳理一遍。 第六部分会从头至尾地实现
    一个字段验证器， 在这个过程中我们会遇到一些微妙的问题， 然后在最
    后一章中就自然引出像类装饰器（class decorator） 和元类（metaclass）
    这些高级的概念。                     

    
                     第十九章   动态属性和特性

"---------------------------------------------------------------------"
                    
                    第二十章    属性描述符
    
"---------------------------------------------------------------------"

                    第二十一章   类元编程
                    
"---------------------------------------------------------------------"