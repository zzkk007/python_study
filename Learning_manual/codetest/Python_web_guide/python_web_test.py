
def bubble_sort(alist):

    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

def selection_sort(alist):

    for i in range(len(alist)-1):
        max_index = i

        for j in range(i + 1, len(alist)):
            if alist[max_index] > alist[j]:
                max_index = j

        if i != max_index:
            alist[i],alist[max_index] = alist[max_index],alist[i]

def insert_sort(alist):

    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


def binary_2(num):

    if num == 0:
        return '0'
    else:
        return binary_2(num >> 1) + str(num & 1)



def binary64(decimal, base):
    KeyCode = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$'
    if decimal == 0:
        return '0'
    else:
        m = decimal % base
        return binary64(decimal //base, base) + str(KeyCode[m])


def quick_sort(alist, start, end):

    if start  >= end:
        return
    mid = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist, 0, low - 1)
    quick_sort(alist, low + 1, end)

def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = gap // 2


def binary_search(alist, item):

    first = 0
    last = len(alist) - 1

    while first <= last:
        midpoint = (first + last)//2

        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

# 递归实现

def binary_search_dg(alist, item):
    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binary_search(alist[:midpoint],item)
          else:
            return binary_search(alist[midpoint+1:],item)

# 链表的实现

class SingleNode(object):
    """单链表节点"""

    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):

        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head

        while cur is not None:
            print('{0}'.format(cur.item))
            cur = cur.next

    def add(self, item):

        node = SingleNode(item)

        node.next = self._head
        self._head = node

    def append(self, item):

        node = SingleNode(item)

        if self.is_empty():
            self._head = node

        else:

            cur = self._head

            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def inset(self, post, item):

        """ 指定位置添加元素 """

        # 若指定位置 post 为第一个元素之前，则执行头部插入

        if post <= 0:
            self.add(item)

        elif post > self.length() - 1:
            self.append(item)

        else:
            node = SingleNode(item)
            count = 0

            # pre 用来指向指定位置 post 的前一个位置 post - 1, 初始从头节点移动到指定位置
            pre = self._head
            while count < post - 1:
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, item):

        cur = self._head
        pre = None

        while cur is not None:

            if cur.item == item:

                # 链表第一个节点就是要删除的节点
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def reversal(self):
        pre, cur = None, self._head

        # 一定要明白链表的特性，cur.next 是一个指针，
        # cur.next 等于谁，cur 的下一项就是谁。

        while cur is not None:
            cur.next, pre , cur = pre, cur, cur.next
        return pre

    def swapPairs(self):

        pre, pre.next = self, self._head

        while pre.next and pre.next.next:
            a = pre.next
            b = a.next

            pre.next, b.next, a.next = b, a, b.next

            pre = a
        return self.next


class Stack(object):

    def __init__(self):
        self.items = list()

    def is_empty(self):

        return self.items is None

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack_2(object):

    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def peek(self):
        assert not self.isEmpty()
        return self._top.item

    def pop(self):
        assert not self.isEmpty()
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1

class _StackNode(object):
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items is None

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)






class Queue_list(object):
    """ Queue ADT, linked list 实现。为了改进环型数组有最大数量的限制，改用
    带有头尾节点的linked list实现。
    """
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._qcount = 0

    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._count

    def enqueue(self, item):
        node = _QueueNode(item)    # 创建新的节点并用尾节点指向他
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._qcount += 1

    def dequeue(self):
        assert not self.isEmpty(), 'Can not dequeue from an empty queue'
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next    # 前移头节点
        self._qcount -= 1
        return node.item

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


''' 2018 - 12 - 19'''

class Node_cycle(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class SinCycLinkedList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self._head
            while cur.next != self._head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        cur =self._head

        if self.is_empty():
            return

        while cur.next != self._head:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        node = Node_cycle(item)

        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head

            cur = self._head

            while cur.next != self._head:
                cur = cur.next
            cur.next = node

            self._head = node

    def append(self, item):
        node = Node_cycle(item)

        if self.is_empty():
            self._head = node
            node.next = self._head

        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, pos, item):

        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node_cycle(item)
            cur = self._head
            count = 0

            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):

        if self.is_empty():
            return

        cur = self._head
        pre = None

        if cur.item == item:

            if cur.next != self._head:

                while cur.next != self._head:
                    cur = cur.next

                cur.next = self._head.next
                self._head = self._head.next
            else:
                self._head = None
        else:
            pre = self._head

            while cur.next != self._head:

                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                pre.next = self._head


class DNode(object):

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):

    def __init__(self):
        self._head = None

    def isEmpty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self._head

        while cur.next != None:
            print(cur.item)
            cur = cur.next
        print('---------')

    def add(self, item):

        node = DNode(item)

        if self.isEmpty():
            self._head = node

        else:

            node.next = self._head
            self._head.prev = node

            self._head = node

    def append(self, item):

        node = DNode(item)

        if self.isEmpty():
            self._head = node

        else:
            cur = self._head

            while cur.next != None:
                cur = cur.next

            cur.next = node
            node.prev = cur

    def search(self, item):
        cur = self._head

        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next

        return False

    def insert(self, pos, item):

        if pos < 0:
            self.add(item)

        elif pos > self.length() - 1:
            self.append(item)

        else:
            node  = DNode(item)
            cur = self._head

            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next

            node.prev = cur
            node.next = cur.next

            cur.next.prev = node
            cur.next = node

def printRev(n):
    if n > 0:
        print(n)
        print(printRev(n - 1))


# 树

class Node_Tree(object):

    def __init__(self, elem = -1, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


# 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点

class Tree(object):

    def __init__(self, root = None):
        self.root = root

    def add(self, elem):

        node = Node_Tree(elem)
        if self.root is None:
            self.root = node

        else:
            queue = []
            queue.append(self.root)

            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.pop(cur.lchild)
                    queue.pop(cur.rchild)


    def preorder(self, roo):

        if roo is None:
            return

        print(roo.elem)
        self.preorder(roo.lchild)
        self.preorder(roo.rchild)


if __name__ == "__main__":

    # printRev(3)

    # source_list = [32, 543, 324, 34, 7, 90, 30, 14, 53, 99, 333]
    # bubble_sort(source_list)
    # selection_sort(source_list)
    # insert_sort(source_list)
    # quick_sort(source_list, 0 , len(source_list)-1)
    # print(source_list)

    # decimal = int(input("please input a decimal:"))
    # print(binary_2(decimal))
    # print(binary64(decimal, 64))

    # testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    # print(binary_search_dg(testlist, 32))

    # stack = Stack_2()

    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)

    # print(stack.peek())
    # print(stack.isEmpty())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())


    # q = Queue_list()
    # q.enqueue("hello")
    # q.enqueue("I")
    # q.enqueue("Love")
    # q.enqueue("world")

    # print('%s' % q.dequeue())
    # print('%s' % q.dequeue())
    # print('%s' % q.dequeue())


    T = Tree()
    T.add(1)
    T.add(2)
    T.add(3)
    T.preorder(T.root)












