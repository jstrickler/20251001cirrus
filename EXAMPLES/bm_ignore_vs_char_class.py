from timeit import Timer


setup = """
import re

s = '''P-32 lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation MOM-999etc ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum'''

pattern1 = r'\b[A-Z]-\d{2,3}\b'
pattern2 = r'\b[A-Za-z]-\d{2,3}\b'
"""

REPEATS = 1000000

code_snippets = [
    '''
re.findall(pattern1, s, re.IGNORECASE)
    ''',
    '''
re.findall(pattern2, s)
    ''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print(f"{code_snippet:60.60s}{t.timeit(REPEATS)}")
    print('-' * 60)

