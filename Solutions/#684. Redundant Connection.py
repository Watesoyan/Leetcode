class Solution(object):
    # union-find set version, takes 36 ms in LeetCode Benchmark
    def find(self, root, x):
        val = root.get(x)
        if val is None:
            root[x] = x
            return x, 0
        else:
            n = 0
            while x != val:
                x = root[x]
                val = root[x]
                n += 1
            return x, n
            
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        root = {}
        
        for u, v in edges:
            ur, nu = self.find(root, u)
            vr, nv = self.find(root, v)
            if ur == vr:
                return [u, v]
            elif nu > nv:
                root[vr] = ur
            else:
                root[ur] = vr
        return None
