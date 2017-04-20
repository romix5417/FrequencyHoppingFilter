import serial
import binascii

def connect_serial(com,baudrate):
    try:
        t = serial.Serial(com,baudrate)
    except Exception as e:
        print("Exception")
        return None

    if t.isOpen():
        return t
    return None

def write_serial(serial,data):
	serial.write(data)	


def main():
    t = connect_serial("COM5", 115200)
    data = bytearray([int(0xa4), int(0x1a)])
    #d=bytes.fromhex('11 22')
    
    t.write(data)
    #print("serial:%s" %(binascii.b2a_hex(t.read(2))))
    print("serial:%s" %t.read(130))

if __name__ == "__main__":
    main()
