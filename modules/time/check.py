import re

time_vtk = re.compile('время|time')

def check(message):
    if time_vtk.match(message.lower()):
        return True
    else:
        return False
