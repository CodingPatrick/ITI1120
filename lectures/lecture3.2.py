def f1(x):
     res=x**2+10
     return res

def f2(x):
     res=x**2+10
     print(res)

print("Running function f1.")
result1 = f1(5)
print("Printing the value that function f1 returns")
print(result1)

print("\nRunning function f2.")
result2 = f2(5)
print("Printing the value that function f2 returns")
print(result2)


print("\nFunction f1 returns a number so we can use that return number.")
result3 = 3 * f1(5)
print("The result of 3 * f1(5) is: ")
print(result3)

print("\nWhy do we have a crash now when trying to do 3 * f2(5)? ")
print("Also unerstand why 3 * f2(5) call prints 35 first and then crashes.")
result4 = 3 * f2(5)

