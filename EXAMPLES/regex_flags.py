import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

pattern = r'''
[A-Z]   # match 1 letter   
-       # match dash
\d{2,3} # match 2 or 3 digits
'''

if re.search(pattern, s, re.IGNORECASE | re.VERBOSE):  # make search case-insensitive
    print("Found pattern.")
print()

m = re.search(pattern, s, re.I | re.M | re.X)  # short version of flag
if m:
    print("Found:", m.group())
print()

for m in re.finditer(pattern, s, re.I | re.X):
    print(m.group())
print()

matches = re.findall(pattern, s, re.I | re.X)
print("matches:", matches)
