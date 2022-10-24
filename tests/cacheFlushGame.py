import pathlib, os, shutil

def cacheFlushGame()->bool:
    removed = False
    path = str(pathlib.Path(__file__).parent.resolve())
    if os.path.isdir(path+"\\__pycache__"):

        shutil.rmtree(path+"\\__pycache__")

        removed = True

    return removed