#countdown_timer
import time
def countdown_timer(seconds):
    while seconds > 0 :
        mins , sec = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins , sec)
        print(time_format, end = '\r')
        time.sleep(1)
        seconds -= 1
    print("00:00\n times up!")

total_seconds = int(input("Enter time in second for countdown: "))
countdown_timer(total_seconds)        