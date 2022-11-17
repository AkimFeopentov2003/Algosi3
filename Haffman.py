# Подготовить таблицу вероятностей каждого символа
def findTheCharFrequency(text):
    result = dict()
    for i in text:
        if i.isalpha():  # Определить, является ли символ английской буквой
            if i in result:
                result[i] += 1
            else:
                result.update({i: 1})
    return result


# Создать класс узла
class Node(object):
    def __init__(self, sym=None, count=None):
        self.sym = sym
        self.count = count
        self.leftChild = None
        self.rightChild = None


# Создать дерево Хаффмана
class HuffmanTree(object):
    # По идее дерева Хаффмана: на основе узла построить дерево Хаффмана в обратном порядке
    def __init__(self, char_Weights):
        self.elements = [Node(k, v) for k, v in char_Weights.items()]
        while len(self.elements) != 1:
            self.elements.sort(key=lambda node: node.count, reverse=True)
            n = Node(count=(self.elements[-1].count + self.elements[-2].count))
            n.leftChild = self.elements.pop(-1)
            n.rightChild = self.elements.pop(-1)
            self.elements.append(n)
        self.root = self.elements[0]
        self.Buffer = list(range(10))

    # Создавать коды с рекурсивным мышлением
    def Hu_generate(self, tree, length):
        node = tree
        if (not node):
            return
        elif node.sym:
            print(node.sym + ' is:', end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return
        self.Buffer[length] = 0
        self.Hu_generate(node.leftChild, length + 1)
        self.Buffer[length] = 1
        self.Hu_generate(node.rightChild, length + 1)

    # Output кодировка Хаффмана
    def get_code(self):
        self.Hu_generate(self.root, 0)


if __name__ == '__main__':
    text = 'aaagsyhshavtgs'
    result = findTheCharFrequency(text)
    print(result)
    tree = HuffmanTree(result)
    tree.get_code()
