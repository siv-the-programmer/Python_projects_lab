# File Search Script

# Overview
This script recursively searches through a directory to locate a file by its exact name.  
It scans all subdirectories, counts how many items have been checked, and provides progress feedback during the scan.

The script is written for learning purposes and focuses on clarity and understanding rather than optimization.

# Purpose
The goal of this script is to demonstrate how to:
- Traverse directories recursively using Python
- Accept user input safely
- Track execution progress
- Stop execution immediately once a match is found
- Structure a Python script using a main entry point

# Requirements
This script uses only Python standard library modules:
- os
- pathlib

No third-party packages are required.

# Script Behavior
The script performs the following actions:
- Defines a root directory to search in
- Prompts the user to enter a filename including its extension
- Recursively scans every file and folder
- Tracks how many items have been scanned
- Prints progress updates every 1000 items
- Displays the file location if found
- Prints a message if the file is not found

# Path Configuration
The directory to be scanned is defined in the script using:
Path("ENTER_YOUR_PATH_TO_LOOK_IN")

This value must be replaced with a valid directory path before running the script.

# User Input
The user is prompted to enter the exact filename to search for.
The match is case-sensitive and must include the file extension.

Example inputs:
notes.txt  
report.pdf  
data.csv  

# File Scanning Logic
The script uses recursive globbing to scan all files and subdirectories.
Each scanned item increases a counter that tracks progress through the file system.

# Progress Feedback
Every 1000 scanned items, the script prints a progress message indicating how many items have been checked so far.
This provides visual feedback during long searches.

# File Match Handling
When a file name matches the user input:
- The terminal screen is cleared
- The file name is displayed
- The full resolved file path is printed
- The total number of scanned items is shown
- The script exits immediately

# File Not Found Handling
If the scan completes without finding the file, a message is printed indicating that the file was not found.

# Execution Flow
1. Script starts
2. User enters target filename
3. Directory scan begins
4. Counter increments for each scanned item
5. Progress messages print every 1000 items
6. Script exits immediately when a match is found
7. If no match exists, a not-found message is displayed

# How to Run
Run the script from the terminal using:
python main.py

Ensure Python 3 is installed and the search path is valid.

# Limitations
- Exact filename match only
- Case-sensitive search
- Stops after first match
- No permission error handling
- No filtering by extension or size

These limitations are intentional to keep the logic simple and readable.

# Learning Outcomes
This script helps build understanding of:
- Recursive directory traversal
- Loop counters and progress tracking
- Function usage for output control
- Script entry points using __main__
- File system interaction with pathlib

# Possible Improvements
Future improvements may include:
- Case-insensitive searching
- Partial filename matching
- Reporting multiple matches
- Permission error handling
- Extension-only searches
- Logging instead of terminal output

# Summary
This script is a foundational exercise in Python file system operations.
It emphasizes clarity, execution flow, and understanding how Python interacts with directories and files.
