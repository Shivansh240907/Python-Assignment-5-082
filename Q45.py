import os

dir_name = "my_new_folder"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created successfully.")
else:
    print(f"Directory '{dir_name}' already exists.")
