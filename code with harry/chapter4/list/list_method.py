# | Method      | Description                      |
# | ----------- | -------------------------------- |
# | `append()`  | Add one item at the end          |
# | `extend()`  | Add multiple items               |
# | `insert()`  | Insert item at a given position  |
# | `remove()`  | Remove first matching item       |
# | `pop()`     | Remove and return item at index  |
# | `clear()`   | Remove all items                 |
# | `index()`   | Get index of first matching item |
# | `count()`   | Count occurrences of an item     |
# | `sort()`    | Sort the list in place           |
# | `reverse()` | Reverse the list in place        |
# | `copy()`    | Return a copy of the list        |



# 🔹 1. append()
# Adds a single element to the end of the list.
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # ['apple', 'banana', 'cherry']


# 🔹 2. extend()
# Adds multiple elements (another list) to the end.
fruits = ['apple', 'banana']
fruits.extend(['cherry', 'orange'])
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
friend=["apple","orange",12,7.0,True,"vinay","sanika"]
fruits.extend(friend)
print(fruits)

# 🔹 3. insert(index, element)
# Inserts an element at a specific index.
fruits = ['apple', 'banana']
fruits.insert(1, 'mango')
print(fruits)  # ['apple', 'mango', 'banana']


# 🔹 4. remove(element)
# Removes the first occurrence of the specified value.
fruits = ['apple', 'banana', 'apple']
fruits.remove('apple')
print(fruits)  # ['banana', 'apple']


# 🔹 5. pop([index])
# Removes and returns the element at the given index (last by default).
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop())
print(fruits)  # ['apple', 'banana']


# 🔹 6. clear()
# Removes all items from the list.
fruits = ['apple', 'banana']
fruits.clear()
print(fruits)  # []


# 🔹 7. index(element)
# Returns the index of the first occurrence of the element.
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))  # 1


# 🔹 8. count(element)
# Counts how many times an element appears in the list.
nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # 3


# 🔹 9. sort()
# Sorts the list in ascending order (modifies original list).
nums = [4, 1, 3, 2]
nums.sort()
print(nums)  # [1, 2, 3, 4]


# 🔹 10. reverse()
# Reverses the order of the list.
nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]
friend=["apple","orange",12,7.0,True,"vinay","sanika"]
friend.reverse()
print(friend)


# 🔹 11. copy()
# Returns a shallow copy of the list.
a = [1, 2, 3]
b = a.copy()
print(b)  # [1, 2, 3]


fruits = ['apple', 'banana', 'cherry']
print(type(fruits))