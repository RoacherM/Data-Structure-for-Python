#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:23
# @Author  : Houps
# @Email   : sir.housir@gmail.com
# @File    : greedy.py
# @Software: IntelliJ IDEA


# 贪心算法的本质是求解问题时，总做出当前看来最优的选择，且局部最优解构成的集合为全局最优解。（需要严格数学证明）
# 性质1：贪心选择性质，即局部最优解一定为当前状态下做出的最好选择，例如找零钱问题中，当前状态下最优选择为找零后的硬币数最接近0
# 性质2：最优子结构性质，即一个问题的最优解包含他的子问题最优解。使用贪心算法前需要严格证明改性质
# 注意：大多数时候，不需要求解其最优解，求解其最优近似解即可。因此解决一般性问题时，不必要做严格的推理证明！

class greedy:
    """
    最优装船问题，将尽可能多的货物箱Wi（非尽可能多的货物重量）,装入总载重为C的货船。
    """

    def __init__(self, W, C):
        self.W = W
        self.C = C
        self.ids = [i for i in range(len(W))]

    def sorts(self):
        """
        给货物排序
        :return: 排序后的货物及对应编号
        """
        # 先用冒泡法对货物进行排序,核心是两两交换
        flag = 1
        for i in range(len(self.W)):
            # flag用于剪枝，当某趟序列只存在元素比较而无交换时，终止本趟排序
            if flag == 1:
                flag = 0
                # 每次遍历冒泡后的数据,由小到大排序
                for j in range(len(self.W) - i - 1):
                    if self.W[j] >= self.W[j + 1]:
                        # 交换
                        tmp = self.W[j + 1]
                        self.W[j + 1] = self.W[j]
                        self.W[j] = tmp
                        # 交换标签
                        tmp_id = self.ids[j + 1]
                        self.ids[j + 1] = self.ids[j]
                        self.ids[j] = tmp_id
                        # 若发生数据交换，则置1
                        flag = 1
        return self.W, self.ids

    def load(self):
        """
        装载货物
        :return: 可以装填的货物编号
        """
        W, ids = self.sorts()
        ct = 0
        ids_ = []
        for i in range(len(W)):
            ct += W[i]
            if ct <= self.C:
                ids_.append(ids[i])
        return ids_


if __name__ == "__main__":
    cargos = [11, 1, 2, 3, 9, 5, 0.5, 8]
    max = 15
    print("可装填的货物编号为：")
    cargos_load = greedy(cargos, max).load()
    for ele in cargos_load:
        print(ele)
