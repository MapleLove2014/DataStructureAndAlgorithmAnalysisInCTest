import sys
from linked_list import LinkedList, Node
def merge_sort(data, f = lambda e : e.value):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data
    work_copy = [ d for d in data ]
    left = work_copy[:len(work_copy)//2]
    right = work_copy[len(work_copy)//2:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    merged_data = merge(sorted_left, sorted_right, f)
    return merged_data

def merge(left, right, f):
    merged_data = []
    left_index = 0
    right_index = 0
    
    while True:
        if left_index == len(left) or right_index == len(right):
            break
        left_ele = left[left_index]
        right_ele = right[right_index]
        if f(left_ele) <= f(right_ele):
            merged_data.append(left_ele)
            left_index += 1
        else:
            merged_data.append(right_ele)
            right_index += 1
    
    while True:
        if left_index == len(left):
            break
        merged_data.append(left[left_index])
        left_index += 1
    while True:
        if right_index == len(right):
            break
        merged_data.append(right[right_index])
        right_index += 1
    return merged_data

def my_print(e, f):
    print(f(e))

def test():
    f = lambda e : e.value
    l = LinkedList()
    l.add_to_last(Node(3))
    l.add_to_last(Node(2))
    l.add_to_last(Node(100))
    l.add_to_last(Node(1))
    r = merge_sort(l, f)
    for e in r:
        my_print(e, f)