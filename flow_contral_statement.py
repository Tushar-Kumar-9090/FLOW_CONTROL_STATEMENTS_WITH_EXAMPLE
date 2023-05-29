
## Q.1 WAP to print a number if the given number is greater than 100??

n=int(input("Enter The Number: "))
if n>100:
    print(f'The given number {n} is greater than 100')
else:
    print(f'The given number {n} is smaller than 100')



## Q.2 Print the string if the string is starting with h???

s=input("Enter the string")
if s[0]=='H' or s[0]=='h':
    print(s)

if s.startswith('h') or s.startswith('H'):
    print(s)


## Q.3  print a string if the given string having morethan 3 words??

## 1st way
s=input("Enter the string")
count=0
for i in s:
    if i==' ':
        count+=1
        if count>=3:
            print(s)
            break


## 2nd way
s=input("Enter the string")
if s.count(' ')>2:
    print(s)


##
s=input("Enter the string")
if len(s.split())>3:
    print(s)



## Q.4  print the string if the string having t for more than 3 times??

s=input("Enter the string")
count=0
for i in s:
    if i=='t' or i=='T':
        count+=1
        if count>3:
            print(s)
            break


##
s=input("Enter the string")
if s.lower().count('t')>3:
    print(s)


## Q.5   print a string if it is having more than 10 charecters??

s=input("Enter a string: ")
if len(s)>10:
    print(s)
