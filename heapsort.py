import shared as s


# Implementation of heapsort as described in textbook.
# For a given parent index 'n', the index of its children
# will be n*2 + 1 and n*2 + 2
#
# H: array representation of heap
# n: size of H
# i: element to add
def heapify(H, n, i):
    left    = (2 * i) + 1   # index of left child
    right   = (2 * i) + 2   # index of right child
    
    if left < n and H[left] > H[i]:
        hi = left   # largest
    else:
        hi = i      # largest
        
    if right < n and H[right] > H[hi]:
        hi = right

    # if needed to, change the root
    if hi != i:
        s.swap(H, i, hi)
        heapify(H, n, hi)


# heap sorting algorithm. 
def heap_sort(A):
    n = len(A)
    
    for i in range(n, -1, -1):
        heapify(A, n, i)
        
    # repeatedly remove root and re-heapify until sorted array achieved
    # (which will always take n-1 iterations)
    for i in range(n - 1, 0, -1):
        s.swap(A, 0, i)
        heapify(A, i, 0)
