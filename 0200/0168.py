class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while n > 0:
            result.append(capitals[(n-1)%26])
            n = (n-1) // 26
        result.reverse()
        return ''.join(result)