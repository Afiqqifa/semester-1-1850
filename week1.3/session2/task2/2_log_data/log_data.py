# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.
with open("site.txt","r") as file:
    header=file.readline()
    for line in file:
        parts=line.strip().split(",")
        if len(parts)>=6:
            date=parts[0]
            time=parts[1]
            ip=parts[2]
            useragent=parts[3]
            request=parts[4]
            code=parts[5]
            if code=="401" and request=="POST /login":
                print(f"IP address {ip} failed to login at {time} on {date}")




# open and read the file

# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20


# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data