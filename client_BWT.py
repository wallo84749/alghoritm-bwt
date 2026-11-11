import socket as sck

IP = "127.0.0.1"
PORT = 5000

messaggio = input("write a string for the BWT alghoritm: ")

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.connect((IP, PORT))
    print("connesione stabilita")

    client.sendall(messaggio.encode())
    dati = client.recv(1024)   #--> acneh questa autobloccante 

    print(f"risposta del server: {dati.decode()}")

print("client terminato")