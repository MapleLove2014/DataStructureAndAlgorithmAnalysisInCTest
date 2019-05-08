class Node():
    def __init__(self, value=None, pre=None, next=None):
        self.value = value
        self.pre = pre
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedListIter():
    def __init__(self, linked_list):
        self.linked_list = linked_list
        self.index = 0
        self.node = self.linked_list.first
        self.next = self.node

    def __iter__(self):
        return self

    def __next__(self):
        if not self.node or self.index == self.linked_list.size:
            raise StopIteration
        self.node = self.next
        self.next = self.next.next
        self.index += 1
        return self.node.value

class LinkedList():
    """ Double Linked List"""
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
        self.size = 0
    
    def add_to_last(self, v):
        previous_last = self.last
        self.last = Node(v, previous_last)
        if not previous_last:
            self.first = self.last
        else:
            previous_last.next = self.last
        self.last.next = self.first
        self.first.pre = self.last
        self.size += 1
    
    def add_all_to_last(self, anotherList):
        for e in anotherList:
            self.add_to_last(e.value)

    def add_pure_values_to_last(self, values):
        for v in values:
            self.add_to_last(v)

    def find_first(self, v):
        f = self.first
        while f and f.next != self.first and f.value != v:
            f = f.next
        return f if f.value == v else None
            
    def remove_first(self, v):
        e = self.find_first(v)
        if not e:
            print("{} does not exist!".format(v))
        else:        
            e.pre.next = e.next
            e.next.pre = e.pre
        self.size -= 1

    def remove(self, i):
        node = self.get(i)
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        return node
    
    def reset_head(self, node):
        self.first = node
        self.last = self.first.pre

    def get(self, i):
        if i < 0 or i >= self.size:
            raise Exception('index out of range')
        node = None
        while i >= 0:
            if not node:
                node = self.first
            else:
                node = node.next
            i -= 1
        return node

    def __len__(self):
        return self.size

    def __iter__(self):
        return LinkedListIter(self)

def main():
    l = LinkedList()
    for x in range(5):
        l.add_to_last(x)
    print(l.size)
    print(l.first)
    print(l.last)
    print(l.first.pre)
    print(l.first.next)
    print(l.last.pre)
    print(l.last.next)

    print('reset head')
    l.reset_head(l.get(3))
    print(l.size)
    print(l.first)
    print(l.last)
    print(l.first.pre)
    print(l.first.next)
    print(l.last.pre)
    print(l.last.next)

if __name__ == '__main__':
    main()