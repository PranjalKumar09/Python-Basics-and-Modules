""" 
Shutil module offers high-level operation on a file like a copy, create, and remote operation on the file. It comes under Python"s standard utility modules. 

shutil.copy(source, destination)

                Preserve File permission           Destination can be Directory           Copied Meta Data           Work with file object
shutil.copy         Yes                                       Yes                                 No                          No
shutil.copyfile     No                                        No                                  No                          No
shutil.copy2        Yes                                       Yes                                 Yes                         No
shutil.copyfileobj  No                                        No                                  No                          Yes

Syntax same of  all


shutil.copytree(src, dst, symlinks = False, ignore = None, copy_function = copy2, ignore_dangling_symlinks = False)

Parameters:
src: string path of  source directory.
dest: string rpath of  destination.
symlinks (optional) : boolean value  depending on which the metadata of the original links or linked links will be copied to the new tree.
ignore (optional) : If ignore is given, it must be a callable that will receive as its arguments the directory being visited by copytree(), and a list of its contents, as returned by os.listdir().
copy_function (optional): default value is copy2. We can use other copy function like copy() for this parameter.
ignore_dangling_symlinks (optional) :When set to True is used to put a silence on the exception raised if the file pointed by the symlink doesn’t exist.

Return Value: This method returns a string which represents the path of newly created directory.



shutil.rmtree(path, ignore_errors=False) 

Parame:  file path. Either a string or bytes object representing a path.
ignore_errors: If ignore_errors is true, errors resulting from failed removals will be ignored.

# Note: this method remove better than os when removing folders containg files



shutil.which(cmd, mode = os.F_OK | os.X_OK)
Parameters:
cmd: A string representing the file.
mode: This parameter specifies mode by which method should execute. os.F_OK tests existence of the path and os.X_OK Checks if path can be executed or we can say mode determines if the file exists and executable.


import shutil  
   
# file search  
cmd = 'anaconda'
   
# Using shutil.which() method 
locate = shutil.which(cmd) 
   
# Print result 
print(locate) #D:\Installation_bulk\Scripts\anaconda.EXE





There is also move a file shutil.move(src, dest)
"""

""" import shutil

file_name = "QR_Generator"

location = shutil.which(file_name)
print (location)  """