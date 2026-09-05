class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        max=(len(heights)-1)*min(heights[-1], heights[0])
        while l<r:
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
            if (r-l)*min(heights[l], heights[r])>max:
                max=(r-l)*min(heights[l], heights[r])
        return max