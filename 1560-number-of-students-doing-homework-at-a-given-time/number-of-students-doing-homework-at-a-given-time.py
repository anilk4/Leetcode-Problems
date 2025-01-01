class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        correct = 0

        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                correct += 1
            
        return correct