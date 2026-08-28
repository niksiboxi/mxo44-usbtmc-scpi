import os

fd = os.open("/dev/usbtmc0", os.O_RDWR)

os.write(fd, b"MMEM:CAT? 'screenshots'\n")
response = os.read(fd, 8192).decode().strip()

os.close(fd)

parts = response.split(',"')

print("Files in screenshots:\n")

for entry in parts[2:]:
    name, filetype, size = entry.rstrip('"').split(',')

    icon = "📁" if filetype == "DIR" else "📄"
    print(f"{icon} {name:40} {size:>10} bytes")