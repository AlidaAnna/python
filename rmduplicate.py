nums=[1,1,2,2,3,3,3,5,5,6,7]
leng=len(nums)
for i in range(leng -1,-1,-1):
    for j in range(i -1,-1,-1):
            if nums[i]==nums[j]:  
                 nums.pop(i)
                 break
print(nums)
            

"""my method leetcode advances method that is goob method by using to pointer"""