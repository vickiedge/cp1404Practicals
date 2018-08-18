#Files - Q 1
OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
name = input("Enter your name: ")
print((name),file=out_file)
out_file.close()

#Files - Q 2

#temp_file = open("name.txt", "r")
#3first_line_str = temp_file.readline()
#first_line_str
#'first line]n'
#for line_str in temp_file:
#    print(line_str)
#temp_file.readline()
#temp_file.close()


in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

#Files - Q 3
in_file=open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
answer = number_1 + number_2
print(answer)
in_file.close()

#Files - Q 4
in_file=open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
