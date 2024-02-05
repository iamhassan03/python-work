from time import time

secs = time()

t_secs = int(secs)      # drop the decimal part 
second = t_secs % 60    # get the current second by rounding-off from all minutes

t_mins = t_secs // 60   # get the total minutes
minute = t_mins % 60    # get the current minute by rounding-off from all hours

t_hours = t_mins // 60    # get the total hours
hour = t_hours % 24         # get the current hour by rounding-off from all days

offset_hours = int(input("Enter offset hours: ").strip())
hour += offset_hours

if hour < 0:
    hour +=24

elif hour > 24:
    hour -= 24

print(f"Curent Time with {offset_hours:+d} offset hours is: {hour}:{minute}:{second} GMT")

