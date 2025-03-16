# How to Resize EBS Volume

+ check disk usage

```bash
df -h
```

+ set execute permission for the scipt  
+ run the script giving size of volume in GB

```bash
chmod +x resize.sh
./resize.sh 20
```

+ while its included in the script its likely the partition and filesystem need to be manully resized

```bash
# Extend the partition
sudo growpart /dev/nvme0n1 1

# Resize the filesystem
sudo resize2fs /dev/nvme0n1p1
```

+ confirm disk usage

```bash
df -h
```