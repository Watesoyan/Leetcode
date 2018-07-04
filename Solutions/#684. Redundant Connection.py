class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        memory = set(edges[0])
        stack = edges[1:]
        
        while True:
            n = len(stack)
            for i in range(n):
                [u, v] = stack[i]
                if u in memory and v in memory:
                    if u > v:
                        u, v = v, u
                    return [u, v]
                elif u in memory:
                    memory.add(v)
                    del stack[i]
                    break
                elif v in memory:
                    memory.add(u)
                    del stack[i]
                    break
