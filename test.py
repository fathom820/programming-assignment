import shared as s

def swap (nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
 
 
# Partition routine using the Dutch national flag algorithm
def partition(nums, start, end):
    mid = start
    pivot = nums[end]
 
    while mid <= end:
        if nums[mid] < pivot:
            swap(nums, start, mid)
            start += 1
            mid += 1
        elif nums[mid] > pivot:
            swap(nums, mid, end)
            end -= 1
        else:
            mid += 1
 
    # nums[start … mid-1] contains all occurrences of a pivot
    return start - 1, mid
 
 
# 3–way Quicksort routine
def quicksort(nums, start, end):
 
    # base condition for 0 or 1 elements
    if start >= end:
        return
 
    # handle 2 elements separately as the Dutch national flag algorithm
    # will work for 3 or more elements
    if start - end == 1:
        if nums[start] < nums[end]:
            swap(nums, start, end)
        return
 
    # rearrange elements across pivot using the Dutch national flag algorithm
    x, y = partition(nums, start, end)
 
    # recur on sublist containing elements that are less than the pivot
    quicksort(nums, start, x)
 
    # recur on sublist containing elements that are more than the pivot
    quicksort(nums, y, end)
 
 
if __name__ == '__main__':
 
    nums = s.file_to_array("input/small/unsorted/0.dat")
 
    # sort list
    quicksort(nums, 0, len(nums) - 1)
 
    # print the sorted list
    print(nums)