def modify_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"Successfully modified {input_file} and saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}") 