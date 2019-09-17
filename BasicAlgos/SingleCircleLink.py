class Node(object):
    """
    单循环链表节点
    """

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SinglyLinkedCircularList(object):
    """
    单循环链表
    """

    def __init__(self, node=None):
        self.__head = node
        # 若为自己，则自己指向自己
        if node:
            node.next = node

    def is_empty(self):
        "判断列表是否为空"
        return self.__head is None

    def length(self):
        "求链表长度"
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def append_head(self, elem):
        """
        添加头部信息
        :param elem:需要添加的元素
        :return:
        """
        node = Node(elem)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            cur = self.__head
            # 循环结束时，cur此时为尾巴
            while cur.next != self.__head:
                cur = cur.next
            # 循环链表中先指定新的头元素，并将头尾连接起来
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append_tail(self, elem):
        """
        添加尾部信息
        :param elem:需要添加的元素
        :return:
        """
        node = Node(elem)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, elem):
        """
        向指定位置插入元素
        :param pos: 要插入的位置
        :param elem: 要插入的元素
        :return:
        """
        if pos <= 0:
            self.append_head(elem)
        elif pos >= self.length():
            self.append_tail(elem)
        else:
            pre = self.__head
            count = 0
            # w循环结束时，count为pos-1
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(elem)
            # 先给node.next赋值，再给pre.next赋值
            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        # 不是尾结点时
        while cur.next != self.__head:
            # 有该元素
            if cur.elem == elem:
                # 处理头结点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 若为头结点，则将原头结点next,head指向cur.next,cur.next
                    rear.next = cur.next
                    self.__head = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                # 无该元素
                pre = cur
                cur = cur.next
        # 退出循环时，cur指向尾节点
        if cur.elem == elem:
            # 链表中只有一个节点时
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, elem):
        """
        查找某元素
        :param elem: 要查找的元素
        :return:Boolean
        """
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.next == elem:
                return True
            else:
                cur = cur.next
        if cur.elem == elem:
            return True
        else:
            return False


if __name__ == '__main__':
    singly_linked_circular_list = SinglyLinkedCircularList()
    print(singly_linked_circular_list.is_empty())
    print(singly_linked_circular_list.length())
    print('===================')

    singly_linked_circular_list.append_tail(1)
    print(singly_linked_circular_list.is_empty())
    print(singly_linked_circular_list.length())
    print('===================')

    singly_linked_circular_list.append_tail(2)
    singly_linked_circular_list.append_tail(3)

    singly_linked_circular_list.append_head(7)

    singly_linked_circular_list.append_tail(4)
    singly_linked_circular_list.append_tail(5)

    singly_linked_circular_list.insert(0, 13)  # 13, 7, 1, 2, 3, 4, 5
    singly_linked_circular_list.travel()

    singly_linked_circular_list.insert(2, 99)  # 13, 7, 99, 1, 2, 3, 4, 5
    singly_linked_circular_list.travel()

    singly_linked_circular_list.insert(11, 22)  # 13, 7, 99, 1, 2, 3, 4, 5, 22
    singly_linked_circular_list.travel()

    singly_linked_circular_list.remove(13)
    singly_linked_circular_list.travel()  # 7 99 1 2 3 4 5 22

    singly_linked_circular_list.remove(22)
    singly_linked_circular_list.travel()  # 7 99 1 2 3 4 5

    singly_linked_circular_list.remove(3)
    singly_linked_circular_list.travel()  # 7 99 1 2 4 5

    print(singly_linked_circular_list.search(666))  # False
    print(singly_linked_circular_list.search(7))  # True
    print(singly_linked_circular_list.search(5))  # True
    print(singly_linked_circular_list.search(1))  # True
