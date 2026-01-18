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
                

def rename_mkv_files_to_match_directories(root_directory: str, file_type: str|None = None):
    dir_list = []
    while len(dir_list) < 1{}
        root_path = have_user_designate_folder()

    ## Look in directory for files and directories
    ## for files
        ## if file_type matches or file_type = None
        ## provide feedback
    ## for directories
        ##r repeat this process

    raise NotImplementedError

if __name__ =="__main__":
    my_log.info("main.py started")
    root_folder = have_user_designate_folder()
    my_log.info("main.py ended")