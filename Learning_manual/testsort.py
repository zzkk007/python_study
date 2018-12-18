
def bubble_sort(alist):

    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1]  = alist[j + 1] , alist[j]


def select_sort(alist):

    for i in range(len(alist)-1):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        if min_index != i:
            alist[min_index], alist[i] = alist[i], alist[min_index]


def insert_sort(alist):

    # 从第二个位置，即下标为 1 的元素开始向前插入

    for i in range(1, len(alist)):

        # 从第 i 个元素开始向前比较, 如果小于前一个元素，交换位置

        for j in range(i, 0 , -1):
            if alist[j] < alist[j - 1]:
                alist[j] , alist[j - 1] = alist[j - 1], alist[j]





def quick_sort(alist, start, end):

    if start >= end:
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

    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)



if __name__ == '__main__':

    source_list = [1, 54, 22, 67, 43, 78, 12, 9, 12]

    #bubble_sort(source_list)

    #select_sort(source_list)

    #insert_sort(source_list)

    quick_sort(source_list, 0, len(source_list)-1)

    print(source_list)