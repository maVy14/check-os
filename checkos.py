import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows',
        'termux' : 'termux'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

if sys.platform == 'win32':
    print("Window")
else: 
    print("none")