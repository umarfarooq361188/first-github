#  two kine of loops:  <1> While Loops      <2> For Loops
# While Loops

# x=input("enter a number ")
# y=int(x)
# while( y <=9):
#     print(y, "is first digit number")
#     y=y+1
    
# print(y,"is not first digit number")

# For Loop

# for x in range (1,10):
#     print(x)

#  Array
# months=['Janu','Fab','Mar','Apr','May','june','july','august']
# for d in months:
#     print(d)

# months=['Janu','Fab','Mar','Apr','May','june','july','august']
# for d in months:
#     if(d=='Apr'):break
#     print(d)

# months=['Janu','Fab','Mar','Apr','May','june','july','august']
# for d in months:
#     if(d=='Apr'):continue
#     print(d)

months=['Janu','Fab','Mar','Apr','May','june','july','august']
for d in months:
    # if(d=='Apr'):break
    # print(d)
    if(d=='june'):continue
    print(d)