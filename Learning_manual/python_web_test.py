
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

if __name__ == "__main__":

    #source_list = [32, 543, 324, 34, 7, 90, 30, 14, 53, 99, 333]
    #bubble_sort(source_list)
    #selection_sort(source_list)
    #insert_sort(source_list)
    #print(source_list)

    decimal = int(input("please input a decimal:"))
    #print(binary_2(decimal))
    print(binary64(decimal, 64))
