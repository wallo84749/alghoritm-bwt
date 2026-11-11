import socket as sck
from alghoritm_BWT import BWT

IP = "127.0.0.1"
PORT = 5000

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:

    server.bind((IP, PORT))

    server.listen()

    print("Server in ascolto...")

    while True:

        conn, address = server.accept()

        with conn:

            print("Client connesso:", address)

            dati = conn.recv(1024)

            messaggio = dati.decode()

            print("Stringa ricevuta:", messaggio)

            risultato = BWT(messaggio)

            print("Risultato BWT:", risultato)

            conn.sendall(risultato.encode())

            print("Risultato inviato al client")
