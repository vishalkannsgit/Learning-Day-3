sub1=int(input("enter your sub1 mark:"))
sub2=int(input("enter your sub2 mark:"))
sub3=int(input("enter your sub3 mark:"))
sub4=int(input("enter your sub4 mark:"))
sub5=int(input("enter your sub5 mark:"))
sub6=int(input("enter your sub6 mark:"))
total=(sub1+sub2+sub3+sub4+sub5+sub6)
print(total)
average=(total/6)
print(average)
if(sub1>sub2 and sub1>sub3 and sub1>sub4 and sub1>sub5 and sub1>sub6):
    print("sub1 is maximum")
elif(sub2>sub3 and sub2>sub4 and sub2>sub5 and sub2>sub6):
    print("sub2 is maximum")
elif(sub3>sub4 and sub3>sub5 and sub3>sub6):
    print("sub3 is maximum")
elif(sub4>sub5 and sub4>sub6):
    print("sub 4 is maximum")
elif(sub5>sub6):
    print("sub 5 is maximum")
else:
    print("sub6 is maximum")
if(sub1>40 and sub2>40 and sub3<40 and sub4>40 and sub5>40 and sub6>40):
    print("fail")
else:
    print("pass")