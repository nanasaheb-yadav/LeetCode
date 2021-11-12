import os

path = "D:\Python\GIT Projects\Python_Codes\\"

def list_files(dir_path, indexes=[]):
    index_str = ".".join(indexes)
    print(f'{index_str} - {dir_path}')
    dir_elements = os.listdir(dir_path)

    files_list = []
    dirs_list  = []

    for f in dir_elements:
        if os.path.isdir(os.path.join(dir_path, f)):
            dirs_list.append(os.path.join(dir_path, f))
        else:
            files_list.append(f)

    findex = 1
    for file in sorted(files_list):
        findex_str = ".".join(indexes + [str(findex)])
        print(f'{findex_str} - {file}')
        findex += 1

    dindex = 1
    for dir in sorted(dirs_list):
        list_files(dir, indexes + [str(dindex)])
        dindex += 1

list_files(path)
