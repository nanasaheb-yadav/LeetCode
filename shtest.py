
import os, sys

def test():

    try:
        c= 2/0
        sys.exit(0)
    except Exception as e:
        sys.exit(e)


