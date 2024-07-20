import os
import re


def rename_files(directory, start_num, end_num):
    # Get list of files in the specified directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Sort files to ensure correct ordering
    files.sort()

    # Counter for the new numbering
    new_num = 1

    for file in files:
        # Extract the current number from the filename
        match = re.match(r'(\d+)', file)
        if match:
            current_num = int(match.group(1))

            # Check if the current number is within the specified range
            if start_num <= current_num <= end_num:
                # Create the new file name
                new_name = f"1.{new_num:02d}{file[len(match.group(1)):]}"

                # Full paths for old and new names
                old_path = os.path.join(directory, file)
                new_path = os.path.join(directory, new_name)

                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed '{file}' to '{new_name}'")

                new_num += 1


if __name__ == "__main__":
    directory = input("Enter the full path of the directory containing the course files: ")

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
    else:
        start_num = int(input("Enter the start number of the range to rename: "))
        end_num = int(input("Enter the end number of the range to rename: "))

        rename_files(directory, start_num, end_num)
        print("File renaming complete!")