import typing as T

Numeric = T.Union[float, int]

Number = int | float
def area(length: Number, width: Number):
    return length * width

print(f"{area(5, 10) = }")
print(f"{area(8.9, 27.28393) = }")
print(f"{area(5, 99.9) = }")


print(f"{area(5, "b") = }")
print(f"{area("spam", 10) = }")

x: int
x = "abc"

print(f"{x = }")

def eggs(id: int | None = None):
    if id is not None:
        pass  # do whatever

eggs()
eggs(35)
eggs("abc")
eggs(None)

def process_files(file_paths: T.Iterable[str]) -> list[str]:
    for file_path in file_paths:
        ...
    return []

def doit(thing: T.Any):
    pass


class Foo:
    def my_method(self, b: "Bar"):
        pass

class Bar:
    pass

f = Foo()
b = Bar()
f.my_method(b)

class Writer(T.Protocol):
    def write(self, data):
        pass

class Foo:
    def write(self, data):
        print(data)

class Bar:
    pass

def toast(writer: Writer):
    writer.write("hello")

toast(Bar())