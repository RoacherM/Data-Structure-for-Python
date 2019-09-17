class stack(object):
    """
    Python实现的顺序堆栈函数，后进先出（LIFO）
    size:栈的大小
    top:栈顶，及非空数值大小
    push():入栈操作，将数据顺序存入堆中
    pop():出栈操作，将数据从栈中弹出
    """

    def __init__(self, maxsize):
        self.size = maxsize
        self.stack = []
        self.top = -1

    # 入栈
    def push(self, data):
        # 栈满则自动扩充栈空间
        if (self.top + 1) == self.size:
            print("The stack is full!Reset the size of stack!")
            self.size = self.top + 1
            self.stack.append(data)
            self.top += 1
        else:
            self.stack.append(data)
            self.top += 1

    # 出栈
    def pop(self):
        # 栈空
        if self.top == -1:
            print("The stack is empty!")
            return 0
        else:
            self.stack.pop()
            self.top -= 1

    # 显示栈中元素
    def show(self):
        print(self.stack)

    # 通过index获取元素
    def __getitem__(self, index):
        return self.stack[index]

    def __setitem__(self, index, value):
        self.stack[index] = value


if __name__ == '__main__':

    # 利用堆栈原理将二进制数转换成十进制数，按0结束压栈操作。
    # 公式：（Xn,Xn-1,...,X1） = X1*2^0+X2*2^1+...+Xn*2^(n-1)
    # 新建size为50的栈
    s = stack(10)
    flag = 0


    # 检查二进制数输入合法性
    def isvalid(s):
        if s == 0 or s == 1:
            return True
        else:
            print("Wrong format for Binary!")
            return False


    # # 二进制转十进制
    def binary2decimal(sk):
        decimal = 0
        binary = ''
        for i in range(sk.top):
            decimal += s[-1] * 2 ** i
            binary += str(s[-1])
            # 删除栈顶元素
            s.pop()
        return decimal, binary[::-1]


    while isvalid(flag):
        digit = input('输入0或者1，按q退出：')
        try:
            if digit == 'q':
                break
            else:
                digit = int(digit)
                s.push(digit)
                flag = digit
        except ValueError:
            print("Wrong format for Binary!")
    s.show()
    number1, binary1 = binary2decimal(s)
    print("binary:" + binary1 + " decimal:" + str(number1))
