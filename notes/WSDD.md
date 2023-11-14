# Links
https://github.com/mdelgert/wsdd

WSDD implements a Web Service Discovery host daemon. This enables (Samba) hosts, like your local NAS device, to be found by Web Service Discovery Clients like Windows.

It also implements the client side of the discovery protocol which allows to search for Windows machines and other devices implementing WSD. This mode of operation is called discovery mode.

# Setup
```bash
cd /usr/bin
sudo wget https://github.com/mdelgert/wsdd/raw/master/src/dist/wsdd
sudo chmod +x wsdd
sudo nano /etc/rc.local
wsdd & #Add this line
```