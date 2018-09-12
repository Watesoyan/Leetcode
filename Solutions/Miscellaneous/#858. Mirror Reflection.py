class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        pos = q
        right= 1  # right== 1 when incident on right 
        up = 1    # up == 1 when light travels upwards 
        
        while True:
            if right:
                if pos == 0:
                    return 0
                if pos == p:
                    return 1
                right = 0
                if up:
                    pos += q
                else:
                    pos -= q
            else:
                if pos == p:
                    return 2
                right = 1
                if up:
                    pos += q
                else:
                    pos -= q
            
            if pos > p:
                pos = 2*p-pos
                up = 0
            
            if pos < 0:
                pos = -pos
                up = 1
