from deepzone.application_context import AppContext

import sys, os
import subprocess
import platform
# import psutil
# import logging

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))
    print(application_path)

# def _elevate():
#     """Elevate user permissions if needed"""
#     if platform.system() == 'Darwin':
#         try:
#             os.setuid(0)
#         except OSError:
#             _mac_elevate()
#
# def _mac_elevate():
#     """Relaunch asking for root privileges."""
#     print("Relaunching with root permissions")
#     applescript = ('do shell script "open '+ sys.executable +'"'
#                    'with administrator privileges')
#     exit_code_1 = subprocess.call(['osascript', '-e', applescript])
#     sys.exit(exit_code_1)

def _elevate():
    """Elevate user permissions if needed"""
    if os.getuid() != 0:
        _mac_elevate()
    else:
        pass

def _mac_elevate():
    """Relaunch asking for root privileges."""
    print("Relaunching with root permissions")
    applescript = ('do shell script "python '+application_path+'/main.py"'
                   'with administrator privileges')
    # applescript = ('do shell script "python ~/Dropbox/Python/NoDistraction/Diet2/src/main/python/deepzone/main.py"'
    #                'with administrator privileges')
    exit_code_1 = subprocess.call(['osascript', '-e', applescript])
    sys.exit(exit_code_1)


if __name__ == '__main__':
    _elevate()
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
