#googled to stackflow for squares

number_x = int(input("Enter the lower number: "))
number_y= int(input("Enter the higher number: "))
even=[]
odd=[]
for i in range(number_x, number_y+1):
    if i%2==0:
        even.append(i)
    elif i%2==1:
        odd.append(i)
number_range=(range(number_x, number_y+1))
squared=[i**2 for i in number_range]
print("The even numbers are: {}".format(even))
print("The odd numbers are: {}".format(odd))
print("The squares of the number sequence are: {}".format(squared))