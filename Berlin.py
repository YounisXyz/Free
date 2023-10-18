import os,platform
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
os.system('git pull')
xyz=platform.architecture()[0]
if xyz=="32bit":
    print('\033[1;91mSorry Your Device Is 32bit,This Tool Is Only For 64bit, Please Upgrade Your Phone ....')
elif xyz=="64bit":
    __import__("Berlin")
 
