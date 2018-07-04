class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = {0}
        keys = set(rooms[0])
        cnt = len(rooms)-1
        
        if cnt == 0:
            return True
        
        while len(keys) > 0:
            ix = keys.pop()
            if ix not in visited:
                cnt -= 1
                visited.add(ix)
                keys |= set(rooms[ix])
                if cnt == 0:
                    return True 
        return False
