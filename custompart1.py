# Custom Ride Builder

# File : ride_builder.py

# Lesson: SPCM2L1 — Nested Conditional Statements (Jr)

print("====================================")

print(" Welcome to Ride Builder! ")

print("====================================")

print()

print("Step 1: Pick your vehicle")

print(" 1 - Bike")

print(" 2 - Car")

print()

choice = int(input("Enter 1 or 2: "))

print()
if choice == 1:
     print("step 2: pick your bike type")
     print("  1 - scooty")
     print("  2 - mountain bike")
     print()

     bike_type = int(input("entre 1 or 2:"))
     print()

     if bike_type == 1:
          print("You picked  : Scooty")
          print("Top speed   : 80 km/h")
          print("Best for    : City roads")
     else:
        print("You picked  : Mountain Bike")
        print("Top speed   : 40 km/h")
        print("Best for    : Off-road trails")
elif choice == 2:
     print("step 2: pick your car type")
     print("  1 - sedan")
     print("  2 - suv")
     print()

     car_type = int(input("entre 1 or 2:"))
     print()

     if car_type == 1:
          print("You picked  : sedan")
          print("seats   : 5 passangers")
          print("Best for    : family trips")
     else:
        print("You picked  : suv")
        print("seats   : 7 passangers")
        print("Best for    : Off-road adventures")
else:
    print("this is not valied")
    
