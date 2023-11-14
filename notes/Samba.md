# Links
https://kalitut.com/samba-on-raspberry-pi/
https://pimylifeup.com/raspberry-pi-samba/

# Samba setup
```bash
sudo apt-get install samba samba-common-bin
sudo cp -p /etc/samba/smb.conf /etc/samba/smb.conf.original
sudo nano /etc/samba/smb.conf
sudo chown mdelgert:mdelgert /mnt/d2
sudo smbpasswd -a mdelgert
sudo systemctl restart smbd
```

# Example /etc/samba/smb.conf
[global]
   workgroup = WORKGROUP
   log file = /var/log/samba/log.%m
   max log size = 1000
   logging = file
   panic action = /usr/share/samba/panic-action %d
   server role = standalone server
   obey pam restrictions = yes
   unix password sync = yes
   passwd program = /usr/bin/passwd %u
   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
   pam password change = yes
   map to guest = bad user
   usershare allow guests = yes

[d2]
   path = /mnt/d2
   writeable = yes
   browseable = yes
   create mask = 0777
   directory mask = 0777
   public = no