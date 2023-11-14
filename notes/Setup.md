# Links
https://github.com/JeffCurless/argoneon
https://github.com/Argon40Tech/Argon40case
https://forum.argon40.com/t/installation-and-setup-for-eon-system/455

# Setup
```bash
sudo apt update
sudo apt upgrade
sudo nano /etc/timezone
curl https://raw.githubusercontent.com/mdelgert/argoneon/main/argoneon.sh | bash
argon-config #2 update RTC 
```
# Enable I2C, use raspi-config and change the setting under Interface Options