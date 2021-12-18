import functools

class Node:
    def __init__(self) -> None:
        self.value = None
        self.left: Node = None
        self.right: Node = None

    def __eq__(self, other: object) -> bool:
        if self.value != other.value:
            return False
        if self.left != None and other.left != None:
            return self.left == other.left
        if self.right != None and other.right != None:
            return self.right == other.right

        return True

    def clone(self):
        node = Node()
        node.value = self.value
        node.left = self.left
        node.right = self.right
        return node

    def clone(self):
        new_node = Node()

        if self.left != None:
            new_node.left = self.left.clone()
        if self.right != None:
            new_node.right = self.right.clone()

        return new_node

class Tree:
    def __init__(self, node: Node) -> None:
        self.root = Node()
        self.root.left = node.left
        self.root.right = node.right

    def clone(self):
        new_tree = Tree()
        new_tree.root = self.root.clone()
        return new_tree

def list_to_node(number: list):
    node = Node()

    if isinstance(number[0], int):
        node.left = number[0]
    else:
        node.left = list_to_node(number[0])

    if isinstance(number[1], int):
        node.right = number[1]
    else:
        node.right = list_to_node(number[1])

    return node

with open("input.in") as file:
    sf_numbers = [list_to_node(eval(line)) for line in file]

def reduce_rec(pair: Node, recursion_count):
    if recursion_count + 1 >= 4:
        if pair.left != None:
            


def reduce(pair: Node):
    while True:
        pair_old = pair.clone()

        

        if pair_old == pair:
            break

    return pair



def add(left, right) -> list:
    node = Node()
    node.left = left
    node.right = right
    
    node = reduce(node)

    return node

result = functools.reduce(lambda a, b: add(a, b), sf_numbers)

def calc_magnitude(sf_number):
    left = 0
    right = 0

    if isinstance(sf_number.left, int):
        left += 3 * sf_number.left
    else:
        left += 3 * calc_magnitude(sf_number.left)

    if isinstance(sf_number.right, int):
        right += 2 * sf_number.right
    else:
        right += 2 * calc_magnitude(sf_number.right)

    return left + right

print(calc_magnitude(result))