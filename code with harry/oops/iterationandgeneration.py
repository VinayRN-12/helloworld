numbers = [1, 2, 3]
it = iter(numbers)   # create iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # ❌ StopIteration error
print()


def countdown(n):
    while n < 100:
        yield n   # pauses & remembers state
        n += 1

for num in countdown(0):
    print(num)




