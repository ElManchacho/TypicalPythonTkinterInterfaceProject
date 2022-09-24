import os, pathlib, shutil

def flushLogs()->None:

    logsDirs = [name for name in os.listdir(".") if os.path.isdir(name)]

    logsFolderPath = str(pathlib.Path(__file__).parent.resolve())

    for folder in logsDirs:
        path = logsFolderPath+'\\'+folder
        shutil.rmtree(path)
        os.mkdir(path)


flushLogs()