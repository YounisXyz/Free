import os, sys
os.system("git pull")
try:
    __import__("Berlin").BERLIN()
except Exception as e:
    exit(str(e))
