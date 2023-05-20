##Need to be work on this

def muliply(*args):
  print(args)
  total = 1
  for arg in args:
    total = total *arg
  return total

def apply(*args, operator):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "empty"
print(apply(1,3,6,7, operator = "*"))


##**kWargs

def named (**kwargs):
  print(kwargs)
  
details = ["name": "Bob", "age": 23]
named(**details)

#####
def named (**kwargs):
  print(kwargs)
  
def print_nicely(**kwargs):
  named(**kwargs)
  for arg, val kwargs.items():
    print(f"{arg} : {val}")
    
print_nicely(name = "Bob", AGE = 25)
