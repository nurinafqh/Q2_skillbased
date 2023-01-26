import socket

def f_to_c(f):
    c = (f - 32) * (5/9)
    return c

def server_main():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("\nSocket has been created")
    
    
    server_socket.bind(('localhost', 8080))
    print("\nSocket is binded to", 8080)
    
    
    server_socket.listen()
    
    print("waiting for connections")
    
    (client_connect, client_address) = server_socket.accept()
    
    while True:
        print(f"Connection from {client_address} has been established.")
        
        data = client_connect.recv(1024)
        
        c = f_to_c(float(data.decode()))
        
        client_connect.send(str(c).encode())
        
        client_connect.close()

if __name__ == '__main__':
    server_main()