from Data_Structure import Structure


class Node(object):
    def __init__(self, x):
        self.next = None
        self.value = x


class hList(Structure):
    def __init__(self):
        super(Structure, self).__init__()
        self.start = None

    def insert(self, x):
        node = Node(x)
        if self.start is None:
            self.start = node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self, x):
        current = self.start
        previous = None

        while 1:
            if current is None:
                break
            elif x == current.value:
                queue = current.next
                if previous is None:
                    self.start = queue
                else:
                    previous.next = queue
                    current = None
                break
            previous = current
            current = current.next

    def find(self, x):
        current = self.start

        while 1:
            if current is None:
                self.comparisons += 1
                print("0")
                break
            elif x == current.value:
                self.comparisons += 2
                print("1")
                break
            current = current.next

    def get_list(self):
        liste = []
        current = self.start
        while 1:
            if current is None:
                break
            else:
                liste.append(current.value)
            current = current.next
        return liste

    # def print(self):
    #     print(self.get_list())
