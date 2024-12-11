import math
#function is used to easy to readablity
# def sum_of_two_number(x,y):
#     return x+y
# print('the sum of the numbers ',sum_of_two_number(23,4))

# def area_of_circle(r):
#     pi=3.14
#     return pi*r**2
# print('the area of the circle is ',area_of_circle(2))


# def add_all_number(*number):
#     sum = 0
#     for i in number:
#         if isinstance(i,(float,int)):
#             sum += i
#     return sum
        
             
# print(add_all_number(2,4,5,6,7))

# squar_root=math.sqrt(16)
# print(squar_root)



# def temperature_convertor(celcius):
#     fahrenheight=(celcius*9/5)+32
#     print(fahrenheight)
# temperature_convertor(-40) 

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

# def print_list(my_list):
#     for i in my_list:
#         print(i)
# example_list=[1,3,4,5,6]
# print(print_list(example_list))

# reverse the given array or list
# def reverse_list(array):
#     reversed_list=array[::-1]
#     print(reversed_list)
# list=[2,4,5,6,8,9]
# reverse_list(list)

# def capitalize_item(my_list):
#     for i in my_list:
    
#         print(i)
# list=['abebe','alemu','kebede']
# capitalize_item(list)

# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

# def add_item(my_list):
#     old_list=[2,4,5,6,7]
#     old_list.append(my_list)
#     print(old_list)
    
# add_item(8)
# def remove_item():
#     items=[2,5,8,9,2,4,5,6]
#     items.remove(items[7])
#     print(items)
# remove_item()

#check the number is even or odd
# def prime_number(number):
#     if number < 1:
#         print('the number is not prime')
#         return
#     count=0
#     for i in range(1,number+1):
#         if number%i==0:
#             count += 1
#     if count==2:
#         print('the number is prime')
#     else:
#         print('the number is not prime')
# x=int(input('enter a number : '))
# prime_number(x)

#Write a functions which checks if all items are unique in the list
# def all_list_item(my_list):
#     if len(my_list)==len(set(my_list)):
#         print('all items in a list is unique')
#     else:
#         print('the list item is not unique')
# list=[2,4,5,6,2,7,8,9]        
# all_list_item(list) 
# 
# 
# Write a function which checks if all the items of the list are of the same data type.
# def all_list_item(my_list):
#     for i in my_list:
#         if isinstance(i,(int)):
#             print('the list data type is all are the same ')
# list=[2,4,5,6,7,8]
# all_list_item(list)    
# check th evariable is  valid or invalid
# def is_valid(variable):
#     if isinstance(variable, str) and variable.isidentifier():
#         print('The variable is a valid identifier.')
#     else:
#         print('The variable is not a valid identifier.')

# Example usage
# s_variable = '99t'
# is_valid(s_variable)  # Output: The variable is not a valid identifier.

# s_variable = 'valid_var'
# is_valid(s_variable)  # Output: The variable is a valid identifier. 
# 
#       
#check the list have a value or empity list
# def empity():
#     list=[2,4,5]
#     if not list:
#         print('it is empity list')
#     else:
#         print('the list have a value')

#Write different functions which take lists. They should calculate_mean, calculate_median, 
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# def mean(my_list):
   
#     sum=0
#     for i in my_list:
#         sum += i
#     avg=sum/len(my_list) 
#     return avg
# list=[2,4,5,6,7,8,9]
# mean(list) 
#   
# def all_num(*nums):
#     if all(isinstance(x,(float,int))for x in nums):
#         return sum(nums)
#     return print('please enter approprate value')
# print(all_num(2,4,5,6,7))
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter=[x for x in numbers if x <= 0]
print(filter)