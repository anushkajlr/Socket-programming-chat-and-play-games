
import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8000

new_socket.bind(("", port))
print("Binding successful!")
print("This is your IP: ", s_ip)

name = input('Enter name: ')

new_socket.listen(1)

conn, add = new_socket.accept()

print("Received connection from ", add[0])
print('Connection Established. Connected From: ', add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')
def game():
    server_score = 0
    client_score = 0
    tie = 0
    m = "how many points"
    conn.send(m.encode())  
    m = conn.recv(1024)
    flag = int(m)
    run = True
    while run:
        choice = input('Me : ')
        message = name +" has played enter your choice"
        conn.send(message.encode())
        oppchoice = conn.recv(1024)
        oppchoice = oppchoice.decode()
        if (oppchoice.lower() == "stone"):
            if(choice == "stone"):
                message = "#it is a tie"
                conn.send(message.encode())
                tie+=1
            elif choice == "paper":
                message = "#server has won"
                conn.send(message.encode())
                server_score+=1
            else:
                message = "#client has won"
                conn.send(message.encode())
                client_score+=1

        elif (oppchoice.lower() == "paper"):
            if(choice == "stone"):
                message = "#client has won"
                conn.send(message.encode())
                client_score+=1
            elif choice == "#paper":
                message = "#it is a tie"
                conn.send(message.encode())
                tie+=1

            else:
                message = "#server has won"
                conn.send(message.encode())
                server_score+=1
        elif oppchoice.lower() == "scissors":
            if(choice == "stone"):
                message = "#server has won"
                conn.send(message.encode())
                server_score+=1

            elif choice == "paper":
                message = "#client has won"
                conn.send(message.encode())
                client_score+=1

            else:
                message = "#it is a tie"
                conn.send(message.encode())
                tie+=1


        if(server_score == flag or client_score == flag):
            run = False
            m = "score card"
            conn.send(m.encode())  


    #scorecard file transfer
    # We can send file sample.txt
    file = open("score.txt", "wb")
    data = "client score is "+str(client_score)+"\nserver score is "+str(server_score)
    if(client_score>server_score):
        win = "CLIENT HAS WON\n"
    elif(client_score<server_score):
        win = "SERVER HAS WON\n"
    else:
        win = "IT IS A TIE"
    data = "HERE IS YOUR SCORECARD\n"+win+data
    data = data.encode()
    file.write(data)
    file.close()
    file = open("score.txt", "rb")
    SendData = file.read(1)


    while SendData:
        #print("Sending data to client...")
        #Now send the content of score.txt to client
        conn.send(SendData)
        SendData = file.read(1)      

    conn.send("#".encode())


conn.send(name.encode())
run = False
m = "do you want to play games or chat enter \'yes\' to play games and \'no\' to chat"
conn.send(m.encode())
m = conn.recv(1024)
m = m.decode()
if m.lower() =="yes":
    m = "playing_game"
    conn.send(m.encode())   
    game()
    

else:
    m = "ok we wont play"
    conn.send(m.encode())
    run2 = True
    while run2:
        message = conn.recv(1024)
        message = message.decode()
        if(message == "end chat"):
            run2 = False
        if(run2!=False):
            print(client, ":", message)
            message = input("Me:")
            if(message == "end chat"):
                run2 = False
            conn.send(message.encode())
        


