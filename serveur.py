import socket

if __name__ == '__main__':
    # Etablissement d'une connexion UDP : socket(), bind()
    socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_udp.bind(("0.0.0.0", 5005))
    
    # Etablissement d'une connexion TCP : socket(), bind(), listen(), accept()
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp.bind(("0.0.0.0", 8888))
    socket_tcp.listen(1)
    conn_tcp, addr = socket_tcp.accept()

    # Partie applicative:

    # Envoi d'un message TCP :
    conn_tcp.send(b"a")
    
    # Attente d'un message UDP a la reception du message sur can1
    data = socket_udp.recv(1024)
    print("Donnee recue :", data.decode()) # Compteur = 1

    # Attente du message TCP :
    data = conn_tcp.recv(1024)
    print("Donnee recue :", data.decode())
    
    # Envoi d'un message TCP :
    conn_tcp.send(b"b")
    
    # Attente d'un message UDP a la reception du message sur can1
    data = socket_udp.recv(1024)
    print("Donnee recue :", data.decode()) # Compteur = 2

    # Attente du message TCP :
    data = conn_tcp.recv(1024)
    print("Donnee recue :", data.decode())

    # Envoi du message pour terminer can1_client-udp
    conn_tcp.send(b"z")
    
    # Attente d'un message UDP a la reception du message sur can1
    data = socket_udp.recv(1024)
    print("Donnee recue :", data.decode()) # compteur = 3

    # Fermeture des sockets
    socket_udp.close()
    conn_tcp.close()
    socket_tcp.close()
