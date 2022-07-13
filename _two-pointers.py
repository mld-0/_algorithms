#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List, Optional
#   {{{2

class ListNode:
    #   {{{
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next
    def from_list(values):
        #   {{{
        if len(values) == 0:
            return None
        result = ListNode()
        first = result
        second = first
        for v in values:
            first.val = v
            first.next = ListNode()
            second = first
            first = first.next
        second.next = None
        return result
        #   }}}
    def to_list(self):
        #   {{{
        result = []
        first = self
        while first is not None:
            result.append(first.val)
            first = first.next
        return result
        #   }}}
    def __repr__(self):
        #   {{{
        return str(self.to_list())
        #   }}}
    #   }}}

#   TODO: 2021-10-04T21:22:34AEDT _algorithms, two-pointers examples

def middleNodeLinkedList_TwoPointers(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the middle node in a given linked list"""
    l = head
    r = head
    while (r is not None) and (r.next is not None):
        l = l.next
        r = r.next.next
    return l


def twoSum_TwoPointers(numbers: List[int], target: int) -> List[int]:
    """Find the indexes of values in sorted list 'numbers' which add to 'target'"""
    l = 0
    r = len(numbers) - 1
    while l < r:
        trial = numbers[l] + numbers[r]
        if trial == target:
            return [l, r]
        elif trial < target:
            l += 1
        elif trial > target:
            r -= 1


def reverseListInplace_TwoPointers(s: List[str]) -> None:
    """Reverse the elements of list 's' inplace"""
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


def removeDuplicatesInPlace_TwoPointers(nums: List[int]) -> int:
    """Remove duplicates in-place, returning number of unique elements"""
    #   position of largest unique value
    l = 0
    #   position in the list
    r = 1
    #   Until we reach end of the list
    while r < len(nums):
        #   Current number is larger than largest unique number
        if nums[r] > nums[l]:
            #   Add it as the next unique number 
            nums[l+1] = nums[r]
            l += 1
        r += 1

    #   Remove extra values
    for i in range(l+1, len(nums)):
        nums[i] = None

    #   Unique values are given by nums[:l+1]
    return l+1



def removeNthFromEndLinkedList_TwoPointers(head: ListNode, n: int) -> ListNode:
    """Remove n-th node from linked list"""
    l = head
    r = head

    for i in range(n):
        r = r.next

    if r is None:
        return head.next

    while r.next is not None:
        r = r.next
        l = l.next

    l.next = l.next.next
    return head


def intervalIntersection_TwoPointers(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Given two sorted list of intervals (as start/end points), return intersection as a sorted list of intervals"""
    result = []
    #   position in A
    l = 0
    #   position in B
    r = 0

    while l < len(A) and r < len(B):
        #   start of interval
        low = max(A[l][0], B[r][0])
        #   end of interval
        high = min(A[l][1], B[r][1])

        if low <= high:
            result.append( [low, high] )

        #   advance interval with smaller end value
        if A[l][1] < B[r][1]:
            l += 1
        else:
            r += 1

    return result



def deleteDuplicatesSortedLinkedList_TwoPointers(head: Optional[ListNode]) -> Optional[ListNode]:
    """Remove duplicate values from sorted linked list"""

    #   Pseudo-Node 'sentinal' inserted before beginning of list, allowing first element to be easily removed if needed
    sentinal = ListNode(0, head)

    #   'l' points to previous node 
    l = sentinal

    #   'r' is advanced to skip duplicates
    r = head

    while r is not None:
        #   Is 'r' a duplicate 
        if r.next is not None and r.val == r.next.val:
            #   If 'r' is a duplicate, advance past duplicates and remove them from list
            while r.next is not None and r.val == r.next.val:
                r = r.next
            l.next = r.next
        else:
            #   Otherwise advance 'l'
            l = l.next
        r = r.next

    head = sentinal.next
    return head


def test_twoSum_TwoPointers():
    #   {{{
    input_values = [ ([2,7,11,15], 9), ([2,3,4], 6), ([-1,0], -1), ]
    input_checks = [ [0,1], [0,2], [0,1] ]
    for (numbers, target), check in zip(input_values, input_checks):
        assert( numbers == sorted(numbers) )
        result = twoSum_TwoPointers(numbers, target)
        print("result=(%s)" % str(result))
        assert( result == check )
    #   }}}

def test_deleteDuplicatesSortedLinkedList_TwoPointers():
    #   {{{
    input_values = [ [1,2,3,3,4,4,5], [1,1,1,2,3], ]
    input_checks = [ [1,2,5], [2,3], ]
    for head_list, check in zip(input_values, input_checks):
        print("head_list=(%s)" % str(head_list))
        head = ListNode.from_list(head_list)
        result = deleteDuplicatesSortedLinkedList_TwoPointers(head)
        print("result=(%s)" % str(result))
        result_list = []
        if result is not None:
            result_list = result.to_list()
        print("result_list=(%s)" % result_list)
        assert result_list == check, "Check failed"
    #   }}}

def test_removeDuplicatesInPlace_TwoPointers():
    #   {{{
    def validate_result(nums: List[int], expectedNums: List[int], k: int):
        assert k == len(expectedNums), "Check comparison failed"
        for i in range(k):
            assert nums[i] == expectedNums[i], "Check comparison failed"
    input_values = [ [1,1,2], [0,0,1,1,1,2,2,3,3,4], [-1,0,0,0,0,3,3], ]
    check_values = [ (2, [1,2]), (5, [0,1,2,3,4]), (3, [-1,0,3]), ]
    assert len(input_values) == len(check_values), "input/check Mismatch"
    for nums, (expectedK, expectedNums) in zip(input_values, check_values):
        nums = nums[:]
        k = removeDuplicatesInPlace_TwoPointers(nums)
        print("result=(%s), k=(%s)" % (nums, k))
        assert k == expectedK, "Check comparison failed"
        validate_result(nums, expectedNums, k)
    print()
    #   }}}

def test_reverseListInplace_TwoPointers():
    #   {{{
    input_values = [ ["h","e","l","l","o"], ["H","a","n","n","a","h"] ]
    input_checks = [ ["o","l","l","e","h"], ["h","a","n","n","a","H"] ]
    for _str, check in zip(input_values, input_checks):
        reverseListInplace_TwoPointers(_str)
        print("_str=(%s)" % str(_str))
        assert( _str == check )
    #   }}}

def test_removeNthFromEndLinkedList_TwoPointers():
    #   {{{
    list_values = [ ([1,2,3,4,5], 2), ([1], 1), ([1,2], 1) ]
    list_checks = [ [1,2,3,5], [], [1] ]
    for (loop_values, loop_n), loop_check in zip(list_values, list_checks):
        loop_node = ListNode.from_list(loop_values)
        result = removeNthFromEndLinkedList_TwoPointers(loop_node, loop_n)
        print("result=(%s)" % str(result))
        result_list = []
        if result is not None: 
            result_list = result.to_list()
        assert( result_list == loop_check)
    #   }}}

def test_middleNodeLinkedList_TwoPointers():
    #   {{{
    input_values = [ [1,2,3,4,5], [1,2,3,4,5,6], [0] ]
    input_checks = [ [3,4,5], [4,5,6], [0] ]
    for node_list, check in zip(input_values, input_checks):
        node = ListNode.from_list(node_list)
        result = middleNodeLinkedList_TwoPointers(node)
        print("result=(%s)" % str(result))
        assert( result.to_list() == check )
    #   }}}

def test_intervalIntersection_TwoPointers():
    #   {{{
    input_values = [ ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]), ([[1,3],[5,9]], []), ([], [[4,8],[10,12]]), ([[1,7]], [[3,10]]) ]
    input_checks = [ [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]], [], [], [[3,7]] ]
    for (A, B), check in zip(input_values, input_checks):
        #print("A=(%s), B=(%s)" % (A, B))
        result = intervalIntersection_TwoPointers(A, B)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    #   }}}


if __name__ == '__main__':
    #   {{{
    print("test_deleteDuplicatesSortedLinkedList_TwoPointers():")
    test_deleteDuplicatesSortedLinkedList_TwoPointers()
    print()
    print("test_removeNthFromEndLinkedList_TwoPointers():")
    test_removeNthFromEndLinkedList_TwoPointers()
    print()
    print("test_removeDuplicatesInPlace_TwoPointers():")
    test_removeDuplicatesInPlace_TwoPointers()
    print()
    print("test_middleNodeLinkedList_TwoPointers():")
    test_middleNodeLinkedList_TwoPointers()
    print()
    print("test_twoSum_TwoPointers():")
    test_twoSum_TwoPointers()
    print()
    print("test_reverseListInplace_TwoPointers():")
    test_reverseListInplace_TwoPointers()
    print()
    print("test_intervalIntersection_TwoPointers():")
    test_intervalIntersection_TwoPointers()
    print()
    #   }}}

