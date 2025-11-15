marks=int(input("Enter the marks"))

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")

#nested if else

age=20
citiZen=True

if age>=18:
    if citiZen:
        print("you can vote")
    else:
        print("only citizen can vote")
else:
    print("you can underage.")