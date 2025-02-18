import os
from datetime import datetime

def copy_lines_to_text_file(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:  # Ensure UTF-8 encoding for the output file
        # Go through each file in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Skip the output file and desktop.ini to prevent them from being copied
            if filename == os.path.basename(output_file) or filename.lower() == 'desktop.ini':
                continue

            # Only process files (skip directories)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:  # Use UTF-8 encoding for input files
                        output.write(f'--- Contents of {filename} ---\n')
                        # Write each line of the current file to the output file
                        for line in file:
                            output.write(line)
                        output.write('\n')  # Add a newline between files
                except UnicodeDecodeError:
                    print(f"Skipping {filename}: unable to decode file.")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
        
        # Add timestamp message at the end of the file
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current date and time
        output.write(f"\nHere's the latest updated code for KIBA core [{timestamp}]\n")

folder_path = "D:\PROJECT\kiba-master\kiba-master\core"  # Path to your folder
output_file = "D:\PROJECT\kiba-master\kiba-master\misc\combined_output.txt"  # The output text file

copy_lines_to_text_file(folder_path, output_file)
print(f"All lines have been copied to {output_file}")
