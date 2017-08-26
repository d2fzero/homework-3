items = [5,7,90,270,24,50,60]
# 2.1
print('Hello,my name is Hiep and these are my sheep size ' , items)
# 2.2
max = 1
for item in items :
    if max < item :
        max = item
print('now my bigest sheep has size ',max,"let's shear it")
# 2.3
item_no = 0
for item in items :
    if item == max :
        items[item_no] = 8
    item_no += 1
print('after shearing ,here is my flock')
print(items)
# 2.4

def onemonth():
    global items
    items = [item + 50 for item in items]
    print('one month has passed,now here is my flock')
    print(items)
    max = 1
    for item in items :
        if max < item :
            max = item
    print('now my bigest sheep has size ',max,"let's shear it")
    item_no = 0
    for item in items :
        if item == max :
           items[item_no] = 8
        item_no += 1
    print('after shearing ,here is my flock')
    print(items)

# 2.5
month = int(input("nhap so thang"))
for i in range (month):
     print('month ' , i+1)
     onemonth()
# 2.6
month = int(input('when you sold your flock ?'))
for i in range (month-1):
    print('month ' , i+1 )
    onemonth()
print('month' , month)
items = [item + 50 for item in items]
print('one month has passed,now here is my flock')
print(items)
tong = 0
for item in items :
    tong = tong+item
print('my flock have size in total ',tong)
print('i would get ', tong ,'* 2$ =',tong * 2,'$')




