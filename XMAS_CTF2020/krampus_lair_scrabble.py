def charCount(word): 
    dict = {} 
    for i in word: 
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def possible_words(lwords, charSet): 
    for word in lwords: 
        word.lower()
        flag = 1
        chars = charCount(word) 
        for key in chars: 
            if key not in charSet: 
                flag = 0
            else: 
                if charSet.count(key) != chars[key]: 
                    flag = 0
        if flag == 1: 
            print(word) 
  
if __name__ == "__main__": 
    input = dir(__builtins__)
    # input = ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'] 
    charSet = ['u', 'h', 'n', 'i', 'g', 'a', 'r', 's', 'e', 't', 'c', 'm', '(', ')', ',', '/']
    possible_words(input, charSet) 
