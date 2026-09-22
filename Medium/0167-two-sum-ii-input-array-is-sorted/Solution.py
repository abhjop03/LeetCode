class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if len(numbers) == 0:
            return []
        s:int = 0
        e:int = len(numbers)-1
        while s < e:
            sum = numbers[s] + numbers[e]
            if sum > target:
                e-=1
            elif sum < target:
                s+=1
            else:
                return [s+1, e+1]
        return []
        