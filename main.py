import zlib
import os

FIRMWARE_HEADER_MAGIC = 0x3042364b
versionNo = None
checksum = None
len = None

##input File Path
input_file_path = 'boxpower_app.bin'

##magic, version, crc, len
header = []

##Version Input
versionNo = int(input('Enter a Version : '))

##input File Copy
f = open('boxpower_app.bin', 'rb')
input_file_data = f.read()
f.close()

##CRC32
def crc(fileName):
    prev = 0
    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return (prev & 0xFFFFFFFF)

checksum = crc(input_file_path)

len = os.stat(input_file_path).st_size

print("magic : \t", hex(FIRMWARE_HEADER_MAGIC))
print("Version : \t", hex(versionNo))
print("CRC32 : \t", hex(checksum))
print("LEN Hex: \t", hex(len))

header.append(FIRMWARE_HEADER_MAGIC)
header.append(versionNo)
header.append(checksum)
header.append(len)

k = open('boxpower_app.fw', 'wb')
for i in header:
    data = int.to_bytes(i, 4, 'little')
    k.write(data)

k.write(input_file_data)
k.close()