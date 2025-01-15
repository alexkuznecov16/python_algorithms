# 7. Write a function to check if a given number is prime.
# prime number is a number that is divisible only by 1 and by itself

def prime(num: int) -> bool:
  if num <= 1:
    return False
  
  for i in range(2, num):
    # iterate each number from 2 to num
    if num % i == 0:
      return False
    
  return True
    
print(prime(1)) # False
print(prime(4)) # False -> divide to 2
print(prime(6)) # False -> divide to 2 and 3
print(prime(7)) # True