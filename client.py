import socket

def client():
  host = socket.gethostname()
  port = 5012

  client_socket = socket.socket()
  client_socket.connect((host, port))

  print("--- Chat --- ")
  message = input(" -> ")

  while message.lower().strip() != 'sair':
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()

    print('[restaurante]: ' + data)
    message = input(" -> ")

  client_socket.close()

if __name__ == '__main__':
  client()