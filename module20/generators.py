
def give_number():
    yield 5
    yield 10
    yield 15


number = give_number()

print("Number : ",next(number))
print("Number : ",next(number))
print("Number : ",next(number))