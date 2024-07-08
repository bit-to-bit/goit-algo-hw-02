from collections import deque

def is_palindrome(text: str) -> bool:
    result = True
    word = deque(text.lower().strip().replace(' ', ''))
    while len(word) > 1 and result == True:
        if word.pop() != word.popleft():
            result = False
    return result

test_words = ['pop', 'Abba', 'cat', 'madam', 'ma da m', 'ma da -m ', 'Civic', '',' ', ' bob']

print('\nIs the text a palindrome?\n')
for e in test_words:
    print(f'{'"' + str(e) + '"':15} ->   {is_palindrome(e)}')
