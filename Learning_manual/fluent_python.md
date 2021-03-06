
"----------------------------------------------------------------------------------------"

                本文档是学习 Fluent Python 的学习笔记

"----------------------------------------------------------------------------------------"
                     
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

                    
"-----------------------------------------------------------------------------------------"
                     
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
            
            >>> import numpy ➊
            >>> a = numpy.arange(12) ➋
            >>> a
            array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
            >>> type(a)
            <class 'numpy.ndarray'>
            >>> a.shape ➌
            (12,)
            >>> a.shape = 3, 4 ➍
            >>> a
            array([[ 0, 1, 2, 3],
            [ 4, 5, 6, 7],
            [ 8, 9, 10, 11]])
            >>> a[2] ➎
            array([ 8, 9, 10, 11])
            >>> a[2, 1] ➏
            9
            >>> a[:, 1] ➐
            array([1, 5, 9])
            >>> a.transpose() ➑
            array([ [ 0, 4, 8],
                    [ 1, 5, 9],
                    [ 2, 6, 10],
                    [ 3, 7, 11]])
             
            ❶ 安装 NumPy 之后， 导入它（NumPy 并不是 Python 标准库的一部分） 。
            ❷ 新建一个 0~11 的整数的 numpy.ndarry， 然后把它打印出来。
            ❸ 看看数组的维度， 它是一个一维的、 有 12 个元素的数组。
            ❹ 把数组变成二维的， 然后把它打印出来看看。
            ❺ 打印出第 2 行。
            ❻ 打印第 2 行第 1 列的元素。
            ❼ 把第 1 列打印出来。
            ❽ 把行和列交换， 就得到了一个新数组。
        
        
    2.9.4 双向队列和其他形式的队列：
        
        利用 .append 和 .pop 方法，我们可以把列表当作栈或者队列来用
        （比如，把 .append 和 .pop(0) 合起来用，就能模拟栈的“先进先出”的特点）。
         但是删除列表的第一个元素（抑或是在第一个元素之前添加一个元素）
        之类的操作是很耗时的， 因为这些操作会牵扯到移动列表里的所有元素。
        
        collections.deque 类（双向队列） 是一个线程安全、 可以快速从两
        端添加或者删除元素的数据类型。 而且如果想要有一种数据类型来存
        放“最近用到的几个元素”， deque 也是一个很好的选择。 这是因为在新
        建一个双向队列的时候， 你可以指定这个队列的大小， 如果这个队列满
        员了， 还可以从反向端删除过期的元素， 然后在尾端添加新的元素。
         
        示例 2-23 中有几个双向队列的典型操作。    
                    
            >>> from collections import deque
            >>> dq = deque(range(10), maxlen=10) ➊
            >>> dq
            deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
            >>> dq.rotate(3) ➋
            >>> dq
            deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
            >>> dq.rotate(-4)
            >>> dq
            deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
            >>> dq.appendleft(-1) ➌
            >>> dq
            deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
            >>> dq.extend([11, 22, 33]) ➍
            >>> dq
            deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
            >>> dq.extendleft([10, 20, 30, 40]) ➎
            >>> dq
            deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)    
            
            ❶ maxlen 是一个可选参数， 代表这个队列可以容纳的元素的数量， 而且一旦设定， 这个属性就不能修改了。
            ❷ 队列的旋转操作接受一个参数 n， 当 n > 0 时， 队列的最右边的 n
              个元素会被移动到队列的左边。 当 n < 0 时， 最左边的 n 个元素会被移动到右边。
            ❸ 当试图对一个已满（len(d) == d.maxlen） 的队列做尾部添加操作
                的时候， 它头部的元素会被删除掉。 注意在下一行里， 元素 0 被删除了。
            ❹ 在尾部添加 3 个元素的操作会挤掉 -1、 1 和 2。
            ❺ extendleft(iter) 方法会把迭代器里的元素逐个添加到双向队列的左边， 因此迭代器里的元素会逆序出现在队列里。     
        
        双向队列实现了大部分列表所拥有的方法， 也有一些额外的符合自身设
        计的方法， 比如说 popleft 和 rotate。 但是为了实现这些方法， 双向
        队列也付出了一些代价， 从队列中间删除元素的操作会慢一些， 因为它只对在头尾的操作进行了优化。
        
        append 和 popleft 都是原子操作， 也就说是 deque 可以在多线程程序
        中安全地当作先进先出的栈使用， 而使用者不需要担心资源锁的问题。
        
        除了 deque 之外， 还有些其他的 Python 标准库也有对队列的实现。
        
        queue:
        
           提供了同步（线程安全） 类 Queue、 LifoQueue 和PriorityQueue
           不同的线程可以利用这些数据类型来交换信息。 这三个类的构造方法都有一个可选参数 maxsize，
           它接收正整数作为输入值，用来限定队列的大小。但是在满员的时候，
           这些类不会扔掉旧的元素来腾出位置。 相反，如果队列满了，它就会被锁住，
           直到另外的线程移除了某个元素而腾出了位置。 这一特性让这些类很适合用来控制活跃线程的数量。 
        
        multiprocessing:
            
            这个包实现了自己的 Queue， 它跟 queue.Queue 类似， 是设计给进程间通信用的。 
            同时还有一个专门的multiprocessing.JoinableQueue 类型， 可以让任务管理变得更方便。
            
        asyncio
            
            Python 3.4 新提供的包， 里面有Queue、 LifoQueue、PriorityQueue和JoinableQueue，
            这些类受到 queue 和 multiprocessing 模块的影响， 但是为异步编程里的任务管理提供了专门的便利。
            
        heapq:
            
            跟上面三个模块不同的是， heapq 没有队列类， 而是提供了
            heappush 和 heappop 方法， 让用户可以把可变序列当作堆队列或者优先队列来使用。
            
"""2.10 本章小结"""

    要想写出准确、 高效和地道的 Python 代码， 对标准库里的序列类型的掌握是不可或缺的。
    
    Python 序列类型最常见的分类就是可变和不可变序列。 但另外一种分类方式也很有用， 
    那就是把它们分为扁平序列和容器序列。 前者的体积更小、 速度更快而且用起来更简单， 
    但是它只能保存一些原子性的数据，比如数字、 字符和字节。 容器序列则比较灵活， 
    但是当容器序列遇到可变对象时， 用户就需要格外小心了， 因为这种组合时常会搞出一些“意外”，
    特别是带嵌套的数据结构出现时， 用户要多费一些心思来保证代码的正确。
    
    列表推导和生成器表达式则提供了灵活构建和初始化序列的方式， 这两个工具都异常强大。
    如果你还不能熟练地使用它们， 可以专门花时间练习一下。 它们其实不难， 而且用起来让人上瘾。
    
    元组在 Python 里扮演了两个角色， 它既可以用作无名称的字段的记录，又可以看作不可变的列表。
    当元组被当作记录来用的时候， 拆包是最安全可靠地从元组里提取不同字段信息的方式。 
    新引入的 * 句法让元组拆包的便利性更上一层楼， 让用户可以选择性忽略不需要的字段。 
    具名元组也已经不是一个新概念了， 但它似乎没有受到应有的重视。
    就像普通元组一样， 具名元组的实例也很节省空间， 但它同时提供了方便地通过名字来获取元组各个字段信息的方式，
    另外还有个实用的 ._asdict()方法来把记录变成 OrderedDict 类型。
    Python 里最受欢迎的一个语言特性就是序列切片， 而且很多人其实还没完全了解它的强大之处。
    比如， 用户自定义的序列类型也可以选择支持NumPy 中的多维切片和省略（...） 。
    另外， 对切片赋值是一个修改可变序列的捷径。重复拼接 seq * n 在正确使用的前提下，
    能让我们方便地初始化含有不可变元素的多维列表。 增量赋值 += 和 *= 会区别对待可变和不可变序列。
    在遇到不可变序列时， 这两个操作会在背后生成新的序列。 但如果被赋值的对象是可变的， 
    那么这个序列会就地修改——然而这也取决于序列本身对特殊方法的实现。
    
    序列的 sort 方法和内置的 sorted 函数虽然很灵活， 但是用起来都不难。 
    这两个方法都比较灵活， 是因为它们都接受一个函数作为可选参数来指定排序算法如何比较大小， 
    这个参数就是 key 参数。 key 还可以被用在 min 和 max 函数里。 
    如果在插入新元素的同时还想保持有序序列的顺序， 那么需要用到 bisect.insort。 
    bisect.bisect 的作用则是快速查找。
    
    除了列表和元组， Python 标准库里还有 array.array。 
    另外， 虽然NumPy 和 SciPy 都不是 Python 标准库的一部分， 但稍微学习一下它们，
    会让你在处理大规模数值型数据时如有神助。
    
    本章末尾介绍了 collections.deque 这个类型， 它具有灵活多用和线
    程安全的特性。 表 2-3 将它和列表的 API 做了比较。 本章最后也提及了
    一些标准库中的其他队列类型的实现。        

"""2.11 延伸阅读"""           
     
     
     
"------------------------------------------------------------------------------------------"
    
                     第三章   字典和集合
 
    字典这个数据结构活跃在所有 Python 程序的背后，即便你的源码里并没有直接用到它。
    它是 Python 语言的基石。模块的命名空间、实例的属性和函数的关键字参数中都可以
    看到它的身影。跟它有关的内置函数在 __builtins__.__dict__ 模块中。
    
    字典的几种创建方式：
    
        def create_dict():
            # 1 创建空字典
            dict1 = {}
            print(dict1)
        
            # 2 直接赋值创建
            dict2 = {'spam':1, 'egg':2, 'bar':3}
            print(dict2)
        
            # 3 通过关键词 dict 和关键参数创建
            dict3 = dict(spam = 1, egg = 2, bar = 3)
            print(dict3)
        
            # 4 通过二元元组列表创建
            list = [('spam', 1), ('egg', 2), ('bar', 3)]
            dict4 = dict(list)
            # dict4 = dict([('spam',1),('egg',2),('bar',3)])
            print(dict4)
        
            # 5 dict和zip结合创建
            dict5 = dict(zip('abc',[1,2,3]))
            print(dict5)
        
            # 6 通过字典推导式创建
            dict6 = {i:2*i for i in range(3)}
            print(dict6)
        
            # 7 通过 dict.fromkeys() 创建
            dict7 = dict.fromkeys(range(3),'x')
            print(dict7)
        
            # 8 其他
            list = ['x',1,'y',2,'z',3]
            dict8 = dict(zip(list[::2], list[1::2]),)
            print(dict8)
        
    
    
    集合（set）的实现其实也依赖于散列表。
    
    本章大纲如下：
        
        常见的字典方法
        如何处理查找不到的键
        标准库中 dict 类型的变种
        set 和 frozenset 类型
        散列表的工作原理
        三列表带来的潜在影响（什么样的数据类型可作为键，不可预知的顺序，等等）
        
"""3.1 泛映射类型 """

    collections.abc 模块中有 Mapping 和 MutableMapping 这两个抽象的基类，它们的作用
    是为 dict 和其他类似的类型定义形式接口。
    
    类                父类              抽象方法                                                      方法
    Mapping	        Collection	__getitem__, __iter__, __len__	                            __contains__, keys, items, values, get, __eq__, and __ne__
    MutableMapping	Mapping	    __getitem__, __setitem__, __delitem__, __iter__, __len__	Inherited Mapping methods and pop, popitem, clear, update, and setdefault     
    
    标准库里所有的映射类型都是利用 dict 来实现的，因此它们有一个共同的限制，
    即只有可散列的数据类型才能用作这些映射里的键（只有键有这个要求，值并不需要可散列的数据类型）。
    
    什么是可散列的数据类型:
        如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值不变的，而且这个对象需要实现 __hash__()方法。
        另外可散列对象还有有 __qe__() 方法，这样才能跟其他键做比较。如果两个可散列的对象是相等的，那么它们的散列值
        一定是一样的。
    
    原子不可变数据类型，（str, bytes 和 数值类型） 都是可散列类型，frozenset 也是可散列的， 
    因为根据其定义， frozenset 里只能容纳可散列类型。 
    元组的话， 只有当一个元组包含的所有元素都是可散列类型的情况下， 它才是可散列的。 
    来看下面的元组tt、 tl 和 tf：
    
        >>> tt = (1, 2, (30, 40))
        >>> hash(tt)
        8027212646858338501
        >>> tl = (1, 2, [30, 40])
        >>> hash(tl)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: unhashable type: 'list'
        >>> tf = (1, 2, frozenset([30, 40]))
        >>> hash(tf)
        -4118419923444501110   
    
    注意：
        虽然元组本身是不可变序列， 它里面的元素可能是其他可变类型的引用。
        
        一般来讲用户自定义的类型的对象都是可散列的， 散列值就是它们
        的 id() 函数的返回值， 所以所有这些对象在比较的时候都是不相
        等的。 如果一个对象实现了 __eq__ 方法， 并且在方法中用到了这
        个对象的内部状态的话， 那么只有当所有这些内部状态都是不可变
        的情况下， 这个对象才是可散列的。
        
        
"""3.2 字典推导 """

    自 python 2.7 以来， 列表推导和生成器表达式的概念就移植到了字典上，从而有了字典推导。
    （后面还有集合推导）。
    字典推导（dictcomp）可以从任何以键值对作为元素的可迭代对象中构建出字典。
    
    示例 3.1 把一个装满元组的列表变成两个不同的字典。
    
        >>> DIAL_CODES = [ 
        ... (86, 'China'),
        ... (91, 'India'),
        ... (1, 'United States'),
        ... (62, 'Indonesia'),
        ... (55, 'Brazil'),
        ... (92, 'Pakistan'),
        ... (880, 'Bangladesh'),
        ... (234, 'Nigeria'),
        ... (7, 'Russia'),
        ... (81, 'Japan'),
        ... ]
        >>> country_code = {country: code for code, country in DIAL_CODES} 
        >>> country_code
        {'China': 86, 'India': 91, 'Bangladesh': 880, 'United States': 1,
        'Pakistan': 92, 'Japan': 81, 'Russia': 7, 'Brazil': 55, 'Nigeria':
        234, 'Indonesia': 62}
        >>>
        >>> {code: country.upper() for country, code in country_code.items() 
        ... if code < 66}
        {1: 'UNITED STATES', 55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA'}
        
"""3.3 常见的映射方法""" 

    映射类型的方法其实很丰富。 表 3-1 为我们展示了dict、 defaultdict 和 OrderedDict 的常见方法，
    后面两个数据类型是 dict 的变种， 位于 collections 模块内。
    
    用 setdefault 处理找不到的键:
        
        当字典 d[k] 不能找到正确的键的时候，Python 会抛异常，这个行为符合 Python 所信奉的"快速失败"哲学。
        每个 Python 程序员都知道可以用 d.get(k, default) 来代替 d[k], 给找不到的键一个默认的返回值
        （这样处理 KeyError 要方便不少。但是要更新某个键对应的值的时候， 不管使用 __getitem__ 还是 get 都会不自然，
        而且效率就像示例 3-2 中的还没有经过优化的代码所显示的那样，dict.get 并不是处理找不到的键的最好方法。
            
            """创建一个从单词到其出现情况的映射"""
            import sys
            import re
            WORD_RE = re.compile(r'\w+')
            index = {}
            with open(sys.argv[1], encoding='utf-8') as fp:
                for line_no, line in enumerate(fp, 1):
                    for match in WORD_RE.finditer(line):
                        word = match.group()
                        column_no = match.start()+1
                        location = (line_no, column_no)
                        # 这其实是一种很不好的实现， 这样写只是为了证明论点
                        occurrences = index.get(word, []) ➊
                        occurrences.append(location) ➋
                        index[word] = occurrences ➌
            
            # 以字母顺序打印出结果
            for word in sorted(index, key=str.upper): ➍
            print(word, index[word])      
            
            ❶ 提取 word 出现的情况， 如果还没有它的记录， 返回 []。
            ❷ 把单词新出现的位置添加到列表的后面。
            ❸ 把新的列表放回字典中， 这又牵扯到一次查询操作。  
            ❹ sorted 函数的 key= 参数没有调用 str.uppper， 而是把这个方法
              的引用传递给 sorted 函数， 这样在排序的时候， 单词会被规范成统一格式。
        
        示例 3-3，这里是示例 3-2 的不完全输出，每一行的列表都代表一个单词的出现情况，
        列表中的元素是一对值，第一个值表示出现的行，第二个值表示出现的列。
            
            $ python3 index0.py ../../data/zen.txt
            a [(19, 48), (20, 53)]
            Although [(11, 1), (16, 1), (18, 1)]
            ambiguity [(14, 16)]
            and [(15, 23)]
            are [(21, 12)]
            aren [(10, 15)]
            at [(16, 38)]
            bad [(19, 50)]
            be [(15, 14), (16, 27), (20, 50)]
            beats [(11, 23)]
            Beautiful [(3, 1)]
            better [(3, 14), (4, 13), (5, 11), (6, 12), (7, 9), (8, 11),
            (17, 8), (18, 25)]
    
        示例 3-4 index.py 用一行就解决了获取和更新单词的出现情况列表。
        
            """创建从一个单词到其出现情况的映射"""
            import sys
            import re
            WORD_RE = re.compile(r'\w+')
            index = {}
            with open(sys.argv[1], encoding='utf-8') as fp:
                for line_no, line in enumerate(fp, 1):
                    for match in WORD_RE.finditer(line):
                    word = match.group()
                    column_no = match.start()+1
                    location = (line_no, column_no)
                    index.setdefault(word, []).append(location) ➊    
            # 以字母顺序打印出结果
            for word in sorted(index, key=str.upper):
                print(word, index[word])    
        
            ➊ 获取单词的出现情况列表， 如果单词不存在， 把单词和一个空列表
              放进映射， 然后返回这个空列表， 这样就能在不进行第二次查找的情况下更新列表了。        
            
        也就是说， 这样写
            my_dict.setdefault(key, []).append(new_value)
        跟这样写：
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(new_value)            
        
     
"""3.4 映射的弹性键查询"""

    有时候为了方便起见， 就算某个键在映射里不存在， 我们也希望在通过
    这个键读取值的时候能得到一个默认值。 有两个途径能帮我们达到这个
    目的， 一个是通过 defaultdict 这个类型而不是普通的 dict， 另一个
    是给自己定义一个 dict 的子类， 然后在子类中实现 __missing__ 方
    法。 下面将介绍这两种方法。
    
    3.4.1 defaultfict: 处理找不到的键的一个选择：
         
        在用户创建 defaultdict 对象的时候， 就需要给它配置一个为找不到的键创造默认值的方法。
        
        具体而言， 在实例化一个 defaultdict 的时候， 需要给构造方法提供
        一个可调用对象， 这个可调用对象会在 __getitem__ 碰到找不到的键
        的时候被调用， 让 __getitem__ 返回某种默认值。       
    
    3.4.2 特殊方法 __missing__
        
        所有的映射类型在处理找不到的键的时候，都会牵扯到 __missing__ 方法。
        这也是这个方法称作“missing”的原因。 虽然基类 dict 并没有定
        义这个方法， 但是 dict 是知道有这么个东西存在的。 也就是说， 如果
        有一个类继承了 dict， 然后这个继承类提供了 __missing__ 方法， 那
        么在 __getitem__ 碰到找不到的键的时候， Python 就会自动调用它，
        而不是抛出一个 KeyError 异常。
        
        
"""3.5 字典的变种"""        
    
    collections.OrderedDict:
        
        这个类型在添加键的时候会保持顺序， 因此键的迭代次序总是一致的。
        OrderedDict 的 popitem 方法默认删除并返回的是字典里的最后
        一个元素， 但是如果像 my_odict.popitem(last=False) 这样调用它，
        那么它删除并返回第一个被添加进去的元素。
    
    collections.ChainMap:
        
        该类型可以容纳数个不同的映射对象， 然后在进行键查找操作的时
        候， 这些对象会被当作一个整体被逐个查找， 直到键被找到为止。 这个
        功能在给有嵌套作用域的语言做解释器的时候很有用， 可以用一个映射
        对象来代表一个作用域的上下文。 
    
    collections.Counter:
        
        这个映射类型会给键准备一个整数计数器。 每次更新一个键的时候
        都会增加这个计数器。 所以这个类型可以用来给可散列表对象计数， 或
        者是当成多重集来用——多重集合就是集合里的元素可以出现不止一
        次。 Counter 实现了 + 和 - 运算符用来合并记录， 还有像
        most_common([n]) 这类很有用的方法。    
    
    colllections.UserDict:
    
        这个类其实就是把标准 dict 用纯 Python 又实现了一遍。
        跟 OrderedDict、 ChainMap 和 Counter 这些开箱即用的类型不
        同， UserDict 是让用户继承写子类的。
    
"""3.6 子类化 UserDict """
    
    就创造自定义映射类型来说， 以 UserDict 为基类， 总比以普通的dict 为基类要来得方便。

"""3.7 不可变映射类型 """

    标准库里所有的映射类型都是可变的， 但有时候你会有这样的需求， 
    比如不能让用户错误地修改某个映射。                 
    
    从 Python 3.3 开始， types 模块中引入了一个封装类名叫
    MappingProxyType。 如果给这个类一个映射， 它会返回一个只读的映
    射视图。 虽然是个只读视图， 但是它是动态的。 这意味着如果对原映射
    做出了改动， 我们通过这个视图可以观察到， 但是无法通过这个视图对
    原映射做出修改。 
    
        >>> from types import MappingProxyType
        >>> d = {1:'A'}
        >>> d_proxy = MappingProxyType(d)
        >>> d_proxy
        mappingproxy({1: 'A'})
        >>> d_proxy[1] ➊
        'A'
        >>> d_proxy[2] = 'x' ➋
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: 'mappingproxy' object does not support item assignment
        >>> d[2] = 'B'
        >>> d_proxy ➌
        mappingproxy({1: 'A', 2: 'B'})
        >>> d_proxy[2]
        'B'
        >>>
        
        ➊ d 中的内容可以通过 d_proxy 看到。
        ➋ 但是通过 d_proxy 并不能做任何修改。
        ➌ d_proxy 是动态的， 也就是说对 d 所做的任何改动都会反馈到它上面。
        
        
"""3.8 集合论"""
    
    “集”这个概念在 Python 中算是比较年轻的， 同时它的使用率也比较
    低。 set 和它的不可变的姊妹类型 frozenset 直到 Python 2.3 才首次以
    模块的形式出现， 然后在 Python 2.6 中它们升级成为内置类型。
    
    集合的本质是许多唯一对象的聚集。
    集合中的元素必须是可散列的， set 类型本身是不可散列的， 
    但是frozenset 可以。 因此可以创建一个包含不同 frozenset 的 set。   
    
    除了保证唯一性， 集合还实现了很多基础的中缀运算符。 
    
    3.8.1 集合字面量：
    
        除空集之外， 集合的字面量——{1}、 {1, 2}， 等等——看起来跟它的
        数学形式一模一样。 如果是空集， 那么必须写成 set() 的形式。    
            
            python3 中
            >>> l = ['spam', 'spam', 'eggs', 'spam']
            >>> l
            ['spam', 'spam', 'eggs', 'spam']
            >>> 
            >>> set(l)
            {'eggs', 'spam'}
            >>> l
            ['spam', 'spam', 'eggs', 'spam']
            >>> ll = set(l)
            >>> ll
            {'eggs', 'spam'}
            >>> 
            >>> 
            >>> l = {'spam', 'spam', 'eggs'}
            >>> l
            {'eggs', 'spam'}
        
        注意：如果要创建一个空集，你必须用不带任何参数的构造方法 set(), 如果只是写成 {} 的形式。
        跟以前一样，你创建的其实是一个空字典。
        
        在Python3 里面，除了空集，集合的字符串表示形式总是以 {...} 的形式出现。
            >>> s = {1}
            >>> type(s)
            <class 'set'>
            >>> s
            {1}
            >>> s.pop()
            1>
            >> s
            set()
                 
        在 python 2 中，set() 是已这样的形式存在的：
        
            >>> l = {'aa','bb','cc','aa'}
            >>> l
            set(['aa', 'cc', 'bb'])
            >>> 
            >>> 
            >>> type(l)
            <type 'set'> 
        
        像 {1, 2, 3} 这种字面量句法相比于构造方法（set([1, 2, 3])） 要
        更快且更易读。 后者的速度要慢一些， 因为 Python 必须先从 set 这个
        名字来查询构造方法， 然后新建一个列表， 最后再把这个列表传入到构
        造方法里。 但是如果是像 {1, 2, 3} 这样的字面量， Python 会利用一
        个专门的叫作 BUILD_SET 的字节码来创建集合。
    
    3.8.2 集合推导：
    
         Python 2.7 带来了集合推导（setcomps） 和之前在 3.2 节里讲到过的字典推导。
         
            >>> {i for i in 'assdf'}  
            {'a', 'd', 'f', 's'}
            >>> 
            >>> from unicodedata import name
            >>> {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
            {'×', '<', '¤', 'µ', '#', '±', '£', '®', '§', '¢', '¥', '$', '%', '÷', '°', '+', '¶', '>', '=', '©', '¬'}
                         
         ➊ 从 unicodedata 模块里导入 name 函数， 用以获取字符的名字。
         ➋ 把编码在 32~255 之间的字符的名字里有“SIGN”单词的挑出来， 放到一个集合里。       
                
"""3.9 dict 和 set 的背后""" 
    
    3.9.2 字典中的散列表：
    
        散列表其实是一个稀疏数组（总是有空白元素的数组称为稀疏数组）。
        在一般的数据结构教材中， 散列表里的单元通常叫作表元（bucket） 。
        在 dict 的散列表当中， 每个键值对都占用一个表元， 每个表元都有两
        个部分， 一个是对键的引用， 另一个是对值的引用。 因为所有表元的大
        小一致， 所以可以通过偏移量来读取某个表元。
        
        因为 Python 会设法保证大概还有三分之一的表元是空的， 所以在快要达
        到这个阈值的时候， 原有的散列表会被复制到一个更大的空间里面。
        
        如果要把一个对象放入散列表，那么首先要计算这个元素键的散列值。
        Python 中可以用 hash() 方法来做这件事件。
        
        01. 散列值和相等性：
        
            内置的 hash() 方法可以用于所有的内置类型对象。如果两个对象在比较的时候相等，
            那么它们的散列值必须相等。否则散列表就不能正常运行了。
            例如，如果 1 == 1.0, 那么 hash(1) == hash(1.0) 也必须为真。
            但其实这两个数字（整型和浮点型）的内部结构时完全不一样的。
            
            为了让散列值能够胜任散列表索引这一角色， 它们必须在索引空间
            中尽量分散开来。 这意味着在最理想的状况下， 越是相似但不相等
            的对象， 它们散列值的差别应该越大。  
            注意其中 1 和 1.0 的散列值是相同的，而 1.0001、1.0002 和 1.0003 的散列值则非常不同。
            
            在32 位的Python中，1、 1.0001、 1.0002 和 1.0003这几个数的散列值的二进制表达对比。
            
                32-bit Python build
                1 00000000000000000000000000000001
                != 0
                1.0 00000000000000000000000000000001
                ------------------------------------------------
                1.0 00000000000000000000000000000001
                ! !!! ! !! ! ! ! ! !! !!! != 16
                1.0001 00101110101101010000101011011101
                ------------------------------------------------
                1.0001 00101110101101010000101011011101
                !!! !!!! !!!!! !!!!! !! ! != 20
                1.0002 01011101011010100001010110111001
                ------------------------------------------------
                1.0002 01011101011010100001010110111001
                ! ! ! !!! ! ! !! ! ! ! !!!! != 17
                1.0003 00001100000111110010000010010110
                ------------------------------------------------                
            
        02. 散列表算法：
        
            为了获取 my_dict[search_key] 背后的值， Python 首先会调用hash(search_key) 来计算 search_key 的散列值，
            把这个值最低的几位数字当作偏移量， 在散列表里查找表元（具体取几位， 得看当前散列表的大小）。 
            若找到的表元是空的， 则抛出 KeyError 异常。 若不是空的， 则表元里会有一对 found_key:found_value。
            这时候 Python 会检验 search_key == found_key 是否为真， 
            如果它们相等的话， 就会返回 found_value。
            
            如果 search_key 和 found_key 不匹配的话，这种情况称为散列冲突。
            发生这种情况是因为，散列表所做的其实是把随机的元素映射到只有几位的数字上，
            而散列表本身的索引又只依赖于这个数字的一部分。
            为了解决冲突，算法会在散列值中另外再取几位，然后用特殊的方法处理一下， 
            把新得到的数字再当作索引来寻找表元。 若这次找到的表元是空的， 则同样抛出 KeyError； 
            若非空， 或者键匹配， 则返回这个值； 或者又发现了散列冲突， 则重复以上的步骤。
            
            添加新元素和更新现有的键值的操作几乎跟上面一样，只不过对于前者，在发现空表元的时候
            放入一个新元素；对于后者，在找到相对于的表元后，原表里的值对象会被替换成新值。
            
            另外在插入新值时， Python 可能会按照散列表的拥挤程度来决定是
            否要重新分配内存为它扩容。 如果增加了散列表的大小， 那散列值
            所占的位数和用作索引的位数都会随之增加， 这样做的目的是为了减少发生散列冲突的概率。
            
    3.9.3  dict 的实现以及导致的结果：       
         
        01. 键必须是可散列的
            
            一个可散列的对象必须满足以下要求。
            (1) 支持 hash() 函数， 并且通过 __hash__() 方法所得到的散列值是不变的。
            (2) 支持通过 __eq__() 方法来检测相等性。
            (3) 若 a == b 为真， 则 hash(a) == hash(b) 也为真。    
            
            所有由用户自定义的对象默认都是可散列的， 因为它们的散列值由id() 来获取，而且它们都是不相等的。
            
        02. 字典在内存上的开销巨大
        
            由于字典使用了散列表， 而散列表又必须是稀疏的， 这导致它在空间上的效率低下。 
            用元组取代字典就能节省空间的原因有两个： 
                其一是避免了散列表所耗费的空间， 
                其二是无需把记录中字段的名字在每个元素里都存一遍。
        
        03. 键查询很快
            
            dict 的实现是典型的空间换时间： 字典类型有着巨大的内存开销， 
            但它们提供了无视数据量大小的快速访问——只要字典能被装在内存里。
            
        04. 键的次序取决于添加顺序
        
            当往 dict 里添加新键而又发生散列冲突的时候， 新键可能会被安排存放到另一个位置。
            
        05. 往字典里添加新键可能会改变已有键的顺序
            
            无论何时往字典里添加新的键， Python 解释器都可能做出为字典扩
            容的决定。 扩容导致的结果就是要新建一个更大的散列表， 并把字
            典里已有的元素添加到新表里。 这个过程中可能会发生新的散列冲
            突， 导致新散列表中键的次序变化。
          
        由此可知， 不要对字典同时进行迭代和修改。 如果想扫描并修改一个字典， 最好分成两步来进行： 
        首先对字典迭代， 以得出需要添加的内容， 把这些内容放在一个新字典里； 
        迭代结束之后再对原有字典进行更新。
        
    3.9.4 set 的实现以及导致的结果：
        
        set 和 frozenset 的实现也依赖散列表， 但在它们的散列表里存放的
        只有元素的引用（就像在字典里只存放键而没有相应的值） 。 在 set 加
        入到 Python 之前， 我们都是把字典加上无意义的值当作集合来用的。
        
        集合里的元素必须是可散列的。
        集合很消耗内存。
        可以很高效地判断元素是否存在于某个集合。元素的次序取决于被添加到集合里的次序。
        往集合里添加元素， 可能会改变集合里已有元素的次序。
                         
"""3.10 本章小结"""

    字典算得上是 Python 的基石。 除了基本的 dict 之外， 标准库还提供现
    成且好用的特殊映射类型， 比如
    defaultdict、 OrderedDict、 ChainMap 和 Counter。 这些映射类型
    都属于 collections 模块， 这个模块还提供了便于扩展的 UserDict类。
    
    大多数映射类型都提供了两个很强大的方法： setdefault 和update。 
    setdefault 方法可以用来更新字典里存放的可变值（比如列表） ， 从而避免了重复的键搜索。 
    update 方法则让批量更新成为可能， 它可以用来插入新值或者更新已有键值对， 
    它的参数可以是包含(key, value) 这种键值对的可迭代对象， 或者关键字参数。 
    
    映射类型的构造方法也会利用 update 方法来让用户可以使用别的映射对象、
    可迭代对象或者关键字参数来创建新对象。
    在映射类型的 API 中， 有个很好用的方法是 __missing__， 当对象找
    不到某个键的时候， 可以通过这个方法自定义会发生什么。
    
    collections.abc 模块提供了 Mapping 和 MutableMapping 这两个抽
    象基类， 利用它们， 我们可以进行类型查询或者引用。 不太为人所知的
    MappingProxyType 可以用来创建不可变映射对象， 它被封装在 types
    模块中。 另外还有 Set 和 MutableSet 这两个抽象基类。
   
    dict 和 set 背后的散列表效率很高， 对它的了解越深入， 就越能理解
    为什么被保存的元素会呈现出不同的顺序， 以及已有的元素顺序会发生
    变化的原因。 同时， 速度是以牺牲空间为代价而换来的。
                                

"------------------------------------------------------------------------------------------"

                     第四章   文本和字节序列    
    人人使用文本，计算机使用字节序列。           
    
    Python 3 明确区分了人类可读的文本字符串和原始的字节序列。
    隐式地把字节序列转换成 Unicode 文本已成过去。
    本章将要讨论 Unicode 字符串、 二进制序列， 以及在二者之间转换时使用的编码。

    ASCII，Unicode 和 UTF-8:
    
    1、ASCII:
        我们知道，计算机内部，所有信息都是一个二进制。每一个二进制(bit)有 0 和 1 两种状态，
        因此八个二进制位就可以组合出256种状态，这被称为一个字节（byte），也就是说，一个字节
        一共可以用来表示256中不同的状态，每一个状态对应一个符号，就是 256 个符号，从00000000到1111111。
       
       上个世纪60年代，美国定制了一套字符编码，对英语字符和二进制之间的关系，做了统一的规定，这被称为 ASCII码
       一直沿用至今。
       
       ASCII 码一共规定了 128 字符的字符编码，比如空格 SPACE 是32(二进制00100000)，大写的字母A是65（二进制01000001）。
       这128个符号（包括32个不能打印出来的控制符号），只占用了一个字节的后面7位，最前面的一位统一规定为0。
    
    2、非 ASCII 编码：
    
        英语用128个符号编码就够了，但是用来表示其他语言，128个符号是不够的。
        比如，在法语中，字母上方有注音符号，它就无法用 ASCII 码表示。
        于是，一些欧洲国家就决定，利用字节中闲置的最高位编入新的符号。
        比如，法语中的é的编码为130（二进制10000010）。这样一来，这些欧洲国家使用的编码体系，可以表示最多256个符号。
   
        但是，这里又出现了新的问题。不同的国家有不同的字母，因此，哪怕它们都使用256个符号的编码方式，
        代表的字母却不一样。比如，130在法语编码中代表了é，在希伯来语编码中却代表了字母Gimel (ג)，
        在俄语编码中又会代表另一个符号。但是不管怎样，所有这些编码方式中，0--127表示的符号是一样的，
        不一样的只是128--255的这一段。
        
        至于亚洲国家的文字，使用的符号就更多了，汉字就多达10万左右。一个字节只能表示256种符号，
        肯定是不够的，就必须使用多个字节表达一个符号。
        比如，简体中文常见的编码方式是 GB2312，使用两个字节表示一个汉字，所以理论上最多可以表示 256 x 256 = 65536 个符号。
        虽然都是用多个字节表示一个符号，但是GB类的汉字编码与后文的 Unicode 和 UTF-8 是毫无关系的。             
    
    3、Unicode:
        
        世界上存在着多种编码方式，同一个二进制数字可以被解释成不同的符号。
        因此，要想打开一个文本文件，就必须知道它的编码方式，否则用错误的编码方式解读，就会出现乱码。
        为什么电子邮件常常出现乱码？就是因为发信人和收信人使用的编码方式不一样。 
        
        可以想象，如果有一种编码，将世界上所有的符号都纳入其中。每一个符号都给予一个独一无二的编码，那么乱码问题就会消失。
        这就是 Unicode，就像它的名字都表示的，这是一种所有符号的编码。
        
        Unicode 当然是一个很大的集合，现在的规模可以容纳100多万个符号。
        每个符号的编码都不一样，比如，U+0639表示阿拉伯字母Ain，U+0041表示英语的大写字母A，
        U+4E25表示汉字严。具体的符号对应表，可以查询unicode.org，或者专门的汉字对应表。
    
    4、 Unicode 的问题：
    
        需要注意的是，Unicode 只是一个符号集，它只规定了符号的二进制代码，却没有规定这个二进制代码应该如何存储。
        比如，汉字严的 Unicode 是十六进制数4E25，转换成二进制数足足有15位（100111000100101），也就是说，
        这个符号的表示至少需要2个字节。表示其他更大的符号，可能需要3个字节或者4个字节，甚至更多。
        这里就有两个严重的问题，第一个问题是，如何才能区别 Unicode 和 ASCII? 计算机怎么知道三个字节表示三个字符
        而不是分别表示一个符号呢？第二个问题是，我们已经知道，英文字母只用一个字节表示就够了，
        如果 Unicode 统一规定，每个符号用三个或四个字节表示，那么每个英文字母前都必然有二到三个字节是0，
        这对于存储来说是极大的浪费，文本文件的大小会因此大出二三倍，这是无法接受的。
        
        它们造成的结果是：1）出现了 Unicode 的多种存储方式，也就是说有许多种不同的二进制格式，可以用来表示 Unicode。
                        2）Unicode 在很长一段时间内无法推广，直到互联网的出现。
    
    5、UTF-8:
        
        互联网的普及，强烈要求出现一种统一的编码方式。UTF-8 就是在互联网上使用最广的一种 Unicode 的实现方式。
        其他实现方式还包括 UTF-16（字符用两个字节或四个字节表示）和 UTF-32（字符用四个字节表示），不过在互联网上基本不用。
        重复一遍，这里的关系是，UTF-8 是 Unicode 的实现方式之一。    
        UTF-8 最大的一个特点，就是它是一种变长的编码方式。它可以使用1~4个字节表示一个符号，根据不同的符号而变化字节长度。
        
        UTF-8 的编码规则很简单，只有二条：
            （1）对于单字节的符号，字节的第一位设为0，后面7位为这个符号的 Unicode 码。
                因此对于英语字母，UTF-8 编码和 ASCII 码是相同的。
            
            （2）对于 n 字节符号（n > 1）,第一个字节的前n位都设置为 1， 第 n + 1 位设为 0，后面字节的前两位一律设置为10.
                剩下的没有提及的二进制位，全部为这个符号的 Unicode 码。
            
            下表总结了编码规则，字母x表示可用编码的位。   
                
                Unicode符号范围     |        UTF-8编码方式
                (十六进制)          |              （二进制）
                ----------------------+---------------------------------------------
                0000 0000-0000 007F | 0xxxxxxx
                0000 0080-0000 07FF | 110xxxxx 10xxxxxx
                0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
                0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx   
            
        跟据上表，解读 UTF-8 编码非常简单。
        如果一个字节的第一位是0，则这个字节单独就是一个字符；
        如果第一位是1，则连续有多少个1，就表示当前字符占用多少个字节。
            
        下面，还是以汉字严为例，演示如何实现 UTF-8 编码。        
        严的 Unicode 是4E25（100111000100101），根据上表，可以发现4E25处在第三行的范围内（0000 0800 - 0000 FFFF），
        因此严的 UTF-8 编码需要三个字节，即格式是1110xxxx 10xxxxxx 10xxxxxx。
        然后，从严的最后一个二进制位开始，依次从后向前填入格式中的x，多出的位补0。
        这样就得到了，严的 UTF-8 编码是11100100 10111000 10100101，转换成十六进制就是E4B8A5。            
    
    6、Unicode 与 UTF-8 之间的转换:
        
        通过上一节的例子，可以看到 "严" 的Unicode 码是 4E25, UTF-8 编码是 E4B8A5,是不要的，它们之间的转换可以通过程序实现。
                
  
         
"""4.1 字符问题"""

    "字符串"是个相当简单的概念：一个字符串是一个字符序列。问题出在"字符"的定义上。
    在 2015 年，“字符”的最佳定义是 Unicode 字符。 因此， 从 Python 3 的
    str 对象中获取的元素是 Unicode 字符， 这相当于从 Python 2 的
    unicode 对象中获取的元素， 而不是从 Python 2 的 str 对象中获取的原始字节序列。
    
    Unicode 标准把字符的标识和具体的字节表述进行了如下的明确的区分：
        （1）字符的标识，即码位，是 0 ~ 1114111 的数字（十进制），在 Unicode 标准中的
            以 4 ~ 6 个十六进制数字表示，而且加前缀 "U+" 例如,字母 A 的码位是 U+0041,
            欧元符号的码位是 U+20AC。
        
        （2）字符的具体表述取决于所用的编码。
             编码是在码位和字节序列之间转换时使用的算法。
             在UTF-8编码中，A（U+0041）的码位编码成单个字节\x41，而在UTF-16LE编码中编码成两个字节\x41\x00。                    
                     
    把码位转换成字节序列的过程就是编码；把字节序列转换成码位的过程是解码。
        
        >>> s = 'café'
        >>> len(s) # ➊
        4
        >> b = s.encode('utf8') # ➋
        >>> b
        b'caf\xc3\xa9' # ➌
        >>> len(b) # ➍
        5
        >> b.decode('utf8') # ➎
        'café'
                     
        ❶ 'café' 字符串有 4 个 Unicode 字符。
        ❷ 使用 UTF-8 把 str 对象编码成 bytes 对象。
        ❸ bytes 字面量以 b 开头。
        ❹ 字节序列 b 有 5 个字节（在 UTF-8 中， “é”的码位编码成两个字节）。
        ❺ 使用 UTF-8 把 bytes 对象解码成 str 对象。             
                     
    如果想帮助自己记住 .decode() 和 .encode() 的区别， 可
    以把字节序列想成晦涩难懂的机器磁芯转储， 把 Unicode 字符串想
    成“人类可读”的文本。 那么， 把字节序列变成人类可读的文本字符
    串就是解码， 而把字符串变成用于存储或传输的字节序列就是编码。                 

"""4.2 字节概要 """

    Python 的字符串类型:
    
        python2.x:
            
            str： 表示8位文本和二进制数据。
            Unicode： 用来表示宽字符Unicode文本。
            
        python3.x:
            
            str: 表示 Unicode 文本（8位或更宽的）。
            bytes: 二进制数据。
            bytearray: 是一个种可变的 bytes 类型。
            

    Python 内置了两种基本的二进制序列类型：
        python3 引入的不可变 bytes 类型
        python2.6 添加的可变 bytearray 类型
       （python 2.6 也引入了 bytes类型，但是那只不过是 str 类型的别名，与python3 的bytes类型不同）
        
        bytes 或 bytearray 对象的各个元素是介于 0~255（含）之间的整数，而不像 Python 2 的 str 对象那样是单个的字符。
        然而， 二进制序列的切片始终是同一类型的二进制序列，包括长度为 1 的切片。
        
        示例 4-2 包含 5 个字节的 bytes 和 bytearray 对象
        
            python2 中：
            >>> cafe = bytes('café', encoding='utf-8')
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: str() takes at most 1 argument (2 given)
            
            python3 中：
            
            >>> cafe = bytes('café', encoding='utf_8') ➊
            >>> cafe
            b'caf\xc3\xa9'
            >>> cafe[0] ➋
            99
            >>> cafe[:1] ➌
            b'c'
            >>> cafe_arr = bytearray(cafe)
            >>> cafe_arr ➍
            bytearray(b'caf\xc3\xa9')
            >>> cafe_arr[-1:] ➎
            bytearray(b'\xa9')    
        
            ❶ bytes 对象可以从 str 对象使用给定的编码构建。
            ❷ 各个元素是 range(256) 内的整数。
            ❸ bytes 对象的切片还是 bytes 对象， 即使是只有一个字节的切片。
            ❹ bytearray 对象没有字面量句法， 而是以 bytearray() 和字节序列字面量参数的形式显示。
            ❺ bytearray 对象的切片还是 bytearray 对象。
        
        my_bytes[0] 获取的是一个整数， 而 my_bytes[:1] 返回的
        是一个长度为 1 的 bytes 对象——这一点应该不会让人意外。 
        s[0] == s[:1] 只对 str 这个序列类型成立。 不过， str 类型的这个行为十分罕见。 
        对其他各个序列类型来说， s[i] 返回一个元素， 而 s[i:i+1] 返回一个相同类型的序列，里面是 s[i] 元素。
        
        虽然二进制序列其实是整数序列，但是它们的字面量表示法表明其中有 ASCII 文本。因此，各个字节的值
        可能会使用下列三种不同的方式显示：
            1、可打印的 ASCII 范围内的字节（从空格到 ~） ， 使用 ASCII 字符本身。
            2、制表符、 换行符、 回车符和 \ 对应的字节， 使用转义序列\t、 \n、 \r 和 \\。
            3、其他字节的值， 使用十六进制转义序列（例如， \x00 是空字节）。
        
        因此， 在示例 4-2 中， 我们看到的是 b'caf\xc3\xa9'： 
        前 3 个字节b'caf' 在可打印的 ASCII 范围内， 后两个字节则不然。   
            
"""4.3 基本的编解码器"""
    
    Python 自带了超过 100 种编解码器（codec, encoder/decoder） ， 用于在
    文本和字节之间相互转换。 每个编解码器都有一个名称， 如 'utf_8'，
    而且经常有几个别名， 如 'utf8'、 'utf-8' 和 'U8'。 这些名称可以传
    给 open()、 str.encode()、 bytes.decode() 等函数的 encoding 参数。
    
     
"""4.4 了解编解码问题"""

    虽然有个一般性的 UnicodeError 异常， 但是报告错误时几乎都会指明
    具体的异常： UnicodeEncodeError（把字符串转换成二进制序列时）
    或 UnicodeDecodeError（把二进制序列转换成字符串时） 。 如果源码
    的编码与预期不符， 加载 Python 模块时还可能抛出 SyntaxError。                       
    
    4.4.1 处理 UnicodeEncodeError:
        
        多数非 UTF 编解码器只能处理 Unicode 字符的一小部分子集。 把文本转
        换成字节序列时， 如果目标编码中没有定义某个字符， 那就会抛出
        UnicodeEncodeError 异常， 除非把 errors 参数传给编码方法或函数，对错误进行特殊处理。
    
    4.4.2 处理UnicodeDecodeError:
    
        不是每一个字节都包含有效的 ASCII 字符， 也不是每一个字符序列都是
        有效的 UTF-8 或 UTF-16。 因此， 把二进制序列转换成文本时， 如果假
        设是这两个编码中的一个， 遇到无法转换的字节序列时会抛出
        UnicodeDecodeError     
                    
    4.4.3 使用预期之外的编码加载模块时抛出的 SyntaxError:
    
        Python3 默认使用 UTF-8 编码源码， Python2(2.5开始)则默认使用ASCII。
        如果加载的 .py 模块中包含 UTF-8 之外的数据， 而且没有声明编码，会得到类似下面的消息：
            SyntaxError: Non-UTF-8 code starting with '\xe1' in file ola.py on line
            1, but no encoding declared; see http://python.org/dev/peps/pep-0263/for details。
            
    4.4.4  如何找出字节序列的编码： 
    
        如何找出字节序列的编码？ 简单来说， 不能。 必须有人告诉你。
        
        有些通信协议和文件格式， 如 HTTP 和 XML， 包含明确指明内容编码
        的首部。 可以肯定的是， 某些字节流不是 ASCII， 因为其中包含大于
        127 的字节值， 而且制定 UTF-8 和 UTF-16 的方式也限制了可用的字节
        序列。 不过即便如此， 我们也不能根据特定的位模式来 100% 确定二进
        制文件的编码是 ASCII 或 UTF-8。
     
                    
"""4.5 处理文本文件"""

    处理文本的最佳实践是“Unicode 三明治”意思是，要尽早把输入（例如读取文件时） 的字节序列解码成字符串。 
    这种三明治中的“肉片”是程序的业务逻辑， 在这里只能处理字符串对象。 
    在其他处理过程中， 一定不能编码或解码。 对输出来说， 则要尽量晚地把字符串编码成字节序列。
    多数 Web 框架都是这样做的， 使用框架时很少接触字节序列。
    在 Django 中， 视图应该输出 Unicode 字符串；Django 会负责把响应编码成字节序列， 而且默认使用 UTF-8 编码。 
    
    在 Python 3 中能轻松地采纳 Unicode 三明治的建议， 因为内置的 open
    函数会在读取文件时做必要的解码， 以文本模式写入文件时还会做必要的编码， 
    所以调用 my_file.read() 方法得到的以及传给my_file.write(text) 方法的都是字符串对象。
    可以看出， 处理文本文件很简单。 但是， 如果依赖默认编码， 你会遇到麻烦。
    
    示例4.9 一个平台上的编码问题：
            open('zen.txt', 'w',encoding='utf_8').write('café')
            print(open('zen.txt').read())
            输出的结果是：caf茅
            
        问题是:在写入文件的时候制定了 UTF-8 编码，但是读取的时候没有这么做，Windows上默认的是GB2312.
        在新版 GNU/Linux 或 Mac OS X中运行同样的语句不会出问题， 因为这几个操作系统的默认编码是UTF-8.
        
        如果打开文件是为了写入， 但是没有指定编码参数， 会使用区域设置中的默认编码， 
        而且使用那个编码也能正确读取文件。
            open('zen.txt', 'w').write('café')
            print(open('zen.txt').read())
            输出的结果是：café
        
        需要在多台设备中或多种场合下运行的代码， 一定不能依赖
        默认编码。 打开文件时始终应该明确传入 encoding= 参数， 因为
        不同的设备使用的默认编码可能不同， 有时隔一天也会发生变化
        
            open('zen.txt', 'w',encoding='utf_8').write('café')
            print(open('zen.txt','r',encoding='utf-8').read())
            输出结果：café
            
"""4.6 为了正确比较而规范化Unicode 字符串"""                

    因为 Unicode 有组合字符，所以字符串比较起来很复杂。
    例如， “café”这个词可以使用两种方式构成， 分别有 4 个和 5 个码位，但是结果完全一样：
    
        >>> s1 = 'café'
        >>> s2 = 'cafe\u0301'
        >>> s1, s2
        ('café', 'café')
        >>> len(s1), len(s2)
        (4, 5)
        >>> s1 == s2
        False     
    在Unicode 标准中， 'é' 和 'e\u0301' 这样的序列叫“标准等价物”（canonical equivalent）
    应用程序应该把它们视作相同的字符。 但是， Python 看到的是不同的码位序列，因此判定二者不相等。
    
    这个问题的解决方案是使用 unicodedata.normalize 函数提供的Unicode 规范化。 
    这个函数的第一个参数是这 4 个字符串中的一个： 'NFC'、 'NFD'、 'NFKC' 和 'NFKD'。
      
    NFC（Normalization Form C） 使用最少的码位构成等价的字符串， 
    而NFD 把组合字符分解成基字符和单独的组合字符。 这两种规范化方式都能让比较行为符合预期：
        
        >>> from unicodedata import normalize
        >>> s1 = 'café' # 把"e"和重音符组合在一起
        >>> s2 = 'cafe\u0301' # 分解成"e"和重音符
        >>> len(s1), len(s2)
        (4, 5)
        >>> len(normalize('NFC', s1)), len(normalize('NFC', s2))
        (4, 4)
        >>> len(normalize('NFD', s1)), len(normalize('NFD', s2))
        (5, 5)
        >>> normalize('NFC', s1) == normalize('NFC', s2)
        True
        >>> normalize('NFD', s1) == normalize('NFD', s2)
        True
        
        
"""4.7 Unicode 文本排序 """        
    
    Python 比较任何类型的序列时， 会一一比较序列里的各个元素。 对字符串来说， 比较的是码位。 
    可是在比较非 ASCII 字符时， 得到的结果不尽如人意。 
    
    在 Python 中， 非 ASCII 文本的标准排序方式是使用 locale.strxfrm函数， 
    根据 locale 模块的文档这 个函数会“把字符串转换成适合所在区域进行比较的形式”。

"""4.8 Unicode数据库"""    
    
    Unicode 标准提供了一个完整的数据库（许多格式化的文本文件） ， 不仅包括码位与字符名称之间的映射， 
    还有各个字符的元数据， 以及字符之间的关系。
    
    
"""4.9 支持字符串和字节序列的双模式API"""

    标准库中的一些函数能接受字符串或字节序列为参数， 然后根据类型展现不同的行为。 
    re 和 os 模块中就有这样的函数。               
    
    4.9.1 正则表达式中的字符串和字节序列:
    
        如果使用字节序列构建正则表达式， \d 和 \w 等模式只能匹配 ASCII 字符； 
        相比之下， 如果是字符串模式， 就能匹配 ASCII 之外的 Unicode 数字或字母。 
    
        示例 4-22 ramanujan.py： 比较简单的字符串正则表达式和字节序列正则表达式的行为.
            
            import re
            re_numbers_str = re.compile(r'\d+') ➊
            re_words_str = re.compile(r'\w+')
            re_numbers_bytes = re.compile(rb'\d+') ➋
            re_words_bytes = re.compile(rb'\w+')
            text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef" ➌
                        " as 1729 = 1³ + 12³ = 9³ + 10³.") ➍
            text_bytes = text_str.encode('utf_8') ➎
            
            print('Text', repr(text_str), sep='\n ')
            print('Numbers')
            print(' str :', re_numbers_str.findall(text_str)) ➏
            print(' bytes:', re_numbers_bytes.findall(text_bytes)) ➐
            print('Words')
            print(' str :', re_words_str.findall(text_str)) ➑
            print(' bytes:', re_words_bytes.findall(text_bytes)) ➒   
            
            ❶ 前两个正则表达式是字符串类型。
            ❷ 后两个正则表达式是字节序列类型。
            ❸ 要搜索的 Unicode 文本， 包括 1729 的泰米尔数字（逻辑行直到右括号才结束） 。
            ❹ 这个字符串在编译时与前一个拼接起来
            ❺ 字节序列只能用字节序列正则表达式搜索。
            ❻ 字符串模式 r'\d+' 能匹配泰米尔数字和 ASCII 数字。
            ❼ 字节序列模式 rb'\d+' 只能匹配 ASCII 字节中的数字。
            ❽ 字符串模式 r'\w+' 能匹配字母、 上标、 泰米尔数字和 ASCII 数字。
            ❾ 字节序列模式 rb'\w+' 只能匹配 ASCII 字节中的字母和数字。
        
        可以使用正则表达式搜索字符串和字节序列， 但是在后一种情况中， ASCII 范围外的字节不会当成数字和组成单词的字母.
        字符串正则表达式有个 re.ASCII 标志， 它让\w、 \W、 \b、 \B、 \d、 \D、 \s 和 \S 只匹配 ASCII 字符。
    
    4.9.2 os 函数中的字符串和字节序列：
    
        GNU/Linux 内核不理解 Unicode， 因此你可能发现了， 对任何合理的编
        码方案来说， 在文件名中使用字节序列都是无效的， 无法解码成字符
        串。 在不同操作系统中使用各种客户端的文件服务器， 在遇到这个问题
        时尤其容易出错。
        
        为了规避这个问题， os 模块中的所有函数、 文件名或路径名参数既能
        使用字符串， 也能使用字节序列。 如果这样的函数使用字符串参数调
        用， 该参数会使用 sys.getfilesystemencoding() 得到的编解码器
        自动编码， 然后操作系统会使用相同的编解码器解码。 这几乎就是我们
        想要的行为， 与 Unicode 三明治最佳实践一致。
    
  
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
    
    在python 中，函数是一等对象，编程语言理论家把"一等对象"定义为满足下述条件的程序实体：
        （1）在运行时创建
        （2）能赋值给变量或数据结构中的元素
        （3）能作为参数传给函数
        （4）能作为函数的返回结果
    在 Python 中， 整数、 字符串和字典都是一等对象——没什么特别的。
    在 Python 中， 所有函数都是一等对象。

"""5.1 把函数视为对象"""

    示例 5-1 创建并测试一个函数， 然后读取它的 __doc__ 属性， 再检查它的类型
        
        >>> def factorial(n): ➊
        ... '''returns n!'''
        ... return 1 if n < 2 else n * factorial(n-1)
        ...
        >>> factorial(42)
        1405006117752879898543142606244511569936384000000000
        >>> factorial.__doc__ ➋
        'returns n!'
        >>> type(factorial) ➌
        <class 'function'>   
        
    ➊ 这是一个控制台会话， 因此我们是在“运行时”创建一个函数。
    ➋ __doc__ 是函数对象众多属性中的一个。
    ➌ factorial 是 function 类的实例。    
    
    示例 5-2 展示了函数对象的“一等”本性。 
        我们可以把 factorial 函数赋值给变量 fact， 然后通过变量名调用。 
        我们还能把它作为参数传给map 函数。 map 函数返回一个可迭代对象， 
        里面的元素是把第一个参数（一个函数） 应用到第二个参数（一个可迭代对象， 
        这里是range(11)） 中各个元素上得到的结果。 

        >>> fact = factorial
        >>> fact
        <function factorial at 0x...>
        >>> fact(5)
        120
        >>> map(factorial, range(11))
        <map object at 0x...>
        >>> list(map(fact, range(11)))
        [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]        
    有了一等函数， 就可以使用函数式风格编程。 函数式编程的特点之一是使用高阶函数。

"""5.2 高阶函数"""
    
    接受函数为参数， 或者把函数作为结果返回的函数是高阶函数（higher-order function），map 函数就是一例。

"""map、 filter和reduce的现代替代品"""
    
    函数式语言通常会提供 map、 filter 和 reduce 三个高阶函数。
    在 Python 3 中， map 和 filter 还是内置函数， 但是由于引入了列表推导和生成器表达式， 
    它们变得没那么重要了。 列表推导或生成器表达式具有 map 和 filter 两个函数的功能， 而且更易于阅读。
    
        >>> list(map(fact, range(6))) ➊
        [1, 1, 2, 6, 24, 120]
        >>> [fact(n) for n in range(6)] ➋
        [1, 1, 2, 6, 24, 120]
        >>> list(map(factorial, filter(lambda n: n % 2, range(6)))) ➌
        [1, 6, 120]
        >>> [factorial(n) for n in range(6) if n % 2] ➍
        [1, 6, 120]
        >>>     
        
        ❶ 构建 0! 到 5! 的一个阶乘列表。
        ❷ 使用列表推导执行相同的操作。
        ❸ 使用 map 和 filter 计算直到 5! 的奇数阶乘列表。
        ❹ 使用列表推导做相同的工作， 换掉 map 和 filter， 并避免了使用lambda 表达式。
    
    在 Python 3 中， map 和 filter 返回生成器（一种迭代器） ， 因此现在它们的直接替代品是生成器表达式。
    在 Python 2 中， reduce 是内置函数， 但是在 Python 3 中放到functools 模块里了。 这个函数最常用于求和。
        
        >>> from functools import reduce ➊
        >>> from operator import add ➋
        >>> reduce(add, range(100)) ➌
        4950
        >>> sum(range(100)) ➍
        4950
        >>>
        
        ❶ 从 Python 3.0 起， reduce 不再是内置函数了。
        ❷ 导入 add， 以免创建一个专求两数之和的函数。
        ❸ 计算 0~99 之和。
        ❹ 使用 sum 做相同的求和； 无需导入或创建求和函数
        sum 和 reduce 的通用思想是把某个操作连续应用到序列的元素上， 累计之前的结果， 把一系列值归约成一个值。

"""5.3 匿名函数"""

    lambda 关键字在 Python 表达式内创建匿名函数。
    
    然而， Python 简单的句法限制了 lambda 函数的定义体只能使用纯表达式。 
    换句话说， lambda 函数的定义体中不能赋值， 也不能使用 while和 try 等 Python 语句。
               
    在参数列表中最适合使用匿名函数。
    
    示例 5-7 使用 lambda 表达式反转拼写， 然后依此给单词列表排序：
        
        >>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
        >>> sorted(fruits, key=lambda word: word[::-1])
        ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
        >>>
    
    Lundh 提出的 lambda 表达式重构秘笈：
        
        (1) 编写注释， 说明 lambda 表达式的作用。
        (2) 研究一会儿注释， 并找出一个名称来概括注释。
        (3) 把 lambda 表达式转换成 def 语句， 使用那个名称来定义函数。
        (4) 删除注释。
    
    lambda 句法只是语法糖： 与 def 语句一样， lambda 表达式会创建函数对象。 这是 Python 中几种可调用对象的一种。    
        
"""5.4 可调用对象"""
    
    Python 数据模型文档列出了 7 种可调用对象:
        (1) 用户调用的函数：
            
            使用 def 语句或 lambda 表达式创建
            
        (2) 内置函数：
            
            使用 c 语言 （CPython）实现的函数，如 len 或 time.strftime.
        
        (3) 内置方法：
            
            使用 c 语言实现的方法，如 dict.get.
        
        (4) 方法：
            
            在类的定义中定义的函数。
            
        (5) 类：
            
            调用类时会运行类的 __new__ 方法创建一个实例， 然后运行__init__ 方法， 初始化实例， 
            最后把实例返回给调用方。 因为 Python没有 new 运算符， 所以调用类相当于调用函数。     
       
        (6) 类的实例：
            
            如果类定义了 __call__ 方法， 那么它的实例可以作为函数调用。
      
        (7) 生成器函数：
        
            使用 yield 关键字的函数或方法。 调用生成器函数返回的是生成器对象。
            
"""5.5 用户定义的可调用类型"""

    不仅 Python 函数是真正的对象，任何 Python 对象都可以表现得像函数。为此，只需实现实例方法 __call__。
    
    示例 5-8 bingocall.py： 调用 BingoCage 实例， 从打乱的列表中取出一个元素
    
        import random
        class BingoCage:
            def __init__(self, items):
                self._items = list(items) ➊
                random.shuffle(self._items) ➋
            def pick(self): ➌
                try:
                    return self._items.pop()
                except IndexError:
                    raise LookupError('pick from empty BingoCage') ➍
            def __call__(self): ➎
                return self.pick()                     
         
        ❶ __init__ 接受任何可迭代对象； 在本地构建一个副本， 防止列表参数的意外副作用。
        ❷ shuffle 定能完成工作， 因为 self._items 是列表。
        ❸ 起主要作用的方法。
        ❹ 如果 self._items 为空， 抛出异常， 并设定错误消息。
        ❺ bingo.pick() 的快捷方式是 bingo()。
            
        如果没有实现def __call__(self) 函数而调用bingo() 会抛出 TypeError: 'BingoCage' object is not callable 异常。
        
        实现 __call__ 方法的类是创建函数类对象的简便方式， 此时必须在内部维护一个状态， 让它在调用之间可用。
        例如 BingoCage 中的剩余元素。 装饰器就是这样，装饰器必须是函数， 而且有时要在多次调用之间“记住”某些事。
        创建保有内部状态的函数， 还有一种截然不同的方式——使用闭包。

"""5.6 函数内省"""
    
    把函数视作对象处理的另一方面： 运行时内省。
    
    除了 __doc__， 函数对象还有很多属性。 使用 dir 函数可以探知factorial 具有下述属性：
    
    >>> dir(factorial)
    ['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', 
     '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', 
     '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', 
     '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
     '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 
     'func_dict', 'func_doc', 'func_globals', 'func_name']
            
    与用户定义的常规类一样，函数使用 __dict__ 属性存储赋予它的用户属性。这相当于一种基本形式的注解。
    
    示例 5-9 列出常规对象没有而函数有的属性
        
        >>> class C: pass # ➊
        >>> obj = C() # ➋
        >>> def func(): pass # ➌
        >>> sorted(set(dir(func)) - set(dir(obj))) # ➍
        ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__',
        '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
        >>>      
        
        ➊ 创建一个空的用户定义的类。
        ➋ 创建一个实例。
        ➌ 创建一个空函数。
        ➍ 计算差集， 然后排序， 得到类的实例没有而函数有的属性列表。
            
           名称                  类型             说明 
        __annotations__          dict       参数和返回值的注解
        __call__             methodwrapper   实现 () 运算符； 即可调用对象协议
        __closure__          tuple           函数闭包， 即自由变量的绑定（通常是 None）
        __code__             code            编译成字节码的函数元数据和函数定义体
        __defaults__         tuple           形式参数的默认值
        __get__              methodwrapper   实现只读描述符协议（参见第 20 章）
        __globals__          dict            函数所在模块中的全局变量
        __kwdefaults__       dict            仅限关键字形式参数的默认值
        __name__             str             函数名称
        __qualname__         str             函数的限定名称， 如 Random.choice       
    
    
"""5.7 从定位参数到仅限关键字参数"""    
       
    Python 最好的特性之一是提供了极为灵活的参数处理机制， 
    而且 Python3 进一步提供了仅限关键字参数(keyword-only argument)。 
    与之密切相关的是， 调用函数时使用 * 和 **“展开”可迭代对象，映射到单个参数。
        
"""5.10 支持函数式编程的包"""       

    虽然 Guido 明确表明， Python 的目标不是变成函数式编程语言， 
    但是得益于 operator 和 functools 等包的支持， 函数式编程风格也可以信手拈来。 
    接下来的两节分别介绍这两个包。    

    5.10.1  operator模块:
        
        在函数式编程中， 经常需要把算术运算符当作函数使用。
        
        示例 5-21 使用 reduce 函数和一个匿名函数计算阶乘
            from functools import reduce
            def fact(n):
                return reduce(lambda a, b: a*b, range(1, n+1))
        
        operator 模块为多个算术运算符提供了对应的函数， 从而避免编写lambda a, b: a*b 这种平凡的匿名函数。    
        示例 5-22 使用 reduce 和 operator.mul 函数计算阶乘
        
            from functools import reduce
            from operator import mul
            def fact(n):
                return reduce(mul, range(1, n+1))   
                
    5.10.2 使用functools.partial冻结参数:
        functools 模块提供了一系列高阶函数， 其中最为人熟知的或许是reduce.
        
  

"---------------------------------------------------------------------"

                     第七章   函数装饰器和闭包

    有很多人抱怨， 把这个特性命名为“装饰器”不好。 主要原因是， 这个名称与 GoF 书 使用的不一致。 
    装饰器这个名称可能更适合在编译器领域使用， 因为它会遍历并注解句法树。

    函数装饰器用于在源码中“标记”函数，以某种方式增强函数的行为。这是一项强大的功能，但是若想掌握，必须理解闭包。
    除了在装饰器中有用处之外， 闭包还是回调式异步编程和函数式编程风格的基础。

"""7.1 装饰器的基础知识"""    
    
    装饰器是可调用的对象， 其参数是另一个函数（被装饰的函数） 。 
    装饰器可能会处理被装饰的函数， 然后把它返回， 或者将其替换成另一个函数或可调用对象。
    
    假如有个名为 decorate 的装饰器：
    
        @decorate
        def target():
            pinrt('running target()')
            
    上述代码的效果与下述写法一样：
    
        def target():
            print('running target')
        target = decorate(target)
    
    两种写法的最终结果一样： 上述两个代码片段执行完毕后得到的target 不一定是原来那个 target 函数， 
    而是 decorate(target) 返回的函数
    
    示例 7-1 装饰器通常把函数替换成另一个函数
    
        >>> def deco(func):
            ... def inner():
                ... print('running inner()')
            ... return inner ➊
        ...
        >>> @deco
        ... def target(): ➋
            ... print('running target()')
        ...
        >>> target() ➌
        running inner()
        >>> target ➍
        <function deco.<locals>.inner at 0x10063b598>
        
    (1) deco 返回 inner 函数对象。
    (2) 使用 deco 装饰 target。
    (3) 调用被装饰的 target 其实会运行 inner。
    (4) 审查对象， 发现 target 现在是 inner 的引用。
        
    严格来说， 装饰器只是语法糖。 如前所示， 装饰器可以像常规的可调用对象那样调用， 其参数是另一个函数。 
    有时， 这样做更方便， 尤其是做元编程（在运行时改变程序的行为）时。
    
    综上， 装饰器的一大特性是， 能把被装饰的函数替换成其他函数。 
    第二个特性是， 装饰器在加载模块时立即执行。  
        
"""7.2 Python 何时执行装饰器"""

    装饰器的一个关键特性是， 它们在被装饰的函数定义之后立即运行。 这通常是在导入时（即 Python 加载模块时）。
    
    示例 7-2 registration.py 模块：
    
        registry = [] ➊
        def register(func): ➋
            print('running register(%s)' % func) ➌
            registry.append(func) ➍
            return func ➎
        @register ➏
        def f1():
            print('running f1()')
        @register
        def f2():
            print('running f2()')
        def f3(): ➐
            print('running f3()')
        
        def main(): ➑
            print('running main()')
            print('registry ->', registry)
            f1()
            f2()
            f3()
        if __name__=='__main__':
            main() ➒     
    
        ❶ registry 保存被 @register 装饰的函数引用。
        ❷ register 的参数是一个函数。
        ❸ 为了演示， 显示被装饰的函数。
        ❹ 把 func 存入 registry。
        ❺ 返回 func： 必须返回函数； 这里返回的函数与通过参数传入的一样。
        ❻ f1 和 f2 被 @register 装饰。
        ❼ f3 没有装饰。
        ❽ main 显示 registry， 然后调用 f1()、 f2() 和 f3()。
        ❾ 只有把 registration.py 当作脚本运行时才调用 main()。
    运行结果为：
        running register(<function f1 at 0x00000000006FC598>)
        running register(<function f2 at 0x00000000006FC620>)
        running register(<function f3 at 0x00000000006FC6A8>)
        running main()
        registry -> [<function f1 at 0x00000000006FC598>, <function f2 at 0x00000000006FC620>, <function f3 at 0x00000000006FC6A8>]
        running f1
        running f2
        running f3    
        
    注意， register 在模块中其他函数之前运行（三次），调用register 时， 传给它的参数是被装饰的函数。
    加载模块后， registry 中有三个被装饰函数的引用： f1 和 f2，f3函数 只在 main 明确调用它们时才执行。
    
    函数装饰器在导入模块时立即执行， 而被装饰的函数只在明确调用时运行。 
    这突出了 Python 程序员所说的导入时和运行时之间的区别。
    
    考虑到装饰器在真实代码中的常用方式， 示例 7-2 有两个不寻常的地方。
    
        装饰器函数与被装饰的函数在同一个模块中定义。 
        实际情况是， 装饰器通常在一个模块中定义， 然后应用到其他模块中的函数上。
        
        register 装饰器返回的函数与通过参数传入的相同。 
        实际上， 大多数装饰器会在内部定义一个函数， 然后将其返回。


"""7.3 变量作用域规则"""

    示例 7-4 一个函数， 读取一个局部变量和一个全局变量
    
        >>> def f1(a):
        ... print(a)
        ... print(b)
        ...
        >>> f1(3)
        3T
        raceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 3, in f1
        NameError: global name 'b' is not defined   
    
    在示例 7-4 中， 如果先给全局变量 b 赋值， 然后再调用 f1， 那就不会出错：    
        
        >>> b = 6
        >>> f1(3)
        36    
        
    示例 7-5 b 是局部变量， 因为在函数的定义体中给它赋值了
    
        >>> b = 6
        >>> def f2(a):
        ... print(a)
        ... print(b)
        ... b = 9
        ...
        >>> f2(3)
        3T
        raceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 3, in f2
        UnboundLocalError: local variable 'b' referenced before assignment    
              
    注意， 首先输出了 3， 这表明 print(a) 语句执行了。 但是第二个语句print(b) 执行不了。
    一开始我很吃惊， 我觉得会打印 6， 因为有个全局变量 b，而且是在 print(b) 之后为局部变量 b 赋值的。
    
    可事实是， Python 编译函数的定义体时， 它判断 b 是局部变量， 因为在函数中给它赋值了。 
    生成的字节码证实了这种判断， Python 会尝试从本地环境获取 b。 后面调用 f2(3) 时， 
    f2 的定义体会获取并打印局部变量 a 的值， 但是尝试获取局部变量 b 的值时， 发现 b 没有绑定值。

    这不是缺陷， 而是设计选择：Python 不要求声明变量， 但是假定在函数定义体中赋值的变量则是局部变量。
    这比 JavaScript 的行为好多了，JavaScript 也不要求声明变量， 但是如果忘记把变量声明为局部变量
    （使用 var） ，可能会在不知情的情况下获取全局变量。
     
    如果在函数中赋值时想让解释器把 b 当成全局变量， 要使用 global 声明：
    
        >>> b = 6
        >>> def f3(a):
        ... global b
        ... print(a)
        ... print(b)
        ... b = 9
        ...
        >>> f3(3)
        36>
        >> b   

        
"""7.5 闭包"""
    
    在博客圈，人们有时会把闭包和匿名函数弄混。 这是有历史原因的： 
    在函数内部定义函数不常见，直到开始使用匿名函数才会这样做。 
    而且，只有涉及嵌套函数时才有闭包问题。 因此， 很多人是同时知道这两个概念的。
    
    其实， 闭包指延伸了作用域的函数， 其中包含函数定义体中引用、 但是
    不在定义体中定义的非全局变量。 函数是不是匿名的没有关系， 关键是
    它能访问定义体之外定义的非全局变量。
    
    示例 7-9： average.py： 计算移动平均值的高阶函数：
        
        def make_averager():
            series = []
            def averager(new_value):
                series.append(new_value)
                total = sum(series)
                return total/len(series)
            return averager
        
        示例 7-10 测试示例 7-9
        >>> avg = make_averager()
        >>> avg(10)
        10.0
        >>> avg(11)
        10.5
        >>> avg(12)
        
        调用 make_averager 时， 返回一个 averager 函数对象。 
        每次调用averager 时， 它会把参数添加到系列值中， 然后计算当前平均值。
        
        注意， series 是 make_averager 函数的局部变量， 因为那个函数的定义体中初始化了series：
        series = []。 可是， 调用 avg(10)时， make_averager 函数已经返回了， 
        而它的本地作用域也一去不复返了。
        
        averager 的闭包延伸到那个函数的作用域之外， 包含自由变量 series 的绑定。
        
        审查返回的 averager 对象， 我们发现 Python 在 __code__ 属性（表示编译后的函数定义体） 
        中保存局部变量和自由变量的名称：
            >>> avg.__code__.co_varnames
            ('new_value', 'total')
            >>> avg.__code__.co_freevars
            ('series',)
             
        series 的绑定在返回的 avg 函数的 __closure__ 属性中。 
        avg.__closure__ 中的各个元素对应于avg.__code__.co_freevars 中的一个名称。 
        这些元素是 cell 对象，有个 cell_contents 属性， 保存着真正的值。 
        这些属性的值如示例 7-12 所示
            >>> avg.__code__.co_freevars
            ('series',)
            >>> avg.__closure__
            (<cell at 0x107a44f78: list object at 0x107a91a48>,)
            >>> avg.__closure__[0].cell_contents
            [10, 11, 12]
    
    综上， 闭包是一种函数， 它会保留定义函数时存在的自由变量的绑定，
    这样调用函数时， 虽然定义作用域不可用了， 但是仍能使用那些绑定。                    
                        
    注意， 只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量。                   

"""7.6 nonlocal 声明"""
    
    示例 7-13 计算移动平均值的高阶函数， 不保存所有历史值， 但有缺陷
    
        def make_averager():
            count = 0
            total = 0
            def averager(new_value):
                count += 1
                total += new_value
                return total / count
            return averager    
        
    尝试使用示例 7-13 中定义的函数， 会得到如下结果：
        
        >>> avg = make_averager()
        >>> avg(10)
        Traceback (most recent call last):
        ...
        UnboundLocalError: local variable 'count' referenced before assignment
        >>>
        
        问题是， 当 count 是数字或任何不可变类型时， count += 1 语句的作用其实与 count = count + 1 一样。
        因此， 我们在 averager 的定义体中为 count 赋值了， 这会把 count 变成局部变量。 
        total 变量也受这个问题影响。
        
    示例 7-9 没遇到这个问题， 因为我们没有给 series 赋值， 我们只是调用 series.append， 
    并把它传给 sum 和 len。 也就是说， 我们利用了列表是可变的对象这一事实。        
    
    但是对数字、 字符串、 元组等不可变类型来说， 只能读取， 不能更新。
    如果尝试重新绑定， 例如 count = count + 1， 其实会隐式创建局部
    变量 count。 这样， count 就不是自由变量了， 因此不会保存在闭包中。

    为了解决这个问题， Python 3 引入了 nonlocal 声明。 它的作用是把变量标记为自由变量， 
    即使在函数中为变量赋予新值了， 也会变成自由变量。 如果为 nonlocal 声明的变量赋予新值， 
    闭包中保存的绑定会更新。 

    示例 7-14 计算移动平均值， 不保存所有历史（使用 nonlocal 修正）
        
        def make_averager():
            count = 0
            total = 0
            def averager(new_value):
                nonlocal count, total
                count += 1
                total += new_value
                return total / count
            return averager    
    
"""7.7 实现一个简单的装饰器"""

    示例 7-15 一个简单的装饰器， 输出函数的运行时间
    
        import time
        def clock(func):
            def clocked(*args): # ➊
                t0 = time.perf_counter()
                result = func(*args) # ➋
                elapsed = time.perf_counter() - t0
                name = func.__name__
                arg_str = ', '.join(repr(arg) for arg in args)
                print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
                return result
                return clocked # ➌            
        
        ❶ 定义内部函数 clocked， 它接受任意个定位参数。
        ❷ 这行代码可用， 是因为 clocked 的闭包中包含自由变量 func。
        ❸ 返回内部函数， 取代被装饰的函数。 
        
"""7.8 标准库中的装饰器"""

    Python 内置了三个用于装饰方法的函数： property、 classmethod 和staticmethod。
    
    另一个常见的装饰器是 functools.wraps， 它的作用是协助构建行为
    良好的装饰器。 我们在示例 7-17 中用过。 标准库中最值得关注的两个
    装饰器是 lru_cache 和全新的 singledispatch（Python 3.4 新增） 。
    这两个装饰器都在 functools 模块中定义。        
    
    7.8.1 使用functools.lru_cache做备忘:
        
        functools.lru_cache 是非常实用的装饰器， 它实现了备忘
        （memoization） 功能。 这是一项优化技术， 它把耗时的函数的结果保存
        起来， 避免传入相同的参数时重复计算。 LRU 三个字母是“Least
        Recently Used”的缩写， 表明缓存不会无限制增长， 一段时间不用的缓存
        条目会被扔掉。
        
        示例 7-18 生成第 n 个斐波纳契数， 递归方式非常耗时
            from clockdeco import clock
            @clock
            def fibonacci(n):
                if n < 2:
                    return n
                return fibonacci(n-2) + fibonacci(n-1)
            if __name__=='__main__':
                print(fibonacci(6))
        
        示例 7-19 使用缓存实现， 速度更快:
            
            import functools
            from clockdeco import clock
            @functools.lru_cache() # ➊
            @clock # ➋
            def fibonacci(n):
                if n < 2:
                    return n
                return fibonacci(n-2) + fibonacci(n-1)  
            if __name__=='__main__':
                print(fibonacci(6))     
              
            ❶ 注意， 必须像常规函数那样调用 lru_cache。 
              这一行中有一对括号： @functools.lru_cache()。 
              这么做的原因是， lru_cache 可以接受配置参数， 稍后说明。
            ❷ 这里叠放了装饰器： @lru_cache() 应用到 @clock 返回的函数上。
            
        特别要注意， lru_cache 可以使用两个可选的参数来配置。 它的签名是：
        
            functools.lru_cache(maxsize=128, typed=False)
        maxsize 参数指定存储多少个调用的结果。 缓存满了之后， 旧的结果会
        被扔掉， 腾出空间。 为了得到最佳性能， maxsize 应该设为 2 的幂。     
    
"""7.9 叠放装饰器 """

    把 @d1 和 @d2 两个装饰器按顺序应用到 f 函数上， 作用相当于 f =d1(d2(f))。
    也就是说， 下述代码:
        
        @d1
        @d2
        def f():
            print('f')
    
    等同于：
        
        def f():
            print('f')
        f = d1(d2(f))     
              
"""7.10 参数化装饰器 """   

    解析源码中的装饰器时，Python 把被装饰的函数作为第一个参数传给装饰器函数。那怎么让装饰器接受其他参数呢？ 
    答案是： 创建一个装饰器工厂函数， 把参数传给它， 返回一个装饰器， 然后再把它应用到要装饰的函数上。 
    不明白什么意思？ 当然。 下面以我们见过的最简单的装饰器为例说明： 
    示例 7-22 中的 register:
        
        registry = []
        def register(func):
            print('running register(%s)' % func)
            registry.append(func)
            return func
        @register
        def f1():
            print('running f1()')
        
        print('running main()')
        print('registry ->', registry)
        f1()
        
    7.10.1 一个参数化的注册装饰器：
    
        为了便于启用或禁用 register 执行的函数注册功能， 我们为它提供一
        个可选的 active 参数， 设为 False 时， 不注册被装饰的函数。 实现方
        式参见示例 7-23。 从概念上看， 这个新的 register 函数不是装饰器，
        而是装饰器工厂函数。 调用它会返回真正的装饰器， 这才是应用到目标
        函数上的装饰器。     
        
        示例 7-23 为了接受参数， 新的 register 装饰器必须作为函数调用：
        
            registry = set() ➊
            def register(active=True): ➋
                def decorate(func): ➌
                    print('running register(active=%s)->decorate(%s)'% (active, func))
                    if active: ➍
                        registry.add(func)
                    else:
                        registry.discard(func) ➎
                    return func ➏
                return decorate ➐
            
            @register(active=False) ➑
            def f1():
                print('running f1()')
            
            @register() ➒
            def f2():
                print('running f2()')
            
            def f3():
                print('running f3()')     
                
            ❶ registry 现在是一个 set 对象， 这样添加和删除函数的速度更快。
            ❷ register 接受一个可选的关键字参数。
            ❸ decorate 这个内部函数是真正的装饰器； 注意， 它的参数是一个函数。
            ❹ 只有 active 参数的值（从闭包中获取） 是 True 时才注册 func。
            ❺ 如果 active 不为真， 而且 func 在 registry 中， 那么把它删除。
            ❻ decorate 是装饰器， 必须返回一个函数。
            ❼ register 是装饰器工厂函数， 因此返回 decorate。
            ❽ @register 工厂函数必须作为函数调用， 并且传入所需的参数。
            ❾ 即使不传入参数， register 也必须作为函数调用（@register()）即要返回真正的装饰器 decorate。
        这里的关键是， register() 要返回 decorate， 然后把它应用到被装饰的函数上。            
             
    7.10.2 参数化clock装饰器：
        
        本节再次探讨 clock 装饰器， 为它添加一个功能： 让用户传入一个格式字符串， 控制被装饰函数的输出。 
          
        示例 7-25 clockdeco_param.py 模块： 参数化 clock 装饰器：
            
            import time
            DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'
            
            def clock(fmt=DEFAULT_FMT): ➊
                def decorate(func): ➋
                    def clocked(*_args): ➌
                        t0 = time.time()
                        _result = func(*_args) ➍
                        elapsed = time.time() - t0
                        name = func.__name__
                        args = ', '.join(repr(arg) for arg in _args) ➎
                        result = repr(_result) ➏
                        print(fmt.format(**locals())) ➐
                        return _result ➑
                    return clocked ➒
                return decorate ➓
            
            if __name__ == '__main__':
                @clock()
                def snooze(seconds):
                    time.sleep(seconds)
                
                for i in range(3):
                    snooze(.123)
            
            ❶ clock 是参数化装饰器工厂函数。
            ❷ decorate 是真正的装饰器。
            ❸ clocked 包装被装饰的函数。
            ❹ _result 是被装饰的函数返回的真正结果。
            ❺ _args 是 clocked 的参数， args 是用于显示的字符串。
            ❻ result 是 _result 的字符串表示形式， 用于显示。
            ❼ 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量。
            ❽ clocked 会取代被装饰的函数， 因此它应该返回被装饰的函数返回的值。
            ❾ decorate 返回 clocked。
            ❿ clock 返回 decorate。
            ⓫ 在这个模块中测试， 不传入参数调用 clock()， 因此应用的装饰器使用默认的格式 str。
    
    
"""7.11 本章小结"""    
    
"---------------------------------------------------------------------"

                     第四部分 面向对象惯用法
                     
    第四部分：重点转移到了类的构建上面，和任何面向对象语言一样， 
    Python 还有些自己的特性， 这些特性可能并不会出现在你我学习基于类的编程的语言中。
    这一部分的章节解释了引用（reference） 的原理、 “可变性”的概念、 实例的生命周期、
    如何构建自定义的集合类型和 ABC、 多重继承该怎么理顺、 什么时候
    应该使用操作符重载及其方法。
        

                     第八章   对象引用、可变性和垃圾回收
                      
    变量是标注， 而不是盒子。 如果你不知道引用式变量是什么， 可以像这样对别人解释别名。  
    
"""8.1 变量不是盒子"""

    示例 8-2 创建对象之后才会把变量分配给对象：
    
        >>> class Gizmo:
        ... def __init__(self):
        ... print('Gizmo id: %d' % id(self))
        ...
        >>> x = Gizmo()
        Gizmo id: 4301489152 ➊
        >>> y = Gizmo() * 10 ➋
        Gizmo id: 4301489432 ➌
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'
        >>>
        >>> dir() ➍
        ['Gizmo', '__builtins__', '__doc__', '__loader__', '__name__',
        '__package__', '__spec__', 'x']                           
       
    ❶ 输出的 Gizmo id: ... 是创建 Gizmo 实例的副作用。
    ❷ 在乘法运算中使用 Gizmo 实例会抛出异常。
    ❸ 这里表明， 在尝试求积之前其实会创建一个新的 Gizmo 实例。
    ❹ 但是， 肯定不会创建变量 y， 因为在对赋值语句的右边进行求值时抛出了异常。
    
    为了理解 Python 中的赋值语句， 应该始终先读右边。 对象在右边创建或获取， 
    在此之后左边的变量才会绑定到对象上， 这就像为对象贴上标注。 忘掉盒子吧！
    
    因为变量只不过是标注， 所以无法阻止为对象贴上多个标注。 贴的多个标注， 就是别名。
    
"""8.2 标识、相等性和别名"""

    示例 8-3 charles 和 lewis 指代同一个对象：
    
        >>> charles = {'name': 'Charles L. Dodgson', 'born': 1832}
        >>> lewis = charles ➊
        >>> lewis is charles
        True
        >>> id(charles), id(lewis) ➋
        (4300473992, 4300473992)
        >>> lewis['balance'] = 950 ➌
        >>> charles
        {'name': 'Charles L. Dodgson', 'balance': 950, 'born': 1832}            
    
        ❶ lewis 是 charles 的别名。
        ❷ is 运算符和 id 函数确认了这一点。
        ❸ 向 lewis 中添加一个元素相当于向 charles 中添加一个元素。 
    
    示例 8-4 alex 与 charles 比较的结果是相等， 但 alex 不是charles：
    
        >>> alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950} ➊
        >>> alex == charles ➋
        True
        >>> alex is not charles ➌
        True
        
        ❶ alex 指代的对象与赋值给 charles 的对象内容一样。
        ❷ 比较两个对象， 结果相等， 这是因为 dict 类的 __eq__ 方法就是这样实现的。
        ❸ 但它们是不同的对象。 这是 Python 说明标识不同的方式： a is notb。
    
    示例 8-3 体现了别名。 在那段代码中， lewis 和 charles 是别名， 即两个变量绑定同一个对象。 
    而 alex 不是 charles 的别名， 因为二者绑定的是不同的对象。 
    alex 和 charles 绑定的对象具有相同的值（== 比较的就是值）但是它们的标识不同。
    
    每个变量都有标识、 类型和值。 对象一旦创建， 它的标识绝不会变； 
    你可以把标识理解为对象在内存中的地址。 is 运算符比较两个对象的标识； 
    id() 函数返回对象标识的整数表示。
    
    对象 ID 的真正意义在不同的实现中有所不同。 在 CPython 中， id() 返
    回对象的内存地址， 但是在其他 Python 解释器中可能是别的值。 关键
    是， ID 一定是唯一的数值标注， 而且在对象的生命周期中绝不会变。
                     
    8.2.1 在==和is之间选择：
        
        == 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识。
            
        然而， 在变量和单例值之间比较时， 应该使用 is。 
        目前， 最常使用 is检查变量绑定的值是不是 None。 
        下面是推荐的写法：
            x is None
        否定的正确写法是：
            x is not None
            
        is 运算符比 == 速度快， 因为它不能重载， 所以 Python 不用寻找并调用特殊方法， 而是直接比较两个整数 ID。 
        而 a == b 是语法糖， 等同于a.__eq__(b)。 继承自 object 的 __eq__ 方法比较两个对象的 ID， 
        结果与 is 一样。 但是多数内置类型使用更有意义的方式覆盖了 __eq__方法， 会考虑对象属性的值。
        相等性测试可能涉及大量处理工作，例如，比较大型集合或嵌套层级深的结构时。
        
    8.2.2 元组的相对不可变性：
    
         元组与多数 Python 集合（列表、 字典、 集， 等等） 一样， 保存的是对象的引用。 
         如果引用的元素是可变的， 即便元组本身不可变， 元素依然可变。 
         也就是说， 元组的不可变性其实是指 tuple 数据结构的物理内容（即保存的引用）不可变，与引用的对象无关。
         
         而 str、 bytes 和 array.array 等单一类型序列是扁平的， 它们保存的不是引用， 
         而是在连续的内存中保存数据本身（字符、 字节和数字） 。   
         
         元组的值会随着引用的可变对象的变化而变。 元组中不可变的是元素的标识。
         
            >>> t1 = (1, 2, [30, 40]) ➊
            >>> t2 = (1, 2, [30, 40]) ➋
            >>> t1 == t2 ➌
            True
            >>> t1 is t2
            >>> false
            >>> id(t1[-1]) ➍
            4302515784
            >>> t1[-1].append(99) ➎
            >>> t1
            (1, 2, [30, 40, 99])
            >>> id(t1[-1]) ➏
            4302515784
            >>> t1 == t2 ➐
            False       
            
            ❶ t1 不可变， 但是 t1[-1] 可变。
            ❷ 构建元组 t2， 它的元素与 t1 一样。
            ❸ 虽然 t1 和 t2 是不同的对象， 但是二者相等——与预期相符。
            ❹ 查看 t1[-1] 列表的标识。
            ❺ 就地修改 t1[-1] 列表。
            ❻ t1[-1] 的标识没变， 只是值变了。
            ❼ 现在， t1 和 t2 不相等。            
                     
 """8.3 默认做浅复制"""
 
    复制列表（或多数内置的可变集合） 最简单的方式是使用内置的类型构造方法。
    
        >>> l1 = [3, [55, 44], (7, 8, 9)]
        >>> l2 = list(l1)
        >>> 
        >>> l2
        [3, [55, 44], (7, 8, 9)]
        >>> 
        >>> 
        >>> l1 == l2
        True
        >>> l1 is l2
        False
        >>> 
        >>> 
        >>> l3 = l1
        >>> l3
        [3, [55, 44], (7, 8, 9)]
        >>> 
        >>> l3 is l1
        True
        >>> 
        >>> l4 = l1[:]
        >>> l4 is l1
        False
        >>> l4 == l1
        True
        >>> 
        
    list(l1) 创建 l1 的副本，副本与源列表相等。
    但是二者指代不同的对象。 对列表和其他可变序列来说， 还能使用简洁的 l2 = l1[:] 语句创建副本
    
    然而，构造方法或[:]做的是浅复制（即复制了最外层容器，副本中的元素是源容器中元素的引用）。
    如果所有元素都是不可变的，那么这样没有问题，还可以节省内存，但是，如果有可变的元素，就
    可能导致意想不到的问题。
    
    示例 8-6 为一个包含另一个列表的列表做浅复制:
    
        >>> l1 = [3,[66,55,44],(7,8,9)]
        >>> l2 = list(l1)     # ➊
        >>> l2
        [3, [66, 55, 44], (7, 8, 9)]
        >>> 
        >>> l1.append(100)    # ➋
        >>> l1
        [3, [66, 55, 44], (7, 8, 9), 100]
        >>> l2
        [3, [66, 55, 44], (7, 8, 9)]
        >>> 
        >>> l1[1].remove(55)   # ➌
        >>> l1
        [3, [66, 44], (7, 8, 9), 100]
        >>> l2
        [3, [66, 44], (7, 8, 9)]
        >>> 
        >>> 
        >>> l2[1] += [33, 22]   # ➍
        >>> l1
        [3, [66, 44, 33, 22], (7, 8, 9), 100]
        >>> 
        >>> 
        >>> l2
        [3, [66, 44, 33, 22], (7, 8, 9)]
        >>> 
        >>> l2[2] += (10,11)   # ➎
        >>> l2
        [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]
        >>> l1
        [3, [66, 44, 33, 22], (7, 8, 9), 100]
    
        ❶ l2 是 l1 的浅复制副本， l2 = list(l1) 赋值后的程序状态。 l1 和 l2指代不同的列表， 
            但是二者引用同一个列表 [66, 55, 44] 和元组(7, 8, 9)。
        ❷ 把 100 追加到 l1 中， 对 l2 没有影响。
        ❸ 把内部列表 l1[1] 中的 55 删除。 这对 l2 有影响， 因为 l2[1] 绑定的列表与 l1[1] 是同一个。
        ❹ 对可变的对象来说， 如 l2[1] 引用的列表， += 运算符就地修改列表。 
            这次修改在 l1[1] 中也有体现， 因为它是 l2[1] 的别名。
        ❺ 对元组来说， += 运算符创建一个新元组， 然后重新绑定给变量l2[2]。 
            这等同于 l2[2] = l2[2] + (10, 11)。 现在， l1 和 l2 中最后位置上的元组不是同一个对象。
 
    为任意对象做深复制和浅复制：
        
        浅复制没什么问题， 但有时我们需要的是深复制（即副本不共享内部对象的引用）。 
        copy 模块提供的 deepcopy 和 copy 函数能为任意对象做深复制和浅复制。    
        
"""8.4 函数的参数作为引用时 """    
    
    Python 唯一支持的参数传递模式是共享传参（call by sharing）。
    共享传参指函数的各个形式参数获得实参中各个引用的副本。也就是说，函数内部的形参是实参的别名。
    
    这种方案的结果是，函数可能会修改作为参数传入的可变对象，但是无法修改那些对象的标识（即不能把一个对象替换成另一个对象） 。      
    示例8-11 中有个简单的函数， 它在参数上调用 += 运算符。 分别把数字、 列表和元组传给那个函数，
    实际传入的实参会以不同的方式受到影响。
    
    示例 8-11 函数可能会修改接收到的任何可变对象
    
        >>> def f(a, b):
        ...     a += b
        ...     return a
        ...
        >>> x = 1
        >>> y = 2
        >>> f(x, y)
        3>
        >> x, y ➊
        (1, 2)
        >>> a = [1, 2]
        >>> b = [3, 4]
        >>> f(a, b)
        [1, 2, 3, 4]
        >>> a, b ➋
        ([1, 2, 3, 4], [3, 4])
        >>> t = (10, 20)
        >>> u = (30, 40)
        >>> f(t, u)
        (10, 20, 30, 40)
        >>> t, u ➌
        ((10, 20), (30, 40))  
        
        ❶ 数字 x 没变。      
        ❷ 列表 a 变了。
        ❸ 元组 t 没变。
    
    8.4.1 不要使用可变类型作为参数的默认值:
    
        可选参数可以有默认值， 这是 Python 函数定义的一个很棒的特性， 这样
        我们的 API 在进化的同时能保证向后兼容。 然而， 我们应该避免使用可变的对象作为参数的默认值。    
    
        示例 8-12 一个简单的类， 说明可变默认值的危险:
        
            class HauntedBus:
                """备受幽灵乘客折磨的校车"""
                def __init__(self, passengers=[]): ➊
                    self.passengers = passengers ➋
                def pick(self, name):
                    self.passengers.append(name) ➌
                def drop(self, name):
                    self.passengers.remove(name)    
            
            ❶ 如果没传入 passengers 参数， 使用默认绑定的列表对象， 一开始是空列表。
            ❷ 这个赋值语句把 self.passengers 变成 passengers 的别名， 而没有传入 passengers 参数时，后者又是默认列表的别名。
            ❸ 在 self.passengers 上调用 .remove() 和 .append() 方法时， 修改的其实是默认列表， 它是函数对象的一个属性。
        
        示例 8-13 备受幽灵乘客折磨的校车:
            
            >>> bus1 = HauntedBus(['Alice', 'Bill'])
            >>> bus1.passengers
            ['Alice', 'Bill']
            >>> bus1.pick('Charlie')
            >>> bus1.drop('Alice')
            >>> bus1.passengers ➊
            ['Bill', 'Charlie']
            >>> bus2 = HauntedBus() ➋
            >>> bus2.pick('Carrie')
            >>> bus2.passengers
            ['Carrie']
            >>> bus3 = HauntedBus() ➌
            >>> bus3.passengers ➍
            ['Carrie']
            >>> bus3.pick('Dave')
            >>> bus2.passengers ➎
            ['Carrie', 'Dave']
            >>> bus2.passengers is bus3.passengers ➏
            True
            >>> bus1.passengers ➐
            ['Bill', 'Charlie']
            
            ❶ 目前没什么问题， bus1 没有出现异常。
            ❷ 一开始， bus2 是空的， 因此把默认的空列表赋值给self.passengers。
            ❸ bus3 一开始也是空的， 因此还是赋值默认的列表。
            ❹ 但是默认列表不为空！
            ❺ 登上 bus3 的 Dave 出现在 bus2 中。
            ❻ 问题是， bus2.passengers 和 bus3.passengers 指代同一个列表。
            ❼ 但 bus1.passengers 是不同的列表。
            
        问题在于， 没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列表。
        这种问题很难发现。 如示例 8-13 所示， 实例化 HauntedBus 时， 如果
        传入乘客， 会按预期运作。 但是不为 HauntedBus 指定乘客的话， 奇怪
        的事就发生了， 这是因为 self.passengers 变成了 passengers 参数
        默认值的别名。 出现这个问题的根源是， 默认值在定义函数时计算（通
        常在加载模块时） ， 因此默认值变成了函数对象的属性。 因此， 如果默
        认值是可变对象， 而且修改了它的值， 那么后续的函数调用都会受到影响。    
        
  
    8.4.2 防御可变参数:
        
        如果定义的函数接收可变参数， 应该谨慎考虑调用方是否期望修改传入的参数。
        除非这个方法确实想修改通过参数传入的对象， 否则在类中直接把参数赋值给实例变量之前一定要三思， 
        因为这样会为参数对象创建别名。 如果不确定， 那就创建副本。 这样客户会少些麻烦。
        
        def __init__(self, passengers=None):
            if passengers is None:
                self.passengers = []
            else:
                self.passengers = list(passengers) ➊
           
        ➊ 创建 passengers 列表的副本； 如果不是列表， 就把它转换成列表


"""8.5 del 和垃圾回收"""
    
    对象绝对不会自行销毁；然而，无法得到对象时，可能会被当作垃圾回收。
    
    del 语句删除名称， 而不是对象。 del 命令可能会导致对象被当作垃圾回收， 
    但是仅当删除的变量保存的是对象的最后一个引用， 或者无法得到对象时。 
    重新绑定也可能会导致对象的引用数量归零， 导致对象被销毁。

"""8.6 弱作用"""

    正是因为有引用， 对象才会在内存中存在。 当对象的引用数量归零后，垃圾回收程序会把对象销毁。 
    但是， 有时需要引用对象， 而不让对象存在的时间超过所需时间。 这经常用在缓存中。        

    弱引用不会增加对象的引用数量。 引用的目标对象称为所指对象（referent）。 
    因此我们说， 弱引用不会妨碍所指对象被当作垃圾回收。    
    弱引用在缓存应用中很有用，因为我们不想仅因为被缓存引用着而始终保存缓存对象。

    8.6.1 WeakValueDictionary简介：
        WeakValueDictionary 类实现的是一种可变映射， 里面的值是对象的弱引用。 
        被引用的对象在程序中的其他地方被当作垃圾回收后， 对应的键会自动从 WeakValueDictionary 中删除。 
        因此， WeakValueDictionary 经常用于缓存。
           
        示例 8-18 实现一个简单的类， 表示各种奶酪：
        
            class Cheese:
            def __init__(self, kind):
                self.kind = kind
            def __repr__(self):
                return 'Cheese(%r)' % self.kind        
        
            >>> import weakref
            >>> stock = weakref.WeakValueDictionary() ➊
            >>> catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
            ... Cheese('Brie'), Cheese('Parmesan')]
            ...
            >>> for cheese in catalog:
            ...     stock[cheese.kind] = cheese ➋
            ...
            >>> sorted(stock.keys())
            ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit'] ➌
            >>> del catalog
            >>> sorted(stock.keys())
            ['Parmesan'] ➍
            >>> del cheese
            >>> sorted(stock.keys())
            []
            
            ❶ stock 是 WeakValueDictionary 实例。
            ❷ stock 把奶酪的名称映射到 catalog 中 Cheese 实例的弱引用上。
            ❸ stock 是完整的。
            ❹ 删除 catalog 之后， stock 中的大多数奶酪都不见了， 这是WeakValueDictionary 的预期行为。
            为什么不是全部呢？
                临时变量引用了对象， 这可能会导致该变量的存在时间比预期长。
                通常，这对局部变量来说不是问题， 因为它们在函数返回时会被销毁。
    
"""8.7 Python对不可变类型施加的把戏"""

    我惊讶地发现， 对元组 t 来说， t[:] 不创建副本， 而是返回同一个对象的引用。 
    此外， tuple(t) 获得的也是同一个元组的引用。    
        
        >>> t1 = (1, 2, 3)
        >>> t2 = tuple(t1)
        >>> t2 is t1 ➊
        True
        >>> t3 = t1[:]
        >>> t3 is t1 ➋
        True    
        
        ❶ t1 和 t2 绑定到同一个对象。
        ❷ t3 也是

        str、 bytes 和 frozenset 实例也有这种行为。
    
    示例 8-21 字符串字面量可能会创建共享的对象:
    
        >>> t1 = (1, 2, 3)
        >>> t3 = (1, 2, 3) # ➊
        >>> t3 is t1 # ➋
        False
        >>> s1 = 'ABC'
        >>> s2 = 'ABC' # ➌
        >>> s2 is s1 # ➍
        True     
        
        ❶ 新建一个元组。
        ❷ t1 和 t3 相等， 但不是同一个对象。
        ❸ 再新建一个字符串。
        ❹ 奇怪的事发生了， a 和 b 指代同一个字符串。
        
    共享字符串字面量是一种优化措施， 称为驻留（interning）。
    千万不要依赖字符串或整数的驻留！ 比较字符串或整数是否相等时， 应该使用 ==， 而不是 is。 
    驻留是 Python 解释器内部使用的一个特性。     

"""8.8 本章小结"""

    每个 Python 对象都有标识、 类型和值。 只有对象的值会不时变化。
    
    变量保存的是引用， 这一点对 Python 编程有很多实际的影响：
    
        1、简单的赋值不创建副本。
        
        2、对 += 或 *= 所做的增量赋值来说， 如果左边的变量绑定的是不可变对象， 会创建新对象； 如果是可变对象， 会就地修改。
        
        3、为现有的变量赋予新值， 不会修改之前绑定的变量。 这叫重新绑定： 现在变量绑定了其他对象。 
           如果变量是之前那个对象的最后一个引用， 对象会被当作垃圾回收。
        
        4、函数的参数以别名的形式传递， 这意味着， 函数可能会修改通过参数传入的可变对象。 这一行为无法避免， 除非在本地创建副本， 
           或者使用不可变对象（例如， 传入元组， 而不传入列表） 。
        
        5、使用可变类型作为函数参数的默认值有危险， 因为如果就地修改了参数， 默认值也就变了， 这会影响以后使用默认值的调用。    

                    
"---------------------------------------------------------------------"

                     第九章   符合 python 风格的对象

    绝对不要使用两个前导下划线， 这是很烦人的自私行为。
    
    得益于 Python 数据模型， 自定义类型的行为可以像内置类型那样自然。
    实现如此自然的行为， 靠的不是继承， 而是鸭子类型（duck typing）    


"""9.1 对象表示形式"""
    
    每门面向对象的语言至少都有一种获取对象的字符串表示形式的标准方式。python 提供了两种方式。
    
        repr() : 以便于开发者理解的方式返回对象的字符串表示形式。
        str()  : 以便于用户理解的方式返回对象的字符串表示形式。
        正如你所知， 我们要实现 __repr__ 和 __str__ 特殊方法， 为 repr()和 str() 提供支持。     

    为了给对象提供其他的表示形式， 还会用到另外两个特殊方法：__bytes__ 和 __format__。
        
        __bytes__ 方法与 __str__ 方法类似： bytes() 函数调用它获取对象的字节序列表示形式。
        __format__ 方法会被内置的 format() 函数和 str.format() 方法调用， 使用特殊的格式代码显示对象的字符串表示形式。
    
    
"""9.2 再谈向量类"""     
    
    示例 9-2 vector2d_v0.py： 目前定义的都是特殊方法
        
        from array import array
        import math
        class Vector2d:
            typecode = 'd' ➊
            def __init__(self, x, y):
                self.x = float(x) ➋
                self.y = float(y)
            def __iter__(self):
                return (i for i in (self.x, self.y)) ➌
            def __repr__(self):
                class_name = type(self).__name__
                return '{}({!r}, {!r})'.format(class_name, *self) ➍
            def __str__(self):
                return str(tuple(self)) ➎    
            def __bytes__(self):
                return (bytes([ord(self.typecode)]) + ➏
                bytes(array(self.typecode, self))) ➐
            def __eq__(self, other):
                return tuple(self) == tuple(other) ➑
            def __abs__(self):
                return math.hypot(self.x, self.y) ➒
            def __bool__(self):
                return bool(abs(self)) ➓
        
        ❶ typecode 是类属性， 在 Vector2d 实例和字节序列之间转换时使用。
        ❷ 在 __init__ 方法中把 x 和 y 转换成浮点数， 尽早捕获错误， 以防调用 Vector2d 函数时传入不当参数。
        ❸ 定义 __iter__ 方法， 把 Vector2d 实例变成可迭代的对象， 这样才能拆包（例如， x, y = my_vector）。 
            这个方法的实现方式很简单，直接调用生成器表达式一个接一个产出分量。
        ❹ __repr__ 方法使用 {!r} 获取各个分量的表示形式， 然后插值， 构成一个字符串； 
            因为 Vector2d 实例是可迭代的对象， 所以 *self 会把x 和 y 分量提供给 format 函数。
        ❺ 从可迭代的 Vector2d 实例中可以轻松地得到一个元组， 显示为一个有序对。
        ❻ 为了生成字节序列， 我们把 typecode 转换成字节序列， 然后……
        ❼ ……迭代 Vector2d 实例， 得到一个数组， 再把数组转换成字节序列。
        ❽ 为了快速比较所有分量， 在操作数中构建元组。 对 Vector2d 实例来说， 可以这样做， 不过仍有问题。 参见下面的警告。
        ❾ 模是 x 和 y 分量构成的直角三角形的斜边长。
        ❿ __bool__ 方法使用 abs(self) 计算模， 然后把结果转换成布尔值， 因此， 0.0 是 False， 非零值是 True。

"""9.3 备选构造方法"""

    我们可以把 Vector2d 实例转换成字节序列了； 同理， 也应该能从字节序列转换成 Vector2d 实例。 
    在标准库中探索一番之后， 我们发现array.array 有个类方法 .frombytes 正好符合需求。 
    下面在 vector2d_v1.py（见示例 9-3） 中为 Vector2d 定义一个同名类方法。
    
    示例 9-3  这段代码只列出了frombytes 类方法:
    
        @classmethod ➊
        def frombytes(cls, octets): ➋
            typecode = chr(octets[0]) ➌
            memv = memoryview(octets[1:]).cast(typecode) ➍
            return cls(*memv) ➎           
    
        ❶ 类方法使用 classmethod 装饰器修饰。
        ❷ 不用传入 self 参数； 相反， 要通过 cls 传入类本身。
        ❸ 从第一个字节中读取 typecode。
        ❹ 使用传入的 octets 字节序列创建一个 memoryview， 然后使用typecode 转换。
        ❺ 拆包转换后的 memoryview， 得到构造方法所需的一对参数。
 
        
"""9.4 classmethod 与staticmethod """

    classmethod: 定义操作类，而不是操作实例的方法。classmethod 改变了调用方法的方式，因此类方法的第一个参数是类本身，而不是实例。
    staticmethod:  装饰器也会改变方法的调用方式， 但是第一个参数不是特殊的值。 
                   其实， 静态方法就是普通的函数， 只是碰巧在类的定义体中， 而不是在模块层定义。 
                   
        示例 9-4 比较 classmethod 和 staticmethod 的行为:
            
            >>> class Demo:
            ... @classmethod
            ... def klassmeth(*args):
            ...     return args # ➊
            ... @staticmethod
            ... def statmeth(*args):
            ...     return args # ➋
            ...
            >>> Demo.klassmeth() # ➌
            (<class '__main__.Demo'>,)
            >>> Demo.klassmeth('spam')
            (<class '__main__.Demo'>, 'spam')
            >>> Demo.statmeth() # ➍
            ()
            >>> Demo.statmeth('spam')
            ('spam',)
            
            ❶ klassmeth 返回全部位置参数。
            ❷ statmeth 也是。
            ❸ 不管怎样调用 Demo.klassmeth， 它的第一个参数始终是 Demo 类。
            ❹ Demo.statmeth 的行为与普通的函数相似。
                  
                          
"""9.5 格式化显示"""       
      
    内置的 format() 函数和str.format()方法把各个类型的格式化方式委托给相应的 .__format__(format_spec) 方法。 
    format_spec 是格式说明符， 它是：
        format(my_obj, format_spec) 的第二个参数， 或者
        str.format() 方法的格式字符串， {} 里代换字段中冒号后面的部分。
        
        >>> brl = 1/2.43 # BRL到USD的货币兑换比价
        >>> brl
        0.4115226337448559
        >>> format(brl, '0.4f') # ➊
        '0.4115'
        >>> '1 BRL = {rate:0.2f} USD'.format(rate=brl) # ➋
        '1 BRL = 0.41 USD   
        
    ❶ 格式说明符是 '0.4f'。
    
    ❷ 格式说明符是 '0.2f'。 代换字段中的 'rate' 子串是字段名称， 与格式说明符无关， 
      但是它决定把 .format() 的哪个参数传给代换字段。        
    
    第 2 条标注指出了一个重要知识点： '{0.mass:5.3e}' 这样的格式字符串其实包含两部分， 
    冒号左边的 '0.mass' 在代换字段句法中是字段名， 冒号后面的 '5.3e' 是格式说明符。 
    格式说明符使用的表示法叫格式规范微语言。
    
    格式规范微语言为一些内置类型提供了专用的表示代码。 比如，b 和 x分别表示二进制和十六进制的 int 类型， 
    f 表示小数形式的 float 类型， 而 % 表示百分数形式：
    
        >>> format(42, 'b')
        '101010'
        >>> format(2/3, '.1%')
        '66.7%'    
            
    格式规范微语言是可扩展的， 因为各个类可以自行决定如何解释format_spec 参数。 
    例如， datetime 模块中的类， 它们的__format__ 方法使用的格式代码与 strftime() 函数一样。 
    下面是内置的 format() 函数和 str.format() 方法的几个示例：    
        
        >>> from datetime import datetime
        >>> now = datetime.now()
        >>> format(now, '%H:%M:%S')
        '18:49:05'
        >>> "It's now {:%I:%M %p}".format(now)
        "It's now 06:49 PM"   
    
    如果类没有定义 __format__ 方法， 从 object 继承的方法会返回str(my_object)。
    我们为 Vector2d 类定义了 __str__ 方法， 因此可以这样做：
        
        >>> v1 = Vector2d(3, 4)
        >>> format(v1)
        '(3.0, 4.0)'   
     
    然而， 如果传入格式说明符， object.__format__ 方法会抛出TypeError：
    
        >>> format(v1, '.3f')
        Traceback (most recent call last):
        ...
        TypeError: non-empty format string passed to object.__format__
    
    示例 9-6 Vector2d.__format__ 方法， 第 2 版， 现在能计算极坐标了:
        
        def __format__(self, fmt_spec=''):
            if fmt_spec.endswith('p'): ➊
                fmt_spec = fmt_spec[:-1] ➋
                coords = (abs(self), self.angle()) ➌
                outer_fmt = '<{}, {}>' ➍
            else:
                coords = self ➎
                outer_fmt = '({}, {})' ➏
            components = (format(c, fmt_spec) for c in coords) ➐
            return outer_fmt.format(*components) ➑    
    
        ❶ 如果格式代码以 'p' 结尾， 使用极坐标。
        ❷ 从 fmt_spec 中删除 'p' 后缀。
        ❸ 构建一个元组， 表示极坐标： (magnitude, angle)。
        ❹ 把外层格式设为一对尖括号。
        ❺ 如果不以 'p' 结尾， 使用 self 的 x 和 y 分量构建直角坐标。
        ❻ 把外层格式设为一对圆括号。
        ❼ 使用各个分量生成可迭代的对象， 构成格式化字符串。
        ❽ 把格式化字符串代入外层格式。
    
"""9.6 可散列的Vector2d """  
    
    按照定义，目前 Vector2d 实例是不可散列的， 因此不能放入集合（set）中：
        
        >>> v1 = Vector2d(3, 4)
        >>> hash(v1)
        Traceback (most recent call last):
        ...
        TypeError: unhashable type: 'Vector2d'
        >>> set([v1])
        Traceback (most recent call last):
        ...
        TypeError: unhashable type: 'Vector2d'
        
    为了把 Vector2d 实例变成可散列的，必须使用 __hash__ 方法（还需要 __eq__ 方法，前面已经实现了）此外， 还要让向量不可变，     
    
    示例 9-7 vector2d_v3.py： 这里只给出了让 Vector2d 不可变的代码：
    
        class Vector2d:
            typecode = 'd'
            
            def __init__(self, x, y):
                self.__x = float(x) ➊     
                self.__y = float(y)
            @property ➋
            def x(self): ➌
                return self.__x ➍
            @property ➎
            def y(self):
                return self.__y
            def __iter__(self):
                return (i for i in (self.x, self.y)) ➏
      
        ❶ 使用两个前导下划线（尾部没有下划线， 或者有一个下划线），把属性标记为私有的。
        ❷ @property 装饰器把读值方法标记为特性。
        ❸ 读值方法与公开属性同名， 都是 x。
        ❹ 直接返回 self.__x。
        ❺ 以同样的方式处理 y 特性。
        ❻ 需要读取 x 和 y 分量的方法可以保持不变， 通过 self.x 和 self.y读取公开特性， 而不必读取私有属性， 
          因此上述代码清单省略了这个类的其他代码。
    
    注意，我们让这些向量不可变是有原因的， 因为这样才能实现__hash__ 方法。 这个方法应该返回一个整数， 
    理想情况下还要考虑对象属性的散列值（__eq__ 方法也要使用） ， 因为相等的对象应该具有相同的散列值。
    
    要想创建可散列的类型， 不一定要实现特性， 也不一定要保护实例属性。 
    只需正确地实现 __hash__ 和 __eq__ 方法即可。 但是， 实例的散列值绝不应该变化， 因此我们借机提到了只读特性。
     
"""9.7 Python 的私有属性和受保护的属性"""

    Python 不能像 Java 那样使用 private 修饰符创建私有属性， 
    但是Python 有个简单的机制， 能避免子类意外覆盖“私有”属性。        
    
    举个例子。 有人编写了一个名为 Dog 的类， 这个类的内部用到了 mood
    实例属性， 但是没有将其开放。 现在， 你创建了 Dog 类的子
    类： Beagle。 如果你在毫不知情的情况下又创建了名为 mood 的实例属性， 
    那么在继承的方法中就会把 Dog 类的 mood 属性覆盖掉。 这是个难以调试的问题。
    
    为了避免这种情况， 如果以 __mood 的形式（两个前导下划线， 尾部没有或最多有一个下划线） 命名实例属性， 
    Python 会把属性名存入实例的__dict__ 属性中， 而且会在前面加上一个下划线和类名。 
    因此， 对Dog 类来说， __mood 会变成 _Dog__mood； 对 Beagle 类来说， 会变成_Beagle__mood。 这个语言特性叫名称改写（name mangling） 。
    
    不是所有 Python 程序员都喜欢名称改写功能， 也不是所有人都喜欢self.__x 这种不对称的名称。 
    有些人不喜欢这种句法， 他们约定使用一个下划线前缀编写“受保护”的属性（如 self._x）。 
    批评使用两个下划线这种改写机制的人认为， 应该使用命名约定来避免意外覆盖属性。
    
    绝对不要使用两个前导下划线， 这是很烦人的自私行为。 如果担心名称冲突， 应该明确使用一种名称改写方式
    （如_MyThing_blahblah） 。 这其实与使用双下划线一样， 不过自己定的规则比双下划线易于理解。
    
    Python 解释器不会对使用单个下划线的属性名做特殊处理， 不过这是很多 Python 程序员严格遵守的约定， 
    他们不会在类外部访问这种属性。遵守使用一个下划线标记对象的私有属性很容易， 就像遵守使用全大写字母编写常量那样容易。
    
    Python 文档的某些角落把使用一个下划线前缀标记的属性称为“受保护的”属性。 
    使用 self._x 这种形式保护属性的做法很常见， 但是很少有人把这种属性叫作“受保护的”属性。 
    有些人甚至将其称为“私有”属性。
    
"""9.8 使用 __slots__ 类属性节省空间"""   

    默认情况下， Python 在各个实例中名为 __dict__ 的字典里存储实例属性。
    为了使用底层的散列表提升访问速度， 字典会消耗大量内存。 
    如果要处理数百万个属性不多的实例， 通过 __slots__类属性， 能节省大量内存， 
    方法是让解释器在元组中存储实例属性， 而不用字典。
    
    继承自超类的 __slots__ 属性没有效果。 Python 只会使用各个类中定义的 __slots__ 属性。
    
    定义 __slots__ 的方式是， 创建一个类属性， 使用 __slots__ 这个名字， 
    并把它的值设为一个字符串构成的可迭代对象， 其中各个元素表示各个实例属性。 
    我喜欢使用元组， 因为这样定义的 __slots__ 中所含的信息不会变化
    
    例 9-11 vector2d_v3_slots.py： 只在 Vector2d 类中添加了__slots__ 属性:
    
        class Vector2d:
            __slots__ = ('__x', '__y')
            typecode = 'd'     
    
    在类中定义 __slots__ 属性的目的是告诉解释器： “这个类中的所有实例属性都在这儿了！”这样， 
    Python 会在各个实例中使用类似元组的结构存储实例变量， 从而避免使用消耗内存的 __dict__ 属性。 
    如果有数百万个实例同时活动， 这样做能节省大量内存。
    
    在类中定义 __slots__ 属性之后， 实例不能再有__slots__ 中所列名称之外的其他属性。 
    这只是一个副作用， 不是__slots__ 存在的真正原因。 不要使用 __slots__ 属性禁止类的用户新增实例属性。 
    __slots__ 是用于优化的， 不是为了约束程序员。
    
    综上， __slots__ 属性有些需要注意的地方， 而且不能滥用， 不能使用
    它限制用户能赋值的属性。 处理列表数据时 __slots__ 属性最有用，
    例如模式固定的数据库记录， 以及特大型数据集。 然而， 如果你经常处
    理大量数据， 一定要了解一下 NumPy（http://www.numpy.org） ； 此外，
    数据分析库 pandas（http://pandas.pydata.org） 也值得了解， 这个库可以
    处理非数值数据， 而且能导入 / 导出很多不同的列表数据格式。 
    
    __slots__ 的问题:
    
        总之， 如果使用得当， __slots__ 能显著节省内存， 不过有几点要注意。
            (1) 每个子类都要定义 __slots__ 属性， 因为解释器会忽略继承的__slots__ 属性。
            (2) 实例只能拥有 __slots__ 中列出的属性， 除非把 '__dict__' 加入 __slots__ 中（这样做就失去了节省内存的功效） 。     
            (3) 如果不把 '__weakref__' 加入 __slots__， 实例就不能作为弱引用的目标。 
    
"""9.9 覆盖类属性"""       

    Python 有个很独特的特性： 类属性可用于为实例属性提供默认值。
    

"---------------------------------------------------------------------"

                     第十章   序列的修改、散列和切片

    不要检查它是不是鸭子、 它的叫声像不像鸭子、 它的走路姿势像不像鸭子，等等。
    具体检查什么取决于你想使用语言的哪些行为。

"""10.2 Vector 类 第1版: 与Vector2d类兼容"""

    示例 10-2 vector_v1.py： 从 vector2d_v1.py 衍生而来:
    
        from array import array
        import reprlib
        import math
        class Vector:
            typecode = 'd'
            def __init__(self, components):
                self._components = array(self.typecode, components) ➊
            def __iter__(self):
                return iter(self._components) ➋
            def __repr__(self):
                components = reprlib.repr(self._components) ➌
                components = components[components.find('['):-1] ➍
                return 'Vector({})'.format(components)
            def __str__(self):
                return str(tuple(self))
        
            def __bytes__(self):
                return (bytes([ord(self.typecode)]) +bytes(self._components)) ➎
            def __eq__(self, other):
                return tuple(self) == tuple(other)
            def __abs__(self):
                return math.sqrt(sum(x * x for x in self)) ➏
            def __bool__(self):
                return bool(abs(self))
            @classmethod
            def frombytes(cls, octets):
                typecode = chr(octets[0])
                memv = memoryview(octets[1:]).cast(typecode)
                return cls(memv) ➐        
            
        ❶ self._components 是“受保护的”实例属性， 把 Vector 的分量保存在一个数组中。
        ❷ 为了迭代， 我们使用 self._components 构建一个迭代器。iter() 函数和 __iter__ 方法在第 14 章讨论。
        ❸ 使用 reprlib.repr() 函数获取 self._components 的有限长度表示形式（如 array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])） 。
        ❹ 把字符串插入 Vector 的构造方法调用之前， 去掉前面的array('d' 和后面的 )。
        ❺ 直接使用 self._components 构建 bytes 对象。
        ❻ 不能使用 hypot 方法了， 因此我们先计算各分量的平方之和， 然后再使用 sqrt 方法开平方。
        ❼ 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行： 直接把 memoryview 传给构造方法， 不用像前面那样使用 * 拆包。    
        
        我使用 reprlib.repr 的方式需要做些说明。 这个函数用于生成大型结构或递归结构的安全表示形式， 
        它会限制输出字符串的长度， 用 '...'截断的部分。
        
"""10.3 协议和鸭子类型 """  

    在面向对象编程中，协议是非正式的接口，只在文档中定义，在代码中不定义。 
    例如， Python 的序列协议只需要 __len__ 和 __getitem__ 两个方法。 
    任何类（如 Spam） ， 只要使用标准的签名和语义实现了这两个方法， 就能用在任何期待序列的地方。 
    Spam 是不是哪个类的子类无关紧要， 只要提供了所需的方法即可。               
       
        import collections
        Card = collections.namedtuple('Card', ['rank', 'suit'])
        class FrenchDeck:
            ranks = [str(n) for n in range(2, 11)] + list('JQKA')
            suits = 'spades diamonds clubs hearts'.split()
            def __init__(self):
                self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
            def __len__(self):
                return len(self._cards)
            def __getitem__(self, position):
                return self._cards[position]
    
    协议是非正式的， 没有强制力， 因此如果你知道类的具体使用场景， 通常只需要实现一个协议的部分。 
    例如， 为了支持迭代， 只需实现__getitem__ 方法， 没必要提供 __len__ 方法

"""10.4 Vector类第2版： 可切片的序列"""

    
    10.4.1 切片原理:
    
        示例 10-4 了解 __getitem__ 和切片的行为
        
            >>> class MySeq:
            ... def __getitem__(self, index):
            ... return index # ➊
            ...
            >>> s = MySeq()
            >>> s[1] # ➋
            1
            >> s[1:4] # ➌
            slice(1, 4, None)
            >>> s[1:4:2] # ➍
            slice(1, 4, 2)
            >>> s[1:4:2, 9] # ➎
            (slice(1, 4, 2), 9)
            >>> s[1:4:2, 7:9] # ➏
            (slice(1, 4, 2), slice(7, 9, None))         

            ❶ 在这个示例中， __getitem__ 直接返回传给它的值。
            ❷ 单个索引， 没什么新奇的。
            ❸ 1:4 表示法变成了 slice(1, 4, None)。
            ❹ slice(1, 4, 2) 的意思是从 1 开始， 到 4 结束， 步幅为 2。
            ❺ 神奇的事发生了： 如果 [] 中有逗号， 那么 __getitem__ 收到的是元组。
            ❻ 元组中甚至可以有多个切片对象。
        
        示例 10-5 查看 slice 类的属性:
        
            >>> slice # ➊
            <class 'slice'>
            >>> dir(slice) # ➋
            ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattribute__', '__gt__',
            '__hash__', '__init__', '__le__', '__lt__', '__ne__',
            '__new__', '__reduce__', '__reduce_ex__', '__repr__',
            '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
            'indices', 'start', 'step', 'stop']
            
            ❶ slice 是内置的类型（2.4.2 节首次出现） 。
            ❷ 通过审查 slice， 发现它有 start、 stop 和 step 数据属性， 以及indices 方法。
            
        调用 dir(slice) 得到的结果中有个 indices 属性，这个方法有很大的作用， 但是鲜为人知。 
        help(slice.indices) 给出的信息如下。
            
            S.indices(len) -> (start, stop, stride)
            
        给定长度为 len 的序列， 计算 S 表示的扩展切片的起始（start）和结尾（stop） 索引， 
        以及步幅（stride）。 超出边界的索引会被截掉， 这与常规切片的处理方式一样。
                
        换句话说， indices 方法开放了内置序列实现的棘手逻辑， 用于优雅地处理缺失索引和负数索引， 
        以及长度超过目标序列的切片。 这个方法会“整顿”元组， 把 start、 stop 和 stride 都变成非负数， 
        而且都落在指定长度序列的边界内。        
                 
    10.4.2 能处理切片的__getitem__方法:
        
        示例 10-6 列出了让 Vector 表现为序列所需的两个方法： __len__ 和__getitem__
        
         
        def __len__(self):
            return len(self._components)
        def __getitem__(self, index):
            cls = type(self) ➊
            if isinstance(index, slice): ➋
                return cls(self._components[index]) ➌
            elif isinstance(index, numbers.Integral): ➍
                return self._components[index] ➎
            else:
                msg = '{cls.__name__} indices must be integers'
                raise TypeError(msg.format(cls=cls)) ➏
                    
        ❶ 获取实例所属的类（即 Vector） ， 供后面使用。
        ❷ 如果 index 参数的值是 slice 对象……
        ❸ ……调用类的构造方法， 使用 _components 数组的切片构建一个新Vector 实例。
        ❹ 如果 index 是 int 或其他整数类型
        ❺ ……那就返回 _components 中相应的元素。
        ❻ 否则， 抛出异常。
        
"---------------------------------------------------------------------"

                     第十一章  接口: 从协议到抽象基类
    协议：
        在 python 中，协议是一个或一组方法。例如 python 的序列协议包含 len 和 getitem 两个方法。
        上下文管理协议包含 enter 和 exit 两个方法。
        
        我们把协议定义为非正式的接口， 是让 Python 这种动态类型语言实现多态的方式。
        
    鸭子类型（duck typing）：
        
        多态的一种形式，这种形式中，对象的类型无关紧要，只要实现了特定的协议即可。
        
        例子：
                class Eg1(object):
                    def __init__(self, text):
                        self.txt = text
                        self.sub_text = text.split('')
                    
                    def __getitem__(self,index):
                        return self.sub_text[index]
                        
                    def __len__(slef):
                        return len(self.sub_txt)
                        
        示例 中Eg1类 实现了 len 和 getitem两个方法，也就是实现了序列协议，那么它的表现就和序列类似。
        通过输出结果就能看出，Eg1的对象可以计算长度，也可以循环处理，这和正常的序列没什么不同。
        因此我们可以把Eg1称为一个鸭子类型，即 只关注它是否实现了相应的协议，不关注它的类型。
    
    抽象基类:
    
        抽象基类就是定义各种方法而不做具体实现的类，任何继承自抽象基类的类必须实现这些方法，否则无法实例化。
        
        那么抽象基类这样实现的目的是什么呢？ 假设我们在写一个关于动物的代码。
        涉及到的动物有鸟，狗，牛。首先鸟，狗，牛都是属于动物的。
        既然是动物那么肯定需要吃饭，发出声音。但是具体到鸟，狗，牛来说吃饭和声音肯定是不同的。
        需要具体去实现鸟，狗，牛吃饭和声音的代码。
        概括一下抽象基类的作用：定义一些共同事物的规则和行为。

        例子：
            
            class Animal(abc.ABC):
                
                @abstractmethod
                def eat(self):
                
                @abstractmethod
                def voice(self):
                
            calss Dog(Animal):
                def eat(self):    
                    print('Dog eating....')
                def voice(self):
                     print('wow....')    
                     
            class Bird(Animal):
                def eat(self):
                    print('Bird eating....')
                def voice(self):
                     print('jiji....')
        
        示例定义了一个抽象基类 Animal，它包含两个抽象方法eat和voice，Dog和Bird都继承了Animal，
        并各自实现了具体的eat和voice方法。Dog和Bird在实例化之后调用相同的方法，但是却有不同的输出，
        这就是最简单的抽象基类的用法。

        注意，自己定义的抽象基类要继承 abc.ABC（abc.ABC 是 Python 3.4 新增的类，python2的语法不是这样的）。
        抽象方法使用 @abstractmethod 装饰器标记，而且定义体中通常只有文档字符串。

        除了继承，还有一种方法可以将类和抽象基类关联起来


"""11.1 Python文化中的接口和协议 """                                        
    
    接口在动态类型语言中是怎么运作的呢？ 
    
    首先， 基本的事实是，Python 语言没有 interface 关键字， 而且除了抽象基类， 每个类都有接口：
    类实现或继承的公开属性（方法或数据属性） ， 包括特殊方法， 如__getitem__ 或 __add__。        
            
    按照定义， 受保护的属性和私有属性不在接口中：即便“受保护的”属性
    也只是采用命名约定实现的（单个前导下划线）；私有属性可以轻松地
    访问，原因也是如此。不要违背这些约定。
    
    另一方面， 不要觉得把公开数据属性放入对象的接口中不妥， 因为如果需要， 
    总能实现读值方法和设值方法， 把数据属性变成特性， 使用obj.attr 句法的客户代码不会受到影响。
    
    示例 11-1 vector2d_v0.py： x 和 y 是公开数据属性：
    
        class Vector2d(object):
            typecode = 'd'
            def __init__(self, x, y):
                self.x = float(x)
                self.y = float(y)
                
            def __iter__(self):
                return (i for i in (self.x, self.y))
    
    示例 11-2 vector2d_v3.py： 使用特性实现 x 和 y 变成了只读特性:
    
        class Vector2d(object):
            typecode = 'd'
            
            def __init__(self, x, y):
                self._x = float(x)
                self._y = float(y)
                
            @property
            def x(self):
                return self._x
                      
            @property
            def y(self):
                return self._y
              
            def __iter__(self):
                return (i for i in (self.x, self.y))
                
    关于接口， 这里有个实用的补充定义：对象公开方法的子集，让对象在系统中扮演特定的角色。 
    Python 文档中的“文件类对象”或“可迭代对象”就是这个意思， 这种说法指的不是特定的类。   
    接口是实现特定角色的方法集合， 这样理解正是 Smalltalk 程序员所说的协议， 其他动态语
    言社区都借鉴了这个术语。 协议与继承没有关系。 一个类可能会实现多个接口， 从而让实例扮演多个角色。
                    
    协议是接口， 但不是正式的（只由文档和约定定义） ， 因此协议不能像
    正式接口那样施加限制（本章后面会说明抽象基类对接口一致性的强制） 。 一个类可能只实现部分接口， 
    这是允许的。 有时， 某些 API 只要求“文件类对象”返回字节序列的 .read() 方法。 
    在特定的上下文中可能需要其他文件操作方法， 也可能不需要。 

"""11.2 Python 喜欢序列"""
    
    Python 数据模型的哲学是尽量支持基本协议。 对序列来说， 即便是最简单的实现， Python 也会力求做到最好。    
    如果没有 __iter__ 和 __contains__方法， Python 会调用 __getitem__ 方法， 设法让迭代和 in 运算符可用。

    示例 11-4 实现序列协议的 FrenchDeck 类
        
        import collections
        Card = collections.namedtuple('Card', ['rank', 'suit'])
        class FrenchDeck:
            ranks = [str(n) for n in range(2, 11)] + list('JQKA')
            suits = 'spades diamonds clubs hearts'.split()
            
            def __init__(self):
                self._cards = [Card(rank, suit) for suit in self.suits
                              for rank in self.ranks]
            def __len__(self):
                return len(self._cards)
        
            def __getitem__(self, position):
                return self._cards[position]    
        


"""11.3 使用猴子补丁在运行时实现协议 """

    示例 11-4 中的 FrenchDeck 类有个重大缺陷： 无法洗牌。 几年前， 第一次编写 FrenchDeck 示例时，
    我实现了 shuffle 方法。 后来， 我对Python 风格有了深刻理解， 
    我发现如果 FrenchDeck 实例的行为像序列， 那么它就不需要 shuffle 方法，因为已经有 random.shuffle 函数可用.
    
    如果遵守既定协议， 很有可能增加利用现有的标准库和第三方代码的可能性， 这得益于鸭子类型。
    
    标准库中的 random.shuffle 函数用法如下：
        
        >>> from random import shuffle
        >>> l = list(range(10))
        >>> shuffle(l)
        >>> l
        [5, 2, 9, 7, 8, 3, 1, 4, 0, 6]
        
    示例 11-5 random.shuffle 函数不能打乱 FrenchDeck 实例:
    
        >>> from random import shuffle
        >>> from frenchdeck import FrenchDeck
        >>> deck = FrenchDeck()
        >>> shuffle(deck)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File ".../python3.3/random.py", line 265, in shuffle
        x[i], x[j] = x[j], x[i]
        TypeError: 'FrenchDeck' object does not support item assignment             
    
    错误消息相当明确， “'FrenchDeck' object does not support itemassignment”
    （'FrenchDeck' 对象不支持为元素赋值） 。 这个问题的原因是， 
    shuffle 函数要调换集合中元素的位置， 而 FrenchDeck 只实现了不可变的序列协议。 
    可变的序列还必须提供 __setitem__ 方法。        

    示例 11-6 为FrenchDeck 打猴子补丁， 把它变成可变的， 让random.shuffle 函数能处理.
    
        >>> def set_card(deck, position, card): ➊
        ... deck._cards[position] = card
        ...
        >>> FrenchDeck.__setitem__ = set_card ➋
        >>> shuffle(deck) ➌
        >>> deck[:5]
        [Card(rank='3', suit='hearts'), Card(rank='4', suit='diamonds'), Card(rank='4',
        suit='clubs'), Card(rank='7', suit='hearts'), Card(rank='9', suit='spades')]
        
        ❶ 定义一个函数， 它的参数为 deck、 position 和 card。
        ❷ 把那个函数赋值给 FrenchDeck 类的 __setitem__ 属性。
        ❸ 现在可以打乱 deck 了， 因为 FrenchDeck 实现了可变序列协议所需的方法。 

    这里的关键是， set_card 函数要知道 deck 对象有一个名为 _cards 的
    属性， 而且 _cards 的值必须是可变序列。 然后， 我们把 set_card 函
    数赋值给特殊方法 __setitem__， 从而把它依附到 FrenchDeck 类
    上。 这种技术叫猴子补丁： 在运行时修改类或模块， 而不改动源码。 猴
    子补丁很强大， 但是打补丁的代码与要打补丁的程序耦合十分紧密， 而
    且往往要处理隐藏和没有文档的部分。
    
    除了举例说明猴子补丁之外， 示例 11-6 还强调了协议是动态
    的： random.shuffle 函数不关心参数的类型， 只要那个对象实现了部
    分可变序列协议即可。 即便对象一开始没有所需的方法也没关系， 后来
    再提供也行。
    
    目前， 本章讨论的主题是“鸭子类型”： 对象的类型无关紧要， 只要实现了特定的协议即可。

"""11.4 Alex Martelli 的水禽 """
    
    鸭子类型，对 Python 来说， 这基本上是指避免使用 isinstance 检查对象的类型（更别提 type(foo) is bar 这种更糟的检查方式了，
    这样做没有任何好处， 甚至禁止最简单的继承方式） 。    
    
    总的来说， 鸭子类型在很多情况下十分有用； 但是在其他情况下，随着发展， 通常有更好的方式。 事情是这样的…… 
    
    近代， 属和种（包括但不限于水禽所属的鸭科） 基本上是根据表型系统学（phenetics） 分类的。 
    表征学关注的是形态和举止的相似性……主要是表型系统学特征。 因此使用“鸭子类型”比喻是贴切的。
    
    然而， 平行进化往往会导致不相关的种产生相似的特征， 形态和举止方面都是如此， 
    但是生态位的相似性是偶然的，不同的种仍属不同的生态位。编程语言中也有这种“偶然的相似性”， 
    比如说下述经典的面向对象编程示例:
    
        class Artist:
            def draw(self): ...
        class Gunslinger:
            def draw(self): ...
        class Lottery:
            def draw(self): ...       

    显然， 只因为 x 和 y 两个对象刚好都有一个名为 draw 的方法， 而且调用时不用传入参数， 
    即 x.draw() 和 y.draw()， 远远不能确保二者可以相互调用， 或者具有相同的抽象。 
    也就是说， 从这样的调用中不能推导出语义相似性。 相反， 我们需要一位渊博的程序员
    主动把这种等价维持在一定层次上。

    生物（和其他学科） 遇到的这个问题， 迫切需要（从很多方面来说， 是催生） 表征学之外的分类方式解决， 
    即支序系统学（cladistics） 。 这种分类学主要根据从共同祖先那里继承的特征分类， 而不是单独进化的特征。
    
    因此， 参照水禽的分类学演化， 在鸭子类型的基础上增加白鹅类型（goose typing）.
    白鹅类型指， 只要 cls 是抽象基类， 即 cls 的元类是abc.ABCMeta， 就可以使用 isinstance(obj, cls)。
    
    使用 isinstance 和 issubclass 测试抽象基类更为人接受。过去，这两个函数用来测试鸭子类型，但用于抽象基类会更灵活。
    然而， 即便是抽象基类， 也不能滥用 isinstance 检查， 用得多了可能导致代码异味， 即表明面向对象设计得不好。
    
    示例 11-7 使用鸭子类型处理单个字符串或由字符串组成的可迭代:
    
        try: ➊
            field_names = field_names.replace(',', ' ').split() ➋
        except AttributeError: ➌
            pass➍
        field_names = tuple(field_names) ➎
            
        ❶ 假设是单个字符串（EAFP 风格， 即“取得原谅比获得许可容易”） 。
        ❷ 把逗号替换成空格， 然后拆分成名称列表。
        ❸ 抱歉， field_names 看起来不像是字符串……没有 .replace 方法， 或者返回值不能使用 .split 方法拆分。
        ❹ 假设已经是由名称组成的可迭代对象了。
        ❺ 为了确保的确是可迭代对象， 也为了保存一份副本， 使用所得值创建一个元组。  
    
    抽象基类是用于封装框架引入的一般性概念和抽象的， 例如“一个序列”和“一个确切的数”。 
    （读者） 基本上不需要自己编写新的抽象基类， 只要正确使用现有的抽象基类， 
    就能获得 99.9% 的好处，而不用冒着设计不当导致的巨大风险。    
              
    
"""11.5 定义抽象基类的子类"""   
    
    import collections
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    
    class FrenchDeck2(collections.MutableSequence):
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'spades diamonds clubs hearts'.split()
        
        def __init__(self):
            self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
        def __len__(self):
            return len(self._cards)

        def __getitem__(self, position):
            return self._cards[position]

        def __setitem__(self, position, value): # ➊
            self._cards[position] = value

        def __delitem__(self, position): # ➋
            del self._cards[position]
    
        def insert(self, position, value): # ➌
            self._cards.insert(position, value)    
        
    ❶ 为了支持洗牌， 只需实现 __setitem__ 方法
    ❷ 但是继承 MutableSequence 的类必须实现 __delitem__ 方法， 这是 MutableSequence 类的一个抽象方法。
    ❸ 此外， 还要实现 insert 方法， 这是 MutableSequence 类的第三个抽象方法。             
                

"""11.6 标准库中的抽象基类 """    
    
    11.6.1 collections.abc模块中的抽象基类
    
        Iterable、 Container 和 Sized:
            各个集合应该继承这三个抽象基类， 或者至少实现兼容的协议。 
            Iterable 通过 __iter__ 方法支持迭代， Container 通过__contains__ 方法支持 in 运算符， 
            Sized 通过 __len__ 方法支持len() 函数。
            
        Sequence、 Mapping 和 Set:
        
            这三个是主要的不可变集合类型， 而且各自都有可变的子类。 
            
        Callable 和 Hashable:
            
            这两个抽象基类与集合没有太大的关系， 只不过因为collections.abc 
            是标准库中定义抽象基类的第一个模块， 而它们又太重要了， 
            因此才把它们放到 collections.abc 模块中。    
                        
            这两个抽象基类的主要作用是为内置函数 isinstance 提供支持， 
            以一种安全的方式判断对象能不能调用或散列。
                              

"---------------------------------------------------------------------"

                     第十二章  继承的优缺点
  
"""12.1 子类化内置类型很麻烦 """  
    
    在 Python 2.2 之前， 内置类型（如 list 或 dict） 不能子类化。 
    在Python 2.2 之后， 内置类型可以子类化了， 但是有个重要的注意事项：
    内置类型（使用 C 语言编写）不会调用用户定义的类覆盖的特殊方法。
    
    至于内置类型的子类覆盖的方法会不会隐式调用， CPython 没有制定官方规则。 
    基本上， 内置类型的方法不会调用子类覆盖的方法。例如， 
    dict 的子类覆盖的 __getitem__() 方法不会被内置类型的get() 方法调用。 
  
    示例 12-1 内置类型 dict 的 __init__ 和 __update__ 方法会忽略我们覆盖的 __setitem__ 方法：
    
        >>> class DoppelDict(dict):
        ... def __setitem__(self, key, value):
        ... super().__setitem__(key, [value] * 2) # ➊
        ...
        >>> dd = DoppelDict(one=1) # ➋
        >>> dd
        {'one': 1}
        >>> dd['two'] = 2 # ➌
        >>> dd
        {'one': 1, 'two': [2, 2]}
        >>> dd.update(three=3) # ➍
        >>> dd
        {'three': 3, 'one': 1, 'two': [2, 2]}   
        
        
        ❶ DoppelDict.__setitem__ 方法会重复存入的值（只是为了提供易于观察的效果） 。 它把职责委托给超类。
        ❷ 继承自 dict 的 __init__ 方法显然忽略了我们覆盖的 __setitem__方法： 'one' 的值没有重复。
        ❸ [] 运算符会调用我们覆盖的 __setitem__ 方法， 按预期那样工作： 'two' 对应的是两个重复的值， 即 [2, 2]。
        ❹ 继承自 dict 的 update 方法也不使用我们覆盖的 __setitem__ 方法：'three' 的值没有重复。
        
    原生类型的这种行为违背了面向对象编程的一个基本原则： 始终应该从实例（self） 所属的类开始搜索方法， 
    即使在超类实现的类中调用也是如此。 
    
    不只实例内部的调用有这个问题（self.get() 不调用self.__getitem__()） ， 
    内置类型的方法调用的其他类的方法， 如果被覆盖了， 也不会被调用。 
    
    示例 12-2 dict.update 方法会忽略 AnswerDict.__getitem__方法
        
        >>> class AnswerDict(dict):
        ... def __getitem__(self, key): # ➊
        ... return 42
        ...
        >>> ad = AnswerDict(a='foo') # ➋
        >>> ad['a'] # ➌
        42
        >>> d = {}
        >>> d.update(ad) # ➍
        >>> d['a'] # ➎
        'foo'
        >>> d
        {'a': 'foo'}       
                              
        ❶ 不管传入什么键， AnswerDict.__getitem__ 方法始终返回 42。
        ❷ ad 是 AnswerDict 的实例， 以 ('a', 'foo') 键值对初始化。
        ❸ ad['a'] 返回 42， 这与预期相符。
        ❹ d 是 dict 的实例， 使用 ad 中的值更新 d。
        ❺ dict.update 方法忽略了 AnswerDict.__getitem__ 方法。 
                            
    直接子类化内置类型（如 dict、 list 或 str） 容易出错，因为内置类型的方法通常会忽略用户覆盖的方法。 
    不要子类化内置类型， 用户自己定义的类应该继承 collections 模块例如UserDict、 UserList 和 UserString，
    这些类做了特殊设计， 因此易于扩展。
        
    示例 12-3 DoppelDict2 和 AnswerDict2 能像预期那样使用， 因为它们扩展的是 UserDict，而不是 dict：
    
        >>> import collections
        >>>
        >>> class DoppelDict2(collections.UserDict):
        ... def __setitem__(self, key, value):
        ... super().__setitem__(key, [value] * 2)
        ...
        >>> dd = DoppelDict2(one=1)
        >>> dd
        {'one': [1, 1]}
        >>> dd['two'] = 2
        >>> dd
        {'two': [2, 2], 'one': [1, 1]}
        >>> dd.update(three=3)
        >>> dd
        {'two': [2, 2], 'three': [3, 3], 'one': [1, 1]}
        >>>
        >>> class AnswerDict2(collections.UserDict):
        ... def __getitem__(self, key):
        ... return 42
        ...        
        >>> ad = AnswerDict2(a='foo')
        >>> ad['a']
        42
        >>> d = {}
        >>> d.update(ad)
        >>> d['a']
        42
        >>> d
        {'a': 42}
        
    综上， 本节所述的问题只发生在 C 语言实现的内置类型内部的方法委托上， 而且只影响直接继承内置类型的用户自定义类。 
    如果子类化使用Python 编写的类， 如 UserDict 或 MutableMapping， 就不会受此影响。
    
    
"""12.2 多重继承和方法解析顺序"""

    任何实现多重继承的语言都要处理潜在的命名冲突， 这种冲突由不相关的祖先类实现同名方法引起。 这种冲突称为“菱形问题” 
    
    示例 12-4 diamond.py： 图 12-1 中的 A、 B、 C 和 D 四个类:
        
        class A:
            def ping(self):
                print('ping:', self)
        
        class B(A):
            def pong(self):
                print('pong:', self)
        
        class C(A):
            def pong(self):
                print('PONG:', self)
        
        class D(B, C):
        
            def ping(self):
                super().ping()
                print('post-ping:', self)
            
            def pingpong(self):
                self.ping()
                super().ping()
                self.pong()
                super().pong()
                C.pong(self)
    
    注意， B 和 C 都实现了 pong 方法， 二者之间唯一的区别是， C.pong 方法输出的是大写的 PONG。
    
    示例 12-5 在 D 实例上调用 pong 方法的两种方式
        
        >>> from diamond import *
        >>> d = D()
        >>> d.pong() # ➊
        pong: <diamond.D object at 0x10066c278>
        >>> C.pong(d) # ➋
        PONG: <diamond.D object at 0x10066c278>
        
        ❶ 直接调用 d.pong() 运行的是 B 类中的版本。
        ❷ 超类中的方法都可以直接调用， 此时要把实例作为显式参数传入        
    
    Python 能区分 d.pong() 调用的是哪个方法， 是因为 Python 会按照特定的顺序遍历继承图。 这个顺序叫方法解析顺序.
    类都有一个名为 __mro__ 的属性， 它的值是一个元组， 按照方法解析顺序列出各个超类， 
    从当前类一直向上， 直到object 类。 D 类的 __mro__ 属性如下:
        
        >>> D.__mro__
        (<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>,
        <class 'diamond.A'>, <class 'object'>)
            
    若想把方法调用委托给超类， 推荐的方式是使用内置的 super() 函数。
    在 Python 3 中， 这种方式变得更容易了， 如示例 12-4 中 D 类的pingpong 方法所示。 
    然而， 有时可能需要绕过方法解析顺序， 直接调用某个超类的方法——这样做有时更方便。 
    例如， D.ping 方法可以这样写：
        
        def ping(self):
            A.ping(self) # 而不是super().ping()
            print('post-ping:', self) 
                        
       
"""12.4 处理多重继承"""
    
    继承有很多用途， 而多重继承增加了可选方案和复杂度。 使用多重继承容易得出令人费解和脆弱的设计。 
    我们还没有完整的理论， 下面是避免把类图搅乱的一些建议。   
    
        01. 把接口继承和实现继承区分开
            使用多重继承时， 一定要明确一开始为什么创建子类。 主要原因可能有：
                继承接口， 创建子类型， 实现“是什么”关系
                继承实现， 通过重用避免代码重复
            其实这两条经常同时出现， 不过只要可能， 一定要明确意图。 通过
            继承重用代码是实现细节， 通常可以换用组合和委托模式。 而接口继承则是框架的支柱。

        02. 使用抽象基类显式表示接口
            现代的 Python 中， 如果类的作用是定义接口， 应该明确把它定义为
            抽象基类。 Python 3.4 及以上的版本中， 我们要创建 abc.ABC 或其他抽象基类的子类。
        
        03. 通过混入重用代码
            
            如果一个类的作用是为多个不相关的子类提供方法实现， 从而实现
            重用， 但不体现“是什么”关系， 应该把那个类明确地定义为混入类
            （mixin class） 。 从概念上讲， 混入不定义新类型， 只是打包方
            法， 便于重用。 混入类绝对不能实例化， 而且具体类不能只继承混
            入类。 混入类应该提供某方面的特定行为， 只实现少量关系非常紧
            密的方法

          
            
"---------------------------------------------------------------------"

                     第十三章  正确重载运算符
  
    有些事情让我不安， 比如运算符重载。 我决定不支持运算符重载，
    这完全是个人选择， 因为我见过太多 C++ 程序员滥用它。---java之父James Gosling。
    
    运算符重载的作用是让用户定义的对象使用中缀运算符或一元运算符。
    在python中，函数调用(())、属性访问(.)、元素访问/切片([])也是运算符。
    
    13.1 运算符重载基础:
    
        不能重载内置类型的运算符
        不能新建运算符， 只能重载现有的
        某些运算符不能重载——is、 and、 or 和 not（不过位运算符&、 | 和 ~ 可以）      
  
    13.2 一元运算符:
    
        - (__neg__) :  一元取负运算符。如果 x 是 -2，那么 -x == 2
        
        + (__pos__) :  一元取正算术运算符。 
        
        ~ (__invert__): 对整数按位取反， 定义为 ~x == -(x+1)。 如果 x 是 2， 那么 ~x== -3。
            
        支持一元运算符很简单， 只需实现相应的特殊方法。 这些特殊方法只有一个参数， self。 
        然后， 使用符合所在类的逻辑实现。 不过， 要遵守运算符的一个基本规则： 始终返回一个新对象。 
        也就是说， 不能修改self， 要创建并返回合适类型的新实例。    
    
        示例 13-1 vector_v6.py： 把一元运算符 - 和 + 添加到示例 10-16中
            
            def __abs__(self):
                return math.sqrt(sum(x * x for x in self))
                
            def __neg__(self):
                return Vector(-x for x in self)  ➊
                
            def __pos__(slef):
                return Vector(self)        ➋
                
        ❶ 为了计算 -v， 构建一个新 Vector 实例， 把 self 的每个分量都取反。
        ❷ 为了计算 +v， 构建一个新 Vector 实例， 传入 self 的各个分量。            

                   
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

    当我在自己的程序中发现用到了模式， 我觉得这就表明某个地方出错了。 程序的形式应该仅仅反映它所要解决的问题。 
    代码中其他任何外加的形式都是一个信号， （至少对我来说） 表明我对问题的抽象还不够深——这通常
    意味着自己正在手动完成的事情， 本应该通过写代码来让宏的扩展自动实现。 ——Paul Graham Lisp 黑客和风险投资人
    
    迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，
    即按需一次获取一个数据项。这就是迭代器模式（Iterator pattern） 。

    所有生成器都是迭代器， 因为生成器完全实现了迭代器接口。 不过， 
    根据《设计模式： 可复用面向对象软件的基础》 一书的定义， 迭代器用于从集合中取出元素；
    而生成器用于“凭空”生成元素。 

    14.1 Sentence类第1版： 单词序列：
        
        我们向这个类的构造方法传入包含一些文本的字符串， 然后可以逐个单词迭代。
        
        示例 14-1 sentence.py： 把句子划分为单词序列：
        
            import re
            import reprlib
            
            RE_WORD = re.compile('\w+')
            
            class Sentence:
                def __init__(self, text):
                    self.text = text
                    self.worlds = RE_WORD.findall(text)  ➊
                    
                def __getitem__(self, index):
                    return self.words[index]  ➋
                    
                def __len__(self):  ➌
                    return len(slef.worlds)
                    
                def __repr__(slef):
                    return 'Sentence(%s)'% reprlib.repr(self.text)  ➍
                    
                    
            ❶ re.findall 函数返回一个字符串列表， 里面的元素是正则表达式的全部非重叠匹配。
            ❷ self.words 中保存的是 .findall 函数返回的结果， 因此直接返回指定索引位上的单词。
            ❸ 为了完善序列协议， 我们实现了 __len__ 方法； 不过， 为了让对象可以迭代， 没必要实现这个方法。
            ❹ reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串表示形式。        
                          
        示例 14-2 测试 Sentence 实例能否迭代:
            
            s = Sentence('"The time has come", the Walrus said,')
            for word in s:
                print(word)
                
            打印结果为：
                The
                time
                has
                come
                the
                Walrus
                said
                
            print(list(s))
                ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
    
        序列可以迭代的原因： iter函数:
            解释器需要迭代对象 x 时， 会自动调用 iter(x)。
            内置的 iter 函数有以下作用。
        
            (1) 检查对象是否实现了 __iter__ 方法， 如果实现了就调用它， 获取一个迭代器。
            
            (2) 如果没有实现 __iter__ 方法， 但是实现了 __getitem__ 方法，
                Python 会创建一个迭代器， 尝试按顺序（从索引 0 开始） 获取元素。
            
            (3) 如果尝试失败， Python 抛出 TypeError 异常， 通常会提示“C object
                is not iterable”（C 对象不可迭代） ， 其中 C 是目标对象所属的类。
        
        任何 Python 序列都可迭代的原因是， 它们都实现了 __getitem__ 方法。 
        其实， 标准的序列也都实现了 __iter__ 方法， 因此你也应该这么做。 

        11.2 节提到过， 这是鸭子类型（duck typing） 的极端形式： 不仅要实现特殊的 __iter__ 方法， 
        还要实现 __getitem__ 方法， 而且__getitem__ 方法的参数是从 0 开始的整数（int） ， 
        这样才认为对象是可迭代的。
        
        在白鹅类型（goose-typing） 理论中， 可迭代对象的定义简单一些， 不过没那么灵活： 
        如果实现了 __iter__ 方法， 那么就认为对象是可迭代的。 
    
    14.2 可迭代的对象与迭代器的对比:
        
        可迭代的对象:
            使用 iter 内置函数可以获取迭代器的对象。 如果对象实现了能返回迭代器的 __iter__ 方法， 
            那么对象就是可迭代的。 序列都可以迭代； 实现了 __getitem__ 方法， 
            而且其参数是从零开始的索引， 这种对象也可以迭代。   
            
        我们要明确可迭代的对象和迭代器之间的关系： Python 从可迭代的对象中获取迭代器。
        具体的 Iterable.__iter__ 方法应该返回一个 Iterator 实例。 
        具体的 Iterator 类必须实现 __next__ 方法。 Iterator.__iter__ 方法直接返回实例本身。
        
        下面是一个简单的 for 循环， 迭代一个字符串。 这里， 字符串 'ABC'是可迭代的对象。 
        背后是有迭代器的， 只不过我们看不到：
        
            >>> s = 'ABC'
            >>> for char in s:
            ... print(char)
            ...
            ABC
        
        如果没有 for 语句， 不得不使用 while 循环模拟， 要像下面这样写：        
            
            >>> s = 'ABC'
            >>> it = iter(s) # ➊
            >>> while True:
            ...     try:
            ...         print(next(it)) # ➋
            ...     except StopIteration: # ➌
            ...         del it # ➍
            ...         break # ➎
            ...
            ABC                   

        标准的迭代器接口有两个方法。
        
            __next__:返回下一个可用的元素， 如果没有元素了， 抛出 StopIteration异常。
            __iter__:返回 self， 以便在应该使用可迭代对象的地方使用迭代器， 例如在 for 循环中。     

        迭代器：
            
            迭代器是这样的对象： 实现了无参数的 __next__ 方法， 返回序列中的下一个元素； 
            如果没有元素了， 那么抛出 StopIteration 异常。
            Python 中的迭代器还实现了 __iter__ 方法， 因此迭代器也可以迭代。
            
    14.3 Sentence类第2版： 典型的迭代器：
    
        示例 14-4 中定义的 Sentence 类可以迭代， 因为它实现了特殊的__iter__ 方法， 
        构建并返回一个 SentenceIterator 实例。 《设计模式： 可复用面向对象软件的基础》 
        一书就是这样描述迭代器设计模式的。
        
        这里之所以这么做， 是为了清楚地说明可迭代的对象和迭代器之间的重要区别， 以及二者之间的联系。    

        示例 14-4 sentence_iter.py： 使用迭代器模式实现 Sentence 类：
        
        import re
        import reprlib
        RE_WORD = re.compile('\w+')
        
        class Sentence:
            def __init__(self, text):
                self.text = text
                self.words = RE_WORD.findall(text)
            def __repr__(self):
                return 'Sentence(%s)' % reprlib.repr(self.text)
            def __iter__(self): ➊
                return SentenceIterator(self.words) ➋
        class SentenceIterator:
            def __init__(self, words):
                self.words = words ➌    
                self.index = 0 ➍
                
            def __next__(self):
                try:
                    word = self.words[self.index] ➎
                except IndexError:
                    raise StopIteration() ➏
                self.index += 1 ➐
                return word ➑
            def __iter__(self): ➒
                return self

        ❶ 与前一版相比， 这里只多了一个 __iter__ 方法。 这一版没有__getitem__ 方法， 
            为的是明确表明这个类可以迭代， 因为实现了__iter__ 方法。
        ❷ 根据可迭代协议， __iter__ 方法实例化并返回一个迭代器。
        ❸ SentenceIterator 实例引用单词列表。
        ❹ self.index 用于确定下一个要获取的单词。
        ❺ 获取 self.index 索引位上的单词。
        ❻ 如果 self.index 索引位上没有单词， 那么抛出 StopIteration 异常。
        ❼ 递增 self.index 的值。
        ❽ 返回单词。
        ❾ 实现 self.__iter__ 方法。
        
        注意， 对这个示例来说， 其实没必要在 SentenceIterator 类中实现__iter__ 方法， 
        不过这么做是对的， 因为迭代器应该实现 __next__和 __iter__ 两个方法， 
        而且这么做能让迭代器通过issubclass(SentenceInterator, abc.Iterator) 测试。 如果让
        SentenceIterator 类继承 abc.Iterator 类， 那么它会继承abc.Iterator.__iter__ 这个具体方法。        

        把Sentence变成迭代器： 坏主意:
        
            构建可迭代的对象和迭代器时经常会出现错误， 原因是混淆了二者。 
            要知道， 可迭代的对象有个 __iter__ 方法， 每次都实例化一个新的迭代器； 
            而迭代器要实现 __next__ 方法， 返回单个元素， 此外还要实现__iter__ 方法，返回迭代器本身。   
            
            因此， 迭代器可以迭代， 但是可迭代的对象不是迭代器。
            
        《设计模式： 可复用面向对象软件的基础》 一书讲解迭代器设计模式时， 在“适用性”一节中说:
        迭代器模式可用来：
            访问一个聚合对象的内容而无需暴露它的内部表示
            支持对聚合对象的多种遍历
            为遍历不同的聚合结构提供一个统一的接口（即支持多态迭代）
        
        为了“支持多种遍历”， 必须能从同一个可迭代的实例中获取多个独立的迭代器， 
        而且各个迭代器要能维护自身的内部状态， 因此这一模式正确的实现方式是， 
        每次调用 iter(my_iterable) 都新建一个独立的迭代器。 
        这就是为什么这个示例需要定义 SentenceIterator 类。    
            
        可迭代的对象一定不能是自身的迭代器。 也就是说， 可迭代的对象
        必须实现 __iter__ 方法， 但不能实现 __next__ 方法。
        
        另一方面， 迭代器应该一直可以迭代。 迭代器的 __iter__ 方法应该返回自身。                       
                         
    14.4 Sentence类第3版： 生成器函数:
    
        实现相同功能， 但却符合 Python 习惯的方式是， 用生成器函数代替SentenceIterator 类。
        
        示例 14-5 sentence_gen.py： 使用生成器函数实现 Sentence 类:
        
        import re
        import reprlib
        
        RE_WORD = re.complie('\w+')
        
        class Sentence(object):
            def __init__(self, text):
                self.text = text
                self.words = RE_WORD.findall(text)
                
            def __repr__(self):
                return 'Sentence(%s)' % reprlib.repr(self.text)
                
            def __iter__(slef):
                for word in self.words:   ➊
                    yield word  ➋
                return  ➌
                
        ❶ 迭代 self.words。
        ❷ 产出当前的 word。
        ❸ 这个 return 语句不是必要的； 这个函数可以直接“落空”， 自动返回。 
            不管有没有 return 语句， 生成器函数都不会抛出 StopIteration异常， 
            而是在生成完全部值之后会直接退出。
        不用再单独定义一个迭代器类！    
        
        生成器函数的工作原理:
            只要 Python 函数的定义体中有 yield 关键字， 该函数就是生成器函数。 
            调用生成器函数时， 会返回一个生成器对象。 也就是说， 生成器函数是生成器工厂。              
          
            >>> def gen_123(): # ➊
            ... yield 1 # ➋
            ... yield 2
            ... yield 3
            ...
            >>> gen_123 # doctest: +ELLIPSIS
            <function gen_123 at 0x...> # ➌
            >>> gen_123() # doctest: +ELLIPSIS
            <generator object gen_123 at 0x...> # ➍
            >>> for i in gen_123(): # ➎
            ... print(i)
            123>
            >> g = gen_123() # ➏
            >>> next(g) # ➐
            1>
            >> next(g)
            2>
            >> next(g)
            3>
            >> next(g) # ➑
            Traceback (most recent call last):
            ...
            StopIteration
            
            ❶ 只要 Python 函数中包含关键字 yield， 该函数就是生成器函数。
            ❷ 生成器函数的定义体中通常都有循环， 不过这不是必要条件； 这里我重复使用 3 次 yield。
            ❸ 仔细看， gen_123 是函数对象。
            ❹ 但是调用时， gen_123() 返回一个生成器对象。
            ❺ 生成器是迭代器， 会生成传给 yield 关键字的表达式的值。
            ❻ 为了仔细检查， 我们把生成器对象赋值给 g。
            ❼ 因为 g 是迭代器， 所以调用 next(g) 会获取 yield 生成的下一个元素。
            ❽ 生成器函数的定义体执行完毕后， 生成器对象会抛出StopIteration 异常。   
                         
        生成器函数会创建一个生成器对象， 包装生成器函数的定义体。 把生成器传给 next(...) 函数时，
        生成器函数会向前， 执行函数定义体中的下一个 yield 语句， 返回产出的值， 
        并在函数定义体的当前位置暂停。 最终， 函数的定义体返回时， 
        外层的生成器对象会抛出StopIteration 异常——这一点与迭代器协议一致。

    14.5 Sentence类第4版： 惰性实现:        
        
        设计 Iterator 接口时考虑到了惰性： next(my_iterator) 一次生成一个元素。 
        懒惰的反义词是急迫， 其实， 惰性求值（lazy evaluation） 
        和及早求值（eager evaluation） 是编程语言理论方面的技术术语。   
        
        示例 14-7 sentence_gen2.py： 在生成器函数中调用 re.finditer生成器函数， 
        实现 Sentence 类:
            
            import re
            import reprlib
            RE_WORD = re.compile('\w+')
            class Sentence:
                def __init__(self, text):
                    self.text = text ➊
                def __repr__(self):
                    return 'Sentence(%s)' % reprlib.repr(self.text    
                def __iter__(self):
                    for match in RE_WORD.finditer(self.text): ➋
                        yield match.group() ➌
            
            ❶ 不再需要 words 列表。
            ❷ finditer 函数构建一个迭代器， 包含 self.text 中匹配 RE_WORD的单词， 产出 MatchObject 实例。
            ❸ match.group() 方法从 MatchObject 实例中提取匹配正则表达式的具体文本。

    14.6 Sentence类第5版： 生成器表达式:
        
        生成器表达式可以理解为列表推导的惰性版本： 不会迫切地构建列表，而是返回一个生成器， 
        按需惰性生成元素。 也就是说， 如果列表推导是制造列表的工厂， 
        那么生成器表达式就是制造生成器的工厂。   
        
        示例 14-9 sentence_genexp.py： 使用生成器表达式实现 Sentence类:
        
            import re
            import reprlib
            RE_WORD = re.compile('\w+')
            class Sentence:
                def __init__(self, text):
                    self.text = text
                def __repr__(self):
                    return 'Sentence(%s)' % reprlib.repr(self.text)
                def __iter__(self):
                    return (match.group() for match in RE_WORD.finditer(self.text))
        
        这里不是生成器函数了（没有 yield） ， 而是使用生成器表达式构建生成器， 然后将其返回。
        不过， 最终的效果一样： 调用 __iter__ 方法会得到一个生成器对象。
        
    
    14.8 等差数列生成器:
        
        典型的迭代器模式作用很简单——遍历数据结构。
        内置的 range 函数用于生成有穷整数等差数列（Arithmetic Progression， AP） ， 
        itertools.count 函数用于生成无穷等差数列。
                
        >>> import itertools
        >>> gen = itertools.count(1, .5)
        >>> next(gen)
        1>
        >> next(gen)
        1.5
        >>> next(gen)
        2.0
        >>> next(gen)
        2.5 

    

"---------------------------------------------------------------------"

                     第十五章  上下文管理器和 else 块
    
    最终， 上下文管理器可能几乎与子程序（subroutine） 本身一样重要。 
    目前， 我们只了解了上下文管理器的皮毛……Basic 语言有with 语句， 而且很多语言都有。 
    但是， 在各种语言中 with 语句的作用不同， 而且做的都是简单的事， 
    虽然可以避免不断使用点号查找属性， 但是不会做事前准备和事后清理。 
    不要觉得名字一样， 就意味着作用也一样。 with 语句是非常了不起的特性。 
                            ——Raymond Hettinger 雄辩的 Python 布道者       
       
    with 语句和上下文管理器:
        
        with 语句会设置一个临时的上下文， 交给上下文管理器对象控制， 并且负责清理上下文。 
        这么做能避免错误并减少样板代码， 因此 API 更安全， 而且更易于使用。 
        除了自动关闭文件之外， with 块还有很多用途。    
        
    for、 while 和 try 语句的 else 子句:
    
        else 子句与 with 语句完全没有关系。
        
    15.1 先做这个， 再做那个： if语句之外的else块:
    
        这个语言特性不是什么秘密， 但却没有得到重视： else 子句不仅能在if 语句中使用， 
        还能在 for、 while 和 try 语句中使用。              
    
        for/else、 while/else 和 try/else 的语义关系紧密， 不过与if/else 差别很大。 
        起初， else 这个单词的意思阻碍了我对这些特性的理解， 但是最终我习惯了。
        else 子句的行为如下:
            for:
                仅当 for 循环运行完毕时（即 for 循环没有被 break 语句中止）才运行 else 块。
            while:
                仅当 while 循环因为条件为假值而退出时（即 while 循环没有被break 语句中止） 才运行 else 块。        
            try:
                仅当 try 块中没有异常抛出时才运行 else 块。 官方文档
                还指出： “else 子句抛出的异常不会由前面的 except 子句处理。”
        
        在所有情况下， 如果异常或者 return、 break 或 continue 语句导致
        控制权跳到了复合语句的主块之外， else 子句也会被跳过。        
                
    15.2 上下文管理器和with块：
    
        上下文管理器对象存在的目的是管理 with 语句， 就像迭代器的存在是为了管理 for 语句一样。
        
        with 语句的目的是简化 try/finally 模式。 这种模式用于保证一段代码运行完毕后执行某项操作， 
        即便那段代码由于异常、 return 语句或sys.exit() 调用而中止， 也会执行指定的操作。 
        finally 子句中的代码通常用于释放重要的资源， 或者还原临时变更的状态。
    
        上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。 with 语句开始运行时， 
        会在上下文管理器对象上调用 __enter__ 方法。 with 语句运行结束后， 
        会在上下文管理器对象上调用 __exit__ 方法， 以此扮演 finally 子句的角色。
    
  
       
                     
"---------------------------------------------------------------------"
                     
                     第十六章   协程

    如果 Python 书籍有一定的指导作用， 那么（协程就是） 文档最匮乏、 最鲜为人知的 Python 特性， 
    因此表面上看是最无用的特性。   ——David Beazley  Python 图书作者   
    
    字典为动词“to yield”给出了两个释义： 产出和让步。 对于 Python 生成器中的 yield 来说， 这两个含义都成立。 
    yield item 这行代码会产出一个值， 提供给 next(...) 的调用方； 此外， 还会作出让步， 
    暂停执行生成器， 让调用方继续工作， 直到需要使用另一个值时再调用next()。 调用方会从生成器中拉取值。

    从句法上看， 协程与生成器类似， 都是定义体中包含 yield 关键字的函数。 
    可是， 在协程中， yield 通常出现在表达式的右边（例如， datum = yield），可以产出值，
    也可以不产出——如果 yield关键字后面没有表达式， 那么生成器产出 None。 
    协程可能会从调用方接收数据， 不过调用方把数据提供给协程使用的是 
    .send(datum) 方法， 而不是 next(...) 函数。 通常，调用方会把值推送给协程。
    
    yield 关键字甚至还可以不接收或传出数据。 不管数据如何流动， yield 都是一种流程控制工具， 
    使用它可以实现协作式多任务： 协程可以把控制器让步给中心调度程序， 从而激活其他的协程。

    从根本上把 yield 视作控制流程的方式， 这样就好理解协程了。

    本章涵盖以下话题：
        生成器作为协程使用时的行为和状态
        使用装饰器自动预激协程
        调用方如何使用生成器对象的 .close() 和 .throw(...) 方法控制协程
        协程终止时如何返回值
        yield from 新句法的用途和语义
        使用案例——使用协程管理仿真系统中的并发活动

    16.1 生成器如何进化成协程：
        
        在Python 2.5之后，yield 关键字可以在表达式中使用， 而且生成器 API 中增加了.send(value)方法。 
        生成器的调用方可以使用 .send(...) 方法发送数据， 发送的数据会成为生成器函数中 yield 表达式的值。
        因此， 生成器可以作为协程使用。 协程是指一个过程， 这个过程与调用方协作， 产出由调用方提供的值。  
        
        现在， 生成器可以返回一个值； 以前， 如果在生成器中给 return语句提供值， 会抛出 SyntaxError 异常。
        
        新引入了 yield from 句法， 使用它可以把复杂的生成器重构成小型的嵌套生成器， 
        省去了之前把生成器的工作委托给子生成器所需的大量样板代码。
    
    16.2 用作协程的生成器的基本行为:
        
        示例 16-1 可能是协程最简单的使用演示:
            >>> def simple_coroutine(): # ➊
            ...     print('-> coroutine started')
            ...     x = yield # ➋
            ...     print('-> coroutine received:', x)
            ...
            >>> my_coro = simple_coroutine()
            >>> my_coro # ➌
            <generator object simple_coroutine at 0x100c2be10>
            >>> next(my_coro) # ➍
            -> coroutine started
            >>> my_coro.send(42) # ➎
            -> coroutine received: 42
            Traceback (most recent call last): # ➏
            ...
            StopIteration    
                
        ❶ 协程使用生成器函数定义： 定义体中有 yield 关键字。
        ❷ yield 在表达式中使用；如果协程只需从客户那里接收数据， 
          那么产出的值是 None——这个值是隐式指定的，因为 yield 关键字右边没有表达式。  
        ❸ 与创建生成器的方式一样， 调用函数得到生成器对象。
        ❹ 首先要调用 next(...) 函数，因为生成器还没启动，没在 yield 语句处暂停，所以一开始无法发送数据。
        ❺ 调用这个方法后，协程定义体中的 yield 表达式会计算出 42；
          现在，协程会恢复，一直运行到下一个 yield 表达式， 或者终止。       
        ❻ 这里， 控制权流动到协程定义体的末尾， 导致生成器像往常一样抛出 StopIteration 异常。

        协程可以身处四个状态中的一个。 当前状态可以使用:
        inspect.getgeneratorstate(...) 函数确定， 该函数会返回下述字符串中的一个。
            'GEN_CREATED' :等待开始执行。
            'GEN_RUNNING' :解释器正在执行。    
            'GEN_SUSPENDED' :在 yield 表达式处暂停。
            'GEN_CLOSED'：执行结束。 
        
        因为 send 方法的参数会成为暂停的 yield 表达式的值， 
        所以， 仅当协程处于暂停状态时才能调用 send 方法， 
        例如 my_coro.send(42)。 不过， 如果协程还没激活（即， 状态是 'GEN_CREATED'）情况就不同了。 
        因此， 始终要调用 next(my_coro) 激活协程——也可以调用my_coro.send(None)，效果一样。
    
        如果创建协程对象后立即把 None 之外的值发给它， 会出现下述错误：
            >>> my_coro = simple_coroutine()
            >>> my_coro.send(1729)
            Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            TypeError: can't send non-None value to a just-started generator    
        
        注意错误消息， 它表述得相当清楚。
            最先调用 next(my_coro) 函数这一步通常称为“预激”（prime） 协程
           （即，让协程向前执行到第一个 yield 表达式，准备好作为活跃的协程使用）。
           
        示例 16-2 产出两个值的协程：
            
            >>> def simple_coro2(a):
            ... print('-> Started: a =', a)
            ... b = yield a
            ... print('-> Received: b =', b)
            ... c = yield a + b
            ... print('-> Received: c =', c)
            ...
            >>> my_coro2 = simple_coro2(14)
            >>> from inspect import getgeneratorstate
            >>> getgeneratorstate(my_coro2) ➊
            'GEN_CREATED'
            >>> next(my_coro2) ➋
            -> Started: a = 14
            14
            >>> getgeneratorstate(my_coro2) ➌
            'GEN_SUSPENDED'
            >>> my_coro2.send(28) ➍
            -> Received: b = 28
            42
            >>> my_coro2.send(99) ➎
            -> Received: c = 99
            Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            StopIteration
            >>> getgeneratorstate(my_coro2) ➏
            'GEN_CLOSED'       
            
            ❶ inspect.getgeneratorstate 函数指明， 处于 GEN_CREATED 状态（即协程未启动）。           
            ❷ 向前执行协程到第一个 yield 表达式， 打印 -> Started: a = 14消息，然后产出 a 的值， 并且暂停， 等待为 b 赋值。
            ❸ getgeneratorstate 函数指明， 处于 GEN_SUSPENDED 状态（即协程在 yield 表达式处暂停）。
            ❹ 把数字 28 发给暂停的协程； 计算 yield 表达式， 得到 28， 然后把那个数绑定给 b。 
              打印 -> Received: b = 28 消息， 产出 a + b 的值(42), 然后协程暂停，等待为 c 赋值。
            ❺ 把数字 99 发给暂停的协程； 计算 yield 表达式， 得到 99， 然后把那个数绑定给 c。 
              打印 -> Received: c = 99 消息， 然后协程终止，导致生成器对象抛出 StopIteration 异常。
            ❻ getgeneratorstate 函数指明， 处于 GEN_CLOSED 状态（即协程执行结束） 。
        
        关键的一点是， 协程在 yield 关键字所在的位置暂停执行。 
        前面说过， 在赋值语句中， = 右边的代码在赋值之前执行。 
        因此， 对于 b =yield a 这行代码来说， 等到客户端代码再激活协程时才会设定 b 的值。 
        这种行为要花点时间才能习惯， 不过一定要理解， 这样才能弄懂异步编程中 yield 的作用（后文探讨） 。    
            
        simple_coro2 协程的执行过程分为 3 个阶段:
            (1) 调用 next(my_coro2)， 打印第一个消息， 然后执行 yield a， 产出数字 14。
            (2) 调用 my_coro2.send(28)， 把 28 赋值给 b， 打印第二个消息， 然后执行 yield a + b， 产出数字 42。
            (3) 调用 my_coro2.send(99)， 把 99 赋值给 c， 打印第三个消息， 协程终止。    
            
    16.3 示例： 使用协程计算移动平均值     
        
        示例 16-3 coroaverager0.py： 定义一个计算移动平均值的协程:
            def averager():
                total = 0.0
                count = 0
                average = None
                while True: ➊
                    term = yield average ➋
                    total += term
                    count += 1
                    average = total/count
                
            ➊ 这个无限循环表明， 只要调用方不断把值发给这个协程， 
              它就会一直接收值， 然后生成结果。 仅当调用方在协程上调用 .close() 方法，
              或者没有对协程的引用而被垃圾回收程序回收时， 这个协程才会终止。
            ➋ 这里的 yield 表达式用于暂停执行协程， 把结果发给调用方；
               还用于接收调用方后面发给协程的值， 恢复无限循环。
               
        使用协程的好处是， total 和 count 声明为局部变量即可， 无需使用实例属性或闭包在多次调用之间保持上下文。        
        
        示例 16-4 coroaverager0.py： 示例 16-3 中定义的移动平均值协程
            >>> coro_avg = averager() ➊
            >>> next(coro_avg) ➋
            >>> coro_avg.send(10) ➌
            10.0
            >>> coro_avg.send(30)
            20.0
            >>> coro_avg.send(5)
            15.0    
                    
            ❶ 创建协程对象。
            ❷ 调用 next 函数， 预激协程。
            ❸ 计算移动平均值： 多次调用 .send(...) 方法， 产出当前的平均值。
        
        调用 next(coro_avg) 函数后， 协程会向前执行到 yield 表达式， 
        产出 average 变量的初始值——None，因此不会出现在控制台中。 
        此时， 协程在 yield 表达式处暂停， 等到调用方发送值。 
        coro_avg.send(10) 那一行发送一个值， 激活协程，
        把发送的值赋给 term， 并更新 total、 count 和 average 三个变量的值， 
        然后开始 while 循环的下一次迭代， 产出 average 变量的值， 等待下一次为 term 变量赋值。
        
    16.4 预激协程的装饰器:
        
        如果不预激， 那么协程没什么用。 调用 my_coro.send(x) 之前， 
        记住一定要调用 next(my_coro)。 为了简化协程的用法， 有时会使用一个预激装饰器。
        
        示例 16-5 coroutil.py： 预激协程的装饰器:
        from functools import wraps
        def coroutine(func):
        
        """装饰器： 向前执行到第一个`yield`表达式， 预激`func`"""
        @wraps(func)
        def primer(*args,**kwargs): ➊
            gen = func(*args,**kwargs) ➋
            next(gen) ➌
            return gen ➍
        return primer    
         
        ❶ 把被装饰的生成器函数替换成这里的 primer 函数；调用 primer 函数时,返回预激后的生成器。
        ❷ 调用被装饰的函数， 获取生成器对象。
        ❸ 预激生成器。
        ❹ 返回生成器。    
        
    16.5 终止协程和异常处理:
        
        协程中未处理的异常会向上冒泡， 传给 next 函数或 send 方法的调用方（即触发协程的对象） 。
        这两个方法是 throw 和 close 处理异常：
        
        generator.throw(exc_type[, exc_value[, traceback]])
        
            致使生成器在暂停的 yield 表达式处抛出指定的异常。 如果生成器处理了抛出的异常， 
            代码会向前执行到下一个 yield 表达式， 而产出的值会成为调用 generator.throw 方法
            得到的返回值。 如果生成器没有处理抛出的异常， 异常会向上冒泡， 传到调用方的上下文中。    
            
        generator.close()
        
            致使生成器在暂停的 yield 表达式处抛出 GeneratorExit 异常。
            如果生成器没有处理这个异常， 或者抛出了 StopIteration 异常（通常是指运行到结尾） ， 
            调用方不会报错。 如果收到 GeneratorExit 异常， 生成器一定不能产出值， 
            否则解释器会抛出 RuntimeError 异常。生成器抛出的其他异常会向上冒泡， 传给调用方。   
             
        示例 16-8 coro_exc_demo.py： 学习在协程中处理异常的测试代码：
            
            class DemoException(Exception):
                """为这次演示定义的异常类型。 """
            def demo_exc_handling():
                print('-> coroutine started')
                while True:
                    try:
                        x = yield
                    except DemoException: ➊
                        print('*** DemoException handled. Continuing...')
                    else: ➋
                        print('-> coroutine received: {!r}'.format(x))
                raise RuntimeError('This line should never run.') ➌
            
            ❶ 特别处理 DemoException 异常。
            ❷ 如果没有异常， 那么显示接收到的值。
            ❸ 这一行永远不会执行。
        
    16.6 让协程返回值：
    
        示例 16-13 coroaverager2.py： 定义一个求平均值的协程， 让它返回一个结果：  
        from collections import namedtuple
        Result = namedtuple('Result', 'count average')
        
        def averager():
            total = 0.0
            count = 0
            average = None
            while True:
                term = yield
                if term is None:
                    break ➊
                total += term
                count += 1
                average = total/count
            return Result(count, average) ➋          
        
        ➊ 为了返回值， 协程必须正常终止； 因此， 这一版 averager 中有个条件判断，以便退出累计循环。
        ➋ 返回一个 namedtuple， 包含 count 和 average 两个字段。 在Python 3.3 之前， 如果生成器返回值， 解释器会报句法错误。        
        
        示例 16-14 coroaverager2.py： 说明 averager 行为的 doctest
        >>> coro_avg = averager()
        >>> next(coro_avg)
        >>> coro_avg.send(10) ➊
        >>> coro_avg.send(30)
        >>> coro_avg.send(6.5)
        >>> coro_avg.send(None) ➋
        Traceback (most recent call last):
        ...
        StopIteration: Result(count=3, average=15.5)    
        
        ❶ 这一版不产出值。
        ❷ 发送 None 会终止循环， 导致协程结束， 返回结果。 一如既往， 
          生成器对象会抛出 StopIteration 异常。 异常对象的 value 属性保存着返回的值
        
        示例 16-15 捕获 StopIteration 异常， 获取 averager 返回的值
        
        >>> coro_avg = averager()
        >>> next(coro_avg)
        >>> coro_avg.send(10)
        >>> coro_avg.send(30)
        >>> coro_avg.send(6.5)
        >>> try:
        ...     coro_avg.send(None)
        ... except StopIteration as exc:
        ...     result = exc.value
        ...
        >>> result
        Result(count=3, average=15.5) 
         
        获取协程的返回值虽然要绕个圈子， 但这是 PEP 380 定义的方式， 
        当我们意识到这一点之后就说得通了： yield from 结构会在内部自动捕获StopIteration 异常。 
        这种处理方式与 for 循环处理 StopIteration异常的方式一样：
        循环机制使用用户易于理解的方式处理异常。 
        对yield from 结构来说， 解释器不仅会捕获 StopIteration 异常， 
        还会把 value 属性的值变成 yield from 表达式的值。 
        可惜， 我们无法在控制台中使用交互的方式测试这种行为， 
        因为在函数外部使用 yieldfrom（以及 yield） 会导致句法出错。
        
    16.7 使用yield from:
        
        首先要知道， yield from 是全新的语言结构。 它的作用比 yield 多很多， 
        因此人们认为继续使用那个关键字多少会引起误解。 在其他语言中， 
        类似的结构使用 await 关键字， 这个名称好多了， 因为它传达了至关重要的一点： 
        在生成器 gen 中使用 yield from subgen()时， subgen 会获得控制权， 
        把产出的值传给 gen 的调用方， 即调用方可以直接控制 subgen。 
        与此同时， gen 会阻塞， 等待 subgen 终止。
    
        yield from 可用于简化 for 循环中的 yield 表达式。
        例如：   
             >>> def gen():
            ...     for c in 'AB':
            ...         yield c
            ...     for i in range(1, 3):
            ...         yield i
            ...
            >>> list(gen())
            ['A', 'B', 1, 2]   
            
        可以改写为：
            
            >>> def gen():
            ... yield from 'AB'
            ... yield from range(1, 3)
            ...
            >>> list(gen())
            ['A', 'B', 1, 2]
                        
        示例 16-16 使用 yield from 链接可迭代的对象:
            
            >>> def chain(*iterables):
            ...     for it in iterables:
            ...         yield from it
            ...
            >>> s = 'ABC'
            >>> t = tuple(range(3))
            >>> list(chain(s, t))
            ['A', 'B', 'C', 0, 1, 2]    
        
        yield from x 表达式对 x 对象所做的第一件事是，调用 iter(x)，从中获取迭代器。 
        因此， x 可以是任何可迭代的对象。
        
        可是， 如果 yield from 结构唯一的作用是替代产出值的嵌套 for 循环， 
        这个结构很有可能不会添加到 Python 语言中。 yield from 结构的
        本质作用无法通过简单的可迭代对象说明， 而要发散思维， 使用嵌套的生成器。
        
        yield from 的主要功能是打开双向通道， 把最外层的调用方与最内层
        的子生成器连接起来， 这样二者可以直接发送和产出值， 还可以直接传
        入异常， 而不用在位于中间的协程中添加大量处理异常的样板代码。 有
        了这个结构， 协程可以通过以前不可能的方式委托职责。
         

"---------------------------------------------------------------------"

                     第十七章   使用期物处理并发

                     
    17.2 阻塞型I/O和GIL：
    
        CPython 解释器本身就不是线程安全的， 因此有全局解释器锁（GIL） ，
        一次只允许使用一个线程执行 Python 字节码。 因此， 一个 Python 进程
        通常不能同时使用多个 CPU 核心。                        
                     
        编写 Python 代码时无法控制 GIL； 不过， 执行耗时的任务时， 可以使用
        一个内置的函数或一个使用 C 语言编写的扩展释放 GIL。 其实， 有个使
        用 C 语言编写的 Python 库能管理 GIL， 自行启动操作系统线程， 利用全
        部可用的 CPU 核心。 这样做会极大地增加库代码的复杂度， 因此大多
        数库的作者都不这么做。             
                     
        然而， 标准库中所有执行阻塞型 I/O 操作的函数， 在等待操作系统返回
        结果时都会释放 GIL。 这意味着在 Python 语言这个层次上可以使用多线程， 
        而 I/O 密集型 Python 程序能从中受益： 一个 Python 线程等待网络响
        应时， 阻塞型 I/O 函数会释放 GIL， 再运行一个线程。             
                     
        Python 标准库中的所有阻塞型 I/O 函数都会释放 GIL， 允许其
        他线程运行。 time.sleep() 函数也会释放 GIL。 因此， 尽管有
        GIL， Python 线程还是能在 I/O 密集型应用中发挥作用。             
                     
                     
"---------------------------------------------------------------------"

                     第十八章    使用 asynicio 包处理并发
                     
    并发是指一次处理多件事。
    并行是指一次做多件事。
    二者不同， 但是有联系。
    一个关于结构， 一个关于执行。
    并发用于制定方案， 用来解决可能（但未必） 并行的问题。
                        ——Rob PikeGo 语言的创造者之一                     
                     
    真正的并行需要多个核心。 现代的笔记本电脑有４个 CPU 核心， 但是
    通常不经意间就有超过 100 个进程同时运行。 因此， 实际上大多数过程
    都是并发处理的， 而不是并行处理。 计算机始终运行着 100 多个进程，
    确保每个进程都有机会取得进展， 不过 CPU 本身同时做的事情不能超
    过四件。 十年前使用的设备也能并发处理 100 个进程， 不过都在同一个核心里。                 
                         
                   
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

    特性至关重要的地方在于， 特性的存在使得开发者可以非常安全并且确定可行地
    将公共数据属性作为类的公共接口的一部分开放出来。

    在 Python 中， 数据的属性和处理数据的方法统称属性（attribute）。 
    其实， 方法只是可调用的属性。
    
    除了这二者之外， 我们还可以创建特性（property） ， 在不改变类接口的前提下， 
    使用存取方法（即读值方法和设值方法） 修改数据属性。 这与统一访问原则相符：
    不管服务是由存储还是计算实现的， 一个模块提供的所有服务都应该通过统一的方式使用。
    
    动态创建属性是一种元编程， 框架的作者经常这么做。



"---------------------------------------------------------------------"
                    
                    第二十章    属性描述符
    
    描述符是对多个属性运用相同存取逻辑的一种方式。 例如， Django
    ORM 和 SQL Alchemy 等 ORM 中的字段类型是描述符， 把数据库记录中
    字段里的数据与 Python 对象的属性对应起来。    
    
    描述符是实现了特定协议的类， 这个协议包括 __get__、 __set__ 和
    __delete__ 方法。 property 类实现了完整的描述符协议。 通常， 可
    以只实现部分协议。 其实， 我们在真实的代码中见到的大多数描述符只
    实现了 __get__ 和 __set__ 方法， 还有很多只实现了其中的一个。
    
                  
"---------------------------------------------------------------------"