

def get_wide_ordinal(char):
    if len(char) != 2:
        return ord(char)
    return 0x10000 + (ord(char[0]) - 0xD800) * 0x400 + (ord(char[1]) - 0xDC00)


print('Unicode value of a: ', get_wide_ordinal('A'))
