# Ask the user to enter the name of the file they want to read
filename = input("Enter the name of the file to read: ")

try:
    # Try to open the file in read mode
    file = open(filename, "r")

    # Read the content of the file
    content = file.read()

    # Close the file after reading
    file.close()

    # Modify the content (Make the text in the file uppercase)
    modified = content.upper()

    # Create a new filename to save the modified content
    new_filename = "new_" + filename

    # Open a new file in write mode and write the modified content
    new_file = open(new_filename, "w")
    new_file.write(modified)

    # Close the new file after writing
    new_file.close()

    # Let the user know it worked!
    print("File was read and modified successfully!")

# If the file doesn't exist, show this error message
except FileNotFoundError:
    print("Error: That file does not exist. Please check the name and try again.")

# If there is any other issue with reading or writing the file
except IOError:
    print("Error: Something went wrong when trying to read or write the file.")

