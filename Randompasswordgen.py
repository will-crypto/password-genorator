import random

#code that creats the passwords
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = input("number of passwords? - ")
number = int(number)

length = input("passord length? - ")
length = int(length)

for p in range(number):
    password = " "
for c in range (length):
    password += random.choice (chars)
print(password)

