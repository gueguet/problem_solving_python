"""
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
"""

import os 

def print_directory_contents(sPath):
    print("Path we analyze : {}".format(sPath))
    for sChild in os.listdir(sPath):

        # join the current directory path and add the child extension to look into it
        sChildPath = os.path.join(sPath, sChild)

        # test if the child is a directory
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

# get the current directory's path
print_directory_contents(os.getcwd())
