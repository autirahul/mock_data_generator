import os

def read_json_file_as_string(file_path:str):
    with open(file_path) as f:
        return f.read()
    
def make_path_if_not_exists(file_path:str):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
   