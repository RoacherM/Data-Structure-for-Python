'''
深度优先遍历： 是一种用于遍历树或者图的算法。沿着树的深度遍历树的节点，尽可能深地搜索树的分支。
            当节点v的所在边都被搜索过了。搜索将回溯到节点v的那条边的起始节点。
            这一过程已知进行，直到已发现从源节点可达的所有节点为止。
            如果还存在未发现的节点，则选择其中一个作为源节点并重复上述过程，整个进程反复进行直到所有节点都被访问为止
            属于盲目搜索
bfs
            从根节点开始，沿着树的宽度遍历树的节点，如果所有节点都被访问，则算法终止
            广度优先遍历一般采用open-close表
'''
class Graph(object):
    """
    实现图的深度优先和广度优先
    """
    def __init__(self,nodes,sides):
        # nodes表示用户输入的点，sides为二元组（u,v）,表示用户输入的边
        # self.sequence为字典，key是点，value为与key相连的边
        self.sequence = {}
        # self.side是临时变量，主要用户保存与指定点v相连的点
        self.side = []
        for node in nodes:
            for side in sides:
                u,v = side
                # 指定点与另一个点在同一个边(可能是源点u或者是终点v)中，
                # 则说明这个点与指定点是相连接的点,则需要将这个点放到self.side中
                if node == u:
                    self.side.append(v)
                elif node == v:
                    self.side.append(u)
            # 遍历属于这个点的所有边，然后将点和边组成字典
            self.sequence[node] = self.side
            self.side = []

    def dfs(self,node):
        """
        深度优先搜索,核心在于pop()
        :param node:
        :return:
        """
        # queue为堆栈，用于存放需要遍历的数据结点
        # order为具体的访问路径，即与该点相连的边
        queue,order = [],[]
        queue.append(node)
        # 如果queue非空,则一直遍历
        while queue:
            v = queue.pop()
            order.append(v)
            # 深度访问：初始节点---儿子---孙子---曾孙，若遇到新结点，则直接去遍历之，遍历后再回来
            # 若遍历的数据不属于order和queue中，则该点还没有访问过，加入queue
            # 每个node访问完了之后要去queue中拿最后一个元素，也就是node节点的孩子
            for w in self.sequence[v]:
                if w not in order and w not in queue:
                    # 将元素加入queue的末尾，每次弹出的也是末尾
                    queue.append(w)
        return order

    def bfs(self,node):
        """
        广度优先搜索，核心在于pop(0)
        :param node:
        :return:
        """
        # queue，order一个用作遍历，一个用作更新结点
        queue,order = [],[]
        queue.append(node)
        order.append(node)
        while queue:
            v = queue.pop(0)
            for w in self.sequence[v]:
                # 出现的点不在order中，则将其添加到queue,order中
                if w not in order:
                    queue.append(w)
                    order.append(w)
        return order

if __name__ == "__main__":
    from PIL import Image
    im = Image.open('Graph.png')
    im.show()
    nodes = [i+1 for i in range(8)]
    print("nodes:",nodes)
    sides = [(1,2),
             (1,3),
             (2,4),
             (2,5),
             (4,8),
             (5,8),
             (3,6),
             (3,7),
             (6,7)]
    G = Graph(nodes,sides)
    print(G.dfs(2))
    print(G.bfs(2))
