
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
  if not os.path.isdir(path):
    return 'Not a directory'

  path_list = os.listdir(path)

  result = []

  for path_item in path_list:
    path_item = os.path.join(path,path_item)
    # print all folders and files in the directory
    
    print(path_item)

    if os.path.isdir(path_item):
      result += find_files(suffix,path_item) 


    if os.path.isfile(path_item) and path_item.endswith(suffix):
      result.append(path_item)
  return result

# printing out lstprint("Printing all files and folders in the directory


print(find_files('.c', './testdir/'))