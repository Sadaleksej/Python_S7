from files_storage import home_functions as hf

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data")
    files_cnt = hf.group_rename_files("xxx", ".txt", path="./data")
    print(f"Переименовано: {files_cnt}")
