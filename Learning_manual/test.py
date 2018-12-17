
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

if __name__ == '__main__':

    b = Bag()
    b.add(1)
    b.add(2)
    b.add(3)
    b.add(4)
    b.add(5)

    # for 使用 __iter__ 构建，用 __next__ 迭代

    for i in b:
        print(i)

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
