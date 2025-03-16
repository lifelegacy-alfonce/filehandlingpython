1: def read_and_modify_file():
2:     try:
3:         filename = input("Enter the filename to read: ")
4: 
5:         # Attempt to open the file
6:         with open(filename, 'r') as file:
7:             content = file.readlines()
8: 
9:         # Modify the content (example: add line numbers)
10:         modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
11: 
12:         # Write to a new file
13:         output_filename = f"modified_{filename}"
14:         with open(output_filename, 'w') as output_file:
15:             output_file.writelines(modified_content)
16: 
17:         print(f"Modified file saved as: {output_filename}")
18: 
19:     except FileNotFoundError:
20:         print(f"Error: The file '{filename}' does not exist.")
21:     except PermissionError:
22:         print(f"Error: Permission denied to read the file '{filename}'.")
23:     except Exception as e:
24:         print(f"An unexpected error occurred: {e}")
25: 
26: # Run the program
27: read_and_modify_file()
