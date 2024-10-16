# imports
import os
import json
import time

DATA_DIR='./Data_Collected/'


def does_file_exist(filename:str):
    
    dir_list = os.listdir(DATA_DIR)

    for f in dir_list:
        if f == filename:
            return True
    
    return False

def gen_new_filename(x):
    
    filename = x

    if not does_file_exist(filename + "0.json"):
        return filename + "0.json"
    
    else:
        for i in range(100):
            i += 1
            if not does_file_exist(filename + str(i) + ".json"):
                return filename + str(i) + ".json"
    return False

