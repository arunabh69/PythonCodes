# Write a Python program to get the volume of a sphere with radius 10.

import math
radius = float(input('Enter radius of circle: '))
area = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius**3

print('Volume = %0.4f.' % (volume))


# Output-
# Enter radius of circle:  10
# Volume = 4188.7902.
