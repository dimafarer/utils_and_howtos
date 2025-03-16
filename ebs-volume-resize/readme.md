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
