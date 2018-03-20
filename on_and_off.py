import os, sys


def closeFile():
    try:
        os.close("/Applications/Safari.app")
        print("App opened successfully!")
    except:
        print("Unexpected error:", sys.exc_info()[0])


def openFile():
    try:
        fd = os.open( "/Applications/Safari.app", os.O_RDWR|os.O_CREAT )
        print("App opened successfully!")
    except:
        print("Unexpected error:", sys.exc_info()[0])
