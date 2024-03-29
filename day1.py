#1. Define a new variable a with value 25, b with 10 and do the following opertions:

# a) Sum a and b
a=25
b=10
print(a+b)

# b)Subtract a from b
a=25
b=10
print(b-a)

#c)Multiply a with b
a=25
b=10
print(a*b)

#d)Divide a/b 
a=25
b=10
print(a/b)

# e)What is the operation that has to be done to get only integer while doing a/b
# floor division method. the symbol // is used to perform integer division
a=25
b=10
print(a//b)

# f) What is the remainder when a is divided by b 
# the reminder is 5
a=25
b=10
print(a%b)
#########################################################################################################

# 2.Define a string with value x = ' How are you' and y="This world is beautiful " and do the following operations:
#  a. Get "how" from the variable x and store it in d

x = 'How are you'
y="This world is beautiful "
d = x.split()[0]
print(d) 

# b. Split x based on white space
x = 'How are you'
split_x = x.split()
print(split_x)

# c.Split the variable y based on the letter "i"
y = "This world is beautiful"
split_y = y.split("i")
print(split_y)

# d.Reverse the string x
x = 'How are you'
reverse_x = x[::-1]
print(reverse_x)

# e. How to get the output "Hwareo" from the string x
x = 'How are you'
output = x[0]+x[2]+x[4:7] + x[9]
print(output)

# f. Create a new string with value =  How are you This world is beautiful using string concatenation
new_string = "How are you" + " " + "This world is beautiful"
print(new_string)
