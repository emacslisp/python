from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        result = ""
        for i in range(len(words)) :
            t = words[i]
            result += t[0]

        return result == s

x = Solution()
words = ["alice","bob","charlie"]
s = "abc"
result = x.isAcronym(words, s)
print(result)
var2 = "Python Programming"
print(var2[1:5])

            