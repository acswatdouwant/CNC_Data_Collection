import telnetlib
import time

host = "10.78.12.15"
port = "5025"
DebugLVL = 0

tn = telnetlib.Telnet(host, port, timeout=5)

tn.set_debuglevel(DebugLVL)


cmd = "?Q500 \r"
serial = "\n"

while True:
    tn.write((cmd).encode('ascii'))
    collected_data = tn.read_until((serial).encode('ascii'))
    print(collected_data)
    time.sleep(10)


# print (collected_data)
tn.close()
print("Connection Closed")
