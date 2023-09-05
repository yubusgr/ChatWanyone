import threading
import socket
import time

#adres tanımlama
host =str(input("Yerel Ağ Adresiniz:"))
port =int(input("Port Girin:"))



#socket 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
print("Dinleme Başladı...")
time.sleep(3)
conn,addr = s.accept()

if s.accept:
    print("Bağlantı Kuruldu, Sohbete Hazır")


#veri al
def al():
    while 1:
        ldata = conn.recv(1024)      
        print("Client:") 
        print(ldata.decode())

thread_verial = threading.Thread(target=al)
thread_verial.start()

while True:
    mesaj = input()
    conn.sendall(mesaj.encode())

        
