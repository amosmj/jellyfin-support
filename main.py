import logging
import os

import paramiko

my_log = logging.getLogger('jellyfin-support')
logging.basicConfig(filename='jellyfin-support.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_me(passing_function):
    def logger(*args, **kwargs):
        my_log.info(f"Running function: {passing_function.__name__}")
        passing_function()
        my_log.info(f"Completed function: {passing_function.__name__}")
        return passing_function(*args, **kwargs)
    return logger

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

    my_log.info("main.py ended")