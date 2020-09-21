import os
import shutil

PATH = "FilesToSort"


def main():
    dirnames = os.listdir(PATH)
    os.chdir(PATH)
    target = os.getcwd()
    for dir in dirnames:
        os.chdir(dir)
        for file in os.listdir(os.getcwd()):
            shutil.move(file, target)
        os.chdir("..")
    for dir in dirnames:
        os.rmdir(dir)


main()
