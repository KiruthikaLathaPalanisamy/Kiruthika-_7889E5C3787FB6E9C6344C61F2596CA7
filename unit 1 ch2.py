#Python program to check if year is a leap year or not
year=2000
#To get year(integer input)from the user
#year=int(intput("Enter a year:"))
#divided by 100 means century year(ending with 00)
#Century year divided by 400 is leap year
if(year%400==0)and(year%100==0):
  print("{0}is a leap year".format(year))
  #not divided by 400 means not a century year
  #year divided 4 is a leap year
elif(year%4==0)and(year%100!=0):
  print("{0} is a leap year".format(year))
  #if not divided by both 400(century year)and 4(not a century year)
#year is not a leap year
else:
  print("{0}is not a leap year".fomat(year))