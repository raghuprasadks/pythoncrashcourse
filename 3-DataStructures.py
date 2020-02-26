'''
List - Dynamic, indexable, duplicate, modify 
'''

data = [3,5,8,9]
print(data)

data[0]

data[4]
newlist = data[1:4]

data[-1]

data.append(11)
max(data)
min(data)
sum(data)
len(data)
data[2] ="Eight"


'''
Dictionary
'''
tele={"raghu":9845547471,"satvik":9845547472}
print(tele)

tele["raghu"]

tele.keys()
tele.values()
for k,v in tele.items():
    print(k,v)
    
tele.update({"raghu":9845547473})

'''
Tuple
'''
data1 = (2,5,7,8)
data1.append(10)

data1[1] = 'Five'

