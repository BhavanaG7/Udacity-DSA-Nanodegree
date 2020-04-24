'''
--------------------------------------------------------------------------------------------------------------------------
Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

----------------------------------------------------------------------------------------------------------------------------
'''
import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """    
    #if the suffix is empty
    if suffix=="":
        print("Empty Suffix")
        return []

    #invalid path
    if len(os.listdir(path))==0:
        return []

    path_list=os.listdir(path)
    path_files=[f for f in path_list if "."+suffix in f]
    path_dir=[f for f in path_list if "." not in f]

    for dirs in path_dir:
        path_files.extend(find_files(suffix,path+"/"+dirs))

    return path_files

#test case
path=os.getcwd()+"/testdir"   

print("files having suffix .c")
print(find_files("c",path))

print("--------------------------------------------")

print("files having suffix .h")
print(find_files("h",path))

print("--------------------------------------------")

print("files having suffix .gitkeep")
print(find_files("gitkeep",path))

print("--------------------------------------------")


#Edge Case:
print("if the suffix doesn't exsists")
print(find_files("z",path))

print("--------------------------------------------")

print("if the suffix is empty string")
print(find_files("",path))