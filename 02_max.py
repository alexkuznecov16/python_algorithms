# 2. Write a program to find the maximum number in an array.

def find_max(array: list) -> float:
  #! option 1
  # return max(array)
  
  #!option 2
  arr_max: float = array[0] # initial maximum number
  for i in array:
    # iterate each number and check with arr_max
    if i > arr_max:
      arr_max = i
  
  return arr_max

print(find_max([10,1,12,6,82,36])) # 82
print(find_max([-99, 0, 12, 4])) # 12