class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    arr.append(num)
                next_digit += 1
        arr.sort()
        return arr
        