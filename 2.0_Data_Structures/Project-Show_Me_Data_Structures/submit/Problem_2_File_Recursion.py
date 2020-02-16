
"""
For this problem, the goal is to write code for finding all files 
under a directory (and all directories beneath it) that end with ".c"
"""
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
  result = []
  if os.path.isfile(path) and path.endswith(suffix):
    return path

  # if not os.path.isdir(path) and os.path.isfile(path):
  #   # print(path)
  #   return path

  if not os.path.isdir(path):# or not os.path.isfile(path):
    return 'Not a directory'



  path_list = os.listdir(path)

  

  for path_item in path_list:
    path_item = os.path.join(path,path_item)
  
    if os.path.isdir(path_item):# Checking if path is a directory
      result += find_files(suffix,path_item)


    if os.path.isfile(path_item) and path_item.endswith(suffix):#If path is a file and ends with the suffix
      result.append(path_item)
  return result

# TEST CASES

print("TEST 1")
print(find_files('.c', './testdir/'))
# Prints ['./testdir/testdir\\subdir1\\a.c', './testdir/testdir\\subdir3\\subsubdir1\\b.c', './testdir/testdir\\subdir5\\a.c', './testdir/testdir\\t1.c']

print("TEST 2")
print(find_files('.', './testdir/'))
# []

# EDGE Case test
print("TEST 3")
print(find_files('', ''))
# Not a directory

print("TEST 4")
print(find_files('.c', './testdir/testdir/subdir1/a.c'))
# Prints ./testdir/testdir/subdir1/a.c