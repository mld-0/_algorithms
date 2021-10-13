#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
from collections import Counter, defaultdict
#   {{{2

#   The Sliding Window technique involves analysing a series of subarrays of an input array, typically in order to reduce a nested loop to a single loop


def lengthOfLongestSubstring_SlidingWindowSeenDict(s: str) -> int:
    """Determine length of longest substring in 's' containing no repeat characters"""
    result = ""
    #   seen[c]: position where 'c' last seen
    seen = dict()
    l = 0

    for r in range(len(s)):
        #   character at 'r' seen before, advance 'l' to after previous instance of said character
        if s[r] in seen and seen[s[r]] >= l:
            l = seen[s[r]] + 1
        trial = s[l:r+1]
        if len(trial) > len(result):
            result = trial
        seen[s[r]] = r

    return len(result)



def findAnagrams_SlidingWindowCounter(s: str, p: str) -> List[int]:
    """Find start indices of all anagrams of search string 'p' in input string 's', updating counter for each search window"""
    if len(p) > len(s):
        return []

    result = []

    #   count characters in search string
    search_counts = Counter(p)

    #   count characters in first window and compare to 'search_counts'
    window_counts = defaultdict(int)
    for c in s[:len(p)]:
        window_counts[c] += 1
    if window_counts == search_counts:
        result.append(0)

    #   count characters in each subsequent window and compare to 'search_counts'
    for i in range(1, len(s)-len(p)+1):
        c_remove = s[i-1]
        c_add = s[i+len(p)-1]

        #   Add last character of new window to count
        window_counts[c_add] += 1

        #   Remove first character of previous window from count
        window_counts[c_remove] -= 1
        if window_counts[c_remove] == 0: del window_counts[c_remove]

        #   Is current window an anagram of search string?
        if window_counts == search_counts:
            result.append(i)

    return result


def test_lengthOfLongestSubstring_SlidingWindowSeenDict():
    #   {{{
    input_values = [ "abcabcbb", "bbbbb", "pwwkew", "", " ", ]
    input_checks = [ 3, 1, 3, 0, 1, ]
    for input_str, check in zip(input_values, input_checks):
        print("input_str=(%s)" % input_str)
        result = lengthOfLongestSubstring_SlidingWindowSeenDict(input_str)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    #   }}}

def test_findAnagrams_SlidingWindowCounter():
    #   {{{
    input_values = [ ("cbaebabacd", "abc"), ("abab", "ab"), ]
    input_checks = [ [0,6], [0,1,2], ]
    for (input_s, input_p), check in zip(input_values, input_checks):
        print("input_s=(%s), input_p=(%s)" % (input_s, input_p))
        result = findAnagrams_SlidingWindowCounter(input_s, input_p)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    #   }}}

if __name__ == '__main__':
    #   {{{
    print("test_lengthOfLongestSubstring_SlidingWindowSeenDict():")
    test_lengthOfLongestSubstring_SlidingWindowSeenDict()
    print()
    print("test_findAnagrams_SlidingWindowCounter():")
    test_findAnagrams_SlidingWindowCounter()
    print()
    #   }}}

