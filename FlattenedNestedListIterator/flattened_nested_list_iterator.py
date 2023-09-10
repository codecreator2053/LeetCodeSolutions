class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1]+=1
        return nestedList[i].getInteger()  
    
    def hasNext(self) -> bool:
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False


class NestedIterator2:
    def __init__(self, nestedList: [NestedInteger]):
        def dfs(nlist, stack):
            for i in range(len(nlist)-1, -1, -1):
                if nlist[i].isInteger():
                    stack.append(nlist[i].getInteger())
                else: dfs(nlist[i].getList(), stack)
        self.stack = []
        dfs(nestedList, self.stack);
        
        
    
    def next(self) -> int:
        item = self.stack[-1]
        self.stack.pop()
        return item
    
    def hasNext(self) -> bool:
        return len(self.stack)>0



class NestedIterator3:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range(len(nestedList)-1, -1, -1):
                self.stack.append(nestedList[i])
        
    
    def next(self) -> int:
        self.hasNext()
        item = self.stack[-1].getInteger()
        self.stack.pop()
        return item
    
    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            top = self.stack[-1].getList()
            self.stack.pop()
            for i in range(len(top)-1, -1, -1):
                self.stack.append(top[i])
        return False
