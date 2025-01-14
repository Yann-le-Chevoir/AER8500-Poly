# AER8500-Poly
Exemple du cours AER8500

Commandes à exécuter sur la MPIC pour activer et configurer can0 et can1 :
```
SpiRequest -d 2 10c 40
ip link set can0 up type can bitrate 500000
ip link set can1 up type can bitrate 500000
```

Filtre pour Wireshark :
```
udp.port==5005 || tcp.port==8888
```

Problèmes de Janvier 2025 à régler:
- Les extensions de VSCode ne permettent pas de déboguer du Python2. Les applications sur la MPIC DOIVENT rouler en Python2.
  On les lance depuis le terminal, car même le "start" dans VSCode ne veut pas utiliser Python2.
  En Python3, on a un segfault avec le 429 et des cast qui ne fonctionnent pas (code à refactorer).
- Pareil, la dernière extension VSCode ne permet pas de démarrer laptop.py en mode débogue avec Python 3.7.8,
  version qui fonctionne.
- laptop.py ne fonctionne pas avec Pyhon 3.13.1, il bloque / n'accepte pas la connexion tcp.
- Même chose avec 3.8.10, version minimale pour faire du debug.
- On doit donc lancer avec 3.7.8 et pas en mode debug. D'où l'ajout des "input" dans le code pour
  y aller step by step sans debug
