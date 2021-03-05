import win32api, win32gui, win32process, win32con
from time import sleep

class ClientController:

    def __init__(self, base_res=(1280,720) ):
        self._base_resolution = base_res
        self._minified_resolution = (600, 400)
    
    def _enum_callback(self, hwnd, args):
        if win32gui.GetWindowText(hwnd) == 'Overwatch':
            win32gui.SetWindowPos(hwnd, None, )

    def resize(self, new_resolution=(1024, 768)):
        windows = []
        



def callback(hwnd, args):
    # win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    if win32gui.GetWindowText(hwnd) == 'Overwatch':
        win32gui.SetWindowPos(hwnd, None, 0, 0, 1920, 1080, 0)
        exit()

windows = []
foreground = win32gui.GetForegroundWindow()
win32gui.EnumWindows(callback, 'Overwatch')
