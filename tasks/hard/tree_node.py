"""
Реализовать алгоритм двоичного дерево поиска

Бинарное дерево поиска (BST) — это дерево, в котором все узлы следуют указанным
ниже свойствам. Левое поддерево узла имеет ключ, меньший или равный ключу его
родительского узла. Правое поддерево узла имеет ключ больше, чем ключ его
родительского узла. Таким образом, BST делит все свои поддеревья на два сегмента:
левое поддерево и правое поддерево и может быть определено как -
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)


https://tproger.ru/translations/binary-search-tree-for-beginners/
"""


class BinaryNode:

    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


class BST:

    def __init__(self, node=None):
        self.node = node

    def add(self, value):
        if self.node is None:
            self.node = BinaryNode(value)
        else:
            self._add_to(self.node, value)

    def _add_to(self, node, value):
        if value < node.value:
            if node.left_node is None:
                node.left_node = BinaryNode(value)
            else:
                self._add_to(node.left_node, value)
        else:
            if node.right_node is None:
                node.right_node = BinaryNode(value)
            else:
                self._add_to(node.right_node, value)

    def contains(self, value):
        if self.node is None:
            return False
        return self._find_node(None, self.node, value) is not None

    def _find_node(self, parent, node, value):
        if node.value == value:
            return parent, node
        elif value < node.value:
            if node.left_node is None:
                return parent, None
            else:
                return self._find_node(node, node.left_node, value)
        elif value > node.value:
            if node.right_node is None:
                return parent, None
            else:
                return self._find_node(node, node.right_node, value)

    def remove(self, value):
        parent, current = self._find_node(None, self.node, value)
        if current is None:
            raise ValueError(f'Не содердит искомого значение {value}')
        if current.right_node is None:
            if parent is None:
                self.node = current.left_node
            else:
                if parent.value > current.value:
                    parent.left_node = current.left_node
                else:
                    parent.right_node = current.left_node
        elif current.right_node.left_node is None:
            current.right_node.left_node = current.left_node
            if parent is None:
                self.node = current.right_node
            else:
                if parent.value > current.value:
                    parent.left_node = current.right_node
                else:
                    parent.right_node = current.right_node
        else:
            left_most = current.right_node.left_node
            left_most_parent = current.right_node
            while left_most.left_node is not None:
                left_most_parent = left_most
                left_most = left_most.left_node
            left_most_parent.left_node = left_most.right_node
            left_most.left_node = current.left_node
            left_most.right_node = current.right_node
            if parent is None:
                self.node = left_most
            else:
                if parent.value > current.value:
                    parent.left_node = left_most
                elif parent.value < current.value:
                    parent.right_node = left_most

    def print_tree(self):
        if self.node is not None:
            self._print_req(self.node, 0)

    def _print_req(self, node, level):
        if node.right_node is not None:
            self._print_req(node.right_node, level + 1)
        print('  ' * level + str(node.value))
        if node.left_node is not None:
            self._print_req(node.left_node, level + 1)
