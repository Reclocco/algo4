class Structure(object):
    def __init__(self):
        self.comparisons = 0

    def insert(self, x):
        pass

    def load(self, f):
        pass

    def delete(self, x):
        pass

    def find(self, x):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def successor(self, x):
        pass

    def inorder(self):
        pass

    def get_comp(self):
        return self.comparisons

    def wipe_comp(self):
        self.comparisons = 0

    def bundle(self):
        comps = self.get_comp()
        self.wipe_comp()
        return comps
