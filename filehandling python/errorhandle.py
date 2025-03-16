def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")

        # Attempt to open the file
        with open(filename, 'r') as file:
            content = file.readlines()

        # Modify the content (example: add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

        # Write to a new file
        output_filename = f"modified_{filename}"
        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_content)

        print(f"Modified file saved as: {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
