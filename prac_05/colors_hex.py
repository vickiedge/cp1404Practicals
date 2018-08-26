# COLOR_CODES = {'AntiqueWhite': '#faebd7', 'aquamarine1': '#7fffd4',
#               'azure1': '#f0ffff', 'beige': '#f5f5dc', 'black': '#000000',
#               'blue1': '#0000ff', 'brown': '#a52a2a', 'CadetBlue1': '#98f5ff',
#               'chartreuse1': '#7fff00', 'coral': '#ff7f50'}

# color = (input("Enter color: "))
# print("{} code is {}".format(color, COLOR_CODES[color]))

COLOUR_CODES = {'AntiqueWhite': '#faebd7', 'aquamarine1': '#7fffd4',
                'azure1': '#f0ffff', 'beige': '#f5f5dc', 'black': '#000000',
                'blue1': '#0000ff', 'brown': '#a52a2a', 'CadetBlue1': '#98f5ff',
                'chartreuse1': '#7fff00', 'coral': '#ff7f50'}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
