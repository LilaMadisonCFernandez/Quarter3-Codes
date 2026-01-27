#DAILY STEPS OF 3 FRIENDS OVER A WEEK
import numpy as np

data = [
    [5200, 5700, 6100, 3600, 4500, 7500, 8000], 
    [2400, 6800, 6000, 4700, 5600, 8100, 5600], 
    [8500, 5900, 3600, 3300, 5700, 5800, 5800]  
    ]
    
#Main Program
def show_data():
    print("DATA:")
    for i in range(len(data)):
        print(f"Friend {i+1}: {data[i]}")
    
def total_data():
    print("\nTOTAL STEPS OF EACH FRIEND:")
    arr = np.array(data)
    for row in arr:
        print(f"{row.sum()} steps")

def average_data():
    print("\nAVERAGE STEPS OF EACH FRIEND:")
    arr = np.array(data)
    for row in arr:
        print(f"{row.mean()} steps")
        
def maxmin_data():
    print("\nMAXIMUM AND MINIMUM VALUE OF DATASET:")
    arr = np.array(data)
    print(f"Maximum value: {arr.max()}")
    print(f"Minumum value: {arr.min()}")

show_data()
total_data()
average_data()
maxmin_data()
