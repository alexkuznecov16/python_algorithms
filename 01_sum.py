#1. Write a function to calculate the sum of two numbers.

def num_sum(num1: float, num2: float) -> str:
  return f'{num1} + {num2} = {num1 + num2}'

print(num_sum(7.7, 8.1)) # 7.7 + 8.1 = 15.8
print(num_sum(0, 6)) # 0 + 6 = 6