import shared as s


# take median of three elements
def median_three(a, b, c):
    return sorted([a, b, c])[1] 
    

# Partitioning algorithm, inspired by
# dutch national flag problem mentioned
# in the handout.
def qs_part(A, lo, hi):
    mid = lo
    if len(A) < 101:
        p = A[lo]
    else:
        # pivot set to median of 3, as described in handout.
        # '//' must be used for floor division in Python 3.
        # it took me an embarrassingly long amount of time
        # to figure that out.
        p = median_three(A[lo], A[(lo + hi) // 2], A[hi]) 
    
    while mid <= hi:
        if A[mid] < p:
            s.swap(A, mid, lo)
            mid += 1
            lo  += 1
        elif A[mid] > p:
            s.swap(A, mid, hi)
            hi  -= 1
        else:
            mid += 1                # move end of "equals" partition forward
    return (lo - 1), mid            # return indexes containing all values == pivot
    

# Quicksort implementation as described in handout.
# A: Array to sort
# lo:       start index (1 after pivot in first case)
# hi:       end index
def quick_sort(A,lo, hi):
    if lo >= hi:
        return                      # if there are 0 or 1 elements in A
    
    if lo - hi == 1:
        if A[lo] < A[hi]:           # if 2 elements, sort them
            s.swap(A, lo, hi)
        return
    
    a, b = qs_part(A, lo, hi)
    quick_sort(A, lo, a)            # recursively sort partition 1 (elements < pivot)
    quick_sort(A, b, hi)            # recursively sort partition 2 (elements > pivot)
    # no need to sort between 'i' and 'j' because those items == pivot