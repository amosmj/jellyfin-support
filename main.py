import logging
import os
import pathlib
import paramiko
import tkinter as tk
from tkinter import filedialog

my_log = logging.getLogger('jellyfin-support')
logging.basicConfig(filename='jellyfin-support.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_me(passing_function):
    def logger(*args, **kwargs):
        my_log.info(f"Running function: {passing_function.__name__}")
        result = passing_function(*args, **kwargs)
        my_log.info(f"Completed function: {passing_function.__name__}")
        return result
    return logger

@log_me
def have_user_designate_folder()-> str:
    # root = tk.Tk()
    # root.withdraw()
    dirname = filedialog.askdirectory()
    my_log.info(f"Directory was selected as {dirname}")
    return dirname



def make_list_of_files(list_of_dirs: list[str]):
    raise NotImplementedError

def mofify_string_with_pattern(string_in: str, substring_to_mod: str, mod_to: str ):
    raise NotImplementedError

def regroup_files_in_folders(out_dir: str, list_of_in_dir: list[str]):
    raise NotImplementedError

def simple_string_replacement(substring_to_replace: str, replace_with: str, list_of_files: list[str], error_when_not_found= False)->list[str]:
    SUBSTRING_NOT_FOUND = -1
    list_of_files_out = []
    for file in list_of_files:
        if file.find(substring_to_replace) != SUBSTRING_NOT_FOUND:
            file.replace(substring_to_replace,replace_with)
        else:
            if error_when_not_found:
                message = (f"The substring {substring_to_replace} was not found in {file}. Per your request, an error has occurred")
                raise ValueError
        list_of_files_out.append(file)
    return list_of_files_out
                

def rename_mp4_files_to_match_directories_and_clean_up_mkv(file_type: str = ""):
    dir_list = []
    while len(dir_list) < 1:
        root_path = have_user_designate_folder()
        root_dir = pathlib.Path(root_path)
        if root_dir.is_dir():
            dir_list.append(root_dir)
        else:
            print("It doesn't look like you selected a directory. Please do so")
    ## Look in directory for files and directories
    while len(dir_list) > 0:
        file_list = []
        working_obj = dir_list[0]
        ## need to get the final directory name here for renaming
        working_obj_parts = working_obj.split('/')
        name_to_substitute_in = working_obj_parts[-1:]
        for obj in working_obj.iterdir():
            if obj.is_dir():
                dir_list.append(obj)
            else: # not a directory. Probably file, see if it's target file type
                file_type_len = len(file_type) * -1
                if file_type == obj[file_type_len: ]: # compare to see if it's the filetype we want. Passing an empty string will rename all file types
                    file_list.append(obj)
        ## Now test for multiple files because we can't rename them all to the same thing
        if len(file_list) == 1:
            os.rename(working_obj, working_obj_parts[:-1]+"/"+name_to_substitute_in)
        else:
            ## print and keep moving
            print(f"You are attempting to rename files but there are multiple files at {working_obj} that you tried to give the same name. Clean up the files and try again.")
        ## clean up our working object from the list and go back to the top of the loop
        dir_list.remove(working_obj)

if __name__ =="__main__":
    my_log.info("main.py started")
    root_folder = have_user_designate_folder()
    my_log.info("main.py ended")