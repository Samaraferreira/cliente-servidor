import socket

def server():
  host = socket.gethostname()
  port = 5012

  server_socket = socket.socket()
  server_socket.bind((host, port))

  server_socket.listen(2)
  conn, address = server_socket.accept()

  print("--- Chat --- ")

  while True:

    message = conn.recv(1024).decode()
    if not message:
      break

    print("[cliente]: " + str(message))

    if "oi" in str(message): 
      message = 'Olá! O que deseja?'
      print(" -> " + message)
    elif "cardapio" in str(message): 
      message = 'Nosso cardápio:  1 - Pizza de Mussarela [R$ 24]     2 - Pizza de calabresa [R$ 28]'
      print(" -> " + message)
    elif "pedido" in str(message): 
      message = 'Faça seu pedido no link -> restaurante.com'
      print(" -> " + message)
    else:
      message = input(" -> ")
    conn.send(message.encode()) 

  conn.close()

if __name__ == '__main__':
  server()