import re

time_vtk = re.compile('время|time')

def check(message):
    if time_vtk.match(message):
        return True
    else:
        return False
