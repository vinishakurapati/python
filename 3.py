#c.	Create a tuple (1, 12, 55, 12, 81) and iterate through the tuple and print the values to stdout
#d.	Check for membership of items ‘55’ and ‘46’ in tuple created in ‘c’
tuple_1 = (1, 12, 55, 12, 81)
print(tuple_1)
for x in tuple_1:
    print(x)
if(55 in tuple_1):
    print("55 exist in tuple_1")
if(46 in tuple_1):
    print("46 exixts in tuple_1")
else:
    print("46 not in tuple_1")