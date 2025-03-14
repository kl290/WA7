print("PingPong!")
for i in range(1, 101):
    output = str(i)
    if i % 3 == 0 and i % 5 == 0:
        output += " PingPong"
    elif i % 3 == 0:
        output += " Ping"
    elif i % 5 == 0:
        output += " Pong"
    print(output)
