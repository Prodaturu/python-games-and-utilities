numbers= [1,2,3,4,5,6,7,8,9,10,11,12]

even_numbers=[[number for number in numbers if number%2==0]]
print('even numebrs are', even_numbers)

odd_numbers= [[number for number in numbers if number%2!=0]]
print('odd numbers are', odd_numbers)

odd_numbers_cubed= [[number**3 for number in numbers if number%2!=0]]
print(odd_numbers_cubed)