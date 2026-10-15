# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
try:
    with open("/workspaces/semester-1-1850/week1.3/session2/task4/images/feep.pgm","r") as file:
        lines=file.readlines()
        dimensions=lines[1].strip()
        maxgrayvalue=lines[2].strip()

        print(f"Dimensions:{dimensions}")
        print(f"Max Gray Value:{maxgrayvalue}")
except FileNotFoundError:
    print("Error file not found")


# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)