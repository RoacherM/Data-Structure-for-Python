#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:11
# @Author  : Houps
# @Email   : sir.housir@gmail.com
# @File    : exhaustive.py
# @Software: IntelliJ IDEA


# 穷举法：在解空间中穷举每一种可能的解，并对每一个解做判断，从而找出问题的答案
# class初始化时的写法，需要调用class时传递参数
class exhaustive(object):
    """
    穷举法寻找素数[1,100]间的素数
    """

    def __init__(self, num):
        self.num = num

    def isprime(self):
        # 将1和2单独处理
        if self.num == 1 or self.num == 2:
            return True
        for i in range(2, self.num):
            if self.num % i == 0:
                return False
            else:
                break
        return True


if __name__ == "__main__":
    a = [i for i in range(1, 50)]
    print("搜索素数的区间为：")
    print(a)
    for a_ in a:
        if exhaustive(a_).isprime():
            print(a_)
            print("**")
