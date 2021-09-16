def removeDuplicates(nums):
            n = 0
            for i in range(1,len(nums)):
                if nums[i] != nums[n]:
                    n+=1
                    nums[n]=nums[i]
            return n+1