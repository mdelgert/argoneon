# Docker
```bash
sudo curl -fsSL https://get.docker.com | bash
sudo usermod -aG docker $USER
sudo reboot
docker run mdelgert/hello-world
```

# Docker DHCP loses ip at random issue - https://raspberrypi.stackexchange.com/questions/136320/raspberry-pi-loses-ipv4-address-randomly-but-keeps-ipv6-address
```bash
sudo nano /etc/dhcpcd.conf
```

# Example add this line to EOF
denyinterfaces veth*

# Portainer Setup
https://docs.portainer.io/user/docker/host/setup
```bash
docker volume create portainer_data
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:latest
```

# Default Templates
https://raw.githubusercontent.com/portainer/templates/master/templates-2.0.json

# Pi Hosted
https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/template/portainer-v2-arm64.json
https://raw.githubusercontent.com/novaspirit/pi-hosted/master/template/portainer-v2-amd64.json

# Default application templates
Cloudflare DDNS
Nginx Proxy Manager v2 with Sqllite
DashMachine