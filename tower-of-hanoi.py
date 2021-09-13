import pprint

class Solution:

    def __init__(self, n):
        self.setup(n)

    def setup(self, n, initial_pole='A'):
        self.n = n
        self.moves = []
        self.poles = { 'A': [], 'B': [], 'C': [] }
        assert( initial_pole in self.poles.keys() )
        self.poles[initial_pole] = [ x for x in range(n,0,-1) ]
        self.print_disks()

    def tower_of_hanoi_recursive(self, n=None, rod_from='A', rod_to='C', rod_aux='B'):
        if n is None:
            n = self.n
        if n == 1:
            self.move_disk(n, rod_from, rod_to)
            return
        self.tower_of_hanoi_recursive(n-1, rod_from, rod_aux, rod_to)
        self.move_disk(n, rod_from, rod_to)
        self.tower_of_hanoi_recursive(n-1, rod_aux, rod_to, rod_from)

    def move_disk(self, n, rod_from, rod_to):
        self.moves.append("(%s)->(%s), n=(%s)" % (str(rod_from), str(rod_to), str(n)))
        val = self.poles[rod_from].pop()
        assert( val == n )
        self.poles[rod_to].append(val)
        self.print_disks()

    def print_disks(self):
        pprint.pprint(self.poles)


n = 5
s = Solution(n)

s.tower_of_hanoi_recursive()
print()

pprint.pprint(s.moves)
print()

