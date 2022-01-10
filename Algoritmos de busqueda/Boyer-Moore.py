class last_occurrence(object):
    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences[letter]


def boyer_moore_match(text, pattern):
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = 1
    j = m - 1
    while i < n:
        print('k:', i, '  j:', j)
        if text[i] == pattern[j]:
            print(text[i], '==', pattern[j])
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1+l)
            j = m - 1 
        print(i)
    return -1


if __name__ == '__main__':
        
    def show_match(text, pattern):
        boyer_moore_match(text, pattern)

    text = 'tbxpaz'
    pattern = 'xpa'
    show_match(text, pattern)