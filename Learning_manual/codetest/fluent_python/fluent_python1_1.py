"""
    我们用 collections.namedtuple 构建了一个简单的类来表示一张纸牌。
    自 Python 2.6 开始， namedtuple 就加入到 Python 里，用以构建
    只有少数属性但是没有方法的对象，比如数据库条目。


"""
import collections
from random import choice

Card = collections.namedtuple('Card',['rank', 'suit'])

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


if __name__ == "__main__":

    deck = FrenchDeck()

    # 一叠牌有多少张
    print(len(deck))

    #随机抽取一张，python 内置了一个序列中随机挑出一个元素的函数 random.choice,
    print(choice(deck))

    """
        通过实行特殊方法来利用 Python 数据模型的两个好处:
        
        1、作为你的类的用户， 他们不必去记住标准操作的各式名称（怎么
            得到元素的总数？ 是 .size() 还是 .length() 还是别的什么？） 。
        
        2、可以更加方便地利用 Python 的标准库，比如 random.choice 函数，从而不用重新发明轮子。
        
        3、 因为 __getitem__ 方法把 [] 操作
    
    """








