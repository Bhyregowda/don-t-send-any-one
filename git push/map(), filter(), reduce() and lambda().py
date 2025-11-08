#MAP() function applies a given function to all the items in an input list
arr=[1,2,3,4,5]
arr=list(map(lambda x:x**2,arr))
print(arr)
#FILTER() function is used ti filter the elements og an iterable based on a certain condition
Fruits=["mango","orange","apple","cherry", "guava"]
print(list(filter(lambda fruit:'g' in fruit, Fruits)))
#reduce() function applies as given function to all the items in an input list and return a single value
from functools import reduce
lst=[2,4,6,8,10]
print(reduce(lambda x,y:x+y,lst))
#lambda() is used to create small, anonymous function
b=lambda a:"even" if a%2==0 else"odd"
b(12)