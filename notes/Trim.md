# Links
https://www.jeffgeerling.com/blog/2020/enabling-trim-on-external-ssd-on-raspberry-pi

# Enable trim
```bash
sudo su
apt-get install -y sg3-utils lsscsi
find /sys/ -name provisioning_mode -exec grep -H . {} + | sort
echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2.2/2-2.2:1.0/host0/target0:0:0/0:0:0:0/scsi_disk/0:0:0:0/provisioning_mode
echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2.4/2-2.4:1.0/host1/target1:0:0/1:0:0:0/scsi_disk/1:0:0:0/provisioning_mode
lsusb
nano /etc/udev/rules.d/10-trim.rules
sudo reboot
sudo systemctl status fstrim.timer
sudo systemctl enable fstrim.timer
sudo fstrim -v /
```

### 10-trim.rules
ACTION=="add|change", ATTRS{idVendor}=="1741", ATTRS{idProduct}=="1156", SUBSYSTEM=="scsi_disk", ATTR{provisioning_mode}="unmap"
ACTION=="add|change", ATTRS{idVendor}=="174e", ATTRS{idProduct}=="1155", SUBSYSTEM=="scsi_disk", ATTR{provisioning_mode}="unmap"

