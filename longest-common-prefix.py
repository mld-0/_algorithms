#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import math
from collections import defaultdict
#   {{{2

#   Longest Common Prefix: Given a list of strings, determine the longest substring that is a prefix to each

class TrieNode(object):
    #    {{{
    def __init__(self):
        self.links = dict()
        self.end = False
        self.size = 0
    def containsKey(self, ch):
        return ch in self.links.keys()
    def put(self, ch, node):
        self.links[ch] = node
        self.size += 1
    def get(self, ch):
        return self.links[ch]
    def setEnd(self):
        self.end = True
    def isEnd(self):
        return self.end
    def getLinks(self):
        return self.size
    #   }}}

class Trie(object):
    #   {{{
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            loop_char = word[i]
            if not node.containsKey(loop_char):
                node.put(loop_char, TrieNode())
            node = node.get(loop_char)
        node.setEnd()
    def search(self, word):
        node = self.searchPrefix(word)
        return (not node is None) and node.isEnd()
    def searchPrefix(self, word):
        node = self.root
        for i in range(len(word)):
            loop_char = word[i]
            if node.containsKey(loop_char):
                node = node.get(loop_char)
            else:
                return None
        return node
    def startsWith(self, prefix):
        node = self.searchPrefix(prefix)
        return not node is None
    def searchLongestPrefix(self, word):
        node = self.root
        prefix = ""
        for i in range(0, len(word)):
            loop_char = word[i]
            if ((node.containsKey(loop_char)) and (node.getLinks() == 1) and (not node.isEnd())):
                prefix += loop_char
                node = node.get(loop_char)
            else:
                return prefix
        return prefix
    #   }}}

class Solution:

    #   Result:
    #       runtime: beats 5%
    def longestCommonPrefix_Ans_Trie(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        trie = Trie()
        for i in range(1, len(strs)):
            trie.insert(strs[i])
        return trie.searchLongestPrefix(strs[0])


    #   Result:
    #       runtime: beats 18%
    def longestCommonPrefix_Ans_SortedFirstLast(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        strs_min = min(strs)
        strs_max = max(strs)

        for i, loop_char in enumerate(strs_min):
            if loop_char != strs_max[i]:
                return strs_min[:i]

        return strs_min


    #   Result:
    #       runtime: beats 80%
    def longestCommonPrefix_Ans_DivConquer(self, strs: list[str], l=0, r=None) -> str:
        if r is None:
            r = len(strs)-1

        #   Base state
        if l == r:
            return strs[l];

        #   Divide
        mid = (l+r) // 2
        left = self.longestCommonPrefix_Ans_DivConquer(strs, l, mid)
        right = self.longestCommonPrefix_Ans_DivConquer(strs, mid+1, r)

        #   Combine:
        min_len = min(len(left), len(right))
        for i in range(0, min_len):
            if left[i] != right[i]:
                return left[:i]

        return left[:min_len]


    #   Result:
    #       runtime: beats 14%
    def longestCommonPrefix_Ans_BSearch(self, strs: list[str]) -> str:
        if len(strs) <= 1:
            return strs[0]

        minLen = min( [ len(x) for x in strs ] )

        low = 1
        high = minLen
        while low <= high:
            middle = (high+low)//2

            isCommonPrefix = True
            for i in range(1, len(strs)):
                if not strs[i].startswith(strs[0][0:middle]):
                    isCommonPrefix = False

            #   Cases:
            #       S[1:mid] not a common string -> j > i S[1:j] is not a common string (disregard second half of search space)
            #       S[1:mid] is a common string -> j > i S[1:i] is a common string (disregard first half of search space)
            if isCommonPrefix:
                low = middle + 1
            else:
                high = middle - 1

        result = strs[0][0:(high+low)//2]
        return result


    #   Result:
    #       runtime: beats 10%
    def longestCommonPrefix_A(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        #   suffix_arrays[i]: list of suffixes of length i for strings in strs
        suffix_arrays = defaultdict(list)
        total_i = 0
        for loop_str in strs:
            for j in range(0, len(loop_str)+1):
                suffix_arrays[j].append(loop_str[:j])
                total_i = max(total_i, j)

        #   hightest i for which each item in suffix_arrays[i] is the same, and len(suffix_arrays[i]) == len(strs)
        max_i = 0
        for i in range(0, total_i+1):
            is_same = True
            if len(suffix_arrays[i]) != len(strs):
                break
            for j in range(1, len(suffix_arrays[i])):
                if suffix_arrays[i][j] != suffix_arrays[i][j-1]:
                    is_same = False
                    print("is_same=False for i=(%s), j=(%s)" % (i, j))
            if not is_same:
                break
            max_i = i

        print("suffix_arrays=(%s)" % str(suffix_arrays))
        print("max_i=(%s)" % str(max_i))

        return suffix_arrays[max_i][0]


    #   Result:
    #       runtime: beats 14%
    def longestCommonPrefix_B(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        suffix_sets = defaultdict(set)
        suffix_sets[0].add("")

        str_maxlen = max( [ len(x) for x in strs ] )

        for j in range(1, str_maxlen+1):
            for loop_str in strs:
                suffix_sets[j].add(loop_str[:j])
                if len(suffix_sets[j]) > 1:
                    return suffix_sets[j-1].pop()

        return suffix_sets[str_maxlen].pop()


    def longestCommonPrefix(self, strs: list[str]) -> str:
        #return self.longestCommonPrefix_Ans_MinMax(strs)
        #return self.longestCommonPrefix_Ans_DivConquer(strs)
        return self.longestCommonPrefix_Ans_Trie(strs)


s = Solution()
strs = ["flower","flow","flight"]
result = s.longestCommonPrefix(strs)
expected = "fl"
print("result=(%s)" % str(result))
assert( result == expected )

strs = ["dog","racecar","car"]
result = s.longestCommonPrefix(strs)
expected = ""
print("result=(%s)" % str(result))
assert( result == expected )

strs = [""]
result = s.longestCommonPrefix(strs)
expected = ""
print("result=(%s)" % str(result))
assert( result == expected )

strs = ["a"]
result = s.longestCommonPrefix(strs)
expected = "a"
print("result=(%s)" % str(result))
assert( result == expected )

strs = ["flower","flower","flower","flower"]
result = s.longestCommonPrefix(strs)
expected = "flower"
print("result=(%s)" % str(result))
assert( result == expected )


