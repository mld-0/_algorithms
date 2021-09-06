from collections import defaultdict

class TrieNode(object):

    def __init__(self):
        self.children = defaultdict(None)
        self.isEndOfWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        loop_node = self.root

        for level in range(len(key)):
            index = key[level]

            if not index in loop_node.children.keys():
                loop_node.children[index] = TrieNode()

            loop_node = loop_node.children[index]

        loop_node.isEndOfWord = True

    
    def search(self, key):
        loop_node = self.root

        for level in range(len(key)):
            index = key[level]

            if not index in loop_node.children.keys():
                return False

            loop_node = loop_node.children[index]

        return loop_node.isEndOfWord


    #   TODO: 2021-09-06T19:05:29AEST _algorithms, trie, implement remove(), print(), longest_matching_prefix()
    def remove(self, key, depth=0):
        raise Exception("Unimplemented")

    def print(self):
        raise Exception("Unimplemented")

    def longest_matching_prefix(self, input_str):
        raise Exception("Unimplemented")


def main():
    keys = [ "the", "a", "there", "anaswe", "any", "by", "their" ]

    t = Trie()

    for key in keys:
        t.insert(key)

    search_list = [ "the", "these", "their", "thaw" ]

    for loop_search in search_list:
        result = t.search(loop_search)
        print("loop_search=(%s), result=(%s)" % (loop_search, result))


if __name__ == "__main__":
    main()




