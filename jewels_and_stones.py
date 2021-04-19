class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_map = {}
        for jewel in jewels:
            jewels_map[jewel] = 0
        for stone in stones:
            if stone in jewels_map.keys():
                jewels_map[stone] += 1
        return sum(jewels_map.values())
