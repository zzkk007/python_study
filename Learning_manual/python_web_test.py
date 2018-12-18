
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

if __name__ == "__main__":

    source_list = [32, 543, 324, 34, 7, 90, 30, 14, 53, 99, 333]
    #bubble_sort(source_list)
    #selection_sort(source_list)
    #insert_sort(source_list)
    #quick_sort(source_list, 0 , len(source_list)-1)
    #print(source_list)

    #decimal = int(input("please input a decimal:"))
    #print(binary_2(decimal))
    #print(binary64(decimal, 64))

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_dg(testlist, 32))
