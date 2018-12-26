"""
    我们用 collections.namedtuple 构建了一个简单的类来表示一张纸牌。
    自 Python 2.6 开始， namedtuple 就加入到 Python 里，用以构建
    只有少数属性但是没有方法的对象，比如数据库条目。


"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    # ['spades', 'diamonds', 'clubs', 'hearts']
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, positions):
        return self._cards[positions]

# {'hearts': 2, 'clubs': 0, 'spades': 3, 'diamonds': 1}
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print("rank_value[%d]" % rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":

    """
        通过实行特殊方法来利用 Python 数据模型的两个好处:

        1、作为你的类的用户， 他们不必去记住标准操作的各式名称（怎么
            得到元素的总数？ 是 .size() 还是 .length() 还是别的什么？） 。

        2、可以更加方便地利用 Python 的标准库，比如 random.choice 函数，从而不用重新发明轮子。

        3、 因为 __getitem__ 方法把 [] 操作交给了 self._cards 列表，所以我们的 deck 类自动
            支持切片操作 （slicing）操作。

        4、仅仅实现了 __getitem__ 方法， 这一摞牌就变成可跌的的了：  

        5、迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__
            方法，那么 in 运算符就会按顺序做一次迭代搜索。于是，in 运算符
            可以用在我们的 FrenchDeck 类上，因为它是可迭代的。
        
        6、排序，用点数来判定扑克牌的大小，2 最小、A 最大，同时黑桃
        最大、红桃次之、方块再次、梅花最小。梅花 2 的大小是 0，黑桃 A 是 51：
        
        7、虽然 FrenchDeck 隐式的继承了 object 类，但功能不是类继承来的。
            我们通过数据模型和一些合成来实现这些功能。通过实现__len__ 和 __getitem__
            这两个特殊方法， FrenchDeck 就跟一个 python 自有的序列数据类型一样，可以
            提现出 python 的核心语言特性（例如迭代和切片）。同时这个类还可以用于标准库中
            诸如 random.choice、reversed 和 sorted 这些函数。
    
    """

    deck = FrenchDeck()

    # 1 一叠牌有多少张
    print(len(deck))

    # 2、3 随机抽取一张，python 内置了一个序列中随机挑出一个元素的函数 random.choice,
    #print(choice(deck))

    # 4 可迭代
    #for card in deck:
    #    print(card)

    # 反向迭代也没有关系
    for card in reversed(deck):
        print(card)

    # 5 in 操作

    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)

    # 6 排序：
    #
    # sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    # list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值。
    # 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
    #
    # sorted 语法
    # sorted(iterable[, cmp[, key[, reverse]]])
    # 参数说明：
    #     iterable -- 可迭代对象
    #     cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，
    #            此函数必须遵守的规则为 大于则返回 1，小于则返回 -1，等于则返回 0
    #     key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的
    #           参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
    #     reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
    #
    #    >>>a = [5,7,6,3,4,1,2]
    #    >>> b = sorted(a) # 保留原列表
    #    >>> a
    #    [5, 7, 6, 3, 4, 1, 2]
    #    >>> b
    #    [1, 2, 3, 4, 5, 6, 7]
    #    >>> L=[('b',2),('a',1),('c',3),('d',4)]
    #    >>> sorted(L, cmp=lambda x,y:cmp(x[1],y[1])) # 利用cmp函数
    #    [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    #    >>> sorted(L, key=lambda x:x[1]) # 利用key
    #    [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    #    >>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    #    >>> sorted(students, key=lambda s: s[2]) # 按年龄排序
    #    [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    #    >>> sorted(students, key=lambda s: s[2], reverse=True) # 按降序
    #    [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    #    >>>
    for card in sorted(deck, key=spades_high):
        print(card)
