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



def append_file(file_name):
    """
    After the user is done entering the products, it is written into a txt file
    Write elements in data into the already existing file

    Argument:
    file_name - name of file name entered by user (string value)
    data - product details that user entered (NEED TO DO)
    """
    if path.exists(file_name):
        f = open(file_name, "a+")
        for key in data:
            f.write(key)
            f.write("\n")
            for values in data[key]:
                f.write(str(values)+'\n')
            f.write("\n")
        f.close()
        global condition
        condition = False #Made to false after entire data has been written into file
    else:
        print("File name doesn't exits.\nEither make new file or append to a existing file")

def write_file(file_name):
    """
    After the user is done entering the products, it is written into a txt file
    Write elements in data into the newly made file

    Argument:
    file_name - name of file name entered by user (string value)
    data - product details that user entered (NEED TO DO)
    """
    if not path.exists(file_name):
        f = open(file_name, "w+")
        for key in data:
            f.write(key)
            f.write("\n")
            for values in data[key]:
                f.write(str(values)+'\n')
            f.write("\n")
        f.close()
        global condition
        condition = False #Made to false after entire data has been written into file
    else:
        print("File name already in use.\nEither append to the existing file or make a new file\n")

def main():
    """
    User gets to choose if they want to make a new file or append.
    User can read the file to get desired output

    Argument:
    data - product details that user entered (NEED TO DO)
    """
    while condition:
        choice_input = input("A. Make new file \nB. Append on file\n")
        if choice_input == "A":
            new_file_name = input("Write your desired file name (include .txt)\n")
            write_file(new_file_name)
        elif choice_input == "B":
            file_name = input("Write the file name (include .txt) or file location\n")
            append_file(file_name)
        else:
            print("Incorrect option\n")
