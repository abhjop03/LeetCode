class Solution:
    def segregate0and1(self, arr):
        # code here
        i = 0
        for j in range(1, len(arr)):
            if arr[i] == 0:
                i+=1
            elif arr[i] == 1 and arr[j] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j+=1
            elif arr[i] == 1 and arr[j] == 1:
                j+=1
        return arr
                