#%%
# imports
import os
import copy
import json
import psychopy
import time

from psychopy import gui



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
    
    with open(fname) as f:
        data_to_write = json.load(f)

    data_to_write["Responses"][b]["Key/Reponse time"].append([col_data])

    with open(fname, "w") as f:
        json.dump(data_to_write, f, indent=2)

#%%
fname = open('Experiment_setup.json')

exp_setup = json.load(fname)

print(exp_setup)
for i in exp_setup:
    print(i)
    
fname.close

'''myDlg = gui.Dlg(title="Experiment Setup")
myDlg.addField(label='Would you like to create a new experiment?: ', choices=['yes','no'])

while ok_data[0] == 'yes':
    myDlg = gui.Dlg(title="Experiment Setup")
    myDlg.addField(label='Number of blocks: ')
    myDlg.addField(label='Amount of time stimuli is on screen: ')
    myDlg.addField(label='Amount of time between stimuli: ')
    myDlg.addField(label='Quit key:')
    ok_data = myDlg.show()
    
print(ok_data)'''
# %%
