import numpy as np
import math
import random

a = np.random.randint(0, 100, 10)
print(a, len(a), type(a), a.dtype)

b = np.sort(a)
print('正确答案：', b)

# for i in range(5, -1, -1):  # 5，4，3，2，1，0
#    print(i)

"""
三种时间复杂度为O(N*N)、额外空间复杂度为O(1)的算法
选择排序           |不稳定
冒泡排序、插入排序  |稳定
"""


# 选择排序
def SelectSort(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        swap(arr, i, minIndex)
    return arr


# 冒泡排序
def BubbleSort(arr):
    if len(arr) < 2:
        return arr
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+i)
    return arr


# 插入排序
def InsertSort(arr):
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):  # i=0时使得下一步j=-1,并不输出i=0时的情况
        for j in range(i-1, -1, -1):
            # print('i={}, j={}'.format(i, j))
            if arr[j+1] < arr[j]:
                swap(arr, j, j+1)
    return arr


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


"""
三种时间复杂度为O(N*logN)的算法
              额外空间复杂度     稳定性
        归并      O(N)           Yes
        堆        O(1)           No
        快排3.0   O(logN)        No
"""


# 归并排序，此写法返回的是list类型
def MergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    # print('left is:{}, right is {}'.format(left, right))
    merged = []  # 新建的辅助数组，python中是list类型。或者新建一个arr，长度大小为R-L+1
    p1, p2 = 0, 0
    left_len, right_len = len(left), len(right)
    while p1 < left_len and p2 < right_len:
        if left[p1] <= right[p2]:
            merged.append(left[p1])
            p1 += 1
        else:
            merged.append(right[p2])
            p2 += 1

    # while p1 < left_len:
    #     merged.append(left[p1])  # 复制剩下的, append直接复制了list,因此需要一个值一个值的加入列表，可改写为extend
    #     p1 += 1
    # while p2 < right_len:
    #     merged.append(right[p2])
    #     p2 += 1

    merged.extend(left[p1:])
    merged.extend(right[p2:])
    # print(merged)
    return merged


# # 归并排序，利用下标进行递归的操作
# # todo: process中return条件的书写，迭代无法终止
# def MergeSort(arr):
#     if len(arr) < 2:
#         return arr
#     process(arr, 0, len(arr)-1)
#     return arr
#
#
# def process(arr, L, R):
#     # base case return
#     mid = L+((R-L) >> 1)
#     process(arr, L, mid)
#     process(arr, mid+1, R)
#     return merge(arr, L, mid, R)
#
#
# def merge(arr, L, M, R):
#     # 左组和右组比较后进行合并
#     help = [0]*(R-L+1)
#     i = 0
#     p1 = L
#     p2 = M+1
#     while p1 <= M and p2 <= R:
#         help[i] = arr[p1] if arr[p1] <= arr[p2] else arr[p2]
#         i = i+1
#         p1 = p1+1
#         p2 = p2+1
#     while p1 <= M:  # 若左右对比后，左组还剩余数字，全部拷贝，注意i++,p1++
#         help[i] = arr[p1]
#         i = i+1
#         p1 = p1+1
#     while p2 <= R:  # 若左右对比后，右组还剩余数字，全部拷贝,i++,p2++
#         help[i] = arr[p2]
#         i = i+1
#         p2 = p2+1
#     for i in range(len(help)):
#         arr[L+i] = help[i]
#     return arr
# 堆排序，组织结构特殊标准的完全二叉树,
# 大根堆定义；关键记录有效区长度
# heapInsert
# heapify
# todo:返回值不排序


# 网上找的打印树的一个函数，很好用，谁用谁知道
def print_tree(array):  # 打印堆排序使用

    # 深度 前空格 元素间空格
    # 1     7       0
    # 2     3       7
    # 3     1       3
    # 4     0       1

    # first=[0]
    # first.extend(array)
    # array=first
    index = 1
    depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()


def HeapSort(arr):
    # todo:大根堆组织出错
    # 先把整个数组变成大根堆：
    if len(arr) < 2:
        return arr
    # 组织大根堆，一个个加入堆
    for i in range(len(arr)):  # O(N)
        heapInsert(arr, i)     # O(logN)
        print(arr)
    print('# 大根堆是：', arr)

    # 等同于做popmax操作
    heapSize = len(arr)       # 有效区长度<-->堆大小
    swap(arr, 0, heapSize-1)  # popmax:有效区第一个数max(大根堆头部)换到最后，此时最后一个数已经排好，断联
    heapSize -= 1             # 已经确定了一个，有效区减一

    # 从头结点开始向下heapify --O(logN)
    while heapSize > 0:
        heapify(arr, 0, heapSize)
        swap(arr, 0, heapSize - 1)  # 有效区第一个数换到最后
        heapSize -= 1
    return arr


def heapInsert(arr, i):  # 从下往上，和父比较，大的话往上跑, O(logN)
    # 包含2个停止条件：比父小；i=0
    while arr[i] > arr[(i-1)//2]:
        swap(arr, i, (i-1)//2)
        i = (i-1)//2


def heapify(arr, i, heapsize):  # 比较以i为根的子树中，左右孩子有无比当前根大的
    left = 2*i+1
    while left < heapsize:  # 左孩子不越界（右孩子有可能越界），说明此时下方还有孩子
        largest = left+1 if left+1 < heapsize and arr[left+1] > arr[left] else left  # 右孩子存在并且更大时，左右孩子比较
        largest = i if arr[i] > arr[largest] else largest      # 父节点、更大值比较
        if largest == i:  # 说明不用再往下沉，两个孩子没有比我大的
            break
        swap(arr, largest, i)  # 把更大的值换到父节点上来
        i = largest
        left = 2*i + 1


quick_sort = lambda array: array if len(array) <= 1 else \
    quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + \
    quick_sort([item for item in array[1:] if item > array[0]])

print('# 一行搞定快排，返回list类型', quick_sort(a))


def QuickSort(arr):
    if len(arr) < 2:
        return arr
    quicksort(arr, 0, len(arr) - 1)
    return arr


def quicksort(arr, L, R):
    if L < R:
        swap(arr, L+random.randint(0, R-L), R)  # [L,...,R]上随机选一个数作为划分值，放到最后
        pless, pmore = partition(arr, L, R)  # 等于区域的左边界、右边界
        quicksort(arr, L, pless-1)
        quicksort(arr, pmore+1, R)


def partition(arr, L, R):  # 以最后一个值arr[R]作为划分值的荷兰国旗问题
    less = L-1
    more = R
    while L < more:  # L作为当前值指针 L<R不对，L当前值走到more里停止
        if arr[L] < arr[R]:
            less += 1
            swap(arr, less, L)
            L += 1
        elif arr[L] > arr[R]:
            more -= 1  # 右边界先扩大一步，再做交换；当前数不动
            swap(arr, more, L)
        else:
            L += 1
    swap(arr, more, R)  # todo 交换最后的比较值和右边界的值，使得中间是等于区；
    # 相等区的第一个数，最后一个数
    return less+1, more


def countSort(a):
    # 对于list输入 O(N)\O(N),保持稳定性
    if len(a) < 2:
        return a
    # 找到最大值、最小值
    min_num = min(a)
    max_num = max(a)
    count_list = [0]*(max_num-min_num+1)
    for i in a:
        count_list[i - min_num] += 1  # count_list中索引含义‘与最小值的差值’，内容是‘数的个数’
    a.clear()
    # 填回
    for ind, i in enumerate(count_list):
        while i != 0:
            a.append(ind+min_num)
            i -= 1
    return a



# c = SelectSort(a)
# print('SelectSort: ', c)
#
# d = BubbleSort(a)
# print('BubbleSort: ', d)
#
# e = InsertSort(a)
# print('InsertSort:', e)
#
# f = MergeSort(a)
# print('MergeSort 归并排序: ', f, '返回list类型')

# g = HeapSort(a)
# print('HeapSort 堆排序： ', g)

h = QuickSort(a)
print('QuickSort 快排：', h)

i = countSort(list(a))
print('count_sort 计数排序：', i)


