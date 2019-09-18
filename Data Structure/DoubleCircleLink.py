class Node(object):
    """双循环链表结点"""
    def __init__(self, elem):
        self.elem = elem
        self.pre = None
        self.next = None


class DoubleLinkedCircularList(object):
    def __init__(self, node=None):
        self.__head = node
        # 若为本身，则自己指向自己
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """求取链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾结点
        print(cur.elem)

    def add(self, elem):
        """向链表头部添加元素"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾结点
            cur.next = node
            node.next = self.__head
            self.__head.pre = node
            self.__head = node

    def append(self, elem):
        """向链表尾部添加元素"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾结点
            cur.next = node
            node.pre = cur
            node.next = self.__head

    def insert(self, pos, elem):
        """往双向循环链表位置pos处插入元素

        Args:
            pos: 插入位置
            elem: 插入的元素
        """
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length() - 1):
            self.append(elem)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 退出循环，cur指向需要插入的位置pos
            node = Node(elem)
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self, elem):
        """删除链表中第一个值为elem的结点"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == elem:
                if cur == self.__head:  # 删除的是头结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    self.__head.pre = None
                    rear.next = self.__head
                else:  # 删除的是中间结点
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                return
            else:
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == elem:
            if cur == self.__head:  # 链表中只有一个结点
                self.__head = None
            else:
                cur.pre.next = self.__head

    def search(self, elem):
        """查找链表中是否存在值为elem的结点"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == elem:
            return True
        return False


if __name__ == '__main__':
    double_linked_circular_list = DoubleLinkedCircularList()
    print(double_linked_circular_list.is_empty())
    print(double_linked_circular_list.length())
    print('===================')

    double_linked_circular_list.append(1)
    print(double_linked_circular_list.is_empty())
    print(double_linked_circular_list.length())
    print('===================')

    double_linked_circular_list.append(2)
    double_linked_circular_list.append(3)

    double_linked_circular_list.add(7)

    double_linked_circular_list.append(4)
    double_linked_circular_list.append(5)
    double_linked_circular_list.travel()  # 7, 1, 2, 3, 4, 5

    double_linked_circular_list.insert(0, 13)  # 13, 7, 1, 2, 3, 4, 5
    double_linked_circular_list.travel()

    double_linked_circular_list.insert(2, 99)  # 13, 7, 99, 1, 2, 3, 4, 5
    double_linked_circular_list.travel()

    double_linked_circular_list.insert(11, 22)  # 13, 7, 99, 1, 2, 3, 4, 5, 22
    double_linked_circular_list.travel()

    double_linked_circular_list.remove(13)
    double_linked_circular_list.travel()  # 7 99 1 2 3 4 5 22

    double_linked_circular_list.remove(22)
    double_linked_circular_list.travel()  # 7 99 1 2 3 4 5

    double_linked_circular_list.remove(3)
    double_linked_circular_list.travel()  # 7 99 1 2 4 5

    print(double_linked_circular_list.search(100))  # False
    print(double_linked_circular_list.search(7))  # True
    print(double_linked_circular_list.search(2))  # True
    print(double_linked_circular_list.search(5))  # True