import re

weather_vtk = re.compile('погода')

def check(message):
    if weather_vtk.match(message.lower()):
        return True
    else:
        return False
