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
fdisk -l
lsblk
sudo fdisk /dev/sdb #n p 1 enter w
sudo mkfs.ext4 /dev/sdb
sudo mkdir /mnt/d1
sudo chown mdelgert:mdelgert /mnt/d1
sudo chown mdelgert:mdelgert /mnt/d2
sudo blkid
df -h #show all mounts
sudo nano /etc/fstab
```

# Label a disk
```bash
sudo e2label /dev/sdb d1
sudo e2label /dev/sdb
```

# Example /etc/fstab
UUID=60415032-d701-44ac-a26d-741fbbf575b3 /mnt/d1 ext4 defaults 0 0
UUID=a51316d2-022d-4ff1-9283-2edb53be13e6 /mnt/d2 ext4 defaults 0 0

# Manual mount before reboot
```bash
sudo mount -a
```

# Example blkid
/dev/sdb: LABEL="d1" UUID="60415032-d701-44ac-a26d-741fbbf575b3" BLOCK_SIZE="4096" TYPE="ext4"
/dev/sdc: LABEL="d2" UUID="a51316d2-022d-4ff1-9283-2edb53be13e6" BLOCK_SIZE="4096" TYPE="ext4"

# How to mount Linux file system using WSL on Windows 11
https://pureinfotech.com/mount-drive-linux-file-system-wsl-windows-11/
https://casivaagustin.com.ar/index.php/mount-an-ext4-partition-on-windows-11/
https://github.com/microsoft/WSL/issues/6319

# Mount WSL (run powershell as admin)
```ps
wmic diskdrive list brief
wsl --mount \\.\PHYSICALDRIVE4 --partition 1
wsl.exe --unmount \\.\PHYSICALDRIVE4
```

# The go to path \\wsl.localhost\Ubuntu1\mnt\wsl\PHYSICALDRIVE4p1
