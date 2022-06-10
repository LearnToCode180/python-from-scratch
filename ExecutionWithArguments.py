import sys

name = sys.argv[1]
last_name = sys.argv[2]
nb1 = int(sys.argv[3])
nb2 = int(sys.argv[4])

print(f"Your file is {sys.argv[0]}") 
print(f"Hello Mr. {name} {last_name}")
print(f"{nb1} + {nb2} = {nb1 + nb2}")