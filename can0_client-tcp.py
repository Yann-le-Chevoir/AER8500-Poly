import socket
import can

if __name__ == '__main__':

    # Création d'un socket TCP et connexion au serveur (handshaking)
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp.connect(("172.16.0.1", 8888))

    # Canbus can0
    can0 = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

    # Partie applicative
    while True:
        # Attente d'un événement : réception d'un message TCP
        msg = socket_tcp.recv(1024)

        # Envoi du même message sur can0 (de la simulation vers un vrai instrument canbus par exemple)
        can0.send(can.Message(data=msg))

        # Attente d'une réponse (autopilote par exemple)
        data = can0.recv(timeout=10)

        # Timeout = condition de sortie de la boucle
        if data is None:
            break

        # Envoi d'un message TCP
        socket_tcp.send(b"Fin de la boucle")

    # Fermeture du socket TCP
    socket_tcp.close()
