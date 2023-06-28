# Algorithm / Intuition
# Keeping count of values

# Intuition: Since in this case there are only 3 distinct values in the array so it’s easy to maintain the count of all, 
# Like the count of 0, 1, and 2. 
# This can be followed by overwriting the array based on the frequency(count) of the values.

# Approach: 

# Take 3 variables to maintain the count of 0, 1 and 2.
# Travel the array once and increment the corresponding counting variables



a = [1, 2, 0, 0, 1, 2, 0, 0, 1, 0, 0]
m = []  # List to store the modified array

d = a.count(0)  # Count of zeros in the array
d1 = a.count(1)  # Count of ones in the array
d2 = a.count(2)  # Count of twos in the array

# Add zeros to the modified array
for i in range(0, d):
    m.append(0)

# Add ones to the modified array
for i in range(d, d + d1):
    m.append(1)

# Add twos to the modified array
for i in range(d + d1, len(a)):
    m.append(2)

print(m)
