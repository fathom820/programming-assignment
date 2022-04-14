import shared as s


# Implementation of heapsort as the algorithm
# was described in the textbook.
# 
# For a given parent index 'n', the index of its children
# will be n*2 + 1 and n*2 + 2
#
# H: array representation of heap
# n: size of H
# i: index of heap
def heapify(H, n, i):
    left    = (2 * i) + 1   # index of left child
    right   = (2 * i) + 2   # index of right child
    
    # if end of left hasn't been reached
    # test if child node violates max-heap
    if left < n and H[left] > H[i]:
        # set highest to lef
        hi = left   # largest
    else:
        # set highest to i
        hi = i      # largest
    
    # if end of right hasn't been reached
    # test if child node violates max-heap
    if right < n and H[right] > H[hi]:
        hi = right

    # if needed to, change the root
    if hi != i:
        s.swap(H, i, hi)
        heapify(H, n, hi)


# Heap sorting implementation using heapify()
# A: Array to sort
def heap_sort(A):
    n = len(A)
    
    # build max heap from array by passing each node in array order
    # must start at index 1, this 'for' loop makes sure that happens
    for i in range(n, -1, -1):
        heapify(A, n, i)
        
    # repeatedly remove root and re-heapify until sorted array achieved
    # (which will always take n-1 iterations)
    for i in range(n - 1, 0, -1):
        s.swap(A, 0, i)
        heapify(A, i, 0)
