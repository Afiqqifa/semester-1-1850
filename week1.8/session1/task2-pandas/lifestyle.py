import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
print(type(data))

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
print(len(data))

# Find the mean average GPA of the students
sum=0
for i in data["GPA"]:
    sum+=i
avg=round(sum/(len(data)),2)
print(avg)

# Find the standard deviation of how much sleep students get per day
print(round(data["Sleep_Hours_Per_Day"].std(),3))


# Find the maximum amount of study hours per day
print(data["Study_Hours_Per_Day"].max())

# Sort the students by social hours per day ascending (lowest -> highest)
sorteddata=data.sort_values(by="Social_Hours_Per_Day",ascending=True)
print(sorteddata["Social_Hours_Per_Day"])

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data["Total_hours"]=(data["Study_Hours_Per_Day"]+data["Extracurricular_Hours_Per_Day"]+data["Sleep_Hours_Per_Day"]+data["Social_Hours_Per_Day"]+data["Physical_Activity_Hours_Per_Day"])


# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
highstress=data[data["Stress_Level"]=="High"]
lowstress=data[data["Stress_Level"]=="Low"]
# Can you work out whether having a higher stress level leads to a higher GPA?
print(data.groupby("Stress_Level")["GPA"].mean())