import os

if __name__ == "__main__":
    if (os.path.isdir("src") == False):
        absPath = os.path.abspath("../glitch-fx-2")
        print("Creating src folder here: {}".format(absPath))
        os.mkdir("src")
    else:
        pass
    os.chdir("src")
    # choose a file already in the src folder
    fileIn = input("Choose an input image file: ")
    print(os.path.join(os.getcwd(), fileIn))
