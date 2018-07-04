class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        """
        times[i] = [u, v, w], 1 <= len(times) <= 6000
        u, v: vertex label, 1 <= u, v <= N
        w   : edge weight,  1 <= w <= 100
        1 <= N <= 100, 1 <= K <= N
        """
        overflow = 101
        delay = [overflow]*N
        delay[K-1] = 0
        
        modif_times = []
        
        for time in times:                # drop the edges that travel from P (P != K) to K
            if time[1] != K:
                modif_times.append(time)
            
        flag = 1
        
        while flag == 1:
            
            flag = 0
            
            for u, v, w in modif_times:
                
                # d(K,V) < inf && d(K,V) > d(K,U) + d(U,V)
                if delay[u-1] < overflow and delay[v-1] > delay[u-1] + w: 
                    delay[v-1] = delay[u-1] + w
                    flag = 1
        
        network_delay = max(delay)
        
        if network_delay < overflow:
            return network_delay
        else:
            return -1
