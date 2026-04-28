from socket import *

serverName = 'LAPTOP-VVT5CIDS'
serverPort = 13999

clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
    print("Terhubung ke server")
    
    sentence = input('Ketik kalimat: ')
    clientSocket.send(sentence.encode())
    
    modifiedSentence = clientSocket.recv(1024)
    print('Response dari server:', modifiedSentence.decode())
    
finally:
    clientSocket.close()
    print("Koneksi ditutup")