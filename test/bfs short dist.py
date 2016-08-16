class Solution:
    def permute(self, numbers, start, result):
        if start == len(numbers):
            result.append(numbers)
            # result.append([x for x in numbers])
            return
        for i in range(start, len(numbers)):
            numbers[start], numbers[i] = numbers[i], numbers[start]
            self.permute(numbers, start + 1, result)
            numbers[start], numbers[i] = numbers[i], numbers[start]

    def solution(self, numbers):
        result = []
        if not numbers or len(numbers) == 0:
            return numbers
        self.permute(numbers, 0, result)
        return result


res1 = Solution().solution([1, 2, 3])
print(res1)
