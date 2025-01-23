def twoSum(nums, target):
    k=1  
    for n in range(len(nums)-1):
        for j in range(k, len(nums)):
            if nums[n] + nums[j] == target:
                return n, j
        k=k+1
          
arrnum=[2,5,5,11]
tar=10

print(twoSum(arrnum, tar))