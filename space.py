print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = int(input("Enter your weight in lbs. "))
planet = int(input("Select a planet by its number "))

# Write an if statement below:
if planet == 1:    # Venus - Gravity 0.91
    weight *= 0.91
    print("Your weight on Venus would be", str(weight), "lbs.")

elif planet == 2:  # Mars - Gravity 0.38
    weight *= 0.38
    print("Your weight on Mars would be", str(weight), "lbs.")

elif planet == 3:  # Jupiter - Gravity 2.34
    weight *= 2.34
    print("Your weight on Jupiter would be", str(weight), "lbs.")

elif planet == 4:  # Saturn - Gravity 1.06
    weight *= 1.06
    print("Your weight on Saturn would be", str(weight), "lbs.")

elif planet == 5:  # Uranus - Gravity 0.92
    weight *= 0.92
    print("Your weight on Uranus would be", str(weight), "lbs.")

else:              # Neptune - Gravity 1.19
    weight *= 1.19
    print("Your weight on Neptune would be", str(weight), "lbs.")
