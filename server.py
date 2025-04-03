import socket 
import threading
# Create a socket object 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
file = open("result.txt","w")

# Bind to an address and port 
server_socket.bind(('localhost', 8000)) 
server_socket.listen(4) 
def listen_client(conn,player) :
    while True :
        try :
            message = conn.recv(1024).decode()
            if not message :
                break
            print(message)
        except:
            print("error")

print("Server is listening...") 
player = []
while len(player) < 2 : 
    conn, addr = server_socket.accept() 
    player.append(conn)
    if len(player) == 2 :
        player[1].sendall("the two playe connected".encode())
        threading.Thread(target=listen_client, args=(conn,player))


print("the two playe connected")



# Close the connection 
conn.close() 
server_socket.close() 