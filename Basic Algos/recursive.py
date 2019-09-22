#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:14
# @Author  : Houps
# @Email   : sir.housir@gmail.com
# @File    : recursive.py
# @Software: IntelliJ IDEA


# 递归与分治：将较大规模的问题拆成较小规模的同类问题，然后逐个解决这些小的子问题
# class无初始化时的写法，调用时用class().method(...)
class recursive:
    def multiply(self, num):
        """
        利用递归法实现n的阶乘操作
        """
        # 单独处理0，0！= 1
        if num == 0:
            return 1
        # 提取递推公式f(n) = n*f(n-1)，其中f(n)表示为n!的阶乘，n>=1
        else:
            return num * self.multiply(num - 1)

    def splits(self, num1, num2):
        """
        将一个整数表示成一些列整数之和，并计算整数的划分总数,每个整数>=1，用P(n,m)表示由最大加数不大于m组成n的个数
       """
        # 总结规律,以6为例，其P(6,m)=11.
        # 当m=6（即n）时，此时ct=1；
        # 当m>=6（n<m）时，P(6,m) = P(6,6)
        # 当n>m>1时，P(n,m) = P(n,m-1)+P(n-m,m) 即第一部分P等于不大于m-1时值
        # 第二部分可以理解为 P(n,m:m等于m) = P(n-m,m),只需要处理P(n-m:m)
        # 当m=1时，P(n,m)=1
        if num2 == 1:
            return 1
        elif num2 > num1:
            return self.splits(num1, num1)
        elif num2 == num1:
            return self.splits(num1, num1 - 1) + 1
        else:
            return self.splits(num1, num2 - 1) + self.splits(num1 - num2, num2)


if __name__ == "__main__":
    print(recursive().multiply(5))
    print(recursive().splits(6, 4))
