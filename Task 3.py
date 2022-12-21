#Task 3

def countWays(n):
  if n < 0: 
    return 0

  if n == 0:
    return 1

  return countWays(n - 1) + countWays(n - 3)

n = int(input("Enter the step number: "))
print(countWays(n), "ways")
input ("Press ENTER for closing program!")
