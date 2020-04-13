from tabulate import tabulate

mydata = [("a", "b", "c"), ("d", "e", "f")]

a = [1,2,3]

print(tabulate(mydata, headers=a))