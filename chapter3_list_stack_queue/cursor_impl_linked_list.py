import sys
from linked_list import Node

def create_node(next):
    return Node(None, None, next)

# initialize the free list
free_list = [create_node(i+1) for i in range(10)]
free_list[-1] = create_node(0)

def print_list(header):
    if not is_empty(header):
        node = header
        while True:
            node = free_list[node].next
            yield free_list[node].value
            if is_last(node):
                break


def insert_after(header, index, ele):
    node = header
    if not is_empty(header):
        i = 0
        node = free_list[header].next
        while i != index:
            if is_last(node):
                break
            node = free_list[node].next
            i += 1
    append_after_node(node, ele)

def append_node(header, ele):
    insert_after(header, sys.maxsize, ele)

def append_after_node(node, ele):
    new_pos = get_node_space()
    free_list[new_pos].value = ele
    free_list[new_pos].next = free_list[node].next
    free_list[node].next = new_pos

def append(header, ele):
    pos = get_node_space()
    last = get_last(header)
    free_list[last].next = pos
    free_list[pos].value = ele

def find(header, ele):
    if is_empty(header):
        return -1
    pos = free_list[header].next
    while pos and free_list[pos].value != ele:
        pos = free_list[header].next
    return pos if pos else -1

def get_last(header):
    pos = free_list[header].next
    while pos and not is_last(pos):
        pos = free_list[header].next
    return pos

def is_last(pos):
    return free_list[pos].next == 0

def is_empty(header):
    return is_last(header)

def get_list_size(header):
    pos = free_list[header].next
    i = 0
    while pos:
        i += 1
        pos = free_list[header].next
    return i

def create_header():
    pos = get_node_space()
    free_list[pos].next = 0
    return pos

def get_node_space():
    if not has_space():
        raise Exception('SpaceRunOutException')
    pos = free_list[0].next
    free_list[0].next = free_list[pos].next
    return pos

def free_node_space(pos):
    free_list[pos].next = free_list[0].next
    free_list[0].next = pos

def has_space():
    return free_list[0].next != 0

if __name__ == "__main__":
    header = create_header()
    append_node(header, 1)
    append_node(header, 3)
    append_node(header, 5)
    append_node(header, 0)
    print(','.join(map(str, print_list(header))))