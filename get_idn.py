import os

fd = os.open("/dev/usbtmc0", os.O_RDWR)

os.write(fd, b"*IDN?\n")
print("IDN:", os.read(fd, 1024))

os.write(fd, b"SYST:VERS?\n")
print("VERS:", os.read(fd, 1024))

os.close(fd)