tup1=tuple(input("Enter elements separated by space: ").split())
tup2=tuple(input("Enter elements separated by space: ").split())
concatenated=tup1 + tup2
print("Concatenated tuple:", concatenated)
n=int(input("Enter number of times to repeat the concatenated tuple: "))
repeated=concatenated * n
print("Repeated tuple:", repeated)