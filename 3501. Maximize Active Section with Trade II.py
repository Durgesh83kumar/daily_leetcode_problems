import math

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        total_1s = s.count('1')
        
        segments = [] 
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segments.append((int(s[i]), i, j - 1, j - i))
            i = j
            
        S = len(segments)
        
        seg_idx = [0] * n
        for idx, (t, st, en, length) in enumerate(segments):
            for k in range(st, en + 1):
                seg_idx[k] = idx
                
        gain = [0] * S
        for i in range(S):
            if segments[i][0] == 1:
                left_len = segments[i - 1][3] if i > 0 else 0
                right_len = segments[i + 1][3] if i < S - 1 else 0
                gain[i] = left_len + right_len
                
        if S > 0:
            max_k = int(math.log(S, 2)) + 1
            st = [[0] * max_k for _ in range(S)]
            for i in range(S):
                st[i][0] = gain[i]
            for j in range(1, max_k):
                for i in range(S - (1 << j) + 1):
                    st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
                    
        def query_rmq(l, r):
            if l > r: 
                return 0
            k = int(math.log(r - l + 1, 2))
            return max(st[l][k], st[r - (1 << k) + 1][k])
            
        
        ans = []
        for q_l, q_r in queries:
            
            if q_r - q_l < 2:
                ans.append(total_1s)
                continue
                
            sL = seg_idx[q_l]
            sR = seg_idx[q_r]
            
            
            if sL == sR:
                ans.append(total_1s)
                continue
            
            
            first_1 = sL + 1 if segments[sL + 1][0] == 1 else sL + 2
            last_1 = sR - 1 if segments[sR - 1][0] == 1 else sR - 2
            
            
            if first_1 > last_1:
                ans.append(total_1s)
                continue
                
            
            def get_gain(k):
                l_seg = k - 1
                r_seg = k + 1
                
                left_len = segments[l_seg][2] - max(q_l, segments[l_seg][1]) + 1
                right_len = min(q_r, segments[r_seg][2]) - segments[r_seg][1] + 1
                
                return left_len + right_len
                
            
            max_g = get_gain(first_1)
            if first_1 != last_1:
                max_g = max(max_g, get_gain(last_1))
                
            
            if first_1 + 2 <= last_1 - 2:
                max_g = max(max_g, query_rmq(first_1 + 2, last_1 - 2))
                
            ans.append(total_1s + max_g)
            
        return ans