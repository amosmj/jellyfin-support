import logging
import os

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

def make_list_of_dirs(dir: str):
    raise NotImplementedError

def make_list_of_files(list_of_dirs: list[str]):
    raise NotImplementedError

def mofify_string_with_pattern(string_in: str, substring_to_mod: str, mod_to: str ):
    raise NotImplementedError

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        logging.info(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        logging.error(f"Error: The file {old_name} does not exist.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    return True


if __name__ =="__main__":
    my_log.info("main.py started")
    root_folder = have_user_designate_folder()
    my_log.info("main.py ended")