i = int(raw_input("Enter the profit"))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0

for index in range(0, 6):
    if i > arr[index]:
        r += rat[index]*(i-arr[index])
        i = arr[index]

print r