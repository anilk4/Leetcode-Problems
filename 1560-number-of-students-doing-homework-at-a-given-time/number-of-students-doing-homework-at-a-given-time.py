class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        correct = 0

        for s, e in zip(startTime, endTime):
            if s <= queryTime and e >= queryTime:
                correct += 1
            
        return correct