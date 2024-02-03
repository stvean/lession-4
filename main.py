import os


def rename_to_lowercase(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, filename.lower())

            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')

        for dir_name in dirs:
            old_path = os.path.join(root, dir_name)
            new_path = os.path.join(root, dir_name.lower())

            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')


if __name__ == "__main__":
    target_directory = input("Enter the target directory path: ")
    if target_directory == '':
        target_directory = '.'

    if os.path.exists(target_directory):
        rename_to_lowercase(target_directory)
        print("Renaming complete.")
    else:
        print("Directory not found.")
