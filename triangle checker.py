s1=int(input("Enter Side 1 : "))
s2=int(input("Enter Side 2 : "))
s3=int(input("Enter Side 3 : "))
if(s1==s2==s3):
    print("Equilateral Triangle")
elif(s1==s2 or s2==s3 or s3==s1):
    print("Isoceles Triangle")
elif(s1>s2 and s1>s3):
    if((s1**2)==((s2**2)+(s3**2))):
        print("Right Angle Triangle")
    else:
        print("Scalene Triangle")
elif(s2>s3 and s2>s1):
    if((s2**2)==((s1**2)+(s3**2))):
        print("Right Angle Triangle")
    else:
        print("Scalene Triangle")
elif(s3>s1 and s3>s2):
    if((s3**2)==((s2**2)+(s1**2))):
        print("Right Angle Triangle")
    else:
        print("Scalene Triangle")
