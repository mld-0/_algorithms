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
    while (not r is None) and (not r.next is None):
        l = l.next
        r = r.next.next
    return l


def twoSum_TwoPointers(numbers: List[int], target: int) -> List[int]:
    """Find the indexes (1-indexed) of values in sorted list 'numbers' which add to 'target'"""
    l = 0
    r = len(numbers) - 1
    while l < r:
        trial = numbers[l] + numbers[r]
        if trial == target:
            return [l+1, r+1]
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
    input_checks = [ [1,2], [1,3], [1,2] ]
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

def test_reverseList_TwoPointers():
    #   {{{
    input_values = [ ["h","e","l","l","o"], ["H","a","n","n","a","h"] ]
    input_checks = [ ["o","l","l","e","h"], ["h","a","n","n","a","H"] ]
    for _str, check in zip(input_values, input_checks):
        reverseList_TwoPointers(_str)
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

if __name__ == '__main__':
    #   {{{
    print("test_deleteDuplicatesSortedLinkedList_TwoPointers():")
    test_deleteDuplicatesSortedLinkedList_TwoPointers()
    print()
    print("test_removeNthFromEndLinkedList_TwoPointers():")
    test_removeNthFromEndLinkedList_TwoPointers()
    print()
    print("test_middleNodeLinkedList_TwoPointers():")
    test_middleNodeLinkedList_TwoPointers()
    print()
    print("test_twoSum_TwoPointers():")
    test_twoSum_TwoPointers()
    print()
    print("test_reverseList_TwoPointers():")
    test_reverseList_TwoPointers()
    print()
    #   }}}
