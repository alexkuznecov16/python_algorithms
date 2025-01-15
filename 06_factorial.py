# 6. Write a program to calculate the factorial of a given number.

def factorial(num: int) -> int:
  #! option 1
  # if num == 1 or num == 2:
  #   return num
  
  # res: int = 1 # initial result
  # for i in range (2, num+1):
  #   # iterate each num between 2 and user num (including)
  #   res *= i # multiply res to each num
  # return res
  
  #! option 2 (recursion)
  if num <= 1:
    return num
  else:
    # every time num multiply to the (num - 1) while num is bigger than 2
    return num * factorial(num - 1)


print(factorial(5)) # 120
print(factorial(2)) # 2
print(factorial(3)) # 6