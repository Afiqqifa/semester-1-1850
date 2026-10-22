
# PGM functions that we write

def readPGM( filename ):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''

    with open(filename,"r") as f:    # read in the file
        data = f.readlines()
        
    data = [line.strip().split() for line in data[1:]] # clean the space-separated data, skip the first line
          
    width = int(data[0][0]) # store the data - compare to the text in the file
    height = int(data[0][1])
    max_gray = int(data[1][0])
    pixels = [[int(data[2+i][j]) for j in range(width)] for i in range(height)] # nested list comprehension for pixel array
    
    return width,height,max_gray,pixels   # tuple of PGM data
    
def writePGM( filename, image ):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # open a file for writing
    with open(filename,"w") as f:
        f.write("P2\n")  # write the PGM code
        f.write(f"{width} {height}\n")  # write the width and height
        f.write(f"{max_gray}\n")  # write the max gray value

        # write the pixel data
        for row in pixels:
            f.write(" ".join(str(pixel) for pixel in row) + "\n")  # join pixel values with space and write to file
    # write the data in PGM format
    # don't forget the PGM code "P2"

    return

def invertPGM( image ):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # your code
    # create a new pixel array of inverted data 
    inverted = []  # you can use a similar nested comprehension to the readPGM() function
    inverted = [[max_gray - pixel for pixel in row] for row in pixels]  # nested list comprehension to invert pixel values
    
    
    return width,height,max_gray,inverted

# code to test the PGM functions

image = readPGM("/workspaces/semester-1-1850/week1.4/session2/tasks/task4/images/feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(f"{image[3]}")
print(invertPGM(image))

# write further code to test your own functions
