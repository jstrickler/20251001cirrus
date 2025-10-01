def shout(word: str, times: int = 1) -> str:
    return word.upper() * times

a: str = shout('Python', 3)
print(f"{a = }")
b: list[float] = shout('Python', 3)
print(f"{b = }")
print()

def read_files(*file_paths: str) -> None:
    for file_path in file_paths:
        print(f"Opening {file_path}")
        with open(file_path) as file_in:
            pass

read_files('../DATA/mary.txt', '../DATA/parrot.txt')
print()

def shout_various(**kwargs: int) -> None: # argument values must be ints
    for word, count in kwargs.items(): # loop through named arguments
        print(word.upper() * count)

shout_various(python=10, perl=1, c=3)

