# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
filename=input("Enter filename to access:")
filenameout=filename.replace(".csv","")+"_out.csv"

with open(filename) as file, open(filenameout,"w") as outfile:
    next(file)

    for line in file:
        line=line.strip()
        if not line:
            continue
        studentarray=line.split(",")
        student_id=studentarray[0]
        studentarray=studentarray[1:]
        gradeslist=[float(i) for i in studentarray if i.strip()!=""]
        
        if not gradeslist:
            continue
        mean=(sum(gradeslist)/len(gradeslist))

        if mean>=70:
            grade="1"
        elif mean>=60:
            grade="2:1"
        elif mean>=50:
            grade="2:2"
        elif mean>=40:
            grade="3"
        else:
            grade="F"
        string=f"{student_id},{mean:.2f},{grade}"
        outfile.write(string+"\n")
        


# open the file

# read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder