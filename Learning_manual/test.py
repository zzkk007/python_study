
class Bag(object):

    """
    constructor  构造函数
    size
    contains
    append
    remove
    iter
    """

    def __init__(self):
        self._items = list()

    def __le__(self):
        return len(self._items)

    def __contains__(self, item):

        return item in self._items

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        assert item in self._items, 'item must in the bag'
        return self._items.remove(item)

    def __iter__(self):
        return _BagIterator(self._items)

class _BagIterator(object):

    """
        注意这里实现了迭代器类
    """

    def __init__(self, seq):
        self._bag_items = seq
        self._cur_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_item < len(self._bag_items):
            item = self._bag_items[self._cur_item]
            self._cur_item +=  1
            return item
        else:
            raise StopIteration

class Set(object):

    """
        使用 list 实现 set ADT
        Set()
        length()
        contains(element)
        add(element)
        remove(element)

        isSubsetOf(setB)
        union(setB)
        intersect(setB)
        difference(setB)
        iterator

    """

    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, item):
        return item in self._theElements

    def add(self, item):
        if item not in self._theElements:
            self._theElements.append(item)

    def print(self):
        for i in self._theElements:
            print('{0}'.format(i))

    def remove(self, item):
        assert item in self._theElements, "The element must be set"

    def __eq__(self, setB):
        if len(self._theElements) != len(setB):
            return False
        else:
            return self.isSubsetof(setB)

    def isSubsetof(self, setB):

        for item in self._theElements:
            if item not in setB:
                return False
            else:
                return True

    def union(self, setB):

        newSet = Set()
        newSet._theElements.extend(self._theElements)

        for item in setB:
            if item not in self._theElements:
                newSet._theElements.append(item)
        return newSet

    def __iter__(self):
        return _SetIterator(self._theElements)


class _SetIterator(object):

    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._items):
            val = self._items[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration

if __name__ == '__main__':

    setA = Set()
    for i in range(10):
        setA.add(i)

    #setA.print()

    for i in setA:
        print(i)

   # print('-----------------')

   #setB = set('iloveyou')

   #setC = setA.union(setB)

   #setC.print()



























    '''
    b = Bag()
    b.add(1)
    b.add(2)
    b.add(3)
    b.add(4)
    b.add(5)

    # for 使用 __iter__ 构建，用 __next__ 迭代

    for i in b:
        print(i)
    
    '''
    # for 语句等价于
    """   
        i = b.__iter__()
        while True:
            try:
                item = i.__next__()
                print(item)
            except StopIteration:
                break
    """
