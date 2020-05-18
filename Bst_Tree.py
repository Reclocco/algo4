from Data_Structure import Structure


class Bs_Tree(Structure):
    def __init__(self):
        super(Structure, self).__init__()
        self.root = None

    def insert(self, x):
        if self.root is not None:
            self.root.insert(x)
        else:
            self.root = Node(x)

    def find(self, x):
        if self.root is not None:
            self.find_helper(self.root, x)
        else:
            print()

    def find_helper(self, node, value):
        while 1:
            if value < node.data:
                # self.comparisons += 2
                if node.left is None:
                    print("0")
                    return
                node = node.left
            elif value > node.data:
                # self.comparisons += 3
                if node.right is None:
                    print("0")
                    return
                node = node.right
            else:
                # self.comparisons += 2
                print("1")
                return

    # def print(self):
    #     if self.root is not None:
    #         self.root.print_tree()

    def load(self, f):
        words = open(f, "r").read().split()

        if self.root is not None:
            self.root.load_helper(words)
        else:
            self.root = Node(words.pop(0))
            self.root.load_helper(words)

    def min(self):
        if self.root is not None:
            print(self.root.min())
        else:
            print()

    def max(self):
        if self.root is not None:
            print(self.root.max())
        else:
            print()

    def successor(self, x):
        if self.root is not None:
            self.root.successor(x)
        else:
            print()

    def delete(self, x):
        if self.root is not None:
            self.root = self.root.delete(x)


class Node(Structure):

    def __init__(self, data):
        super(Structure, self).__init__()
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        current = self
        while 1:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right
            else:
                current.data = data
                return

    def find(self, value):
        if value < self.data:
            self.comparisons += 2
            if self.left is None:
                print("0")
                return
            return self.left.find(value)
        elif value > self.data:
            self.comparisons += 3
            if self.right is None:
                print("0")
                return
            return self.right.find(value)
        else:
            self.comparisons += 2
            print("1")

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def load_helper(self, f):
        for value in f:
            self.insert(value)

    def min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    def min_rel(self, node):
        while node.left is not None:
            node = node.left
        return node

    def max_rel(self, node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, x):
        current = self
        while 1:
            if current is None:
                print()
                break
            elif current.data > x:
                current = current.left
            elif current.data < x:
                current = current.right
            elif current.data == x:
                if current.right is not None:
                    print(current.right.data)
                    break
                else:
                    print()
                    break

    def delete(self, x):
        node = self
        return self.delete_help(node, x)

    def delete_help(self, node, x):
        if node is None:
            return node

        if x < node.data:
            node.left = Node.delete_help(self, node.left, x)
        elif x > node.data:
            node.right = Node.delete_help(self, node.right, x)
        else:
            if node.left is None:
                temp = node.right
                return temp
            elif node.right is None:
                temp = node.left
                return temp

            temp = self.min_rel(node.right)
            node.data = temp.data
            node.right = self.delete_help(node.right, temp.data)

        return node
