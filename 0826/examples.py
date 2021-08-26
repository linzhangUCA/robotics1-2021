# inch to mm
1/4*25.4

# Fahrenheit to Celcius
(99-32)*5/9

# Pythagorean theorem
(3**2+4**2)**.5

# variables
a = 2
b = 2.71
c = 'r'
d = 'robot'

# if statement
x = input("Please enter a number: ")
if x>0:
    print("positive")
elif x==0:
    print("zero")    
else:
    print("negative")

# for loop
for i in range(10):
    print(i)
    
# another for loop
robots = ['atlas', 'r2d2', 'gundam-rx-78-2', 'roomba']
for robot in robots:
    print("name: {}, name length: {}".format(robot, len(robot)))
    
# while loop
theta = -3.1415926
while theta < 3.1415926:
    print(theta)
    theta = theta + 0.5 # theta += 0.5
    if int(theta)==0:
        theta = 1
    if theta >= 2.5:
        print("{}, time to break".format(theta))
        break

# define function
def add_two_number(a,b):
    c = a + b
    return c
