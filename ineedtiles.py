# this program calulates how many tiles I need
# when tilling a wall or floor (in m2)

length = float (input ("Enter room length"))

width = float (input ("Enter room width"))

# length = 4.0
# width = 2.0

area = length * width

needed = area * 1.05

print("You need", needed, "tiles metres squared.")

