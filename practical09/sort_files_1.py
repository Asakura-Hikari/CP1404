import os
import shutil


def main():
    os.chdir("FilesToSort")
    files = os.listdir('.')
    dir_list = []
    for file in files:
        suffix = file.split('.')
        dir_list.append(suffix[1])

    try:
        for dir in dir_list:
            os.mkdir(dir)
        os.mkdir('doc')
        os.mkdir('docx')
        os.mkdir('xls')
        os.mkdir('xlsx')
        os.mkdir('png')
        os.mkdir('jpg')
        os.mkdir('gif')
        os.mkdir('txt')
    except FileExistsError:
        pass
    filenames = os.listdir('.')
    print(filenames)

    for filename in filenames:
        if os.path.isfile(filename):
            list_for_name = get_name_list(filename)
            if list_for_name[1] == 'doc':
                shutil.move(filename, 'doc/' + filename)

            if list_for_name[1] == 'docx':
                shutil.move(filename, 'docx/' + filename)

            if list_for_name[1] == 'xls':
                shutil.move(filename, 'xls/' + filename)

            if list_for_name[1] == 'xlsx':
                shutil.move(filename, 'xlsx/' + filename)

            if list_for_name[1] == 'jpg':
                shutil.move(filename, 'jpg/' + filename)

            if list_for_name[1] == 'png':
                shutil.move(filename, 'png/' + filename)

            if list_for_name[1] == 'gif':
                shutil.move(filename, 'gif/' + filename)

            if list_for_name[1] == 'txt':
                shutil.move(filename, 'txt/' + filename)


def get_name_list(filename):
    list_for_name = filename.split('.')
    return list_for_name


main()
