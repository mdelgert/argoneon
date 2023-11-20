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
sudo blkid
sudo reboot
df -h #show all mounts
```

# Label a disk
```bash
sudo e2label /dev/sdb d1
sudo e2label /dev/sdb
```

# Example /etc/fstab
UUID=b957fb13-bfe2-4ead-b9b3-df50d45c8bd2 /mnt/d1 ext4 defaults 0 0

# Example blkid
/dev/sda1: LABEL_FATBOOT="bootfs" LABEL="bootfs" UUID="0B22-2966" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="ad6767fc-01"
/dev/sda2: LABEL="rootfs" UUID="3ad7386b-e1ae-4032-ae33-0c40f5ecc4ac" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="ad6767fc-02"
/dev/sdc: UUID="05aac87c-defe-4df7-bbe7-c35e84fdb6ef" BLOCK_SIZE="4096" TYPE="ext4"
/dev/sdb: UUID="b957fb13-bfe2-4ead-b9b3-df50d45c8bd2" BLOCK_SIZE="4096" TYPE="ext4"

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
