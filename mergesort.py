# "merge" two arrays
# there are two separate pointers to each array that crawl through the values.
# their values are compared with each step of the algorithm.
# if the value at one pointer is higher than the other, then that value
# will be added to the output array and the higher pointer will
# move forward in its array.
def merge(left, right):
    out = []
    lp  = 0 # pointer for left
    rp  = 0 # pointer for right
    
    while lp < len(left) and rp < len(right):
        # for each loop, compare elements 
        # at each position of both arrays
        if left[lp] < right[rp]:
            out.append(left[lp])
            lp += 1
        else:
            out.append(right[rp])
            rp += 1
    
    # add any extras to the end of the array
    # i spent forever trying to figure out how to make this work;
    # it turns out, you need to use ".extend" and not ".append" for
    # this sort of operation. it also took me an embarrassingly
    # long amount of time to figure that out.
    out.extend(left[lp : ])
    out.extend(right[rp : ])
    
    return out
        
# Top-down merge sort algorithm
# A[]   = array to sort
def merge_sort(A):
    if len(A) == 1:
        return A
    
    mid         = len(A) // 2       # middle index - if size is odd, left partition will be 1 larger
    left        = A[ : mid]         # everything to left of mid
    right       = A[mid : ]         # everything to right of and including mid
    
    # recursively merge sort two halves
    left_part   = merge_sort(left)
    right_part  = merge_sort(right)
    
    return merge(left_part, right_part)