# Links
https://thesecmaster.com/how-to-partition-and-format-the-hard-drives-on-raspberry-pi/

# Seel all partitions
```bash
parted
print all
```

# Clear all partions
```bash
sudo fdisk /dev/sdb #d 1 enter w
```

# SSD Setup
```bash
lsblk
sudo fdisk /dev/sdb #n p 1 enter w
sudo mkfs.ext4 /dev/sdb
sudo mkdir /mnt/d2
sudo blkid
sudo nano /etc/fstab
sudo reboot
df -h #show all mounts
```

# Example /etc/fstab
UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX /mnt/d2 ext4 defaults 0 0