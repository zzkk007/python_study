import ctypes

class Array(object):

    def __init__(self, size):
        assert size > 0, 'array size must be > 0 '

        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):

        assert index >= 0 and index < len(self), 'out of range'
        return  self._elements[index]

    def __setitem__(self, index, value):

        assert index >= 0 and index < len(self), 'out of range'
        self._elements[index] = value

    def clear(self, value):
        """ 设置每个元素为 value"""

        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator(object):

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


class Aarray2D(object):

    """
        要实现的方法
        Array2D(nrows, ncols) : constructor

        numRows()
        numCols()
        clear(value)
        getitem(i, j)
        setitem(i, j, value)

    """
    def __init__(self, numrows, numclos):
        self._the_rows = Array(numrows)

        for i in range(numrows):
            self._the_rows[i] = Array(numclos)

    @property
    def numRows(self):
        return len(self._the_rows)

    @property
    def numCols(self):
        return len(self._the_rows[0])

    def clear(self, value):
        for row in self._the_rows:
            row.clear(value)

    def __getitem__(self, ndx_tuple):
        assert len(ndx_tuple) == 2

        row, col = ndx_tuple[0], ndx_tuple[1]
        assert (row >= 0 and row < self.numRows and col >= 0 and col < self.numCols)

    def __setitem__(self, ndx_tuple, value):

        assert len(ndx_tuple) == 2
        row , col = ndx_tuple[0], ndx_tuple[1]
        assert (row >= 0 and row < self.numRows and col>= 0 and col < self.numCols)

        the_1d_array = self._the_rows[row]
        the_1d_array[col] = value



if __name__ == '__main__':

    a = Array(10)
    a[0] = 1
    a[1] = 2
    a[2] = 3
    a[3] = 4
    a[4] = 5
    a[5] = 6

    print(a[5])

    for i in a:
        print(i)

    """
        结果如下：
        
        6
        1
        2
        3
        4
        5
        6
        None
        None
        None
        None
        
    """




