a=str(input("Please type a string for  'a' variable:  "))
b=str(input("Please type a string for  'b' variable:  "))
c=str(input("Please type a string for  'c' variable:  "))
d=str(input("Please type a string for  'd' variable:  "))
e=str(input("Please type a string for  'e' variable:  "))

max_len = 0

if len(a) > len(b):
    max_len = len(a)
else:
    max_len = len(b)
if max_len < len(c):
    max_len = len(c)
if max_len < len(d):
    max_len = len(d)
if max_len < len(e):
    max_len = len(e)

print(max_len)

# using list[]

strings=[a, b, c, d, e]

max_len_str = max(strings, key=len)
print(len(max_len_str))
