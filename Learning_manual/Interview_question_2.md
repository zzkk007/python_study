"---------------------------------------------------"
    
            面试中碰到的问题

"---------------------------------------------------"

1、python 测试工具以及区别

    a. pep8/pycodestyle:
    
        PEP 8 是一种 Python 代码规范指南，目的是保持代码的一致性，可读性。
        检查自己代码是否符合 PEP8 规范，一个的简单的工具就是：pep8
        
        安装： pip install pep8
        在使用时发现 pep8 给出了一个警告：
                
            $ pep8 gkcx.py
            /usr/local/lib/python3.5/dist-packages/pep8.py:2124: UserWarning:
            
            pep8 has been renamed to pycodestyle (GitHub issue #466)
            Use of the pep8 tool will be removed in a future release.
            Please install and use `pycodestyle` instead.    
        
        意思是 pep8 已被 pycodestyle 替代！
        
        安装：pip install pycodestyle
        
        使用：$ pycodestyle [file name or directory name]
        $ pycodestyle gkcx.py
    
    b. Pyflakes:
    
        一个用于检查 Python 源文件错误的简单程序。
        
        Pyflakes 分析程序并检查各种错误。它通过解析源文件实现，无需导入它。
        因此在模块中使用是安全的，没有任何副作用。
        
        不会检查代码风格
        由于它是单独检查各个文件，因此它也相当的快，当然检查范围有一定的局限性。
        
        安装：pip install pyflakes
        
        使用：pyflakes [file name or directory name]
        $ pyflakes gkcx.py           
                    
    c. Pylint:
    
        PyLint 是 Python 源代码分析器，可以分析 Python 代码中的错误，
        查找不符合代码风格标准和有潜在问题的代码，是一个可以用于验证
        多个文件的模块和包的工具。
        
        缺省情况下，PyLint 启用许多规则，它具有高度可配置性，
        从代码内部处理程序控制它，另外，编写插件添加到自己的检查中是可能的。
        
        安装：pip install pylint
        使用：pylint [options] module_or_package
        $ pylint gkcx.py
        
        如果运行两次 Pylint，它会同时显示出当前和上次的运行结果，从而可以看出代码质量是否得到了改进。
        
        错误代码含义:
        
            C：惯例，违反了编码风格标准
            R：重构，代码非常糟糕
            W：警告，某些 Python 特定的问题
            E：错误，很可能是代码中的错误
            F：致命错误，阻止 Pylint 进一步运行的错误
    
    d. flake8:
    
        Flake8 是由 Python 官方发布的一款辅助检测 Python 代码是否规范的工具，
        相对于目前热度比较高的 Pylint 来说，Flake8 检查规则灵活，支持集成额外插件，扩展性强。
        Flake8 是对下面三个工具的封装：

        PyFlakes：静态检查 Python 代码逻辑错误的工具。
        Pep8： 静态检查 PEP8 编码风格的工具。
        NedBatchelder’s McCabe ：静态分析 Python 代码复杂度的工具。
        不光对以上三个工具的封装，Flake8还提供了扩展的开发接口。    
        
        安装： pip install flake8  
        使用:  基本使用方法：flake8 [file name or directory name]
          
  
3、functools.wraps 库：

    python装饰器中functools.wraps的作用详解
    
    　　# 定义一个最简单的装饰器
    　　def user_login_data(f):
    　　　　def wrapper(*args, **kwargs):
    　　　　　　return f(*args, **kwargs)
    　　　　return wrapper
    
    　　# 用装饰器装饰以下两个函数　　
    　　@user_login_data
    　　def num1():
    　　　　print("aaa")
    
    　　@user_login_data
    　　def num2():
    　　　　print("bbbb")
  
    　　if __name__ == '__main__':
    　　　　print(num1.__name__)
    　　　　print(num2.__name__)       
        
    以上代码的输出结果为：wrapper、wrapper。
    
    由此函数使用装饰器时,函数的函数名即 __name__已经被装饰器改变.
    一般定义装饰器的话可以不用考虑这点,但是如果多个函数被两个装饰器装饰时就报错,
    因为两个函数名一样,第二个函数再去装饰的话就报错.

    解决方案就是引入  functools.wraps  ,以上代码的解决如下: 
    
        def user_login_data(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                return f(*args, **kwargs)
                
            return wrapper      
    
    增加@functools.wraps(f), 可以保持当前装饰器去装饰的函数的 __name__ 的值不变
    以上输出结果就是:
        num1
        num2
        
    Python装饰器（decorator）在实现的时候，有一些细节需要被注意。
    例如，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）。
    这样有时候会对程序造成一些不便。
    
    所以，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
    写一个decorator的时候，最好在实现之前加上functools的wrap，
    它能保留原有函数的名称和docstring。
        
   
4、python2 和 python3 的区别:
    
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
        
    （5）父类调用：
   
        Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx 
    
    
    （6）API的变化:
        
        zip()、map()和filter()现在都返回迭代器，而不是列表
        keys()、dic.items()和dic.values()现在返回“视图”，而不是列表
        iterkeys()、dic .iteritems()和dic .itervalues()不再受支持   
        
    (7)
        long整数类型被Python3废弃，统一使用int
        xrange()函数被 pytho3 废弃
        raw_input()函数被 pytho3 废弃        
    
5、协程:

    迭代器和生成器：
    
    (1) 迭代协议：
    
        迭代协议是指：对象需要提供 next 方法，他要么返回迭代中的下一项，
            要么就引起一个 StopIteration 异常，以终止迭代。
        
        可迭代对象：实现了迭代以协议的对象。    
    
    (2) 生产器：
    
        python 使用生产器对延迟操作提供了支持，所谓的延迟操作，是指在需要的时候才生产结果，
        而不是立刻产生结果。这也是生成器的主要好处。
        
        因此，生成器的唯一注意事项就是：生成器只能遍历一次。 
    
  
6、单例模式:

    单例是什么：

        确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，
        单例模式是一种对象创建型模式。	


    创建单例-保证只有1个对象:

        # 实例化一个单例
        class Singleton(object):
            __instance = None
    
            def __new__(cls, age, name):
                
                #如果类数字能够__instance没有或者没有赋值
                #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
                #能够知道之前已经创建过对象了，这样就保证了只有1个对象
                
                if not cls.__instance:
                        cls.__instance = object.__new__(cls)
                
                return cls.__instance
    
    
        a = Singleton(18, "dongGe")
        b = Singleton(8, "dongGe")
    
        id(a)
            140298627282200
        id(b)
            140298627282200
    
        a.age = 19
        print(b.age)
            19
    


    创建单例时，只执行1次__init__方法:

        # 实例化一个单例
        class Singleton(object):	
            __instance = None
            __first_init = False
            
            def __new__(cls, age, name):
                if not cls.__instance:
                    cls.__instance = object.__new__(cls)
                return cls.__instance
    
            def __init__(self, age, name):
                if not self.__first_init:
                    self.age = age
                    self.name = name
                    Singleton.__first_init = True
    
        a = Singleton(18, "dongGe")
        b = Singleton(8, "dongGe")
    
        print(id(a))
            140298627282200
        print(id(b))
            140298627282200
    
    
        print(a.age)
            18
        print(b.age)
            18
    
        a.age = 19
        print(b.age)
            19

    想创建单例必须使用__new__，代表要实例化的类。
    __init__只能保证一个实例参数一致，并不能保证一个实例。
    
7、装饰器：
        
    def w1(func):
        def inner():
        
            # 验证1
            # 验证2
            # 验证3
            func()
        return inner
    
    @w1
    def f1():
        print('f1')
    
    Python 解释器就会从上到下解释代码，步骤如下：
    
        (1) def w1(func):  ==> 将 w1 函数加载到内存
        (2) @w1
        
    没错，从表面上看解释器仅仅会解释这两句代码，因为函数在没有被调用之前起内部代码不会被执行。
    从表面上看解释器着实会执行这两句，但是 @w1 这一句代码里却有大文章， 
    @函数名 是python的一种语法糖。        
            
    上例@w1内部会执行一下操作：
        
        执行 w1 函数，并将 @w1 下面的函数作为 w1 函数的参数，即：@w1 等价于 w1(f1)
        内部会执行：
            
            def inner():
                # 验证 1
                # 验证 2
                # 验证 3
                f1()  # func 是参数，此时 func 等于 f1
            #返回的 inner，inner代表的是函数，非执行函数,
            #其实就是将原来的 f1 函数塞进另外一个函数中。    
            return inner
    

8、再议装饰器：
    
    #定义函数：完成包裹数据
    def makeBold(fn):
        def wrapped():
            return "<b>" + fn() + "</b>"
        return wrapped
    
    #定义函数：完成包裹数据
    def makeItalic(fn):
        def wrapped():
            return "<i>" + fn() + "</i>"
        return wrapped
    
    @makeBold
    def test1():
        return "hello world-1"
    
    @makeItalic
    def test2():
        return "hello world-2"
    
    @makeBold
    @makeItalic
    def test3():
        return "hello world-3"
    
    print(test1()))
    print(test2()))
    print(test3()))              
    
    运行结果:
        
        <b>hello world-1</b>
        <i>hello world-2</i>
        <b><i>hello world-3</i></b>            
                                 
    装饰器(decorator)功能:
    
        引入日志
        函数执行时间统计
        执行函数前预备处理
        执行函数后清理功能
        权限校验等场景
        缓存    
                         
9、装饰器示例：

    例1:无参数的函数：
    
    from time import ctime, sleep
  
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s"%(func.__name__,ctime()))   
            func()
        return wrappedfunc
    
    @timefun
    def foo():
        pront("I am foo")
        
    foo()
    sleep(2)
    foo()
    
    上面的代码理解装饰器执行行为可以理解成:
        
        #foo先作为参数赋值给func后,foo接收指向timefun返回的wrappedfunc
        foo = timefunc(foo)
        
        #调用foo(),即等价调用wrappedfunc()
        foo()
        
    例2:被装饰的函数有参数:
    
        from time import ctime, sleep

        def timefun(func):
            def wrappedfunc(a, b):
                print("%s called at %s"%(func.__name__, ctime()))
                print(a, b)
                func(a, b)
            return wrappedfunc
        
        @timefun
        def foo(a, b):
            print(a+b)
        
        foo(3,5)
        sleep(2)
        foo(2,4)        
    
    例3:被装饰的函数有不定长参数:
    
        from time import ctime, sleep

        def timefun(func):
            def wrappedfunc(*args, **kwargs):
                print("%s called at %s"%(func.__name__, ctime()))
                func(*args, **kwargs)
            return wrappedfunc
        
        @timefun
        def foo(a, b, c):
            print(a+b+c)
        
        foo(3,5,7)
        sleep(2)
        foo(2,4,9)    
                    
    例4:装饰器中的return:
    
        from time import ctime, sleep

        def timefun(func):
            def wrappedfunc():
                print("%s called at %s"%(func.__name__, ctime()))
                func()
            return wrappedfunc         
         
        @timefun
        def foo():
            print("I am foo")
        
        @timefun
        def getInfo():
            return '----hahah---'                          
        
        foo()
        sleep(2)
        foo()   
        
        print(getInfo())
        
        执行结果：
            foo called at Fri Nov  4 21:55:35 2016
            I am foo
            foo called at Fri Nov  4 21:55:37 2016
            I am foo
            
            getInfo called at Fri Nov  4 21:55:37 2016
            None
        
        如果修改装饰器为return func()，则运行结果： 
            def timefun(func):
                def wrappedfunc():
                    print("%s called at %s"%(func.__name__, ctime()))
                    return func()
                return wrappedfunc           
            
        执行结果：
                
                foo called at Fri Nov  4 21:55:57 2016
                I am foo
                foo called at Fri Nov  4 21:55:59 2016
                I am foo
                getInfo called at Fri Nov  4 21:55:59 2016
                ----hahah---
            
        一般情况下为了让装饰器更通用，可以有return

10、装饰器带参数：
    
    装饰器带参数,在原有装饰器的基础上，设置外部变量
    
    from time import ctime, sleep
    
    def timefunc_age(pre="hello"):
        def timefunc(func):
            def wrappedfunc():
                print("%s called at %s %s"%(func.__name__,ctime(), pre)) 
                return func()
            return wrappedfunc
        return timefunc
        
    @timefunc_age('world') 
    def too():
        print("I am too")          
   
    too()
   

11、下面是什么函数？

    # 这是一个求质数函数，除了 1 和 本身之外没有别的约数。
    def g(n):
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
        
    xlist = [x for x in range(1,20) if g(x)]
    print(xlist)
    #[1, 2, 3, 5, 7, 11, 13, 17, 19]
       
       
12、产生一个混合密码：
  
    >>> import string
    >>> dir(string)
    ['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', 
    '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
    '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 
    'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
  
    >>> string.ascii_letters
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> string.hexdigits
    '0123456789abcdefABCDEF'
    >>> string.ascii_uppercase
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    >>> string.punctuation
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 
    >>> string.printable
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    
    >>> ss =random.sample(string.printable, 8)
    >>> ss
    ['&', ':', 'A', '}', '%', 'b', 'V', 'B']
    >>> "".join(ss)
    '&:A}%bVB'
    
              
'-------------------------------------------------------------------'

                         MySQL
                        
'-------------------------------------------------------------------'

1、MySQL 查询优化:
    
    查询优化几个方向:
        
        a、尽量避免全文扫描，给相应字段增加索引，应用索引来查询
        b、删除不用或者重复的索引
        c、查询重写，等价转换（谓词、子查询、连接查询）
        d、删除内容重复不必要的语句，精简语句
        e、整合重复执行的语句
        f、缓存查询结果
        
    MYSQL查询语句优化:
        
        a、避免使用不兼容的数据类型。
            
            例如float和int、char和varchar、binary和varbinary是不兼容的。
            数据类型的不兼容可能使优化器无法执行一些本来可以进行的优化操作。    
            
        b、索引字段上进行运算会使索引失效。
                
            尽量避免在WHERE子句中对字段进行函数或表达式操作，这将导致引擎放弃使用索引而进行全表扫描。
            如： SELECT * FROM T1 WHERE F1/2=100 应改为: SELECT * FROM T1 WHERE F1=100*2    
            
        c、 避免使用!=或＜＞、IS NULL或IS NOT NULL、IN ，NOT IN等这样的操作符.
                
            因为这会使系统无法使用索引,而只能直接搜索表中的数据。
            例如: SELECT id FROM employee WHERE id != “B%” 
            优化器将无法通过索引来确定将要命中的行数,因此需要搜索该表的所有行。
            在in语句中能用exists语句代替的就用exists.   
            
        d、尽量使用数字型字段.
            
            一部分开发人员和数据库管理人员喜欢把包含数值信息的字段设计为字符型，
            这会降低查询和连接的性能，并会增加存储开销。
            这是因为引擎在处理查询和连接回逐个比较字符串中每一个字符，
            而对于数字型而言只需要比较一次就够了。
        
        e、能够用BETWEEN的就不要用IN
            
        f、能够用DISTINCT的就不用GROUP BY
            
        g、尽量不要用SELECT INTO语句。SELECT INTO 语句会导致表锁定，阻止其他用户访问该表。
            

2、MySQL 注入，代码层防止注入的原理：
        
    所谓SQL注入，就是通过把SQL命令插入到Web表单提交或输入域名或页面请求的查询字符串。
    终于达到欺骗server运行恶意的SQL命令。

    详细来说，它是利用现有应用程序，将（恶意）的SQL命令注入到后台数据库引擎运行的能力，
    它能够通过在Web表单中输入（恶意）SQL语句得到一个存在安全漏洞的站点上的数据库。
    而不是依照设计者意图去运行SQL语句。   
        
    依据相关技术原理，SQL注入能够分为平台层注入和代码层注入。
        
        前者由不安全的数据库配置或数据库平台的漏洞所致；
        后者主要是因为程序猿对输入未进行仔细地过滤，从而运行了非法的数据查询。
        
    基于此，SQL注入的产生原因通常表如今下面几方面：
        ①不当的类型处理；
        ②不安全的数据库配置。
        ③不合理的查询集处理；
        ④不当的错误处理；
        ⑤转义字符处理不合适；
        ⑥多个提交处理不当。
        
    注入方法：

        1.猜表名。列名等

            先猜表名  
                And (Select count(*) from 表名)<>0
                
            猜列名
                And (Select count（列名） from 表名）<>0
                
            或者也能够这样 
                and exists (select * from 表名）            
                and exists (select 列名 from 表名）          
                返回正确的，那么写的表名或列名就是正确  

        2.后台身份验证绕过漏洞:
            
            验证绕过漏洞就是'or'='or'后台绕过漏洞，利用的就是AND和OR的运算规则，
            从而造成后台脚本逻辑性错误。
                
            比如管理员的账号password都是admin。那么再比方后台的数据库查询语句是

            user=request("user")
            passwd=request("passwd")                
            sql='select admin from adminbate where user='&'''&user&'''&' and passwd='&'''&passwd&'''              
            那么我使用'or 'a'='a来做usernamepassword的话，那么查询就变成了                
            select admin from adminbate where user=''or 'a'='a' and passwd=''or 'a'='a'               
            这种话，依据运算规则。这里一共同拥有4个查询语句，那么查询结果就是 假or真and假or真，
            先算and 再算or，终于结果为真。这样就能够进到后台了        
            
        3. 怎样预防 呢？归纳一下，主要有下面几点：
            
            a. 永远不要信任用户的输入。对用户的输入进行校验，能够通过正則表達式，
               或限制长度；对单引號和双"-"进行转换等。
                
            b.永远不要使用动态拼装sql，能够使用參数化的sql或者直接使用存储过程进行数据查询存取。
                
            c.永远不要使用管理员权限的数据库连接，为每一个应用使用单独的权限有限的数据库连接。
                
            d.不要把机密信息直接存放。加密或者hash掉password和敏感的信息。
                
            e. 应用的异常信息应该给出尽可能少的提示，
               最好使用自己定义的错误信息对原始错误信息进行包装。
                
            f.sql注入的检測方法一般採取辅助软件或站点平台来检測。
                软件一般採用sql注入检測工具jsky，站点平台就有亿思站点安全平台检測工具。
                MDCSOFT SCAN等。採用MDCSOFT-IPS能够有效的防御SQL注入。XSS攻击等。

    
3、MySQL 常用的引擎，及其区别：
    
    MyISAM:
        
        此引擎不支持事务，也不支持外键。
        
        锁级别为表锁，表锁的优点是开销小，加锁快；缺点是锁粒度大，发送锁冲突概率高，
        容纳并发能力低，这个引擎适合查询为主的业务。
        
        MyISAM 强调了快速读取操作。它存储表的行数，于是 SELECT COUNT(*) FROM TABLE 时
        只需要直接读取已经保存好的值而不需要进行全表扫描。    
        
    InnoDB:
        
        此引擎，支持事务，支持外键，支持回滚，支持 Hash/B-tree 索引类型。
        
        锁级别为行锁，行锁的优点是适用于高并发的频繁表修改，高并发的性能优于 MyISAM。
        缺点是系统消耗比较大，索引不仅缓存自身，也缓存数据，相比 MyISAM 需要更大的内存。
        
        InnoDB 中不保存表的具体行数，也就是说，执行 select count(*) from table 时，
        InnoDB 要扫描一遍整个表来计算有多少行。
        
    Memory:
    
        Memory 是内存级别的存储引擎，数据存储在内存中，所以他能够存储的数据量较小。
        
        因为内存特性，存储引擎对数据的一致性支持交差。但访问速度非常快，默认使用 hash 索引。
        
        锁级别为表锁，不支持事务。    


4、数据库常用到的函数：
    
    数据处理函数/单行处理函数：
        
        Lower		转换小写
        upper		转换大写
        substr		取子串（substr(被截取的字符串,起始下标,截取的长度)）
        length		取长度
        trim		去空格
        str_to_date	将字符串转换成日期
        date_format	格式化日期
        format		设置千分位
        round		四舍五入
        rand()		生成随机数
        Ifnull		可以将null转换成一个具体值
        now()		获得当前时间    
    
    聚合：为了快速得到统计数据，提供了5个聚合函数：
    
        1、count( *)表示计算总行数，括号中写星与列名，结果是相同的
		    select count( *) from students;

        2、max(列)表示求此列的最大值
            select max(id) from student where gender = 0;
    
        3、min(列)表示求此列的最小值
            select min(id) from student where isdelete = 0;
    
        4、sum(列)表示求此列的和
            select sum(id) from student where gender =1;
    
        5、avg(列)求此列的平均值
            select avg(id) from students where isdelete=0 and gender=0;     
    
    
'---------------------------------------------------------------------'
    
                            other
    
'---------------------------------------------------------------------'    

1、RESTful api:




2、二叉树，通过前序遍历(ADCEFGHB)和中序遍历(CDFEGHAB)写出后序遍历：
    
    前序遍历: 根节点 --> 左子树 --> 右子树
    
    中序遍历: 左子树 --> 根节点 --> 右子树
    
    后序遍历: 左子树 --> 右子树 --> 根节点
    
    
             A
          D     B
        C    E
           F   G
                 H
    
    后序遍历的结果是: CFHGEDBA 
        
3、























        