import os
import shutil

PATH = "FilesToSort"


def main():
    dirnames = os.listdir(PATH)
    os.chdir(PATH)
    target = os.getcwd()
    for dir in dirnames:
        if os.path.isdir(dir):
            os.chdir(dir)
            for file in os.listdir(os.getcwd()):
                print("moving {} to {}".format(file, target))
                shutil.move(file, target)
            os.chdir("..")
    for dir in dirnames:
        if os.path.isdir(dir):
            os.rmdir(dir)


main()
