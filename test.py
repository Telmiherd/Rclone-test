import subprocess

# Define the rclone command to list files in a folder
remote = "shared"  # Replace with your remote name
folder_path = '/"Site Control"'  # Replace with the folder path
print(folder_path)
#rclone_command = f"rclone lsf {remote}:{folder_path}"
rclone_command = f"rclone ls shared:/"
working_directory = "C:\\Users\\null\\Desktop\\rclone"

# Run the rclone command and capture the output
result = subprocess.run(rclone_command, cwd=working_directory, shell=True, capture_output=True, text=True)


# Check if the command was successful
if result.returncode == 0:
    # Save the output to a text file
    with open("file_list.txt", "w", encoding="utf-8") as file:
        file.write(result.stdout)
else:
    print(f"Error: {result.stderr}")