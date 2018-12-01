from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time
mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)
stayed_time=12
pos=mc.player.getTilePos()

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1] :
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

while True:
    pos=mc.player.getTilePos()
    resp=ser.readline()
    rs=str(resp)
    rs1=int(rs.split('\\')[0][2:])
    print(rs1)
    if rs1<800:
        for y in range(int(rs1/10)):
            mc.setBlock(pos.x,pos.y-y,pos.z,46)
    
        
