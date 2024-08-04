import os

def rename_files_and_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            new_name = name.replace(' ', '_')
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
        for name in dirs:
            new_name = name.replace(' ', '_')
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))

# Replace 'your_directory_path' with the path to the directory you want to process
rename_files_and_folders('/home/amitk/Downloads/Mastering_Mutual_Fund_Investment _Part3/Mastering Mutual Fund Investment _ndash; Part 3 of 3/[TutsNode.com] - Mastering Mutual Fund Investment - Part 3 of 3')
