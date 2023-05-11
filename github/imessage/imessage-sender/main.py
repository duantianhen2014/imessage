#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Author: Chhaileng Peng <hello@chhaileng.com>
# GitHub: @chhaileng

import datetime
import sys
import os
import time

if len(sys.argv) < 2:
    print("""Usage: python3 main.py \"phone/email\"""")
    print("""   Example: python3 main.py \"imsg@icloud.com\"""")
    exit(5)

to = sys.argv[1]

#to = "phone/email" 
msg = "Hi! I'm Send By Python Time:" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for i in range(5):
  print("Sending '" + msg + "' ...")
  os.system('osascript scripts/sendiMessage.scpt "' + to + '" "' + msg + '"')
  time.sleep(0.5)
