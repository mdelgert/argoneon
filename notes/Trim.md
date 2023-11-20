# Links
https://www.jeffgeerling.com/blog/2020/enabling-trim-on-external-ssd-on-raspberry-pi

# Enable trim
```bash
sudo su
apt-get install -y sg3-utils lsscsi
find /sys/ -name provisioning_mode -exec grep -H . {} + | sort
lsusb
nano /etc/udev/rules.d/10-trim.rules
sudo reboot
sudo systemctl status fstrim.timer
sudo systemctl enable fstrim.timer
sudo fstrim -v /
sudo fstrim -v /mnt/d1
sudo fstrim -v /mnt/d2
sudo fstrim -v --all
```

### 10-trim.rules
ACTION=="add|change", ATTRS{idVendor}=="1741", ATTRS{idProduct}=="1156", SUBSYSTEM=="scsi_disk", ATTR{provisioning_mode}="unmap"
ACTION=="add|change", ATTRS{idVendor}=="174e", ATTRS{idProduct}=="1155", SUBSYSTEM=="scsi_disk", ATTR{provisioning_mode}="unmap"
ACTION=="add|change", ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="9210", SUBSYSTEM=="scsi_disk", ATTR{provisioning_mode}="unmap"

### Settings
```bash
echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2.2/2-2.2:1.0/host0/target0:0:0/0:0:0:0/scsi_disk/0:0:0:0/provisioning_mode
echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2.3/2-2.3:1.0/host1/target1:0:0/1:0:0:0/scsi_disk/1:0:0:0/provisioning_mode
echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2.4/2-2.4:1.0/host2/target2:0:0/2:0:0:0/scsi_disk/2:0:0:0/provisioning_mode
echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2.4/2-2.4:1.0/host2/target2:0:0/2:0:0:1/scsi_disk/2:0:0:1/provisioning_mode
```

### lsusb
Bus 002 Device 005: ID 1741:1156 Pinas sata
Bus 002 Device 003: ID 174e:1155 Pinas SATA
Bus 002 Device 004: ID 0bda:9210 Realtek Semiconductor Corp. RTL9210 M.2 NVME Adapter