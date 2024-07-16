n = "Start"
m = "Stop"
o = "Quit"
count = 1
count1 = 2
start_level = 0
while count < count1:
    a = input(">")
    if a == "help":
        print("Start : To start the car.\nStop  : To stop the car.\nQuit  : To exit.")
    elif a == n and start_level == 0:
        print("Ready to Go...")
        start_level += 1
    elif start_level > 0 and a == n:
        print("Car is already started..")
    elif a == m:
        print("Car stopped.")
        start_level -= 1
    elif a != "help" and a != n and a != m and a != o:
        print("I don not understand...")
    elif a == o:
        break
