
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
            
            >>> lax_coordinates = (33.9425, -118.408056) (1)
            >>> city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) (2)
            >>> traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')] (3)
            >>> for passport in sorted(traveler_ids): (4)
            ... print('%s/%s' % passport) (5)
            ...
            BRA/CE342567
            ESP/XDA205856
            USA/31195855
            >>> for country, _ in traveler_ids: (6)
            ... print(country)
            ...
            USA
            BRA
            ESP
        
        (1) 洛杉矶国际机场的经纬度。
        (2) 东京市的一些信息： 市名、 年份、 人口（单位： 百万） 、 人口变化
            （单位： 百分比） 和面积（单位： 平方千米） 。
        (3) 一个元组列表， 元组的形式为 (country_code,passport_number)。
        (4) 在迭代的过程中， passport 变量被绑定到每个元组上。
        (5) % 格式运算符能被匹配到对应的元组元素上。
        (6) for 循环可以分别提取元组里的元素， 也叫作拆包（unpacking） 。 因
            为元组中第二个元素对我们没有什么用， 所以它赋值给“_”占位符。
    
    2.3.2  元组拆包：
    
        元组 ('Tokyo', 2003, 32450, 0.66, 8014) 里
        的元素分别赋值给变量 city、 year、 pop、 chg 和 area， 而这所有的
        赋值我们只用一行声明就写完了。 同样， 在后面一行中， 一个 % 运算符
        就把 passport 元组里的元素对应到了 print 函数的格式字符串空档
        中。 这两个都是对元组拆包的应用。      
        
        元组拆包可以应用到任何可迭代对象上， 唯一的硬性要求是， 
        被可迭代对象中的元素数量必须要跟接受这些元素的元组的空档数一致。
        除非我们用 * 来表示忽略多余的元素， 在“用 * 来处理多余的元素”
        
        最好辨认的元组拆包形式就是平行赋值，也就是说把一个可迭代对象里的元素
        一并赋值到由对应的变量组成的元组中。
        就像下面代码：
            
            >>> lax_coordinates = (33.9425, -118.408056)
            >>> latitude, longitude = lax_coordinates # 元组拆包
            >>> latitude
            33.9425
            >>> longitude
            -118.408056
        
        另外一个很优雅的写法当属不使用中间变量交换两个变量的值：
            
            >>> b, a = a, b
        
        还可以用 * 运算符把一个可迭代对象拆开作为函数的参数：    
            
            内置函数divmod(a, b):
            
            本函数是实现a除以b，然后返回商与余数的元组。如果两个参数a,b都是整数，
            那么会采用整数除法，结果相当于（a//b, a % b)。如果a或b是浮点数，
            相当于（math.floor(a/b), a%b)。
                
            >>> divmod(20, 8)
            (2, 4)
            >>> t = (20, 8)
            >>> divmod(*t)
            (2, 4)
            >>> quotient, remainder = divmod(*t)
            >>> quotient, remainder
            (2, 4)
        
        这里元组拆包的用法则是让一个函数可以用元组的
        形式返回多个值， 然后调用函数的代码就能轻松地接受这些返回值。 比
        如 os.path.split() 函数就会返回以路径和最后一个文件名组成的元
        组 (path, last_part):   
            
            >>> import os
            >>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
            >>> filename
            'idrsa.pub'                       
        在进行拆包的时候， 我们不总是对元组里所有的数据都感兴趣， _ 占位
        符能帮助处理这种情况， 上面这段代码也展示了它的用法。   
        
        用*来处理剩下的元素
        在 Python 中， 函数用 *args 来获取不确定数量的参数算是一种经典写法了。
        于是 Python 3 里， 这个概念被扩展到了平行赋值中：
        
            >>> a, b, *rest = range(5)
            >>> a, b, rest
            (0, 1, [2, 3, 4])
            >>> a, b, *rest = range(3)
            >>> a, b, rest
            (0, 1, [2])
            >>> a, b, *rest = range(2)
            >>> a, b, rest
            (0, 1, [])  
            
    2.3.3 嵌套元组拆包：
    
        接受表达式的元组可以是嵌套式的，例如 (a, b, (c, d))
        只要这个接受元组的嵌套结构符合表达式本身的嵌套结构，Python
        就可以做出正确的应对。
        
        示例 2-8 用嵌套元组来获取经度
            
            metro_areas = [
                ('Tokyo','JP',36.933,(35.689722,139.691667)), #(1)
                ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
                ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
                ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
                ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
                ] p
                rint('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
                fmt = '{:15} | {:9.4f} | {:9.4f}'
                for name, cc, pop, (latitude, longitude) in metro_areas: # (2)
                if longitude <= 0: # (3)
                print(fmt.format(name, latitude, longitude))           
        
        (1) 每个元组内有 4 个元素， 其中最后一个元素是一对坐标。
        (2) 我们把输入元组的最后一个元素拆包到由变量构成的元组里， 这样就获取了坐标。
        (3) if longitude <= 0: 这个条件判断把输出限制在西半球的城市。
        
        示例 2-8 的输出是这样的：
            
                            |    lat.  | long.
            Mexico City     | 19.4333  | -99.1333
            New York-Newark | 40.8086  | -74.0204
            Sao Paul        | -23.5478 | -46.6358
        
        在 Python 3 之前， 元组可以作为形参放在函数声明中， 
        例如def fn(a, (b, c), d):。 然而 Python 3 不再支持这种格式 
        
        元组已经设计得很好用了， 但作为记录来用的话， 还是少了一个功能：
        我们时常会需要给记录中的字段命名。 namedtuple 函数的出现帮我们
        解决了这个问题。       
        
    2.3.4 具名元组    
    
        collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名
        的元组和一个有名字的类---这个带名字的类对调试程序由很大帮助。
        
        用 namedtuple 构建的类的实例所消耗的内存根元组是一样的，因为字段名
        都被存在对应的类里面。这个实例根普通的对象实例比起来也要小一些，因为
        Python 不会用 __dict__ 来存放这些实例的属性。
        
        from collections import namedtuple
        City = namedtuple('City', 'name country population coordinates') #(1)
        tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))  # (2)
        print(tokyo)
        print(tokyo.population)                                         #(3)
        print(tokyo[1])       
 
        输出：
        City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
        36.933
        JP
        
        (1) 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段名字。后者可以是
            由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
        (2) 存放的对应字段里的数据要以一串参数的形式传入到构造函数中
            (注意，元组的构造函数却只接受单一的可迭代对象)
        (3) 你可以通过字段名或者位置来获取一个字段的信息。
        
        
        除了从普通元组那里继承来的属性之外，具名元组还可以有一些自己专有的属性。
        几个常用的: _fields 类属性，类方法 _make(iterable) 和实例方法 _asdict()。
        
        示例 2-10 具名元组的属性和方法（接续前一个示例）
            
            >>> City._fields  #(1)
            ('name', 'country', 'population', 'coordinates')
            >>> LatLong = namedtuple('LatLong', 'lat long')
            >>> delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
            >>> delhi = City._make(delhi_data)  #(2)
            >>> delhi._asdict()  #(3)
            OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population',
            21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
            >>> for key, value in delhi._asdict().items():
            print(key + ':', value)
            name: Delhi NCR
            country: IN
            population: 21.935
            coordinates: LatLong(lat=28.613889, long=77.208889)  
        
        (1) _fields 属性是一个包含这个类所有字段名称的元组。
        (2) 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例， 它的作用跟 City(*delhi_data) 是一样的。
        (3) _asdict() 把具名元组以 collections.OrderedDict 的形式返回， 我们可以利用它来把元组里的信息友好地呈现出来。
     
        现在我们知道了， 元组是一种很强大的可以当作记录来用的数据类型。
        它的第二个角色则是充当一个不可变的列表。      
    
    2.3.5 作为不可变列表的元组:
        
        除了根增减元素相关的方法之外，元组支持列表的其他所有方法。还有一个例外，元组没有__reversed__方法，
        但这个方法只是一个优化而已，reversed(my_tuple) 这个用法在没有 __reversed__的情况下也是合法的。
        

"""2.4 切片"""
    
    在 python 里，像 list、tuple、str 这类序列类型都支持切片操作，但是实际上切片操作比人们想象的更强大。
    
    2.4.1 为什么切片和区间会忽略最后一个元素:
    
        在切片个区间操作里不包含区间范围的最后一个元素是 python 的风格， 这个习惯符号 Python、C
        和其他语言里以 0 作为其实下标的传统。这样做带来的好处如下：
        
            （1）当只有最后一个位置信息时，我们也可以快速看出切片和区间里有几个元素:
                range(3) 和 my_list[:3] 都返回三个元素
                
            （2）当起止位置信息都可见时，我们可以快速计算出切片和区间的长度，用最后一个数
                减去第一个下标 (stop - start)即可
            
            （3）这样做让们可以利用任意一个下标来把序列分割成不重叠的两个部分，只有写成
                my_list[:x] 和 my_list[x:] 就可以了。
            
                >>> l = [10, 20, 30, 40, 50, 60]
                >>> l[:2] # 在下标2的地方分割
                [10, 20]
                >>> l[2:]
                [30, 40, 50, 60]
            
                >>> l[:3] # 在下标3的地方分割
                [10, 20, 30]
                >>> l[3:]
                [40, 50, 60]  
    
    2.4.2 对对象进行切片:
        
        一个众所周知的密码，我们还可以用 s[a:b:c] 的形式对 s 在 a 和 b
        之间以 c 为间隔取值， c 的值还可以为负，负值意味着反向取值。
        
        a:b:c 这种用法只能作为索引或者下标用在 [] 中来返回一个切片对象：slice(a, b, c)。
        
        对seq[start:stop:step] 进行求值的时候， Python 会调用seq.__getitem__(slice(start, stop, step))。
        就算你还不会自定义序列类型， 了解一下切片对象也是有好处的。 
        例如你可以给切片命名， 就像电子表格软件里给单元格区域取名字一样。
    
    2.4.3 多维切片和省略:
    
        [] 运算符里还可以使用以逗号分开的多个索引或者是切片， 外部库
        NumPy 里就用到了这个特性， 二维的 numpy.ndarray 就可以用 a[i,j] 
        这种形式来获取， 抑或是用 a[m:n, k:l] 的方式来得到二维切片。  
        要正确处理这种 [] 运算符的话， 对象的特殊方法 __getitem__ 和 __setitem__ 
        需要以元组的形式来接收a[i, j] 中的索引。 也就是说， 
        如果要得到 a[i, j] 的值， Python 会调用 a.__getitem__((i, j))。
        
        Python 内置的序列类型都是一维的， 因此它们只支持单一的索引，
        成对出现的索引是没有用的。
    
    2.4.4 给切片赋值：
        
        如果把切片放在赋值语句的左边， 或把它作为 del 操作的对象， 我们就
        可以对序列进行嫁接、 切除或就地修改操作。 通过下面这几个例子， 你
        应该就能体会到这些操作的强大功能：
        
        >>> l = list(range(10))
        >>> l
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> l[2:5] = [20, 30]
        >>> l
        [0, 1, 20, 30, 5, 6, 7, 8, 9]
        >>> del l[5:7]
        >>> l
        [0, 1, 20, 30, 5, 8, 9]
        >>> l[3::2] = [11, 22]
        >>> l
        [0, 1, 20, 11, 5, 22, 9]
        >>> l[2:5] = 100 
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: can only assign an iterable
        2
        2>>> l[2:5] = [100]
        >>> l
        [0, 1, 100, 22, 9]        
    
        如果赋值的对象是一个切片， 那么赋值语句的右侧必须是个可迭代
        对象。 即便只有单独一个值， 也要把它转换成可迭代的序列。       
        
"""2.5 对序列使用 + 和 * """

    Python 程序员会默认序列是支持 + 和 * 操作的。 
    通常 + 号两侧的序列由相同类型的数据所构成， 
    在拼接的过程中，两个被操作的序列都不会被修改， 
    Python 会新建一个包含同样类型数据的序列来作为拼接的结果。               
        
    + 和 * 都遵循这个规律， 不修改原有的操作对象， 而是构建一个全新的序列。
    
    建立由列表组成的列表：
        
        示例 2-12 一个包含 3 个列表的列表， 嵌套的3个列表各自有3个元素来代表井字游戏的一行方块
        
            >>> board = [['_'] * 3 for i in range(3)]  #（1）
            >>> board
            [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            >>> board[1][2] = 'X'  #（2）
            >>> board
            [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']] 
            
            （1）建立一个包含 3 个列表的列表， 被包含的 3 个列表各自有 3 个元素。 打印出这个嵌套列表                   
            （2）把第 1 行第 2 列的元素标记为 X， 再打印出这个列表。
        
        示例 2-13 展示了另一个方法， 这个方法看上去是个诱人的捷径， 但实际上它是错的。
        示例 2-13  含有 3 个指向同一对象的引用的列表是毫无用处的
            
            >>> weird_board = [['_'] * 3] * 3  #（1）
            >>> weird_board
            [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            >>> weird_board[1][2] = 'O'   #（2）
            >>> weird_board
            [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
            
            （1）外面的列表其实包含 3 个指向同一个列表的引用。 当我们不做修改的时候， 看起来都还好。
            （2） 一旦我们试图标记第 1 行第 2 列的元素， 就立马暴露了列表内的 3个引用指向同一个对象的事实。
        
        示例 2-13 犯的错误本质上跟下面的代码犯的错误一样：
        
            row = ['_'] * 3
            board = []
            for i in range(3):
                board.append(row)  # (1)
            
            print(board) # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            board[1][1] = 3
            print(board) # [['_', 3, '_'], ['_', 3, '_'], ['_', 3, '_']]
             
            (1) 追加同一个行对象（row） 3 次到游戏板（board） 。
        
        相反， 示例 2-12 中的方法等同于这样做：
            
            >>> board = []
            >>> for i in range(3):
            ... row=['_'] * 3 # (1)
            ... board.append(row)
            ...
            >>> board
            [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
            >>> board[2][0] = 'X'
            >>> board # (2)
            [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]          
                
            (1) 每次迭代中都新建了一个列表， 作为新的一行（row） 追加到游戏板（board）.
            (2) 正如我们所期待的， 只有第 2 行的元素被修改。


"""2.6 序列的增量赋值"""    
    
        增量赋值运算符 += 和 *= 的表现取决于它们的第一个操作对象。简单起见，我们把讨论集中在增量加法
        （+=）上， 但这些概念对 *= 和其他增量运算符来说都是一样的。
        
        += 背后的特殊方法是 __iadd__ (用于"就地加法")。但是如果一个类没有是实现这个方法的话，Python
        会退一步调用 __add__。
        
        考虑下面这个简单表达式： >>> a += b
        
        如果 a 实现了 __iadd__ 方法，就会调用这个方法，同时对可变序列（如 list、bytearray、array.array）
        来说，a 就会就地改动，就像调用 a.extend(b) 一样。 但是如果 a 没有实现 __iadd__的话， a += b
        这个表达式的效果就变得跟 a = a + b 一样了。首先计算 a + b ,得到一个新的对象，然后赋值给 a。
        也就是在这个表达式中，变量名会不会被关联到新的对象， 完全取决于这个类型有没有实现__iadd__ 这个方法。
        
        上面所说的这些关于 += 的概念也适用于 *=， 不同的是， 后者相对应的是 __imul__。
        
        python2 中:
        
            >>> l = [1, 2, 3]
            >>> id(l)
            4311953800  # (1)
            >>> l *= 2
            >>> l
            [1, 2, 3, 1, 2, 3]
            >>> id(l)
            4311953800  # (2)
            >>> t = (1, 2, 3)
            >>> id(t)
            4312681568  # (3)
            >>> t *= 2
            >>> id(t)
            4301348296    
            
            (1) 刚开始的列表的 ID
            (2) 运用增量乘法后，列表的 ID 没有变， 新元素追加到列表上了。
            (3) 元组最开始的 ID
            (4) 运用增量乘法之后，新的元组被创建。
        
        对不可变序列进行重复拼接操作的话， 效率会很低， 因为每次都有一个
        新对象， 而解释器需要把原来对象中的元素先复制到新的对象里， 然后
        再追加新的元素。 
        
        
        一个关于 += 的谜题：
        
            >>> t = (1, 2, [30, 40])
            >>> t[2] += [50, 60]    
            到底会发生下面 4 种的情况中的哪一种？
            
            a. t 变成 (1, 2, [30, 40, 50, 60])。
            b. 因为 tuple 不支持对它的元素赋值，所以会抛出 TypeError 异常。
            c. 以上两个都不是。
            d. a 和 b 都不对。
        
            答案是：选项 d, t[2] 被改动了，但是也抛出异常出来。
            
            >>> t = (1,2,[20,30])
            >>> t[2] += [50,60]
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: 'tuple' object does not support item assignment
            >>> 
            >>> t
            (1, 2, [20, 30, 50, 60])  
            
            Python 为表达式 s[a] += b 生成的字节码， 可能这个现象背后的原因会变得清晰起来。
            示例 2-16 s[a] = b 背后的字节码
            
                >>> dis.dis('s[a] += b')
                1 0 LOAD_NAME 0(s)
                3 LOAD_NAME 1(a)
                6 DUP_TOP_TWO
                7 BINARY_SUBSCR #（1）
                8 LOAD_NAME 2(b)
                11 INPLACE_ADD  #（2）
                12 ROT_THREE
                13 STORE_SUBSCR #（3）
                14 LOAD_CONST 0(None)
                17 RETURN_VALU
                
            （1）将 s[a] 的值存入 TOS（Top Of Stack， 栈的顶端） 
            （2）计算 TOS += b。 这一步能够完成， 是因为 TOS 指向的是一个可变对象
            （3）s[a] = TOS 赋值。 这一步失败， 是因为 s 是不可变的元组
            
            这其实是个非常罕见的边界情况， 在 15 年的 Python 生涯中， 我还没见过谁在这个地方吃过亏。
            至此我得到了 3 个教训：
                
                (1) 不要把可变对象放在元组里面。
                (2) 增量赋值不是一个原子操作。 我们刚才也看到了， 它虽然抛出了异常， 但还是完成了操作。
                (3) 查看 Python 的字节码并不难， 而且它对我们了解代码背后的运行机制很有帮助。   
                
                
""" 2.7 list.sort 方法和 内置函数 sorted """

    list.sort 方法会就地排序列表，也就是说不会把原列表赋值一份。这也就是这个方法的返回值 None 的原因。
    本方法不会创建新的列表，在这种情况下，返回 None 其实是 Python 的一个惯例。    
    如果一个函数或者方法对对象进行的是就地改动， 那它就应该返回 None， 好让调用
    者知道传入的参数发生了变动， 而且并未产生新的对象。 例如， random.shuffle 函数也遵守了这个惯例。        
             
    用返回 None 来表示就地改动这个惯例有个弊端， 那就是调用者无法将其串联起来。 
    而返回一个新对象的方法（比如说 str 里的所有方法） 则正好相反， 它们可以串联起来调用， 
    从而形成连贯接口（fluent interface）。
    
    与 list.sort 相反的是内置函数 sorted， 它会新建一个列表作为返回值。 
    这个方法可以接受任何形式的可迭代对象作为参数， 甚至包括不可变序列或生成器。 
    而不管 sorted 接受的是怎样的参数， 它最后都会返回一个列表。
    
    不管是 list.sort 方法还是 sorted 函数， 都有两个可选的关键字参数。
    语法：sorted(iterable[, cmp[, key[, reverse]]])
        
        reverse: 
            如果被设定为 True, 被排序的元素里会降序输出。默认 False
        
        key: 
            一个只有一个参数的函数， 这个函数会被用在序列里的每一个元素上，
            所产生的结果将是排序算法依赖的对比关键字。 比如说， 
            在对一些字符串排序时， 可以用 key=str.lower 来实现忽略大小写的排序， 
            或者是用 key=len 进行基于字符串长度的排序。
            这个参数的默认值是恒等函数（identity function）， 
            也就是默认用元素自己的值来排序。
            
            可选参数 key 还可以在内置函数 min() 和 max() 中起作用。
            另外， 还有些标准库里的函数也接受这个参数， 
            像itertools.groupby() 和 heapq.nlargest() 等。
            
         
    下面通过几个小例子来看看这两个函数和它们的关键字参数：
    
        >>> fruits = ['grape', 'raspberry', 'apple', 'banana']
        >>> sorted(fruits)
        ['apple', 'banana', 'grape', 'raspberry'] ➊
        >>> fruits
        ['grape', 'raspberry', 'apple', 'banana'] ➋
        >>> sorted(fruits, reverse=True)
        ['raspberry', 'grape', 'banana', 'apple'] ➌
        >>> sorted(fruits, key=len)
        ['grape', 'apple', 'banana', 'raspberry'] ➍
        >>> sorted(fruits, key=len, reverse=True)
        ['raspberry', 'banana', 'grape', 'apple'] ➎
        >>> fruits
        ['grape', 'raspberry', 'apple', 'banana'] ➏
        >>> fruits.sort() ➐
        >>> fruits
        ['apple', 'banana', 'grape', 'raspberry'] ➑
    
        ❶ 新建了一个按照字母排序的字符串列表。
        ❷ 原列表并没有变化。
        ❸ 按照字母降序排序。
        ❹ 新建一个按照长度排序的字符串列表。 因为这个排序算法是稳定
            的， grape 和 apple 的长度都是 5， 它们的相对位置跟在原来的列表里是一样的。
        ❺ 按照长度降序排序的结果。 结果并不是上面那个结果的完全翻转，
          因为用到的排序算法是稳定的， 也就是说在长度一样时， grape 和 apple
          的相对位置不会改变。
        ❻ 直到这一步， 原列表 fruits 都没有任何变化。
        ❼ 对原列表就地排序， 返回值 None 会被控制台忽略。
        ❽ 此时 fruits 本身被排序。        
 
"""2.8 用 bisect 来管理已排序的序列 """

    bisect 模块包含两个主要的函数， bisect 和 insort。 两个函数都是用二分查找算法
    来在有序的序列中查找和插入元素。
    
    2.8.1 用 bisect 来搜索:
        
        bisect(haystack, needle) 在 haystack 里搜索 needle(针) 的位置。
        该位置满足的条件是， 把 needle 插入这个位置之后， haystack 还能保持升序。 
        也就是在说这个函数返回的位置前面的值， 都小于或等于 needle 的值。 
        其中 haystack 必须是一个有序的序列。 你可以先用 bisect(haystack, needle)查找位置index， 
        再用 haystack.insert(index, needle) 来插入新值。 但你也可用insort 来一步到位， 并且后者的速度更快一些。
             
        import bisect
        import sys
        HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
        NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
        ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
        def demo(bisect_fn):
        for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle) ➊
        offset = position * ' |' ➋print(ROW_FMT.format(needle, position, offset)) ➌
        if __name__ == '__main__':
        if sys.argv[-1] == 'left': ➍
        bisect_fn = bisect.bisect_left
        else:
        bisect_fn = bisect.bisect
        print('DEMO:', bisect_fn.__name__) ➎
        print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
        demo(bisect_fn)
        
        ❶ 用特定的 bisect 函数来计算元素应该出现的位置。
        ❷利用该位置来算出需要几个分隔符号。
        ❸ 把元素和其应该出现的位置打印出来。
        ❹ 根据命令上最后一个参数来选用 bisect 函数。
        ❺ 把选定的函数在抬头打印出来。



"""2.9 当列表不是首选时 """

    虽然列表既灵活又简单， 但面对各类需求时， 我们可能会有更好的选择。 
    比如， 要存放 1000 万个浮点数的话， 数组（array） 的效率要高得多， 
    因为数组在背后存的并不是 float 对象， 而是数字的机器翻译， 也就是字节表述。 
    这一点就跟 C 语言中的数组一样。 再比如说， 如果需要频繁对序列做先进先出的操作， 
    deque（双端队列） 的速度应该会更快。
    
    如果在你的代码里， 包含操作（比如检查一个元素是否出现在一个集合中） 的频率很高， 
    用 set（集合） 会更合适。 set 专为检查元素是否存在做过优化。 但是它并不是序列， 
    因为 set 是无序的。
    
    2.9.1 数组:
    
        如果我们需要一个只包含数字的列表， 那么 array.array 比 list 更高效。 
        数组支持所有跟可变序列有关的操作， 包括 .pop、 .insert 和.extend。 
        另外， 数组还提供从文件读取和存入文件的更快的方法， 如.frombytes 和 .tofile。
        
        Python 数组跟 C 语言数组一样精简。 创建数组需要一个类型码， 这个类
        型码用来表示在底层的 C 语言应该存放怎样的数据类型。 比如 b 类型码
        代表的是有符号的字符（signed char） ， 因此 array('b') 创建出的
        数组就只能存放一个字节大小的整数， 范围从 -128 到 127， 这样在序列
        很大的时候， 我们能节省很多空间。 而且 Python 不会允许你在数组里存
        放除指定类型之外的数据   
        
        示例 2-20 一个浮点型数组的创建、 存入文件和从文件读取的过程
    
            >>> from array import array ➊
            >>> from random import random
            >>> floats = array('d', (random() for i in range(10**7))) ➋
            >>> floats[-1] ➌
            0.07802343889111107
            >>> fp = open('floats.bin', 'wb')
            >>> floats.tofile(fp) ➍
            >>> fp.close()
            >>> floats2 = array('d') ➎
            >>> fp = open('floats.bin', 'rb')
            >>> floats2.fromfile(fp, 10**7) ➏
            >>> fp.close()
            >>> floats2[-1] ➐
            0.07802343889111107
            >>> floats2 == floats ➑
            True
            
            ❶ 引入 array 类型。
            ❷ 利用一个可迭代对象来建立一个双精度浮点数组(类型码是 'd')，这里我们用的可迭代对象是一个生成器表达式。
            ❸ 查看数组的最后一个元素。
            ❹ 把数组存入一个二进制文件里。
            ❺ 新建一个双精度浮点空数组。
            ❻ 把 1000 万个浮点数从二进制文件里读取出来。
            ❼ 查看新数组的最后一个元素。
            ❽ 检查两个数组的内容是不是完全一样。
    
        从上面的代码我们能得出结论， array.tofile 和 array.fromfile 用起来很简单。 
        把这段代码跑一跑， 你还会发现它的速度也很快。 一个小试验告诉我， 
        用 array.fromfile 从一个二进制文件里读出 1000 万个双精度浮点数只需要 0.1 秒，
        这比从文本文件里读取的速度要快 60倍， 因为后者会使用内置的 float 方法把每一行文字转换成浮点数。
        
        另外， 使用 array.tofile 写入到二进制文件， 比以每行一个浮点数的
        方式把所有数字写入到文本文件要快 7 倍。 另外， 1000 万个这样的数
        在二进制文件里只占用 80 000 000 个字节（每个浮点数占用 8 个字节，
        不需要任何额外空间） ， 如果是文本文件的话， 我们需要 181 515 739个字节。
    
        另外一个快速序列化数字类型的方法是使用pickle（https://docs.python.org/3/library/pickle.html） 
        模块。 pickle.dump 处理浮点数组的速度几乎跟 array.tofile 一样快。 
        不过前者可以处理几乎所有的内置数字类型， 包含复数、 嵌套集合， 甚至用户自定义的类。
        前提是这些类没有什么特别复杂的实现。 
        
        从 Python 3.4 开始， 数组类型不再支持诸如 list.sort() 这种就地排序方法。 
        要给数组排序的话， 得用 sorted 函数新建一个数组：
            a = array.array(a.typecode, sorted(a))   
        
    2.9.2 内存视图：
    
        memoryview 是一个内置类， 它能让用户在不复制内容的情况下操作同一个数组的不同切片。 
        memoryview 的概念受到了 NumPy 的启发。
        
        内存视图其实是泛化和去数学化的 NumPy 数组。 它让你在不需要
        复制内容的前提下， 在数据结构之间共享内存。 其中数据结构可以
        是任何形式， 比如 PIL图片、 SQLite 数据库和 NumPy 的数组， 等等。 
        这个功能在处理大型数据集合的时候非常重要。
                      
        memoryview.cast 的概念跟数组模块类似， 能用不同的方式读写同一块内存数据，
        而且内容字节不会随意移动。 这听上去又跟 C 语言中类型转换的概念差不多。 
        memoryview.cast 会把同一块内存里的内容打包成一个全新的 memoryview 对象给你 。
        
        示例 2-21 通过改变数组中的一个字节来更新数组里某个元素的值:
        
            >>> numbers = array.array('h', [-2, -1, 0, 1, 2])
            >>> memv = memoryview(numbers) ➊
            >>> len(memv)
            5>
            >> memv[0] ➋
            -2
            >>> memv_oct = memv.cast('B') ➌
            >>> memv_oct.tolist() ➍
            [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
            >>> memv_oct[5] = 4 ➎
            >>> numbers
            array('h', [-2, -1, 1024, 1, 2]) ➏    
            
            ❶ 利用含有 5 个短整型有符号整数的数组（类型码是 'h'） 创建一个memoryview。
            ❷ memv 里的 5 个元素跟数组里的没有区别。
            ❸ 创建一个 memv_oct， 这一次是把 memv 里的内容转换成 'B' 类型，也就是无符号字符。
            ❹ 以列表的形式查看 memv_oct 的内容。
            ❺ 把位于位置 5 的字节赋值成 4。
            ❻ 因为我们把占 2 个字节的整数的高位字节改成了 4， 所以这个有符号整数的值就变成了 1024。
            
    2.9.3 NuuPy 和 SciPy:
        
        如果利用数组来做高级的数字处理是你的日常工作， 那么 NumPy和 SciPy 应该是你的常用武器。
             
        凭借着 NumPy 和 SciPy 提供的高阶数组和矩阵操作， Python 成为科学计算应用的主流语言。
        NumPy 实现了多维同质数组（homogeneous array）和矩阵， 这些数据结构不但能处理数字， 
        还能存放其他由用户定义的记录。 通过 NumPy， 用户能对这些数据结构里的元素进行高效的操作。
        
        SciPy 是基于 NumPy 的另一个库， 它提供了很多跟科学计算有关的算法， 专为线性代数、 
        数值积分和统计学而设计。 SciPy 的高效和可靠性归功于其背后的 C 和 Fortran 代码， 
        而这些跟计算有关的部分都源自于Netlib 库（http://www.netlib.org） 。 
        换句话说， SciPy 把基于 C 和 Fortran的工业级数学计算功能用交互式且高度抽象的 Python 
        包装起来， 让科学家如鱼得水。
        
        示例 2-22 对 numpy.ndarray 的行和列进行基本操作:
        
                
    
                
        
        
       
 
 
 
 
        
     
          
                    
        
        
        
        
        
        
        
        
        
        
        


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