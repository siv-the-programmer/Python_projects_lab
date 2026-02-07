import os
from pathlib import Path
while True:
# Main function
    def main():
        print("BRUTE FILE FINDER")
        print("-----------")
        # path = Path to look in.
        path = Path("C:\\Users\\sivar\\OneDrive")
        # Ask to enter the file name
        print("Press exit to leave")
        print("Press cls to clear the screen")
        print()
        print("Enter a filename and the extension, eg: .txt or .docx")
        
        
        # targetpath = name of the file
        targetpath = input("Search>>: ")
        
        # Number of files checked
        checked = 0
        

        # Visual output vibe i got going here
        
        def output():
            print()
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
            
            # If i type exit it exits the program
            if targetpath == "exit":
                exit()
            
            # Every scan of 1000 items will print the amount being scanned
            # Think of it like a loading screen
            if checked % 1000 == 0:
                check()
                
            # if the file extension name matches the name given then call the output function
            if item.name == targetpath:
                output()
                return
            
            # If i type exit it exits the program
            if targetpath.lower() == "exit":
                print("exiting...")
                return
            
            # what I type does not have an extension || it will not search but allow you to type again
            if "." not in targetpath or targetpath.startswith(".") or targetpath.endswith("."):
                print("Please enter a valid file name with extension")
                os.system("cls")
                return main()
            if targetpath == "cls":
                os.system("cls")
                
                    
                
                
        else:
            print("file not found")
            
        
        

    if __name__ == "__main__":
        main()