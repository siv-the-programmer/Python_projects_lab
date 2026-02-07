import os
from pathlib import Path

# Main function
def main():
    # path = Path to look in.
    path = Path("ENTER_YOUR_PATH_TO_LOOK_IN")
    # Ask to enter the file name
    print("Enter a filename and the extension, eg: .txt or .docx")
    # targetpath = name of the file
    targetpath = input(">: ")
    
    # Number of files checked
    checked = 0
    
    # Visual output vibe i got going here
    def output():
        os.system("clear")
        print(f"Found: ***{targetpath}***")
        print()
        print(f"file found in {item.resolve()}")
        print()
        print(f"{checked} files scanned")
        
        # This function is the loader or amount of files i went through so far
    def check():
        print(f"checked: {checked} items Nothing found yet")
  
    # Loop through the path and scan everything
    for item in path.rglob("*"):
        
        # increase the counter by 1 
        checked += 1
        
        # Every scan of 1000 items will print the amount being scanned
        # Think of it like a loading screen
        if checked % 1000 == 0:
            check()
            
        # if the file extension name matches the name given then call the output function
        if item.name == targetpath:
            output()
            return
        
        
    else:
        print("file not found")
    
    
    
    
    
    
if __name__ == "__main__":
    main()
