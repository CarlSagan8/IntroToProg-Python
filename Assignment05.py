# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MClark,2.12.2021,Added code to complete assignment 5
# MClark,2.14.2021, Tried to pretty code up
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
File = open(objFile, "r")
for item in File:
    lstRow = item.split(",")
    dicRow = {"Task":lstRow[0].strip(), "Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
File.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your Current Data is: " '\n')
        for row in lstTable:
            print(row["Task"] + ',' + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input('Task Name: ')
        strPriority = input('Task Priority: ')
        dicAdd = {"Task":strTask, "Priority":strPriority}
        lstTable.append(dicAdd)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("This is your current Data:" '\n')
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"])
        taskRemove = input("What is the name of the task you would like to remove?: ")
        for row in lstTable:
            if row["Task"] == taskRemove:
                lstTable.remove(row)
            else:
                print("Could not find task")
        print("This is the current list:")
        for item in lstTable:
            print(item["Task"] + "," + item["Priority"])
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Would You Like to Save Your Data?")
        strOption = str(input(" Enter 'y' or 'n': "))
        if (strOption.lower() == 'y'):
            objFile = open("ToDoList.txt", "w")
            for row in lstTable:
                objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
            objFile.close()
            print("Data Saved")
        else:
            print(' Changes were not saved')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Would you like to exit the program?")
        strExit = str(input("Enter 'exit' to exit program: "))
        print("Thank you, Goodbye :)")
        break  # and Exit the program