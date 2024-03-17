#1recurrence fn means remaining all
#2basecase means 0fact default basecase is 1

def recur_fact(n):
  if n == 1:
     return n
  else:
     return n*recur_fact(n-1)     #function calling itself

#taking input from the user
no = int(input("User Input : "))
print("The factorial of", no, "is", recur_fact(no))

