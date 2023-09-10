#O(3^n), recursive but very slow
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def tryCrossing(stones, cur, step):
            if cur >= len(stones):
                return False
            if cur == len(stones)-1:
                return True
            next_val = stones[cur] + step
            if next_val in stones:
                return tryCrossing(stones, stones.index(next_val), step) \
                or tryCrossing(stones, stones.index(next_val), step+1) \
                or (tryCrossing(stones, stones.index(next_val), step-1) if step>1 else False)
            else: return False
                    
        return tryCrossing(stones, 0, 1)


#Adding a memo to reduce redundant checking helps a lot with the backtracking
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def tryCrossing(stones, cur, step, memo):
            if (cur, step) in memo:
                return False
            if cur >= len(stones):
                return False
            if cur == len(stones)-1:
                return True
            next_val = stones[cur] + step
            if next_val not in stones:
                memo.add((cur, step))
                return False
            for i in [step-1, step, step+1]:
                if i>0 and tryCrossing(stones, stones.index(next_val), i, memo):
                    return True
            memo.add((cur, step))
            return False

        memo = set()
        return tryCrossing(stones, 0, 1, memo)