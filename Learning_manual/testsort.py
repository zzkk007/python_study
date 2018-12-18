
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
    # 递归退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)









if __name__ == '__main__':

    source_list = [1, 54, 22, 67, 43, 78, 12, 9, 12]

    #bubble_sort(source_list)

    #select_sort(source_list)

    #insert_sort(source_list)

    quick_sort(source_list, 0, len(source_list)-1)

    print(source_list)