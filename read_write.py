"""
NWHacks 2021

This py file deals with writing user input into txt file and reads the txt file
and used for output.

This py file uses the data written from user.py for writing
This py file is used by main.py for getting desired output. 
"""

#def read_file()
""" Reads the txt file
"""



#def append_file()

def write_file():
    """
    After the user is done entering the products, it is written into a txt file
    """

def main():
    """
    User gets to choose if they want to make a new file or append.
    User can read the file to get desired output
    """
    while True:
        choice_input = input("A. Make new file \nB. Append on file\n")
        if choice_input == "A":
            new_file_name = input("Write your desired file name (include .txt)\n")
            write_file(new_file_name)
            break
        elif choice_input == "B":
            file_name = input("Write the file name (include .txt) or file location\n")
            append_file(file_name)
            break
        else:
            print("Incorrect option\n")

if __name__ == "__main__":
    main()
