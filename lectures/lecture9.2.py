def crypto(s):
    '''
    (str) -> str

    >>> crypto("abcd")
    'badc'
    >>> crypto("abcde")
    'badce'
    '''
    if len(s) <= 1:
        return s
    
    new_s = ''
    for i in range(0, len(s) - 1, 2):
        new_s = new_s + s[i+1] + s[i]

    if len(s) % 2 == 1:
        new_s = new_s + s[-1]
        
    return new_s
