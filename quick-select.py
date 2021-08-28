#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import sys
import time
import random
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def partition_random(A, l=0, r=None):
    """Select random element as pivot, move (in place) all smaller elements left, and all other elements right, of pivot, and return final element of pivot"""
    if r is None:
        r = len(A)-1
    pivot_index = random.randint(l,r)
    pivot = A[pivot_index]
    logging.debug("pivot=(%s), index=(%s)" % (str(pivot), str(pivot_index)))
    #   swap pivot/end 
    A[pivot_index], A[r] = A[r], A[pivot_index]
    #   
    j = l
    for i in range(l, r+1):
        if A[i] < pivot:
            A[i], A[j] = A[j], A[i]
            j += 1
    if j < r:
        A[r], A[j] = A[j], A[r]
    logging.debug("pivot, A=(%s)" % str(A))
    return j


def quickselect(A, k, l=0, r=None):
    """Find k-th smallest element in list A"""
    if r is None:
        r = len(A)-1
    if (k < 0 or k > r-l+1):
        raise IndexError("k=(%s) out of range for l=(%s), r=(%s)" % (k, l, r))

    index = partition_random(A, l, r)

    if (index-l == k):
        return A[index]

    if (index-l > k):
        return quickselect(A, k, l, index-1)
    else:
        return quickselect(A, k-index+l-1, index+1, r)



nums = [3, 1, 5, 9, 4, 7]

for k in range(0, len(nums)):
    result = quickselect(nums, k)
    print("quickselect: k=(%s)" % k)
    print("result=(%s)" % result)
    print()


