import subprocess
from datetime import datetime

# Define the rclone command to list files in a folder
remote = "shared"  # Replace with your remote name
folder_path = '/"Site Control"'  # Replace with the folder path
print(folder_path)
#rclone_command = f"rclone lsf {remote}:{folder_path}"
rclone_command = f"rclone lsl shared:/"
working_directory = "C:\\Users\\null\\Desktop\\rclone"

# Run the rclone command and capture the output
result = subprocess.run(rclone_command, cwd=working_directory, shell=True, capture_output=True, text=True)


# Check if the command was successful
if result.returncode == 0:
    # Parse the output to extract file names and modification times
    file_data = []
    for line in result.stdout.strip().split('\n'):
        parts = line.split()
        print(parts)
        if len(parts) >= 3:
            # Ignore the first part (file size or other metadata)
            date_time_str = parts[1]  # Join date and time parts
            mod_time = datetime.strptime(date_time_str, '%Y-%m-%d')
            file_data.append((mod_time, parts[2:]))

    # Sort the file data by modification time
    sorted_file_data = sorted(file_data, key=lambda x: x[0], reverse=True)

    # Write the sorted data to a text file
    with open("file_list.txt", "w", encoding="utf-8") as file:
        for mod_time, file_parts in sorted_file_data:
            file_name = ' '.join(file_parts)
            file.write(f"{mod_time.strftime('%Y/%m/%d')} {file_name}\n")

else:
    error_output = result.stderr
    print(f"Error: {result.stderr}")