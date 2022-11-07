class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        return 'key : {}, left {}, right {}'.format(self.key, left, right)


def read_data():
    n = int(input())
    nodes = [Node(0) for _ in range(n)]
    for i in range(n):
        key, left, right = map(int, input().split())
        nodes[i].key = key
        if left != -1:
            nodes[i].left = nodes[left]
        if right != -1:
            nodes[i].right = nodes[right]
    return nodes[0]


def in_order(current, st):
    if not current:
        return
    in_order(current.left, st)
    st += str(current.key) + ' '
    in_order(current.right, st)


def pre_order(current, st):
    if not current:
        return
    st += str(current.key) + ' '
    pre_order(current.left, st)
    pre_order(current.right, st)


def post_order(current, st):
    if not current:
        return
    post_order(current.left, st)
    post_order(current.right, st)
    st += str(current.key) + ' '


# def breadth_first_search(root):
#     queue = [root]
#     while queue:
#         tmp_queue = []
#         for element in queue:
#             print(element.key, end=' ')
#             if element.left:
#                 tmp_queue.append(element.left)
#             if element.right:
#                 tmp_queue.append(element.right)
#         queue = tmp_queue


def main():
    root = read_data()
    st = []
    in_order(root, st)
    st = st[:-1]
    for i in st:
        print(i, end='')
    print()
    st = []
    pre_order(root, st)
    st = st[:-1]
    for i in st:
        print(i, end='')
    print()
    st = []
    post_order(root, st)
    st = st[:-1]
    for i in st:
        print(i, end='')


main()
