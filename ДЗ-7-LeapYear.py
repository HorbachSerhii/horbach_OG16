def year(y=(int(input("Print the Year You want to know:  ")))):
    if (y%4==0) and (y%100!=0) or (y%400==0):
        print(y, "is Leap Year!!!")
    else:
        print(y, "is not a Leap Year")
year()