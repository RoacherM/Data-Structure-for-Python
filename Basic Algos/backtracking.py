#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:23
# @Author  : Houps
# @Email   : sir.housir@gmail.com
# @File    : backtracking.py
# @Software: IntelliJ IDEA


# 回溯法：在包含问题的所有解的解空间树中，按照深度优先搜索的策略从根节点出发深度搜索解空间树。当探索到某一结点时，先判断该结点是否包含问题的解，
# 如果包含，就从该点出发继续搜索；否则，跳过以该结点为根的子树的系统搜索，逐层向其祖先结点回溯，这个过程称为剪枝。

class backtracking:
    """
    回溯法解N皇后问题：在N*N的棋盘中，求无冲突的摆放N个皇后棋子的情况。所谓无冲突是指该棋子的横竖交叉上均无其他棋子。
    """
    def __init__(self):
        self.ct = 0
    def Queen(self, column, Q, N):
        """
        求解N皇后问题的所有解
        """
        if column == N:
            for row in range(N):
                for column_ in range(N):
                    print(Q[row][column_], end='')
                print('\n')
            print('++++++')
            self.ct+=1
        # 用递归方式实现回溯查找
        for row in range(N):
            if self.isvalid(row, column, Q):
                Q[row][column] = 1
                self.Queen(column + 1, Q, N)
                Q[row][column] = 0
        return self.ct

    def isvalid(self, row, column, Q):
        """
        检查棋子摆放是否合理
        :return: Boolean
        """
        # 判断行
        for column_ in range(N):
            if Q[row][column_] == 1 and column_ != column:
                return 0
        # 判断列
        for row_ in range(N):
            if Q[row_][column] == 1 and row_ != row:
                return 0
        # 判断左上
        for row_ in range(N):
            for column_ in range(N):
                if row_ == row - 1 and column_ == column - 1 and Q[row_][column_] == 1:
                    return 0
        # 判断左下
        for row_ in range(N):
            for column_ in range(N):
                if row_ == row + 1 and column_ == column - 1 and Q[row_][column_] == 1:
                    return 0
        # 判断右上
        for row_ in range(N):
            for column_ in range(N):
                if row_ == row - 1 and column_ == column + 1 and Q[row_][column_] == 1:
                    return 0
        # 判断右下
        for row_ in range(N):
            for column_ in range(N):
                if row_ == row + 1 and column_ == column + 1 and Q[row_][column_] == 1:
                    return 0
        return 1


if __name__ == "__main__":
    N = 8
    Q = [[0 for i in range(N)] for j in range(N)]
    chess = backtracking().Queen(0, Q, N)
    print(chess)
