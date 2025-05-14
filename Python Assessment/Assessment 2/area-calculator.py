#function to find area
def area(length, width):
    return length * width

#main code to calculate and print the area of a rectangle by user input and variables
def main():
    length = float(input("Enter the length of Rectangle: "))
    width = float(input("Enter the width of Rectangle: "))
    c_area = area(length, width)
    print(f"Area is: {c_area}")

#to run main() code
if __name__ == '__main__':
    main()