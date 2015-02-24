import re

time-vtk = re.compile('(время)+')

def check(message):
    if time-vtk.match(message):
        return True
    else:
        return False
