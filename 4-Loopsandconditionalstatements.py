'''
Loops - while and for
'''

#While

start = 1
end = 10

while(start<=end):
    print(start)
    start = start +1
    
for i in range(10):
    print(i)
    
for i in range(1,11):
    print(i)
    
for i in range(2,21,2):
    print(i)

for i in range(1,11):
    if (i==5):
        break
    print(i)

for i in range(1,11):
    if (i==5):
        continue
    print(i)

age = 17

if(age >= 18):
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')
    
marks = 85

if (marks >=90 and marks <=100):
    print('A+')
elif (marks >=80 and marks <=90):
    print('A')
else:
    print('Grade other than A+ or A')
    
