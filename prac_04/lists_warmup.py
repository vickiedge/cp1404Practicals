numbers=[3,1,4,1,5,9,2]
#3
#2
#1
#[2]
#[1,5]
#True
#False
#False
#[3,1,4,1,5,9,2,6,5,3] evaluated to an expression but didn't change list

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
for number in numbers:
    if number is 5:
        print("Yes, 5 present")
        break
for number in numbers:
    if number is 7:
        print("Yes, 7 present")
        break
for number in numbers:
    if number is "3":
        print("Yes, str 3 present")
        break
print(numbers + [6,5,3])



