items = ['t-shirt','sweater']
loop_continue = True
while loop_continue :
     choice = str(input('Welcome to our shop, what do you want (C, R, U, D) ?'))
     def ouritem():
         item_no = 1
         for item in items :
             print('Our items:')
             print(item_no , end=' ')
             print(item)
             item_no +=1
     if choice == "c" :
         new_item = input("enter new item")
         items.append(new_item)
     elif choice == "r" :
         ouritem()
     elif choice  == 'u' :
         stt =int(input('update position'))
         newitem = input('new item?')
         items[stt-1]= newitem
         ouritem()
     elif choice == 'd' :
         remove=int(input("delete position"))
         items.pop(remove-1)
         ouritem()
     else :
         loop_continue = False