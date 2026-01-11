#DAILY STEPS OF 3 FRIENDS OVER A WEEK
import numpy as np

names = ["Madison", "Isabel", "Annlynn"]
data = [
    [5200, 5700, 6100, 3600, 4500, 7500, 8000], 
    [2400, 6800, 6000, 4700, 5600, 8100, 5600], 
    [8500, 5900, 3600, 3300, 5700, 5800, 5800]  
    ]
    
#Main Program

#Total steps for each person
def totalsteps():
    print("TOTAL STEPS FOR EACH PERSON OVER A WEEK:")
    for i in range(len(data)):
        print(f"{names[i]}'s total steps: {sum(data[i])} steps")
        
def maxmindifference_data():
    print("\nMAXIMUM, MINIMUM, AND DIFFERENCE OF STEPS:")
    totals = np.array([np.sum(person) for person in data])
    print(f"Highest total steps: {names[totals.argmax()]} - {totals.max()} steps")
    print(f"Lowest total steps: {names[totals.argmin()]} - {totals.min()} steps")
    print(f"Difference: {totals.max() - totals.min()} steps")


totalsteps()
maxmindifference_data()