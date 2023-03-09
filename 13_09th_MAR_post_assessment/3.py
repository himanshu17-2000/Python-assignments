import os 
import argparse
import sys

#Run the Sccript to see the Folder Structure 
def create_folder_struture(args):
    arr = ['src' , 'db' , 'models' , 'config' ,'routes']
    try:
        for i in arr: 
            os.makedirs(f"./{args.name}/{i}")
        file = open(f"./{args.name}/app.py" , "a")
        
    except FileExistsError :
        print('file already exists , delete and run again  or use different name')
if __name__ == "__main__" :

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default="Folder",
                        help="Enter first number. This is a utility for calculation. Please contact harry bhai")
    args = parser.parse_args()
    create_folder_struture(args)