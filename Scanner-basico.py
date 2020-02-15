from socket import *

print("Enter the IP to scan:", end=" ")
_ip=input()
print("Enter starting port number:", end=" ")
_start = input()
_start_int = int(_start)
print("Enter ending port number:", end=" ")
_end = input()
_end_int = int(_end)
print("\033[4;37;42m"+"[>>>>>] Starting Scanning: ", _ip + "\033[0;m" + "\n")

for port in range(_start_int,_end_int):
    print("\033[3;36m"+"[***] Listening Port" + " " + str(port) + "..." + "\033[0;m")
    _s = socket(AF_INET,SOCK_STREAM)
    _s.settimeout(5)
    if(_s.connect_ex((_ip,port))==0):
        print("\033[1;32m"+"[ ✔ ] Open Port " + str(port) + "\033[0;m")
    else:
        print("\033[1;31m"+"[ X ] Closed Port " + str(port) + "\033[0;m")
    _s.close()
print("\n"+"\033[1;37;43m"+"[<<<<<] Scanning is Done...." + "\033[0;m")