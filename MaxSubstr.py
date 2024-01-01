class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        visited = set()
        keys = set()
        count = {}
        flag = 0
        maxlen = 0
        for n in s:
            if n in visited:
                count[n] +=1
                keys.add(n)
                flag = 1
            else:
                visited.add(n)
                count[n] = 1        

        if flag == 1:
            for key in keys:
                prev_key_idx = 0
                for _ in range(count[key]-1):
                        

                    if count[key] > 2:
                        l = len(s[s.index(key)+1:len(s)-s[-1::-1].index(key)-1])
                        maxlen = max(maxlen, l)
                        break

                    l = len(s[s.index(key, prev_key_idx)+1:s.index(key, prev_key_idx + s.index(key)+1)])
                    prev_key_idx = s.index(key, prev_key_idx)
                    maxlen = max(maxlen, l)
                    
            return maxlen
        
        return -1
