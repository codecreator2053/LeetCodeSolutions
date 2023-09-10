#set->O(1), get->O(n), O()
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key][timestamp] = value
        else:
            self.store[key] = {timestamp:value}
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        min_time = -float('inf')
        
        for time in self.store[key].keys():
            if time > timestamp:
                continue
            if time > min_time:
                min_time = time
        if min_time == -float('inf'):
            return ""
        return self.store[key][min_time]


#O(1) for set, #O(log(n)) for get
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([timestamp, value])
        else:
            self.store[key] = [[timestamp, value]]
            
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        s = self.store[key]
        l = 0; r = len(s)
        while l<r:
            mid = (l+r)//2
            if s[mid][0] <= timestamp:
                l = mid+1
            elif s[mid][0] > timestamp:
                r = mid
            else:
                return s[mid][1]
            
        return "" if r==0 else s[r-1][1]