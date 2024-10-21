# imports
import os
import copy
import json
import time



def open_file(filename:str):
    with open(filename) as f:
        load_file = json.load(f)
    return load_file


def write_json(data, filename:str):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def json_writer(fname,a,b:str,c,col_data):
    data_dict = {
                    "Block": a,
                    "Responses":
                    {
                        b:
                        {
                            "Key/Response time": [c]
                        }
                    }
                }
    
    data_to_write = open_file(fname)

    data_to_write["Responses"][b]["Key/Reponse time"].append([col_data])

    write_json(data_to_write, fname)

    

