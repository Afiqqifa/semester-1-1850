# Week 1.2, Session 2: Task 6
print("Update status of the machine")

temp=int(input("Machine's temperature: "))
psi=int(input("Machine's pressure: "))
opstatus=int(input("Machine's operational status (1 for operating and 0 if not): "))

action1=False
action2=False

if temp>80:
    action1=True
    print("Machine's temperature too high")
elif 50<=temp<=80:
    print("Machine's temperature is within safe limits")
else:
    print("Machine's temperature is low")

if psi>100:
    action2=True
    print("Machine's pressure is high")
elif 70<=psi<=100:
    print("Machine's pressure is stable")
else:
    print("Machine's pressure is low") 

if opstatus==1:
    if action1==True and action2==True:
        print("Machine's temperature and pressure is high, it is recommended to turn off and undergo maintenance")
        status=f"Temp:{temp},PSI:{psi},Opstatus:{opstatus},action:it is recommended to turn off and undergo maintenance\n"
    elif action1==True and action2==False:
        print("Machine's temperature is high, it is recommended to turn off")
        status=f"Temp:{temp},PSI:{psi},Opstatus:{opstatus},action:it is recommended to turn off\n"
    elif action1==False and action2==True:
        print("Machine's pressure is high, it is recommended to turn off and undergo maintenance")
        status=f"Temp:{temp},PSI:{psi},Opstatus:{opstatus},action:it is recommended to turn off and undergo maintenance\n"
    else:
        print("No action needed, machines is operating normally")
        status=f"Temp:{temp},PSI:{psi},Opstatus:{opstatus},action:no action needed machine is operating normally\n"
else:
    if action2==True:
        print("No action needed, machine is not operating, undergo maintenance")
        status=f"Temp:{temp},PSI:{psi},Opstatus:{opstatus},action:no action needed machine is not operating but need to undergo maintenance\n"
    else:
        print("No action needed, machine is not operating")
        status=f"Temp:{temp},PSI:{psi},Opstatus:{opstatus},action:no action neede\n"

with open("machine_log.txt","a") as file:
    file.write(status)
