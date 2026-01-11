#DAILY STEPS OF 3 FRIENDS OVER A WEEK
import numpy as np

data = [
    [5200, 5700, 6100, 3600, 4500, 7500, 8000], 
    [2400, 6800, 6000, 4700, 5600, 8100, 5600], 
    [8500, 5900, 3600, 3300, 5700, 5800, 5800]  
    ]
    
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


#MAIN PROGRAM
arr = np.array(data)

#Total steps per day
daily_total = arr.sum(0)

for i in range(len(days)):
    print(f"{days[i]}: {daily_total[i]} steps")

#Most active day
max_day = daily_total.argmax()
print("\nMost active day:", days[max_day])