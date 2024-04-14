import os

def find_files_less_than(folder_name):
    retrieved_files = []
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size < 1024 * 1024:
                retrieved_files.append(file_path)
    return retrieved_files


folder_name = ''
retrieved_files = find_files_less_than(folder_name)

print("Files less than 1MB in size:")
for file_path in retrieved_files:
    print(file_path)
