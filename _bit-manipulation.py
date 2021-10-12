#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
#   {{{2

#   bitwise tricks:
#       (n & (-n)) isolates the rightmost one bit of 'n'
#       (n & (n-1)) sets rightmost one bit of 'n' to zero


def reverseBits_witchcraft_i(n: int) -> int:
    def reverseByte(byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023
    shift = 32 - 8
    result = 0
    while n:
        result += reverseByte(n & 0xff) << shift
        n = n >> 8
        shift -= 8
    return result


def reverseBits_witchcraft_ii(n: int) -> int:
    #   {{{
    #   Step 0.
    #   abcd efgh ijkl mnop qrst uvwx yzAB CDEF <-- n
    #   
    #   Step 1.
    #                       abcd efgh ijkl mnop <-- n >> 16, same as (n & 0xffff0000) >> 16
    #   qrst uvwx yzAB CDEF                     <-- n << 16, same as (n & 0x0000ffff) << 16
    #   qrst uvwx yzAB CDEF abcd efgh ijkl mnop <-- after OR
    #   
    #   Step 2.
    #             qrst uvwx           abcd efgh <-- (n & 0xff00ff00) >> 8
    #   yzAB CDEF           ijkl mnop           <-- (n & 0x00ff00ff) << 8
    #   yzAB CDEF qrst uvwx ijkl mnop abcd efgh <-- after OR
    #   
    #   Step 3.
    #        yzAB      qrst      ijkl      abcd <-- (n & 0xf0f0f0f0) >> 4
    #   CDEF      uvwx      mnop      efgh      <-- (n & 0x0f0f0f0f) << 4
    #   CDEF yzAB uvwx qrst mnop ijkl efgh abcd <-- after OR
    #   
    #   Step 4.
    #     CD   yz   uv   qr   mn   ij   ef   ab <-- (n & 0xcccccccc) >> 2
    #   EF   AB   wx   st   op   kl   gh   cd   <-- (n & 0x33333333) << 2
    #   EFCD AByz wxuv stqr opmn klij ghef cdab <-- after OR
    #   
    #   Step 5.
    #    E C  A y  w u  s q  o m  k i  g e  c a <-- (n & 0xaaaaaaaa) >> 1
    #   F D  B z  x v  t r  p n  l j  h f  d b  <-- (n & 0x55555555) << 1
    #   FEDC BAzy xwvu tsrq ponm lkji hgfe dcba <-- after OR
    #   }}}
    n = (n >> 16) | (n << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    return n


#   TODO: 2021-10-03T22:21:03AEDT _algorithms, bit-manipulation, bin2int, int2bin example functions
def bin2int(s: str) -> int:
    raise NotImplementedError()


def int2bin(i: int) -> str:
    raise NotImplementedError()



def test_reverseBits():
    #   {{{
    input_values = [ 0b0101, 0b00000010100101000001111010011100, 0b11111111111111111111111111111101, ]
    input_checks = [ 2684354560, 964176192, 3221225471, ]

    for n, check in zip(input_values, input_checks):
        result_i = reverseBits_witchcraft_i(n)
        result_ii = reverseBits_witchcraft_ii(n)
        assert result_i == check, "Check i failed"
        assert result_ii == check, "Check ii failed"
        print("result=(%s)" % str(result_i))
    #   }}}

def test_bin2int():
    #   {{{
    raise NotImplementedError()
    #   }}}

def test_int2bin():
    #   {{{
    raise NotImplementedError()
    #   }}}

if __name__ == '__main__':
    print("test_reverseBits():")
    test_reverseBits()
    print()
    print("test_bin2int():")
    test_bin2int()
    print()
    print("test_int2bin():")
    test_int2bin()
    print()

