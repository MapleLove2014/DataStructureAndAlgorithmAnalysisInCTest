import logging
import json

logging.basicConfig(level='INFO')

class Node():
    def __init__(self):
        self.value = 0
        self.label = 'root'
        self.children = []
        self.parent = 0

class Tree():
    def __init__(self):
        self.root = Node()

    def __find__(self, node, value):
        if not node:
            return None
        if str(node.value) == str(value):
            return node
        for child in node.children:
            n = self.__find__(child, value)
            if n:
                return n
        return None
    def find(self, value):
        return self.__find__(self.root, value)
            
    def add(self, node):
        if not node:
            raise Exception('add node failure : invalid node')
        parent = self.find(node.parent)
        if not parent:
            logging.error('add node failure : parent node not found')
        else:
            parent.children.append(node)

    def __top_down_traverse__(self, node, pre_padding):
        print('{}{}'.format(pre_padding, node.label))
        for child in node.children:
            self.__top_down_traverse__(child, pre_padding+'\t')

    def top_down_traverse(self, pre_padding=''):
        self.__top_down_traverse__(self.root, pre_padding)

def main():
    with open('metajson.json', mode='rt', encoding='utf-8') as metajson:
        options = json.load(metajson)
        option_tree = Tree()
        for option in options:
            node = Node()
            node.label = option['label']
            node.value = option['value']
            node.parent = option['parentValue']
            option_tree.add(node)
        option_tree.top_down_traverse()

main()