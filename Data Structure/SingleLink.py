class Node(object):
    """
    单链表节点
    """

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SinglyLinkedList(object):
    """
    单链表
    """

    def __init__(self, node=None):
        self.__head = None

    def is_empty(self):
        "判断列表是否为空"
        return self.__head is None

    def length(self):
        "返回链表长度"
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        "遍历链表"
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next

    def append_head(self, elem):
        "添加头部元素"
        node = Node(elem)
        node.next = self.__head
        self.__head = node

    def append_tail(self, elem):
        "添加尾部元素"
        node = Node(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, elem):
        """
        向链表pos处插入元素
        :param pos:插入位置
        :param elem:需要插入的元素
        """
        if pos <= 0:
            self.append_head(elem)
        elif pos > (self.length() - 1):
            self.append_tail(elem)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 执行完while后，count = pos-1，即为pos的前一位
            # 将pos.next赋值给node.next
            # 将node赋值给pre.next
            node = Node(elem)
            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        """
        从列表中删除第一个值为elem的元素
        :param elem:要删除的元素
        :return:
        """
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == elem:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, elem):
        """
        查找是否存在某个元素
        :param elem: 需要查找的元素
        :return: True(有)/False(无)
        """
        cur = self.__head
        while cur is not None:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    print(singly_linked_list.is_empty())
    print(singly_linked_list.length())
    print("\n++++++++++++++++++++++++++")

    singly_linked_list.append_tail(1)
    print(singly_linked_list.is_empty())
    print(singly_linked_list.length())
    print("++++++++++++++++++++++++++")

    singly_linked_list.append_tail(2)
    singly_linked_list.append_tail(3)

    singly_linked_list.append_head(7)

    singly_linked_list.append_tail(4)
    singly_linked_list.append_tail(5)

    singly_linked_list.insert(0, 12)
    singly_linked_list.travel()
    print("\n+++++++++++++++++++++++++++++++")

    singly_linked_list.insert(2, 99)
    singly_linked_list.travel()
    print("\n+++++++++++++++++++++++++++++++")

    singly_linked_list.remove(5)
    singly_linked_list.travel()
    print("\n+++++++++++++++++++++++++++++++")

    singly_linked_list.remove(4)
    singly_linked_list.travel()
    print("\n+++++++++++++++++++++++++++++++")

    print(singly_linked_list.search(2))
    print(singly_linked_list.search(4))
