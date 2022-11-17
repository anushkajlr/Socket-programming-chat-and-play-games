import time, socket, sys,os
 
socket_server = socket.socket()
server_host = "127.0.1.1"
ip = socket.gethostbyname(server_host)
sport = 8000
 
#print('This is your IP address: ',ip)
#server_host = input('Enter friend\'s IP address:')
name = input('Enter your name: ')
 
 
socket_server.connect((server_host, sport))
 
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' has joined...')
run = True
game_flag = 0
playing_game = 0
while run:
    go_back = 0
    message = (socket_server.recv(1024)).decode()
    
    if(message == "score card"):
        run = False
        game_flag = 1
    
    if(message == "end chat"):
        run = False
    if(message == "playing_game"):
        playing_game = 1
    if(run!=False):
        print(server_name, ":", message)
        # if(playing_game == 2):
        #     print(server_name, ":", message)#we want to print as well
        #     message = (socket_server.recv(1024)).decode()
        #     print(server_name, ":", message)
        

        if(playing_game == 1):#to receive the score msg
            message = (socket_server.recv(1024)).decode()
            print(server_name, ":", message)
            playing_game = 0
        if(message[0] == '#'):
            go_back = 1

        if go_back ==0:
            message = input("Me : ")
            if(message == "end chat"):
                run = False
            socket_server.send(message.encode()) 

if(game_flag):
    file = open("recv.txt", "wb") 
    print("\n Copied file name will be recv.txt at client side\n")

    # Receive any data from server side
    RecvData = socket_server.recv(1)

    while RecvData:
        if(RecvData.decode()=="#"):
            break
        file.write(RecvData)
        RecvData = socket_server.recv(1)

    # Close the file opened at server side once copy is completed

    print("\n Here is your scorecard \n")
    file.close()
    os.startfile("recv.txt")
else:
    print("convo over")

