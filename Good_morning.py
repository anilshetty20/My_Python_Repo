import time

curr_time= time.strftime('%H:%M:%S')
print("The current time in India is :",curr_time)
curr_hour=int(time.strftime('%H'))
if 5<=curr_hour<=11:
    print("Good Morning")
elif 12<=curr_hour<=16:
    print("Good Afternoon")
elif 17<=curr_hour<=20:
    print("Good Evening")
else:
    print("Good Night")

