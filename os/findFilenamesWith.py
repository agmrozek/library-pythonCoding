import os

def search_bgp_files():
    cwd = os.getcwd() 
    for filename in os.listdir(cwd): 
        if "bgp" in filename.lower(): 
            print(os.path.join(cwd, filename)) 

