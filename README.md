This is a file recovery tool which makes use of python. 
  The Recovery_Script is the main python script containing all the logic and info as comments its a small script which can be implemented with ease, 
  -The drive letter that you want to perform recovery on needs to be updated in the Recovery_Script file, 
  -All the recoververd files are written into the recovered folder.
The Run_me bat file automates the whole process by performing a check to ensure python is installed and installs it if nessary and executes the python script.


This script makes use of file signatures to find the deleted files and restore it.  
It bypasses the file system and access the raw bits of data and scans the drive for any suitable files wit the help of file signatures,
Since it by pases the file system spefic folders cant be used as foldres are indexing values given to a block of data interpretated as folder by the file system
