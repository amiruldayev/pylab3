print("\t\t\t\t TASK 1.1 ")
print(f"{4} {8} {15} {16} {23} {42}")


print("\t\t\t\t TASK 1.2 ")
print(f"{4}\n{8}\n{15}\n{16}\n{23}\n{42}")


print("\t\t\t\t TASK 1.3 ")
try:
    firstnum = int(input("First number:")) #запрашивает число
    print(firstnum + 1)  # к числу добавляет 1
    print(firstnum + 2)  # к числу добавляет 2
except ValueError: #вывод, если вместо числа написать строку
    print("Write a number:")


print("\t\t\t\t TASK 1.4 ")
a=int(input("num 1:"))
b=int(input("num 2:"))
c=int(input("num 3:"))
print(a+b+c)


print("\t\t\t\t TASK 1.5 ")
onefive = int(input("Insert:"))
print(f"Volume:{onefive*onefive*onefive}")
print(f"Total surface area:{onefive*onefive*6}")







print("\t\t\t\t TASK 2.1 ")
schoolchildren = int(input("schoolchildren:"))
tangerines = int(input("tangerines:"))
print(tangerines/schoolchildren)
print(tangerines%schoolchildren)


print("\t\t\t\t TASK 2.2 ")
num = int(input("Insert:"))
print(f"The digit in the thousands position is {int(num/1000)}\n\
The number in the hundreds position is {int(num%1000/100)}\n\
The digit in the tens position is {int(num%1000/10%10)}\n\
The digit in the position of units is {int(num%1000%10)}\n\
")


print("\t\t\t\t TASK 2.3 ")
try:
    people = int(input("Number of people:"))
    print(round(people/2)) #вывести округленное число

except ValueError:
    print("write numbers:")



print("\t\t\t\t TASK 2.4 ")
x = int(input("Insert:"))
y = x << 1 #сдвиг влево
print(f"The result of << is {y}")


print("\t\t\t\t TASK 2.5 ")
try: #проверка на исключение, если пользователь внесет строку вместо цифр
    fnumber = int(input("Please enter the first number: "))
    snumber = int(input("Please enter the second number: "))
    operation = input("Please choose the operation (+, -, *, /): ")

    if(operation == "+"):
        print(fnumber+snumber)

    if (operation == "-"):
        print(fnumber - snumber)

    if (operation == "*"):
        print(fnumber * snumber)

    if (operation == "/"):
        print(fnumber / snumber)
except ValueError:
    print("Error! write numbers")
