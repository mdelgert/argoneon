### Test readwrite speed
```bash
dd if=/dev/zero of=testfile bs=4M count=100
dd if=/dev/zero of=testfile bs=20M count=5 oflag=direct
```