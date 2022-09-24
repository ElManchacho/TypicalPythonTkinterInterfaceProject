import pathlib, os, shutil

def cacheFlushGame():
    path = str(pathlib.Path(__file__).parent.resolve())
    if os.path.isdir(path+"\__pycache__"):

        shutil.rmtree(path+"\__pycache__")