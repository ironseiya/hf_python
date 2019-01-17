from os import getcwd
import sys
import os
import datetime

where_am_I = getcwd()
print(where_am_I)


print(sys.platform)
print(sys.version)
print(os.environ)
print(os.getenv("HOME"))


print(datetime.date.today().month)
print(datetime.date.today().day)
print(datetime.date.today().year)
