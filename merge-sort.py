import random

def merge_sort(A):
    if len(A) <= 1:
        return

    mid = len(A)//2
    L = A[:mid]
    R = A[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    while (i < len(L) and j < len(R)):
        if (L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while (i < len(L)):
        A[k] = L[i]
        i += 1
        k += 1
    while (j < len(R)):
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort_inplace(A, l=0, r=None):
    if r is None:
        r = len(A)-1
    if l >= r:
        return

    mid = l + (r-l) // 2

    merge_sort_inplace(A, l, mid)
    merge_sort_inplace(A, mid+1, r)

    l2 = mid + 1

    # If the direct merge is already sorted
    if (A[mid] <= A[l2]):
        return

    # Two pointers to maintain l
    # of both Aays to merge
    while (l <= mid and l2 <= r):

        # If element 1 is in right place
        if (A[l] <= A[l2]):
            l += 1
        else:
            value = A[l2]
            k = l2

            # Shift all the elements between l1, l2 right by 1.
            while (k != l):
                A[k] = A[k - 1]
                k -= 1

            A[l] = value

            l += 1
            mid += 1
            l2 += 1

values = [ random.randint(1, 20) for x in range(20) ]
print(values)
merge_sort(values)
print(values)

values = [ random.randint(1, 20) for x in range(20) ]
print(values)
merge_sort_inplace(values)
print(values)





