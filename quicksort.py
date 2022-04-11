import time
import random


# swap two values in an array
# A[]: array; i, j: two indexes in A[]
def array_swap(A, i, j):
    A[i], A[j] = A[j], A[i]


# take median of three elements
def median_three(a, b, c):
    return sorted([a, b, c])[1] 
    

def qs_part(A, lo, hi):
    mid = lo
    if len(A) < 101:
        p = 0
    else:
        p = median_three(A[lo], A[(lo + hi) // 2], A[hi]) # pivot set to median of 3, as described in handout 
    # ('//' must be used for floor division in Python 3 -- it took me longer than I'm willing to admit to figure that out.)
    
    while mid <= hi:
        if A[mid] < p:
            array_swap(A, mid, lo)
            mid += 1
            lo  += 1
        elif A[mid] > p:
            array_swap(A, mid, hi)
            hi  -= 1
        else:
            mid += 1
    return (lo - 1), mid # return partition
    

# Quicksort implementation as described in handout.
# A: Array to sort
# write:    name of file to write sorted results to
# out:      name of file to write runtime to
# lo:       start index (1 after pivot in first case)
# hi:       end index
def quick_sort(A,lo, hi):
    if lo >= hi:
        return # if there are 0 or 1 elements in A
    
    if lo - hi == 1:
        if A[lo] < A[hi]: # if 2 elements, sort them
            array_swap(A, lo, hi)
        return
    
    i, j = qs_part(A, lo, hi)
    quick_sort(A, lo, i) # recursively sort partition 1 (elements < pivot)
    quick_sort(A, j, hi) # recursively sort partition 2 (elements > pivot)
    # no need to sort between 'i' and 'j' because those items == pivot