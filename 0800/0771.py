class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        n = 0
        for i in S:
            if i in J:
                n += 1
        return n