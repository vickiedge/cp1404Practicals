#error check loop for number of items
#number_of_items determines number of times price requested
#total adds price to total each time
#if statement accounts for discount

def main():
    total = 0
    number_of_items = int(input("Number of items: "))
    while number_of_items <= 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    for i in range (number_of_items):
        price = float(input("Price of item: "))
        total += price
    if total > 100:
        discount = total * 0.1
        total = total - discount
    print("Total price for {} items is ${:.2f}".format(number_of_items, total))
main()
