from win10toast import ToastNotifier
import time

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time =="11:39:00":
        print(current_time)
        break
    else:
        pass

hr = ToastNotifier()
hr.show_toast('Time',f'Current time is {current_time}')