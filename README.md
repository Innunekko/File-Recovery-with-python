
This is a file recovery tool which makes use of python. 

**Script Components**   
    Recovery_Script.py: The main Python script containing the logic and comments for easy implementation.    
    Run_me.bat: A batch file that automates the process by checking for Python installation, installing it if necessary, and executing the Python script.

**How it Works**    
    The script bypasses the file system and directly accesses the raw bits of data on the drive. It scans the drive for files matching specific signatures and restores them. Since it doesn't rely on the file            system, it cannot recover files to specific folders, as folders are simply indexing values assigned to blocks of data by the file system.

**Configuration**    
    To use the script, the user needs to update the drive letter in the Recovery_Script.py file. All recovered files will be written to a folder named "recovered".
