class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        for i in nums1:
            if i not in nums2:
                answer[0].append(i)
        for j in nums2:
            if j not in nums1:
                answer[1].append(j)
        for i in range(len(answer)):
            answer[i] = list(set(answer[i]))
        return answer