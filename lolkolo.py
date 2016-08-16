# import collections
# import win32com.client
#
# a = (3, 4, 1, 4, 1)
#
#
# # count = {}
# #
# # for i in a:
# #     if i not in count:
# #         count[i] = 1
# #     else:
# #         count[i] += 1
# # # print count
# # # counter = collections.Counter(a)
# # # print count
# # for i in count.keys():
# #     if count[i] > len(a) / 3:
# #         print i
#
# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def repeatedNumber(self, A):
#         count = {}
#
#         for i in A:
#             if i not in count:
#                 count[i] = 1
#             else:
#                 count[i] += 1
#         for i in count.keys():
#             if count[i] > 1:
#                 return i
#         return -1
#
#
# lol = Solution()
# print lol.repeatedNumber(a)

import itertools


def findsubsets(S, m):
    return set(itertools.combinations(S, m))


from itertools import chain, combinations


def powerset(iterable):
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))


# print list(powerset("123"))

def permutations(A, B=''):
    assert len(A) >= 0
    assert len(A) == len(set(A))
    if len(A) == 0:
        return [B]
    else:
        res = []
        for i in range(len(A)):
            res.extend(permutations(A[0:i] + A[i + 1:], B + A[i]))

        return res


print permutations('word')
