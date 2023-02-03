# from AppOpener import open
# from datetime import datetime
# myobj = datetime.now()
# print(myobj.hour)
# if myobj.hour == 17:
#     open("microsoft edge")


import webbrowser

import time

link = input ("zoomlink")

alarm = input("17:06:20")
 
Current_time = time.strftime("%H:%M:%S") 
  
while (Current_time != alarm):
    
    print ("Waiting, the current time is " + Current_time  )
    
    Current_time = time.strftime("%H:%M:%S")
    
    time.sleep(1)
    
if (Current_time == alarm):
    
    print ("Starting Lecture")
    
    webbrowser.open('zoomlink')