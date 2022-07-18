from types import MemberDescriptorType


def findMedianSortedArrays (nums1, nums2) -> float:
    LengthsSum = len(nums1) + len(nums2)
    lastUpdate = "0"
    nums1Index , nums2Index,median = 0 , 0, 0
    for i in range(int(LengthsSum/2)):
        if nums1[nums1Index] < nums2[nums2Index]:

    print("lastUpdate = {}".format(lastUpdate))

        
    return median
print(findMedianSortedArrays([1,3,4,5,6,9],[2,7,8]))