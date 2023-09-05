import threading
import socket

#adres tanımlama
host=str(input("Host Adress:"))
port=int(input("Port:"))
   


#socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while 1:
    try:
        s.connect((host,port))
        print("Bağlantı Kuruldu Sohbet Hazır")
        break
    except:
        print("sunucuya bağlanılamadı")


#veri gonder
def ilet():
     mesajat = input()
     s.sendall(mesajat.encode())

#veri al
def al():
    while 1:
        ldata = s.recv(1024)
        print("Server:")
        print(ldata.decode())

thread_verial = threading.Thread(target=al)
thread_verial.start()

while True:
    ilet()

        
