class Tree:
    def __init__(self, data=None):
        self.key = data
        self.children = []
 
    def set_root(self, data):
        self.key = data
 
    def add(self, node):
        self.children.append(node)
 
    def search(self, key):
        if self.key == key:
            return self
        for child in self.children:
            temp = child.search(key)
            if temp is not None:
                return temp
        return None
 
    def count_leaf_nodes(self):
        leaf_nodes = []
        self.count_leaf_nodes_helper(leaf_nodes)
        return len(leaf_nodes)
 
    def count_leaf_nodes_helper(self, leaf_nodes):
        if self.children == []:
            leaf_nodes.append(self)
        else:
            for child in self.children:
                child.count_leaf_nodes_helper(leaf_nodes)
 
 
tree = None
 
print('Menu (this assumes no duplicate keys)')
print('add <data> at root')
print('add <data> below <data>')
print('count')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'add':
        data = int(do[1])
        new_node = Tree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            tree = new_node
        elif suboperation == 'below':
            position = do[3].strip().lower()
            key = int(position)
            ref_node = None
            if tree is not None:
                ref_node = tree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            ref_node.add(new_node)
 
    elif operation == 'count':
        if tree is None:
            print('Tree is empty.')
        else:
            count = tree.count_leaf_nodes()
            print('Number of leaf nodes: {}'.format(count))
 
    elif operation == 'quit':
        break