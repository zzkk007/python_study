
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

# Implementation of Map ADT using a single list.
class _MapEntry:
    def __init__(self, key, val):
        self.key = key
        self.value = val

class Map(object):
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    # Helper method used to find the index position of a category. If the
    # key is not found, None is returned.
    def _findPosition(self, key):
        for e, ndx in enumerate(self._entryList):
            if e.key == key:
                return ndx
            return None

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    # Adds a new entry to the map if the key does exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add(self, key, val):
        ndx = self._findPosition(self, key)
        if ndx is not None:
            self._entryList[ndx].value = val
            return False
        else:
            self._entryList.append(_MapEntry(key, val))
            return True

    def valueOf(self, key):
        ndx = self._findPosition(self, key)
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(self, key)
        assert ndx is not None, "Invalid map key."
        self._entryList.pop(ndx)

    def keyArray(self):
        keys = list()
        for e in self._entryList:
            keys.append(e.key)
        return keys


    #def __iter__(self):
    #    return _MapGenerator(self._entryList)

    __setitem__ = add
    __getitem__ = valueOf

    def _MapGenerator(entryList):
        for e in entryList:
            yield

if __name__ == '__main__':

     Map1 = Map()
     Map1.add(1, 2)

     print(Map1.valueOf(1))
