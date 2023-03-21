def double_number(number):
    return number*2

print(list(map(double_number,[1,2,3])))

print(list(map(lambda num: num*2,[1,2,3])))
print(list(map(lambda num: num**2,[1,2,3])))

