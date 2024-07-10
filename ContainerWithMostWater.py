def maxArea(height):
    left,right=0,len(height)-1
    max_water=0
    while left<right:
        width=right-left
        min_height=min(height[left],height[right])
        current_water=width*min_height
        max_water=max(max_water,current_water)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_water
heights=[1,8,6,2,5,4,8,3,7]
print(maxArea(heights))
