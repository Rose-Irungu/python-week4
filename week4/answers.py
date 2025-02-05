def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (in this case, we just add a prefix for demonstration)
        modified_content = "Modified Content:\n" + content

        # Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Modified content has been written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading from or writing to the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Ask the user for the filename
input_filename = input("Enter the filename to read from: ")
output_filename = input("Enter the filename to write to: ")

# Call the function to read, modify, and write the file
read_and_modify_file(input_filename, output_filename)
