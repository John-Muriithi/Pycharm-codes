fname = str(input("enter the first name of the student"))
sname = str(input("enter the second name of the student"))
marks = int(input("enter the marks of the student"))
print("NAME:",fname,sname,'\n'"MARKS:",marks)
if marks>=40 and marks<100:
    print("CATEGORY: PASS")
elif marks<40 and marks>0:
    print("CATEGORY: FAIL")
else:
    print("enter correct marks")