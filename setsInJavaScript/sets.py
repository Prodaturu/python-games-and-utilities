
list1 = ['ruby', 'python', 'javascript']
list2 = ['ruby', 'SQL', 'JAVA', 'javascript']

#+ Print all programming languages without repetition

programming_Languages = list1 + list2

# print({1,2,2,2,2})
#result: {1,2}
#: sets dont have index, duplicates

# things = {1,3}
#print(2 in things)
#result: False

# set([1,2,2,2])
#result: {1,2}

#* So lists can be used to remove duplicates in an array

things = set(programming_Languages)
print(things)