def add(x, y = 5):
  print(x + y)
add(5)#working clearly because about the fonc. default parameter


####### Return value 
def add(x, y):
  return x + y
  print(x + y)#Never get called..

result = add(3, 4)
print(result)

#######Lambda fonc. Map() , now you see what is it.

def double(x):
    return x*2
  
sequence = [1, 2, 3, 4]

doubled = [double(x) for x in sequence]
doubled = list(map(double,sequence))#same
