
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
    
8、  

    
          