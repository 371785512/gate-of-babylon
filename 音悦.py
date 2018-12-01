import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)
song1=[1,1,5,5,6,6,5,4,4,3,3,2,2,1]
song2=[3,2,1,2,3,3,3,2,2,2,3,3,3,3,2,1,2,3,3,3,1,2,2,3,2,1]
song3=[5,3,3,4,2,2,1,2,3,4,5,5,5,5,3,3,4,2,2,1,1,5,5,3]
for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)


def run():
    action = "empty"
    while action != "q":
        print ('q for quit,others for command')
        action = input("> ")
        print('hhhhh')
        if action=='1':
        #ser.write(action.encode())
        #time.sleep(1)
        #ser.write("y".encode())
        #time.sleep(1)
        #ser.write("g".encode())
        #time.sleep(1)
            print('got1')
            for x in song1:
                print(x)
                ser.write(str(x).encode())
                ser.write(str('a').encode())
                time.sleep(1)
        if action =='2':    
            for y in song2:
                print(y)
                ser.write(str(y).encode())
                ser.write(str('a').encode())
                time.sleep(1)
        if action =='3':
            for z in song3:
                print(z)
                ser.write(str(z).encode())
                ser.write(str('a').encode())
                time.sleep(1)
run()
