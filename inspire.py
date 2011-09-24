

from datetime import datetime

 
time = datetime.now();


print time;

"""
# windows

import urllib2

urlStr = 'http://www.python.org/'
try:
  fileHandle = urllib2.urlopen(urlStr)
  str1 = fileHandle.read()
  fileHandle.close()
  print '-'*50
  print 'HTML code of URL =', urlStr
  print '-'*50
except IOError:
  print 'Cannot <strong class="highlight">open</strong> URL %s for reading' % urlStr
  str1 = 'error!'
  
print str1
"""

from win32com.client import Dispatch
ie = Dispatch("InternetExplorer.Application")

ie.Visible = 1 
ie.Navigate('http://www.youtube.com/watch?v=JLhe5rnoLnU&feature=related')
"""
if ie.Busy:
    sleep(2)

hrefs = []


for link in ie.Document.links:
   print link.href
"""

#ie.Quit()
#lambo


import pyHook
import pythoncom

def onclick(event):
    print event.Position
    return True

hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()


