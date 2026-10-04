tasks=[]
try:
    file=open("tasks.txt","r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except:
    print("Creating a new to-do list")
while True:
    print("/n1-View 2-Add 3-Delete 4-exit")
    choice=input("enter your choice:")

    if choice=="1":
        if len(tasks)==0:
            print("No tasks yet")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choice=="2":
        new_task=input("Enter new task")
        tasks.append(new_task)
        file=open("tasks.txt", "w")
        for t in tasks:
            file.write(t + "\n")
        file.close()
        print("Task saved!")
    elif choice=="3":
        num=int(input("Enter task number to delete:"))
        tasks.pop(num-1)
        file=open("tasks.txt","w")
        for t in tasks:
            file.write(t + "\n")
        file.close()
        print("Task completed")

    elif choice=="4":
        print("Bye!")
        break
