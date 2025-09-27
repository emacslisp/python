from typing import List
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        dict = {}
        result = []
        for i in friends:
            dict[i] = 1

        for i in order:
            if dict.get(i) == 1:
                result.append(i)

        return result


solution = Solution()
order = [3,1,2,5,4]
friends = [1,3,4]
result = solution.recoverOrder(order, friends)
for i in result:
    print(i)
