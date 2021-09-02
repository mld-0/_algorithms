#   VIM SETTINGS: {{{3
        #   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import random
from random import randint
#   {{{2


def find_suffix_array(s: str) -> list[int]:
    result = [ x[1] for x in sorted( [s[i:],i] for i in range(len(s)) ) ]
    return result


def binary_search_suffix_array(pattern: str, text: str, suffix_array: list[int]) -> int:
    l = 0
    r = len(text)-1
    while (l <= r):
        mid = l + (r-l) // 2
        loop_pattern = pattern[:len(pattern)]
        loop_text = text[suffix_array[mid]:][:len(pattern)]
        if loop_pattern == loop_text:
            return suffix_array[mid]
        if loop_pattern < loop_text:
            r = mid - 1
        else:
            l = mid + 1
    return None

#   TODO: 2021-09-03T03:12:28AEST _algorithms, suffix-arrays, (applications of): longest_repeated_substring, longest_common_substring, longest_palindromic_substring
def longest_repeated_substring(s: str) -> str:
    pass
def longest_common_substring(s1: str, s2: str) -> str:
    pass
def longest_palindromic_substring(s: str) -> str:
    pass

text = "banana"
search = "nan"
suffix_array = find_suffix_array(text)
result = binary_search_suffix_array(search, text, suffix_array)
print("text=(%s)\nsuffix_array=(%s)" % (text, str(suffix_array)))
print("search=(%s), result=(%s)" % (search, str(result)))
print()

length = 50
get_random_str = lambda x: ''.join(chr(randint(ord('a'), ord('z'))) for x in range(int(x)))
text = get_random_str(length)
search = text[17:23]
suffix_array = find_suffix_array(text)
result = binary_search_suffix_array(search, text, suffix_array)
print("text=(%s)\nsuffix_array=(%s)" % (text, str(suffix_array)))
print("search=(%s), result=(%s)" % (search, str(result)))
print()



#   LINK: http://web.stanford.edu/class/cs97si/suffix-array.pdf
#   LINK: https://louisabraham.github.io/notebooks/suffix_arrays.html
#   {{{
##   TODO: 2021-09-02T22:37:54AEST _algorithms, suffix-array, is 'suffix_array_naive' correct (what is the definition of a suffix array), (also) what is the use of one?
##   suffix_array[i] is the index of the suffix at position i in the sorted list of all suffixes
##   since comparisons of suffixes takes O(n), and sorting O(n*ln(n)), the result is O(n**2*ln(n)) time and O(n**2) space requirements
#def suffix_array_naive(s):
#    suffix_list = [ (s[i:], i) for i in range(0, len(s)) ]
#    suffix_array_inverse = [ rank for suffix, rank in sorted(suffix_list) ]
#
#    suffix_array = [None] * len(suffix_array_inverse)
#    for i in range(len(suffix_array_inverse)):
#        suffix_array[suffix_array_inverse[i]] = i
#
#    return suffix_array
#random.seed(0)
#random_str = lambda x: ''.join(chr(randint(ord('a'), ord('z'))) for x in range(int(x)))
#
#s = "xabxac"
#result = suffix_array_naive(s)
#print("suffix_array_naive: '%s'" % s)
#print("result=(%s)" % str(result))
#
#s = "banana"
#result = suffix_array_naive(s)
#print("suffix_array_naive: '%s'" % s)
#print("result=(%s)" % str(result))
##   Ongoing: 2021-08-30T22:27:39AEST or is the suffix array of 'banana' [5, 3, 1, 0, 4, 2](?) (which implies first two lines of 'suffix_array_naive()' are sufficent to compute suffix array?)
#assert( result == [3, 2, 5, 1, 4, 0] )
#
#s = random_str(20)
#result = suffix_array_naive(s)
#print("suffix_array_naive: '%s'" % s)
#print("result=(%s)" % str(result))
