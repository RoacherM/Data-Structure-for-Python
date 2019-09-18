class Node(object):
    def __init__(self, elem):
        """双链表结点"""
        self.elem = elem
        self.pre = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """获取链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    def append_head(self, elem):
        """向双链表头部添加元素"""
        node = Node(elem)
        if self.is_empty():  # 链表为空
            self.__head = node
        else:
            node.next = self.__head
            # [node.next]为node后的第一个元素
            node.next.pre = node
            self.__head = node

    def append_tail(self, elem):
        """向链表尾部添加结点"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, pos, elem):
        """向链表位置pos处插入元素elem"""
        if pos <= 0:
            self.append_head(elem)
        elif pos >= self.length():
            self.append_tail(elem)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 退出循环时，cur即为pos位置
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
        while cur is not None:
            if cur.elem == elem:
                if cur == self.__head:  # 若是头结点
                    self.__head = cur.next  # 链表中只有一个结点
                    if cur.next:
                        cur.next.pre = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:  # 如果不是尾结点
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next

    def search(self, elem):
        """查找链表中是否存在元素elem"""
        cur = self.__head
        while cur is not None:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    double_linked_list = DoubleLinkedList()
    print(double_linked_list.is_empty())
    print(double_linked_list.length())
    print('===================')

    double_linked_list.append_tail(1)
    print(double_linked_list.is_empty())
    print(double_linked_list.length())
    print('===================')

    double_linked_list.append_tail(2)
    double_linked_list.append_tail(3)

    double_linked_list.append_head(7)

    double_linked_list.append_tail(4)
    double_linked_list.append_tail(5)

    double_linked_list.insert(0, 13)  # 13, 7, 1, 2, 3, 4, 5
    double_linked_list.travel()

    double_linked_list.insert(2, 99)  # 13, 7, 99, 1, 2, 3, 4, 5
    double_linked_list.travel()

    double_linked_list.insert(11, 22)  # 13, 7, 99, 1, 2, 3, 4, 5, 22
    double_linked_list.travel()

    double_linked_list.remove(13)
    double_linked_list.travel()  # 7 99 1 2 3 4 5 22

    double_linked_list.remove(22)
    double_linked_list.travel()  # 7 99 1 2 3 4 5

    double_linked_list.remove(3)
    double_linked_list.travel()  # 7 99 1 2 4 5

    print(double_linked_list.search(100))  # False
    print(double_linked_list.search(7))  # True
    print(double_linked_list.search(2))  # True
    print(double_linked_list.search(5))  # True