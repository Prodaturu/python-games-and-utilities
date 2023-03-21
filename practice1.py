
# #+ create a function that 'Doubles input list & return them':

# nums = [1,2,3,4,5]
# result=[]
# def double(nums: list) -> list:
  
#   for number in nums:
#     result.append(number*2)
#   return print(result)

# double(nums)

#+ Function to 'Count no of words in the input string':

# def count_words(phrase):
#     return print(len(phrase.split()))

# count_words('I am Saikiran Prodaturu')

#+ Create a funtion to 'Sum of nums in list is returned':

# def sum_list(numbers):
#   total =int(0)
#   for number in numbers:
#     total += int(number)
#     return print(total)

# sum_list([1,2,3,4,5])

#+ Create a function to 'find the maximum number in a list':

# def find_max(nums):
#   current_max= nums[0] 
#   #: nums[0] is a better way 
#   #: since, if given num > max. code is useless
#   for num in nums:
#     if num > current_max:
#       current_max = num
#   return print(current_max)

# find_max([1,2,3,4,5])

## Dictionary practice:

#+ Create a function 'takes in a string and returns a dict with used words and frquency':

#word_frequency('I love Batman because I am Batman')

def word_frequency(phrase):
  result={} #ä empty dictionary
  words=phrase.split()
  for word in words:
    if word in words:
      if word in result:
        result[word]+=1
      else:
        result[word]=1
  return result

print(word_frequency('I love Batman because I am Batman'))
