import socket

def client_main():
 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 8080))
 
    f = float(input("Enter temperature in F(Fahrenheit): "))

    client_socket.send(str(f).encode())
 
    c = client_socket.recv(1024).decode()

    print(f"The temperature in C(Celcius): {c}")
    # Close the client socket
    client_socket.close()

if __name__ == '__main__':
    client_main()