# Write to a file
with open("maths.txt", "w") as f:
    f.write("Week 4")
print("Wrote 'Week 4' to maths.txt")

# Reading math.txt
try:
    with open("math.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: 'math.txt' not found.")
 
