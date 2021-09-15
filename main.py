import getpass
import telnetlib
import time
HostIP = input("Hostname: ")
Port = 23
User = input("Username: ")
Password = getpass.getpass('Password: ')
Telnet = telnetlib.Telnet(HostIP, Port)
Telnet.read_until(b"login: ")
Telnet.write(User.encode('ascii') + b"\n")
Telnet.read_until(b"Password: ")
Telnet.write(Password.encode('ascii') + b"\n")
Telnet.write(b"")
time.sleep(1)
while True:
    time.sleep(.1)
    Output = Telnet.read_very_eager().decode('ascii')
    In = input(Output)
    Telnet.write(In.encode('ascii') + b"\n")
    #print(Output)
print("DONE")