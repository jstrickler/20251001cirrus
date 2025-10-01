class MyException(Exception):
    pass

try:
    x = 5
    y = "cheese"
    raise MyException("wow, this is fun")
    z = x + y
    f = open("sesame.txt")
    print("Bottom of try")

except (IOError, TypeError) as err:  # Use a tuple of 2 or more exception types
    print("Naughty programmer! ", err)

except MyException as err:
    print("did not see this coming!", err)

except Exception as err:
    print(err)