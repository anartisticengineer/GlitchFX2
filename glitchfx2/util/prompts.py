from os import path


class Prompt:
    def __init__(self):
        pass

    # ask where to find the file
    @staticmethod
    def get_input_file():
        # FIRST PROMPT
        return input("\nChoose an input image file... ")

    @staticmethod
    def cant_find_src(_path_name):
        print("I couldn't find a src folder.")
        print("So I made one for you to store your photos~")
        print("Creating your src folder at " + _path_name)
        print("Run the program again and you should be good!")

    @staticmethod
    def enter_effect():
        return input("\nEnter an effect ~ x to finish... ")

    # ask what to save the file as
    @staticmethod
    def get_output_file_name(_original_file_name):
        (origName, ext) = path.splitext(_original_file_name)
        default_name = origName + "-glitched"
        print("\nEnter an output file name...")
        return (input("Or leave blank for the default name... ") or default_name) + ext