import collections
import win32com.client

a = (3, 4, 1, 4, 1)


# count = {}
#
# for i in a:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] += 1
# # print count
# # counter = collections.Counter(a)
# # print count
# for i in count.keys():
#     if count[i] > len(a) / 3:
#         print i

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        count = {}

        for i in A:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for i in count.keys():
            if count[i] > 1:
                return i
        return -1


lol = Solution()
print lol.repeatedNumber(a)
