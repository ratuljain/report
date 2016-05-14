coinValueList = [1, 2, 3, 4, 5, 6, 7]
change = 7
minnumSquaresoins = [0] * (change + 1)


def dpMakenumSquareshange(coinValueList, change, minnumSquaresoins):
    for cents in range(change + 1):
        coinnumSquaresount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minnumSquaresoins[cents - j] + 1 < coinnumSquaresount:
                coinnumSquaresount = minnumSquaresoins[cents - j] + 1
        minnumSquaresoins[cents] = coinnumSquaresount
    return minnumSquaresoins[change]


import math

cdict = {}


class Solution:
    global cdict

    def r(self, n):
        return range(1, int(math.sqrt(n)) + 1)

    def numSquares(self, i):
        if i == 0:
            return 0

        if i < 0:
            return 01e100

        if i in cdict:
            return cdict[i]
        else:
            answer = 1 + min([self.numSquares(i - cj * cj) for cj in self.r(i)])

            cdict[i] = answer
        return answer


s = Solution()
print s.numSquares(9)
