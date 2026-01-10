#DAILY STEPS OF 3 FRIENDS OVER A WEEK
import numpy as np

data = [
    [5200, 5700, 6100, 3600, 4500, 7500, 8000], #Madison
    [2400, 6800, 6000, 4700, 5600, 8100, 5600], #Isabel
    [8500, 5900, 3600, 3300, 5700, 5800, 5800]  #Annlynn
    ]
    
#Main Program

print("Madison's data for the last day:", data[0][6])

data[1][0] = 3000
print("Isabel's updated data for the first day:", data[1][0])

arr = np.array(data)
print(arr.mean())
