import os
import shutil

PATH = "FilesToSort"


def main():
    os.chdir(PATH)
    files = os.listdir('.')
    dir_list = []
    for file in files:
        suffix = get_name_list(file)
        dir_list.append(suffix[1])
    for dir in dir_list:
        try:
            os.mkdir(dir)
        except FileExistsError:
            pass
    for dir in dir_list:
        os.chdir(dir)
        target = os.getcwd()
        os.chdir("..")
        for file in files:
            file_type = get_name_list(file)
            if file_type[1] == dir:
                print("moving {} to {}".format(file, dir))
                shutil.move(file, target)
                files.pop(files.index(file))


def get_name_list(filename):
    list_for_name = filename.split('.')
    return list_for_name


main()
