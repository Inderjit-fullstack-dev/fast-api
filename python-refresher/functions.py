import calc as math_lib


print(math_lib.add(1, 2))

# Variable length argument
def add2(*args):
    return sum(args)

# specify the return type
def say_hello() -> str:
    return "Hello World"
print(say_hello())


def get_max(highest_number:int, lowest_number:int) -> int:
    return max(lowest_number, highest_number)

print(get_max(44, 22))

#specify the parameter names with different param location
print(get_max(lowest_number=55, highest_number=100))

def get_person(firstname:str, lastname: str, age: int) -> dict:
    return {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }

person =get_person(firstname="John", lastname="Smith", age=30)
print(person.get("firstname"))


