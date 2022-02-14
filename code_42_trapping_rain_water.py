class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n < 3: 
            return 0
        p_left = 0
        max_left = 0
        p_right = n-1
        max_right = 0
        rain_trapped = 0
        while p_left <= p_right:
            if height[p_left] <= height[p_right]:
                if height[p_left] >= max_left:
                    max_left = height[p_left]
                else:
                    rain_trapped += max_left - height[p_left]
                p_left += 1
            else:
                if height[p_right] >= max_right:
                    max_right = height[p_right]
                else:
                    rain_trapped += max_right - height[p_right]
                p_right -= 1
        return rain_trapped