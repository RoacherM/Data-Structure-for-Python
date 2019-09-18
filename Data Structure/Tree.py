class Node(object):
    """
    树结点
    """

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """
    树类，包括树结点的添加
    递归法：先序遍历、中序遍历、后序遍历
    堆栈法：先序遍历、中序遍历、后序遍历
    队列法：层次遍历
    """

    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """
        为树增加结点
        :param elem:增加的元素
        :return:
        """
        node = Node(elem)
        # 当树为空时，直接对根节点赋值
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        # 先添加左节点，再添加右节点
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                # 如果该结点存在右子树，则抛弃该结点，myQueue指向同层左结点，将原始结点推出去
                self.myQueue.pop(0)

    def front_recursion(self, root):
        """
        递归法先序遍历
        :return:
        """
        if root == None:
            return
        print(root.elem)
        self.front_recursion(root.lchild)
        self.front_recursion(root.rchild)

    def middle_recursion(self, root):
        """
        递归法中序遍历
        :return:
        """
        if root == None:
            return
        self.middle_recursion(root.lchild)
        print(root.elem)
        self.middle_recursion(root.rchild)

    def later_recursion(self, root):
        """
        递归法后序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        self.later_recursion(root.lchild)
        self.later_recursion(root.rchild)
        print(root.elem)

    def front_stack(self, root):
        """
        堆栈法树的先序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        myStack = []
        node = root
        # 从根节点开始遍历
        while node or myStack:
            # 当左子树为空时，跳出循环
            while node:
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            # 开始遍历右子树
            node = myStack.pop()
            node = node.rchild

    def middle_stack(self, root):
        """
        堆栈法树的中序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        else:
            myStack = []
            node = root
            # 从根节点开始遍历
            while node or myStack:
                while node:
                    myStack.append(node)
                    node = node.lchild
                # 开始遍历右子树
                node = myStack.pop()
                print(node.elem)
                node = node.rchild

    def later_stack(self, root):
        """
        堆栈法树的后序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        else:
            myStack1 = []
            myStack2 = []
            node = root
            myStack1.append(node)
            # 找出后序遍历的逆序，存于myStack2中，append操作用于添加新结点
            while myStack1:
                node = myStack1.pop()
                if node.lchild:
                    myStack1.append(node.lchild)
                if node.rchild:
                    myStack1.append(node.rchild)
                myStack2.append(node)
            while myStack2:
                print(myStack2.pop().elem)

    def level_queue(self, root):
        """
        利用队列实现树的层次遍历,即广度优先遍历
        :param root:
        :return:
        """
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild:
                myQueue.append(node.lchild)
            if node.rchild:
                myQueue.append(node.rchild)


if __name__ == '__main__':
    from PIL import Image
    im = Image.open('Tree.png')
    im.show()

    elems = range(10)  # 生成十个数据作为树节点
    tree = Tree()  # 新建一个树对象
    for elem in elems:
        tree.add(elem)  # 逐个添加树的节点

    print('队列实现层次遍历:')
    tree.level_queue(tree.root)

    print('\n\n递归实现先序遍历:')
    tree.front_recursion(tree.root)
    print('\n递归实现中序遍历:')
    tree.middle_recursion(tree.root)
    print('\n递归实现后序遍历:')
    tree.later_recursion(tree.root)

    print('\n\n堆栈实现先序遍历:')
    tree.front_stack(tree.root)
    print('\n堆栈实现中序遍历:')
    tree.middle_stack(tree.root)
    print('\n堆栈实现后序遍历:')
    tree.later_stack(tree.root)
