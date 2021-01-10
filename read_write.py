"""
NWHacks 2021

This py file deals with writing user input into txt file and reads the txt file
and used for output.

This py file uses the data written from user.py for writing
This py file is used by main.py for getting desired output. 
"""

def write_file(file_name, data):
    """
    After the user is done entering the products, it is written into a txt file

    Argument:
    file_name - name of file name entered by user (string value)
    data - product details that user entered (NEED TO DO)
    """
    f = open(file_name, "a+")
    for key in data:
        f.write("#"+key+"\t#"+str(data[key][0])+"\t#"+data[key][1])
        f.write("\n")
    f.close()

def main(data):
    """
    User gets to choose if they want to make a new file or append.
    User can read the file to get desired output

    Argument:
    data - product details that user entered (NEED TO DO)
    """

    print("Writing into Inventory.txt\nPlease hold on\n")
    write_file('Inventory.txt', data)
    print("Done writing!")
