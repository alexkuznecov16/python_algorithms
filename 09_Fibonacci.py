# 9. Write a function that returns the Fibonacci sequence up to a given number of terms.

def Fibonacci(limit: int) -> list:
  sequence: list = [0, 1] # initial sequence
  
  while(sequence[-1] + sequence[-2] <= limit):
    sequence.append(sequence[-1] + sequence[-2])
    
  return sequence
  
print(Fibonacci(30)) # [0, 1, 1, 2, 3, 5, 8, 13, 21]
print(Fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8]
print(Fibonacci(2)) # [0, 1, 1, 2]