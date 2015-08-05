import operator

class Node:

    def __init__(self):
        self.value = ''
        self.nodes = {}
        self.labels = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

    def add_node(self, node):
        self.nodes[node.value] = node

    def get_node(self, value):
        return self.nodes[value]

    def set_label(self, label, value):
        self.labels[label] = value

    def increment_label(self, label):
        self.labels[label] += 1

class DecisionTree:

    def __init__(self):
        self.numbers = []
        self.node_root = Node()
        self.len_pixels = 0

    def load_numbers(self, numbers):
        self.set_numbers(numbers)
        self.init_node_root()
        self.create_nodes()

    def set_numbers(self, numbers):
        self.numbers = numbers
        self.len_pixels = len(self.numbers[0]['pixels'])

    def init_node_root(self):
        self.node_root = Node()

        for number in self.numbers:
            self.node_root.increment_label(number['label'])

    def create_nodes(self):
        len_pixels = len(self.numbers[0]['pixels'])
        line = 1

        for number in self.numbers:
            self.add_node(self.node_root, number, 0)

            if line % 100 == 0:
                print "line:", line

            line += 1

    def add_node(self, node_parent, number, number_col):
        if number_col >= self.len_pixels:
            return

        node = None
        node_value = number['pixels'][number_col]

        if node_value in node_parent.nodes:
            node = node_parent.get_node(node_value)
            node.increment_label(number['label'])
        else:
            node = Node()
            node.value = node_value
            node.increment_label(number['label'])
            node_parent.add_node(node)

        self.add_node(node, number, number_col + 1)

    def get_label(self, pixels):
        node = self.search_pixel_node(self.node_root, pixels, 0)
        sorted_labels = sorted(node.labels.items(), key=operator.itemgetter(1))
        return sorted_labels[::-1][0][0]

    def get_label_node(self, pixels):
        node = self.search_pixel_node(self.node_root, pixels, 0)
        return node

    def search_pixel_node(self, node, pixels, pixel_col):
        pixel = pixels[pixel_col]

        if (pixel in node.nodes) and (pixel_col < self.len_pixels - 1):
            return self.search_pixel_node(node.nodes[pixel], pixels, pixel_col + 1)
        else:
            return node

