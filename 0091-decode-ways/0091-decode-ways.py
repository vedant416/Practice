class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]

            result = decode(index + 1)
            if index+1 < len(s) and int(s[index] + s[index+1]) < 27:
                result += decode(index + 2)

            memo[index] = result
            return result

        return decode(0)