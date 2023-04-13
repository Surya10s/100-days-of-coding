import numbers
# creating an empty list
lst = []
uniques = []
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
for number in lst: 
         if number not in uniques:
              uniques.append(number)
print(uniques)
