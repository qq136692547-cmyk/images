import struct, zlib, os
W, H = 320, 180
raw = bytearray()
for y in range(H):
    raw.append(0)
    for x in range(W):
        r = int(255 * x / W); g = 40; b = int(255 * y / H)
        if 120 <= x <= 200 and 70 <= y <= 110:
            r, g, b = 255, 255, 255
        raw += bytes((r, g, b))
def chunk(typ, data):
    return struct.pack(">I", len(data)) + typ + data + struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff)
png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")
os.makedirs("img", exist_ok=True)
open("img/test-upload-verify.png", "wb").write(png)
print("测试图已生成:", os.path.getsize("img/test-upload-verify.png"), "bytes")
