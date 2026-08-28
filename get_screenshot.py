#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

filename = sys.argv[1]

fd = os.open("/dev/usbtmc0", os.O_RDWR)

try:
    cmd = f"MMEM:DATA? 'screenshots/{filename}'\n"
    os.write(fd, cmd.encode())

    data = bytearray()

    while True:
        try:
            chunk = os.read(fd, 65536)
            if not chunk:
                break

            data.extend(chunk)

            if b"IEND\xaeB`\x82" in data:
                break

        except TimeoutError:
            break

finally:
    os.close(fd)

if data.startswith(b"#"):
    digits = int(chr(data[1]))
    data = data[2 + digits :]

with open(filename, "wb") as f:
    f.write(data)

print(f"Saved {filename}")