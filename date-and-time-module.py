#Date and Time


#date - Class
#Example - 1 [ Current date ]
'''
from datetime import date
x = date.today()
print(x)
'''
#Example - 2 [ Specifc Date ]
'''
from datetime import date
x = date(2018,8,24)
print(x) #2018-08-24
'''
#Example - 3 [ Current date ] [ Access of date ]
'''
from datetime import date
x = date.today()
print(x) #2025-12-18
print(x.year) #2025
print(x.month) #12
print(x.day) #18
'''
#Example - 4 [ Specific date ] [ Access of date ]
'''
from datetime import date
x = date(2018,8,24)
print(x) #2018-08-24
print(x.year) #2018
print(x.month) #8
print(x.day) #24
'''
#weekday() - Gets the week day of the defined date
#Example - 5 [ Get Weekday ]
'''
Monday - 0
Tuesday - 1
Wednesday - 2
Thursday - 3
Friday - 4
Saturday - 5
Sunday - 6

from datetime import date
x = date.today()
print(x.weekday()) #3
'''
#time - Class
'''
hh:mm:ss
hh - hours
mm - minutes
ss - Seconds
'''
#Example - 1 [ Specific time ]
'''
from datetime import time
x = time(10,45,34)
print(x) #10:45:34
x = time(21,34,45)
print(x) #21:34:45
y = time(12,34,67) #ValueError: second must be in 0..59
y = time(12,65,12) #ValueError: minute must be in 0..59
y = time(27,45,34) #ValueError: hour must be in 0..23
'''
#Example - 2 [ Accessing of Data ]
'''
from datetime import time
x = time(12,13,14)
print(x) #12:13:14
print(x.hour) #12
print(x.minute) #13
print(x.second) #14
'''
#datetime - Class
'''
Format -> yyyy,mm,dd,HH,MM,SS
'''
#now() - Helps to get current date and time
#Example - 1 [ Current date and Time ]
'''
from datetime import datetime
x = datetime.now()
print(x) #2025-12-18 10:03:49.068973
'''
#Example - 2 [ Specific Date and time ]
'''
from datetime import datetime
x1 = datetime(2017,8,24,22,34,56)
print(x1) #2017-08-24 22:34:56
x2 = datetime(2017,8,24)
print(x2) #2017-08-24 00:00:00
'''

#Example - 3 [ Accessing of data ]
'''
from datetime import datetime
x = datetime.now()
print(x) #2025-12-18 10:07:32.802093
print(x.date()) #2025-12-18
print(x.time()) #10:07:32.802093
print(x.year) #2025
print(x.month) #12
print(x.day) #18
print(x.hour) #10
print(x.minute) #7
print(x.second) #32
'''

#timedelta - Class
#Example - 1 [ Adding ] [datetime]
'''
from datetime import datetime
from datetime import timedelta
x = datetime.now()
print(x) #2025-12-18 10:11:14.299313
print(x + timedelta(days=2))
#OP=> 2025-12-20 10:11:14.299313
print(x + timedelta(days=30))
#OP=> 2026-01-17 10:11:14.299313
'''
#Example - 2 [ Subtraction ] [ datetime ]
'''
from datetime import datetime
from datetime import timedelta
x = datetime.now()
print(x)
#OP=> 2025-12-18 10:14:09.978096
print(x - timedelta(days=30))
#OP=> 2025-11-18 10:14:09.978096
print(x - timedelta(hours=10))
#OP=> 2025-12-18 00:14:09.978096
'''

#Example - 3 [ Addition ] [ Date ]
'''
from datetime import date
from datetime import timedelta
x = date.today()
print(x) #2025-12-18
print(x + timedelta(days=20)) #2026-01-07
print(x + timedelta(hours=24)) #2025-12-19
'''
#Example - 4 [ Subtraction ] [ Date ]
'''
from datetime import date
from datetime import timedelta
x = date.today()
print(x) #2025-12-18
print(x-timedelta(days=20)) #2025-11-28
print(x-timedelta(hours=24)) #2025-12-17
'''


#Date and Time Formatting
#Example - 1 [ Date ]
'''
from datetime import date
x = date.today()
print(x) #2025-12-18 [ yyyy-mm-dd ]
print(x.strftime("%d-%m-%Y")) #18-12-2025 [ dd-mm-yyyy ]
print(x.strftime("%d/%m/%Y")) #18/12/2025 [ dd/mm/yyyy ]
'''
#Example - 2 [ time ]
'''
from datetime import time
x = time(22,45,13)
print(x) #22:45:13 [ HH:MM:SS ]
print(x.strftime("%M-%S-%H")) #45-13-22
print(x.strftime("Hours : %H")) #Hours : 22
print(x.strftime("Minutes : %M")) #Minutes : 24
print(x.strftime("Seconds : %S")) #Seconds : 13
'''

#Example - 3 [ datetime ]
'''
from datetime import datetime
x = datetime.now()
print(x)
#OP=> 2025-12-18 10:33:00.844535 [ yyyy-mm-dd HH:MM:SS ]
print(x.strftime("%d/%m/%Y - %S:%M:%H"))
#OP=> 18/12/2025 - 59:33:10
'''

#Time Module
#Example
import time
print("Hello World")
time.sleep(3)
print("Hello Python")
