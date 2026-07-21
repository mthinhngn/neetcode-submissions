class Solution:
    def twoSum(self, nums, target):

# Using Hash Map
# 1/ Create a box call "seen" to store a interger
# and its location alr see
# Checking every combination to see if they comeup with
# target -> O(n^2)
# Better: check if the diff exist -> O(n)
# 2/ diff = target - nums[i]
# 3/ retur i and j
# 4/ using a loop to get get the 1, 2, 3 number to
#compare with the diff intergers

#After vid:
# 1/ Using hash map to store bot index and value
# 2/ Find the diffent number = target - nums[i],
# remember both index and value
# 3/ do calation for all the array first, then if 
# diff value alr in the "seen". Return index

        seen = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i     
        return 
