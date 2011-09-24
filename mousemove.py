import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(-2000,-10)


#http://timgolden.me.uk/pywin32-docs/contents.html
#http://stackoverflow.com/questions/3720938/win32-moving-mouse-with-setcursorpos-vs-mouse-event
