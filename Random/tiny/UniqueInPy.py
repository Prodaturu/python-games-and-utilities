
## create a function unique that takes in a list and returns only unique items

#+ method 1: using 'for' loop:

# def unique (list):
#     unique_list = []
#     for i in list:
#         if i not in unique_list:
#             unique_list.append(i)
#     return unique_list

#+ Method 2: using set:

def unique(list_in): return list(set(list_in))

print(unique(['go', 'ruby','go', 'python','python']))
# #ä result: ['python','ruby','go']
#   #: the order may be different everytime

#* Converting the above Unique function into Lambda function

#unique = lambda list_in: list(set(list_in))
# print(unique(['go', 'ruby','go', 'python','python']))
  #: lambda is a overkill for this case