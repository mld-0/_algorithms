from collections import defaultdict

class TrieNode(object):

    def __init__(self):
        self.children = defaultdict(None)
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    #   TODO: 2021-09-06T19:05:29AEST _algorithms, trie, implement remove(), print(), longest_matching_prefix()
    def longest_matching_prefix(self, input_str):
        raise Exception("Unimplemented")


    def node_is_empty(self, node):
        return len(node.children.keys()) == 0

    def insert(self, key):
        """Insert word in Trie"""
        loop_node = self.root

        for level in range(len(key)):
            index = key[level]

            if not index in loop_node.children.keys():
                loop_node.children[index] = TrieNode()

            loop_node = loop_node.children[index]

        loop_node.isEndOfWord = True

    def search(self, key):
        """Search for word in Trie"""
        loop_node = self.root

        for level in range(len(key)):
            index = key[level]

            if not index in loop_node.children.keys():
                return False

            loop_node = loop_node.children[index]

        return loop_node.isEndOfWord

    def get_words(self, node=None, text="", level=0):
        """Get list of words in Trie"""
        result = []
        if node is None:
            node = self.root
        if node.isEndOfWord:
            result.append(text)

        for c in sorted(node.children.keys()):
            text_list = list(text + " ")
            text_list[level] = c
            text = ''.join(text_list).strip()
            for word in self.get_words(node.children[c], text, level+1):
                result.append(word)

        return result

    def remove(self, key, node=None, depth=0):
        if node is None:
            node = self.root

        #   if processing last character of key
        if (depth == len(key)):

            if node.isEndOfWord:
                node.isEndOfWord = False

            #   if node is not a prefix of another word, remove it
            if self.node_is_empty(node):
                node = TrieNode()

            return node

        #   recurse for child corresponding to next character of key
        index = key[depth]
        node.children[index] = self.remove(key, node.children[index], depth+1)

        #   if node has no children and is not end of another word, remove it
        if self.node_is_empty(node) and node.isEndOfWord == False:
            node = TrieNode()

        return node

def main():
    #keys = [ "the", "a", "there", "anaswe", "any", "by", "their" ]
    keys = [ "the", "a", "there", "answer", "any", "by", "bye", "their" ]

    t = Trie()

    for key in keys:
        t.insert(key)

    search_list = [ "the", "these", "their", "thaw" ]
    for loop_search in search_list:
        result = t.search(loop_search)
        print("loop_search=(%s), result=(%s)" % (loop_search, result))

    words_list = t.get_words()
    print("words_list=(%s)" % words_list)

    t.remove("answer")
    t.remove("their")

    search_list = [ "the", "these", "their", "thaw" ]
    for loop_search in search_list:
        result = t.search(loop_search)
        print("loop_search=(%s), result=(%s)" % (loop_search, result))

    words_list = t.get_words()
    print("words_list=(%s)" % words_list)

if __name__ == "__main__":
    main()

