import socket
import can

if __name__ == '__main__':

    # Socket UDP du client :
    socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Canbus can1
    can1 = can.interface.Bus(bustype='socketcan', channel='can1', bitrate=500000)

    # Compteur de messages reçus initialisé à 0
    compteur = 0

    # Partie applicative
    while True:
        # Attente d'un évenement : reception d'un message sur can1
        input_msg = can1.recv()

        # Envoi d'un message UDP au serveur : compteur de messages reçus
        compteur += 1
        socket_udp.sendto(bytes([compteur]), ("172.16.0.1", 5005))

        # Traitement + réponse
        if input_msg.data.decode() == "z":
            # Condition de sortie de la boucle
            break
        elif input_msg.data.decode() == "a":
            output_msg = can.Message(data=[0, 1, 2, 3, 4, 5, 6, 7])
        else:
            output_msg = can.Message(data=[255])

        try:
            can1.send(output_msg)
        except can.CanError:
            print("Erreur envoi sur can1")

    # Fermeture du socket UDP
    socket_udp.close()
