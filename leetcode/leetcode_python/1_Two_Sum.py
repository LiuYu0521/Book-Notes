class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index in range(len(nums)):
            x = nums[index]
            complement = target - x
            if(complement in map):
                return [map[complement],index]
            map[x] = index
        return False


if __name__ == '__main__':

    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
