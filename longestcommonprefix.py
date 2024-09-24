class Solution:

    def longestCommonPrefix(self, strs):

        if not strs:
            return ''

        prefix = strs[0]

        for i in range(1, len(strs)):

            while strs[i].find(prefix) !=0:

                prefix = prefix[:-1]

                print(prefix)

                if not prefix:

                    return ''
        return prefix

result = Solution().longestCommonPrefix(['flower', 'flow', 'flight'])

print(result)