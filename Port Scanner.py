import sys
import socket
from datetime import datetime

if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1])
else:
    print("Invalid ip or syntax")

print(f"scanning:{target}")
print("Started Time:"+str(datetime.now()))


try:
    start=int(input("Enter Starting Port"))
    end=int(input("Enter the end port"))
    for port in range(start,end):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        
        if result==0:
            print(f"The port on {port} is open")
        s.close()

except KeyboardInterrupt:
    print("Exiting....")
except socket.gaierror:
    print("IP doesn't exist")
except socket.error:
    print("Error occured")
