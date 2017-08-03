import os
def rename_files():
        #(1) get file names from folder
        file_list = os.listdir(r"C:\Users\shahid\Downloads\Compressed\prank")
        #print(file_list)
        save_path = os.getcwd()
        print("Current Working Directory is"+save_path)
        os.chdir(r"C:\Users\shahid\Downloads\Compressed\prank")
        
        
        #(2) Rename each file name with removig numbers.
        for file_name in file_list:
            os.rename(file_name, file_name.translate(None, "0123456789"))
        os.chdir(save_path)
rename_files()
        
        
