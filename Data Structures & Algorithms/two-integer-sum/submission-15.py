class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]
            seen[num] = i



    # taget = diff + seen
    # we add the num to seen and store in index
    # for every loop, we check the diff number, by target - current num
    # if we see diff in seen, we return the index of the diff, and the current number
    # else, we add the current number to seen