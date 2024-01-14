def zai():
 Q=input("Enter your operation from the given list as it is written \n\nAdd,Subtract,Division,Multiply,\n")
 Value_1=int(input("Enter Your 1st Number\n"))
 Value_2=int(input("Enter Your 2nd Number\n"))
 A=str("Add")
 S=str("Subtract")
 D=str("Division")
 M=str("Multiply")
 if Q==A:
  print(Value_1+Value_2)
 elif Q==S:
  print(Value_1-Value_2)
 elif Q==D:
  print(Value_1/Value_2)
 elif Q==M:
  print(Value_1*Value_2)
zai()
