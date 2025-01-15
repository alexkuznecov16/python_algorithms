# 5. Write a function that takes an array of numbers and returns a new array with only the even numbers.

def get_even(array: list) -> list:
  return [i for i in array if i % 2 == 0]

print(get_even([1,2,3,4,5,6,7,8,9,10])) # [2, 4, 6, 8, 10]