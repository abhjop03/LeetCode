class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums1 = []
        nums2 = []
        for num in nums:
            if num < 0:
                nums1.append(num*num)
            else:
                nums2.append(num*num)
        nums1.reverse()

        idx1 = 0
        idx2 = 0
        count = 0

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2] and idx1 < len(nums1):
                nums[count] = nums1[idx1]
                idx1+=1
            elif nums2[idx2] < nums1[idx1] and idx2 < len(nums2):
                nums[count] = nums2[idx2]
                idx2+=1
            elif nums1[idx1] == nums2[idx2]:
                nums[count] = nums1[idx1]
                idx1+=1
                count+=1
                nums[count] = nums2[idx2]
                idx2+=1
            count+=1

        while idx1 < len(nums1):
            nums[count] = nums1[idx1]
            idx1+=1
            count+=1

        while idx2 < len(nums2):
            nums[count] = nums2[idx2]
            idx2+=1
            count+=1
            
        
        return nums