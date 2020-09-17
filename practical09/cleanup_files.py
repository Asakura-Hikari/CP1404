import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for i, byte in enumerate(filename):
        if i+1 != len(filename):
            if byte.islower() and filename[i+1].isupper():
                new_name += byte+"_"
            else:
                new_name += byte
    new_name += filename[len(filename) - 1]
    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')

    # add a loop to rename the files
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))
        print("File names:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


demo_walk()
