class Node:

    def __init__(self):
        self.nodes = {}
        self.labels = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

    def set_label(self, label, value):
        self.labels[label] = value

    def increment_label(self, label):
        self.labels[label] += 1

class DecisionTree:

    def __init__(self):
        self.numbers = []
        self.node_root = Node()

    def set_numbers(self, numbers):
        self.numbers = numbers

    def init_node_root(self):
        self.node_root = Node()

        for number in self.numbers:
            self.node_root.increment_label(number['label'])

