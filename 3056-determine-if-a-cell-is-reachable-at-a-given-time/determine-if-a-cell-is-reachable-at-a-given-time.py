class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy :
            return t > 1 or t == 0
        
        height = abs(sy - fy)
        width =  abs(sx - fx)
        corner_moves = abs(height - width)
        return  (min(height, width) + corner_moves)  <= t