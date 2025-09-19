import time

curr_time=int(time.strftime("%H"))

if 5<=curr_time<=11:
    print("Good Morning")
elif 12<=curr_time<=4:
    print("Good Afternoon")
elif 5<=curr_time<=7:
    print("Good Evening")
else:
    print("Good Night")